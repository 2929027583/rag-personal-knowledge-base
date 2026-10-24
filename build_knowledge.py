from pathlib import Path
import os
import re

from dotenv import load_dotenv
from openai import OpenAI
import chromadb

# 从项目根目录的 .env 读取 API Key
load_dotenv(Path(__file__).with_name(".env"))

def split_markdown_into_chunks(text):
    lines = text.splitlines()
    chunks = []
    heading_stack = []
    body_lines = []
    in_code = False
    fence_marker = None

    def flush():
        body = "\n".join(body_lines).strip()

        if body:
            title_path = " > ".join(heading_stack)

            if title_path:
                chunk = f"标题路径：{title_path}\n\n{body}"
            else:
                chunk = body

            chunks.append(chunk)

        body_lines.clear()

    for line in lines:
        stripped = line.strip()

        # 识别代码块的开始和结束
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]

            if not in_code:
                in_code = True
                fence_marker = marker
            elif marker == fence_marker:
                in_code = False
                fence_marker = None

            body_lines.append(line)
            continue

        # 只在代码块外识别 Markdown 标题
        match = None
        if not in_code:
            match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)

        if match:
            flush()

            level = len(match.group(1))
            title = match.group(2).strip()

            heading_stack = heading_stack[:level - 1]
            heading_stack.append(title)
            continue

        body_lines.append(line)

    flush()
    return chunks
# ============================================================
# 1. 找到知识库文件夹
# ============================================================

knowledge_dir = Path(__file__).resolve().parent / "knowledge"

# 获取 knowledge 文件夹下所有 Markdown 文件
files = list(knowledge_dir.glob("*.md"))

print("发现知识库文件：")
for file in files:
    print("-", file.name)


# ============================================================
# 2. 读取所有 Markdown 文件
# ============================================================

all_chunks = []

for file_path in files:

    print(f"\n正在读取：{file_path.name}")

    text = file_path.read_text(encoding="utf-8")

    print("文本长度：", len(text))

    # --------------------------------------------------------
    # 按 Markdown 标题切分
    #
    # # 一级标题
    # ## 二级标题
    # ### 三级标题
    # --------------------------------------------------------

    chunks = split_markdown_into_chunks(text)

    for chunk in chunks:
        if len(chunk) < 10:
            continue

        all_chunks.append(chunk)
# ============================================================
# 3. 查看切分结果
# ============================================================

print("\n==============================")
print("切分完成！")
print("Chunk数量：", len(all_chunks))
print("==============================")

for i, chunk in enumerate(all_chunks):

    print(f"\n--- Chunk {i} ---")
    print(chunk)

# ============================================================
# 4. 创建 Embedding 客户端
# ============================================================

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# ============================================================
# 5. 调用阿里云 Embedding
# ============================================================

embeddings = []

# 阿里云 Embedding 一次最多处理 20 个文本
batch_size = 20

for i in range(0, len(all_chunks), batch_size):

    batch = all_chunks[i:i + batch_size]

    print(f"\n正在处理第 {i + 1} ~ {i + len(batch)} 个 Chunk")

    response = client.embeddings.create(
        model="qwen3.7-text-embedding",
        input=batch,
        dimensions=1024
    )

    batch_embeddings = [
        item.embedding
        for item in response.data
    ]

    embeddings.extend(batch_embeddings)


print("\n==============================")
print("Embedding成功！")
print("向量数量：", len(embeddings))
print("向量维度：", len(embeddings[0]))
print("==============================")


# ============================================================
# 6. 连接 Chroma 数据库
# ============================================================

chroma_client = chromadb.PersistentClient(
    path=str(Path(__file__).resolve().parent / "chroma_db")
)

collection = chroma_client.get_or_create_collection(
    name="my_knowledge"
)

print("当前集合：", collection.name)
print("写入前文档数量：", collection.count())


# ============================================================
# 7. 保存 Chunk + 向量
# ============================================================

# 获取旧数据的 ID，并删除旧数据
old_ids = collection.get()["ids"]

if old_ids:
    collection.delete(ids=old_ids)

# 写入最新的 Chunk 和向量
collection.add(
    ids=[f"chunk_{i}" for i in range(len(all_chunks))],
    documents=all_chunks,
    embeddings=embeddings
)

print("\n==============================")
print("知识库建立完成！")
print("Chunk 数量：", len(all_chunks))
print("Embedding 数量：", len(embeddings))
print("Chroma 中的文档数量：", collection.count())
print("==============================")
