"""列出知识库里所有 chunk 的序号、标题和开头，用来挑选评测问题。"""
from pathlib import Path

import chromadb

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(__file__).resolve().parent / "chunks.txt"

collection = chromadb.PersistentClient(
    path=str(PROJECT_ROOT / "chroma_db")
).get_collection("my_knowledge")
data = collection.get(include=["documents"])

lines_out = []

for i, (doc_id, doc) in enumerate(zip(data["ids"], data["documents"]), 1):
    # chunk 的第一行是 "标题路径：xxx"，标题就是这一行去掉前缀
    lines = doc.splitlines()
    if lines and lines[0].startswith("标题路径："):
        title = lines[0][len("标题路径："):].strip()
    else:
        title = "（无标题）"

    # 标题之后的内容压成一行，只取前 90 个字，方便快速浏览
    body = " ".join(lines[1:])[:90]

    lines_out.append(f"{i:03d}  {title}")
    lines_out.append(f"     {body}")

OUTPUT.write_text("\n".join(lines_out), encoding="utf-8")
print(f"共 {len(data['ids'])} 个 chunk，已写入 {OUTPUT}")
