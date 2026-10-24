"""测量 LLM 查询改写的延迟。"""
import json
import statistics
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVAL_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = EVAL_DIR / "data"
REPORTS_DIR = EVAL_DIR / "reports"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import rag
from eval_retrieval import p95

EVAL_FILE = DATA_DIR / "eval_set_multiturn.json"
REPORT_FILE = REPORTS_DIR / "rewrite_latency_report.md"
RESULTS_FILE = REPORTS_DIR / "rewrite_latency_results.json"


def main():
    items = json.loads(EVAL_FILE.read_text(encoding="utf-8"))

    # 预热一次，避免首次连接建立把 P95 拉高
    rag.rewrite_query(
        "那它呢",
        [
            {"role": "user", "content": "什么是继承"},
            {"role": "assistant", "content": "继承是子类获取父类成员。"},
        ],
    )

    records = []
    latencies = []

    for item in items:
        question = item["question"]
        if not rag.needs_history_context(question):
            continue

        start = time.perf_counter()
        rewritten = rag.rewrite_query(question, item["history"])
        elapsed = time.perf_counter() - start

        latencies.append(elapsed)
        records.append({
            "question": question,
            "rewritten": rewritten,
            "changed": rewritten != question,
            "latency": round(elapsed, 4),
        })

    n = len(latencies)
    metrics = {
        "n": n,
        "p50": statistics.median(latencies),
        "p95": p95(latencies),
        "mean": statistics.mean(latencies),
        "min": min(latencies),
        "max": max(latencies),
    }

    print(f"改写样本数：{n}")
    print(f"P50：{metrics['p50']:.3f}s")
    print(f"P95：{metrics['p95']:.3f}s")
    print(f"平均：{metrics['mean']:.3f}s")
    print(f"最小/最大：{metrics['min']:.3f}s / {metrics['max']:.3f}s")

    lines = [
        "# 查询改写延迟",
        "",
        f"- 样本数：{n}",
        f"- P50：{metrics['p50']:.3f}s",
        f"- P95：{metrics['p95']:.3f}s",
        f"- 平均：{metrics['mean']:.3f}s",
        f"- 最小：{metrics['min']:.3f}s",
        f"- 最大：{metrics['max']:.3f}s",
        "",
        "> 包含一次 DeepSeek 调用和网络往返；测量前已做一次预热。",
        "",
        "## 逐题结果",
        "",
        "| # | 追问 | 改写后问题 | 耗时 |",
        "|---:|---|---|---:|",
    ]

    for i, record in enumerate(records, 1):
        rewritten = record["rewritten"] if record["changed"] else "（未改变）"
        lines.append(
            f"| {i} | {record['question']} | {rewritten} | {record['latency']:.3f}s |"
        )

    lines.append("")

    RESULTS_FILE.write_text(
        json.dumps(
            {"metrics": metrics, "records": records},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n明细已写入 {RESULTS_FILE} 和 {REPORT_FILE}")


if __name__ == "__main__":
    main()
