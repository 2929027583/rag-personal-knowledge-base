"""负样本评测：知识库外的问题不应该返回来源。"""
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
from eval_retrieval import title_of

NEG_FILE = DATA_DIR / "eval_negative.json"
REPORT_FILE = REPORTS_DIR / "eval_negative_report.md"
RESULTS_FILE = REPORTS_DIR / "eval_negative_results.json"
TOP_K = 5
THRESHOLD = rag.RELEVANT_DISTANCE


def retrieve(question: str):
    embedding = rag._embed_text(question)
    result = rag.collection.query(
        query_embeddings=[embedding],
        n_results=TOP_K,
        include=["documents", "distances"],
    )
    return [
        {
            "rank": i,
            "title": title_of(doc),
            "distance": round(float(distance), 4),
        }
        for i, (doc, distance) in enumerate(
            zip(result["documents"][0], result["distances"][0]), 1
        )
    ]


def build_report(records) -> str:
    false_positive = sum(1 for r in records if r["has_source"])
    best_distances = [r["best_distance"] for r in records]

    lines = [
        "# 负样本检索评测",
        "",
        f"- 题目数：{len(records)}",
        f"- TOP_K：{TOP_K}",
        f"- 距离阈值：{THRESHOLD}",
        f"- 来源误报：{false_positive} / {len(records)}",
        f"- 来源误报率：{false_positive / len(records):.1%}",
        f"- 平均最佳距离：{sum(best_distances) / len(best_distances):.4f}",
        f"- P50 最佳距离：{sorted(best_distances)[len(best_distances) // 2]:.4f}",
        "",
        "> 误报定义：top-k 里至少有一条距离 <= 阈值，实际会展示来源。",
        "",
        "## 逐题结果",
        "",
        "| # | 问题 | 最佳距离 | 最佳标题 | 有来源 |",
        "|---:|---|---:|---|:---:|",
    ]

    for i, record in enumerate(records, 1):
        mark = "✅" if record["has_source"] else ""
        lines.append(
            f"| {i} | {record['question']} | {record['best_distance']:.4f} | "
            f"{record['top_k'][0]['title']} | {mark} |"
        )

    lines.append("")
    return "\n".join(lines)


def main():
    questions = json.loads(NEG_FILE.read_text(encoding="utf-8"))
    records = []

    for question in questions:
        top_k = retrieve(question)
        records.append({
            "question": question,
            "best_distance": top_k[0]["distance"],
            "has_source": any(entry["distance"] <= THRESHOLD for entry in top_k),
            "top_k": top_k,
        })

    false_positive = sum(1 for r in records if r["has_source"])
    print(f"负样本数：{len(records)}")
    print(f"来源误报：{false_positive} / {len(records)}")
    print(f"误报率：{false_positive / len(records):.1%}")
    print(
        "最佳距离："
        + ", ".join(f"{r['best_distance']:.4f}" for r in records)
    )

    RESULTS_FILE.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    REPORT_FILE.write_text(build_report(records), encoding="utf-8")
    print(f"\n明细已写入 {RESULTS_FILE} 和 {REPORT_FILE}")


if __name__ == "__main__":
    main()
