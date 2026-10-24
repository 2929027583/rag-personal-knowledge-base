import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# 从项目根目录的 .env 读取 API Key
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = client.embeddings.create(
    model="qwen3.7-text-embedding",
    input="FastAPI可以使用Depends实现依赖注入",
    dimensions=1024
)

embedding = response.data[0].embedding

print("Embedding 成功！")
print("向量维度：", len(embedding))
print("前10个向量值：", embedding[:10])
