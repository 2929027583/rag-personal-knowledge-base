"""检索评测：只调用 embedding + Chroma，不调用 DeepSeek。

对 eval_set.json 里的每个问题：
1. 把问题转成向量
2. 从知识库取最相似的前 TOP_K 段
3. 看标准答案的标题是否出现在结果里
4. 统计 Hit@1、Hit@5、MRR 和延迟

同时输出：
- eval_results.json：每道题 + top-k 明细，给程序用
- eval_report.md：同样的内容，排版成方便阅读的报告
"""
import json
import os
import re
import statistics
import sys
import time
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVAL_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = EVAL_DIR / "data"
REPORTS_DIR = EVAL_DIR / "reports"

load_dotenv(PROJECT_ROOT / ".env")

# 默认读 eval/data/eval_set.json；也可以在命令行传别的文件，方便做对照实验
EVAL_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else DATA_DIR / "eval_set.json"
RESULTS_FILE = REPORTS_DIR / "eval_results.json"
REPORT_FILE = REPORTS_DIR / "eval_report.md"
TOP_K = 5
EMBED_MODEL = "qwen3.7-text-embedding"

embedding_client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
collection = chromadb.PersistentClient(
    path=str(PROJECT_ROOT / "chroma_db")
).get_collection("my_knowledge")


def norm(text: str) -> str:
    """去掉笔记导出时带的 HTML / Markdown 标记，再压缩空格。"""
    text = re.sub(r"<[^>]+>", "", text)              # <font style="..."> / </font>
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)     # **加粗**
    text = text.replace("`", "")                     # 行内代码
    text = re.sub(r"\s+", " ", text)                 # 连续空白压成一个空格
    return text.strip()


def title_of(doc: str) -> str:
    """chunk 的第一行是 '标题路径：xxx'，取出来并清洗。"""
    lines = doc.splitlines()
    if lines and lines[0].startswith("标题路径："):
        return norm(lines[0][len("标题路径："):])
    return ""


def snippet_of(doc: str, max_len: int = 80) -> str:
    """取标题之后的内容开头，方便在报告里判断这段讲什么。"""
    lines = doc.splitlines()
    raw_body = (
        "\n".join(lines[1:])
        if lines and lines[0].startswith("标题路径：")
        else doc
    )

    body = norm(raw_body)
    if not body:
        # Excel 笔记里很多内容是截图，去掉 HTML 后没有可读文字
        return "（仅图片，无可读文字）" if "<img" in raw_body else ""

    return body[:max_len] + ("…" if len(body) > max_len else "")


def retrieve(question: str, top_k: int):
    """返回 [(chunk 文本, 距离), ...]，按距离从近到远。"""
    embedding = embedding_client.embeddings.create(
        model=EMBED_MODEL,
        input=question,
        dimensions=1024,
    ).data[0].embedding

    result = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents", "distances"],
    )
    return list(zip(result["documents"][0], result["distances"][0]))


def p95(values):
    """样本很少时，P95 近似等于最慢的一次。"""
    values = sorted(values)
    index = min(len(values) - 1, int(round(0.95 * (len(values) - 1))))
    return values[index]


def build_report(records, metrics) -> str:
    """生成 Markdown 报告，每题列出 top-k 明细。"""
    lines = [
        "# 检索评测报告",
        "",
        f"- 题目数：{metrics['n']}",
        f"- TOP_K：{TOP_K}",
        f"- Hit@1：{metrics['hit1']:.1%}",
        f"- Hit@5：{metrics['hit5']:.1%}",
        f"- MRR：{metrics['mrr']:.3f}",
        f"- P50：{metrics['p50']:.3f}s",
        f"- P95：{metrics['p95']:.3f}s",
        "",
        "> 命中判定：检索结果的标题（清洗后）与期望标题完全一致。",
        "",
        "---",
        "",
    ]

    for i, record in enumerate(records, 1):
        status = f"命中，排名 {record['rank']}" if record["rank"] else "MISS"
        lines.append(f"## {i}. {record['question']}")
        lines.append("")
        lines.append(f"- 期望标题：`{record['expected_title']}`")
        lines.append(f"- 结果：**{status}**")
        lines.append(f"- 本次耗时：{record['latency']:.3f}s")
        lines.append("")
        lines.append("| 排名 | 距离 | 标题 | 命中 | 内容开头 |")
        lines.append("|---:|---:|---|:---:|---|")

        for item in record["top_k"]:
            mark = "✅" if item["is_expected"] else ""
            title = item["title"].replace("|", "\\|")
            snippet = item["snippet"].replace("|", "\\|")
            lines.append(
                f"| {item['rank']} | {item['distance']:.4f} | "
                f"{title} | {mark} | {snippet} |"
            )

        lines.append("")

    return "\n".join(lines)


def main():
    items = json.loads(EVAL_FILE.read_text(encoding="utf-8"))

    hit1 = 0
    hit5 = 0
    rr_sum = 0.0
    latencies = []
    records = []

    print(f"共 {len(items)} 道题，TOP_K={TOP_K}\n")

    for item in items:
        question = item["question"]
        expected = norm(item["expected_title"])

        start = time.perf_counter()
        results = retrieve(question, TOP_K)
        elapsed = time.perf_counter() - start
        latencies.append(elapsed)

        # 把前 TOP_K 条整理成结构化数据，后面既用于统计也写进报告
        top_k_items = []
        for i, (doc, distance) in enumerate(results, 1):
            title = title_of(doc)
            top_k_items.append({
                "rank": i,
                "distance": round(float(distance), 4),
                "title": title,
                "snippet": snippet_of(doc),
                "is_expected": title == expected,
            })

        rank = next(
            (entry["rank"] for entry in top_k_items if entry["is_expected"]),
            None,
        )

        if rank == 1:
            hit1 += 1
        if rank is not None:
            hit5 += 1
            rr_sum += 1 / rank

        records.append({
            "question": question,
            "expected_title": expected,
            "rank": rank,
            "hit@1": rank == 1,
            "hit@5": rank is not None,
            "reciprocal_rank": round(1 / rank, 4) if rank else 0,
            "latency": round(elapsed, 4),
            "top_k": top_k_items,
        })

        print(f"[{'rank ' + str(rank) if rank else 'MISS'}] {question}")

        # 没命中时把前 5 条打印出来，方便排查是题目问题还是检索问题
        if rank is None:
            for entry in top_k_items:
                print(
                    f"    {entry['rank']}. {entry['distance']:.4f}  "
                    f"{entry['title']}"
                )

    n = len(items)
    metrics = {
        "n": n,
        "top_k": TOP_K,
        "hit1": hit1 / n,
        "hit5": hit5 / n,
        "mrr": rr_sum / n,
        "p50": statistics.median(latencies),
        "p95": p95(latencies),
    }

    print("\n===== 结果 =====")
    print(f"题目数: {n}")
    print(f"Hit@1:  {metrics['hit1']:.1%}")
    print(f"Hit@5:  {metrics['hit5']:.1%}")
    print(f"MRR:    {metrics['mrr']:.3f}")
    print(f"P50:    {metrics['p50']:.3f}s")
    print(f"P95:    {metrics['p95']:.3f}s")

    RESULTS_FILE.write_text(
        json.dumps({"metrics": metrics, "records": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    REPORT_FILE.write_text(build_report(records, metrics), encoding="utf-8")

    print(f"\n明细已写入 {RESULTS_FILE} 和 {REPORT_FILE}")


if __name__ == "__main__":
    main()
