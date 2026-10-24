"""多轮追问检索评测：基线、历史拼接、双查询合并、双查 + LLM 改写。"""
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVAL_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = EVAL_DIR / "data"
REPORTS_DIR = EVAL_DIR / "reports"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import rag
from eval_retrieval import norm, title_of

EVAL_FILE = DATA_DIR / "eval_set_multiturn.json"
REPORT_FILE = REPORTS_DIR / "eval_multiturn_report.md"
RESULTS_FILE = REPORTS_DIR / "eval_multiturn_results.json"
TOP_K = 5
THRESHOLD = rag.RELEVANT_DISTANCE


def retrieve(query: str):
    """只调用 embedding + Chroma，不调用 DeepSeek。"""
    embedding = rag._embed_text(query)
    result = rag.collection.query(
        query_embeddings=[embedding],
        n_results=TOP_K,
        include=["documents", "distances"],
    )
    return [
        {
            "id": chunk_id,
            "rank": i,
            "title": title_of(doc),
            "distance": round(float(distance), 4),
        }
        for i, (chunk_id, doc, distance) in enumerate(
            zip(
                result["ids"][0],
                result["documents"][0],
                result["distances"][0],
            ),
            1,
        )
    ]


def merge(results_by_query):
    """按 chunk id 合并多路检索结果，保留距离更小的那条，并重新编号。"""
    merged = {}
    for results in results_by_query:
        for item in results:
            old = merged.get(item["id"])
            if old is None or item["distance"] < old["distance"]:
                merged[item["id"]] = item

    ordered = sorted(merged.values(), key=lambda item: item["distance"])
    return [
        {**item, "rank": i}
        for i, item in enumerate(ordered, 1)
    ]


def build_queries(item, strategy: str, rewritten_query: str) -> list[str]:
    question = item["question"]
    concat_query = rag.build_search_query(question, item["history"])

    if strategy == "baseline":
        queries = [question]
    elif strategy == "concat":
        queries = [concat_query]
    elif strategy == "dual":
        queries = [question]
        if concat_query != question:
            queries.append(concat_query)
    elif strategy == "all":
        queries = [question]
        if concat_query != question:
            queries.append(concat_query)
        if rewritten_query not in queries:
            queries.append(rewritten_query)
    else:
        raise ValueError(f"unknown strategy: {strategy}")

    # 去重，保持顺序
    return list(dict.fromkeys(queries))


def evaluate_one(item, strategy: str, rewritten_query: str) -> dict:
    queries = build_queries(item, strategy, rewritten_query)
    top_k = merge([retrieve(query) for query in queries])[:TOP_K]
    expected = norm(item["expected_title"])

    rank = next(
        (entry["rank"] for entry in top_k if entry["title"] == expected),
        None,
    )
    expected_distance = next(
        (entry["distance"] for entry in top_k if entry["title"] == expected),
        None,
    )

    return {
        "queries": queries,
        "rank": rank,
        "expected_distance": expected_distance,
        "best_distance": top_k[0]["distance"] if top_k else None,
        # 生产环境 top_k=2，所以单独看前两条里有没有通过阈值的
        "source@2": any(entry["distance"] <= THRESHOLD for entry in top_k[:2]),
        "source@5": any(entry["distance"] <= THRESHOLD for entry in top_k),
        "top_k": top_k,
    }


def summarize(records: list[dict]) -> dict:
    n = len(records)
    return {
        "n": n,
        "hit1": sum(1 for r in records if r["rank"] == 1) / n,
        "hit5": sum(1 for r in records if r["rank"] is not None) / n,
        "mrr": sum((1 / r["rank"] if r["rank"] else 0) for r in records) / n,
        "source@2": sum(1 for r in records if r["source@2"]) / n,
        "source@5": sum(1 for r in records if r["source@5"]) / n,
        "avg_best_distance": sum(r["best_distance"] for r in records) / n,
    }


def build_report(records, metrics: dict) -> str:
    lines = [
        "# 多轮追问检索评测",
        "",
        f"- 题目数：{len(records)}",
        f"- TOP_K：{TOP_K}",
        f"- 距离阈值：{THRESHOLD}",
        "",
        "| 策略 | Hit@1 | Hit@5 | MRR | 有来源率@5 | 有来源率@2 | 平均最佳距离 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    labels = {
        "baseline": "基线（只用当前问题）",
        "concat": "历史拼接（单查询）",
        "dual": "双查询合并",
        "all": "双查 + LLM 改写",
    }
    for key in ("baseline", "concat", "dual", "all"):
        m = metrics[key]
        lines.append(
            f"| {labels[key]} | {m['hit1']:.1%} | {m['hit5']:.1%} | "
            f"{m['mrr']:.3f} | {m['source@5']:.1%} | "
            f"{m['source@2']:.1%} | {m['avg_best_distance']:.4f} |"
        )

    lines.extend([
        "",
        "> 有来源率@2 按生产环境的 top_k=2 计算：前两条里有任意一条距离 <= 阈值。",
        "",
        "## 逐题对比",
        "",
        "| # | 追问 | 改写后问题 | 基线排名 | 双查排名 | 全量排名 | 基线距离 | 双查距离 | 全量距离 | 有来源@2 |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|:---:|",
    ])

    for i, record in enumerate(records, 1):
        base = record["baseline"]
        dual = record["dual"]
        allr = record["all"]

        def rank_text(entry):
            return str(entry["rank"]) if entry["rank"] else "MISS"

        def dist_text(entry):
            return (
                f"{entry['expected_distance']:.4f}"
                if entry["expected_distance"] is not None
                else "—"
            )

        rewritten = record["rewritten_query"]
        rewritten_text = "—" if rewritten == record["question"] else rewritten
        source_mark = "✅" if allr["source@2"] else ""
        lines.append(
            f"| {i} | {record['question']} | {rewritten_text} | "
            f"{rank_text(base)} | {rank_text(dual)} | {rank_text(allr)} | "
            f"{dist_text(base)} | {dist_text(dual)} | {dist_text(allr)} | {source_mark} |"
        )

    lines.append("")
    return "\n".join(lines)


def main():
    items = json.loads(EVAL_FILE.read_text(encoding="utf-8"))
    records = []

    for item in items:
        # 只对依赖上下文的追问调用改写；其他情况会直接返回原问题
        rewritten = rag.rewrite_query(item["question"], item["history"])
        records.append({
            "question": item["question"],
            "expected_title": norm(item["expected_title"]),
            "rewritten_query": rewritten,
            "baseline": evaluate_one(item, "baseline", rewritten),
            "concat": evaluate_one(item, "concat", rewritten),
            "dual": evaluate_one(item, "dual", rewritten),
            "all": evaluate_one(item, "all", rewritten),
        })

    metrics = {
        key: summarize([r[key] for r in records])
        for key in ("baseline", "concat", "dual", "all")
    }

    print("策略          Hit@1   Hit@5   MRR     有来源@5  有来源@2")
    for key, label in (
        ("baseline", "基线    "),
        ("concat", "历史拼接"),
        ("dual", "双查合并"),
        ("all", "双查+改写"),
    ):
        m = metrics[key]
        print(
            f"{label}      {m['hit1']:.1%}   {m['hit5']:.1%}   {m['mrr']:.3f}   "
            f"{m['source@5']:.1%}     {m['source@2']:.1%}"
        )

    RESULTS_FILE.write_text(
        json.dumps(
            {"metrics": metrics, "records": records},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    REPORT_FILE.write_text(
        build_report(records, metrics),
        encoding="utf-8",
    )
    print(f"\n明细已写入 {RESULTS_FILE} 和 {REPORT_FILE}")


if __name__ == "__main__":
    main()
