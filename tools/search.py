# import chromadb
#
# # 连接 Chroma（与 build_knowledge.py 使用同一个本地目录，才能读到已建好的库）
# # PersistentClient 从磁盘加载数据，所以这里能直接复用之前构建的知识库
# chroma_client = chromadb.PersistentClient(
#     path="./chroma_db"
# )
#
# # 获取知识库：注意这里用 get_collection（不是 get_or_create）
# # 因为知识库应该已经由 build_knowledge.py 建好了，取不到就会报错
# collection = chroma_client.get_collection(
#     name="my_knowledge"
# )
#
# #print("知识库连接成功！")
# #print("知识库中的文档数量：", collection.count())
#
# # 输入问题：input() 会暂停程序，等待用户在终端里输入并按回车
# question = input("\n请输入你的问题：")
#
# #print("\n你的问题：")
# #print(question)
# import os
# from openai import OpenAI
#
#
# # 创建百炼客户端（用于把文本转成向量）
# # api_key 从环境变量 DASHSCOPE_API_KEY 读取，避免把密钥写死在代码里
# client = OpenAI(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )
#
#
# # 把用户问题转换成向量
# # 关键点：这里必须用和建库时（build_knowledge.py）完全相同的模型和维度，
# # 否则问题和知识库的向量不在同一语义空间，检索会不准甚至报错
# response = client.embeddings.create(
#     model="qwen3.7-text-embedding",
#     input=question,
#     dimensions=1024
# )
#
# # input 传的是单个字符串，所以返回 data 里只有一条结果，取 [0] 即问题的向量
# question_embedding = response.data[0].embedding
#
# #print("\n问题 Embedding 成功！")
# #print("向量维度：", len(question_embedding))
# # =========================
# # 5. 从知识库检索最相关的内容
# # =========================
#
# # query 用问题向量去知识库里找最相似的记录
# #   query_embeddings —— 查询向量，必须是列表（所以包成 [question_embedding]）
# #   n_results        —— 返回最相似的前 2 条
# results = collection.query(
#     query_embeddings=[question_embedding],
#     n_results=2,
#     include=["documents", "distances"]
# )
# # 临时查看检索结果和距离
# for i, document in enumerate(results["documents"][0]):
#     distance = results["distances"][0][i]
#     print(f"结果{i + 1}，距离：{distance:.4f}")
#     print(document[:100])
#     print("-" * 30)
# #print("\n检索结果：")
#
# # results["documents"] 是二维列表：外层对应每个查询，内层才是命中的文档
# # 这里只有一个查询，所以取 [0] 拿到实际的文档列表
# # for i, document in enumerate(results["documents"][0]):
# #     print(f"\n--- 结果 {i + 1} ---")
# #     print(document)
# # =========================
# # 6. 整理检索到的知识
# # =========================
#
# # 把检索到的多段文档用空行拼成一段完整文本，作为"上下文"喂给大模型
# context = "\n\n".join(results["documents"][0])
#
# #print("\n提供给大模型的知识：")
# #print(context)
# # =========================
# # 7. 调用 DeepSeek
# # =========================
#
# # 再创建一个客户端，这次指向 DeepSeek（用于生成最终回答）
# # 用的是另一个环境变量 DEEPSEEK_API_KEY
# deepseek_client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )
#
# # 调用对话接口生成回答
# # messages 是对话历史，两个角色：
# #   system —— 设定大模型的身份和规则（这里要求它只依据知识库回答，不知道就说不知道）
# #   user   —— 用户的提问，这里把"检索到的知识 + 原始问题"一起塞进提示词
# response = deepseek_client.chat.completions.create(
#     model="deepseek-chat",
#     temperature=0.2,
#     messages=[
#         {
#             "role": "system",
#             "content": """
# 你是一个个人知识库助手。
#
# 你的任务是根据提供的知识库内容，帮助用户快速理解和解决问题。
#
# 回答规则：
# 1. 优先使用知识库中的内容。
# 2. 如果知识库内容足够回答问题，就不要额外扩展。
# 3. 可以使用你的通用知识进行解释、总结、举例或推理，但不要偏离用户的问题。
# 4. 先给出结论，再进行必要的解释。
# 5. 回答尽量简洁，一般控制在3～5句话。
# 6. 如果需要分点，最多使用3点。
# 7. 不要重复用户的问题。
# 8. 不要进行无关的扩展。
# 9. 如果知识库没有相关内容，请明确告诉用户“知识库中没有相关内容”，然后可以补充你的通用知识。
# 10. 不要编造知识库中不存在的内容。
#
# 请根据以上规则回答用户的问题。
# """
#         },
#         {
#             "role": "user",
#             "content": f"""
# 【知识库内容】
# {context}
#
# 【用户问题】
# {question}
# """
#         }
#     ]
# )
#
# print("\n========================")
# print("AI回答：")
# print(response.choices[0].message.content)
import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

# 从项目根目录的 .env 读取 API Key
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

# =========================
# 1. 初始化（只做一次，不要放进循环）
# =========================

# 连接知识库
chroma_client = chromadb.PersistentClient(path=str(PROJECT_ROOT / "chroma_db"))
collection = chroma_client.get_collection(name="my_knowledge")

# 向量客户端（阿里云百炼）
embedding_client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 生成客户端（DeepSeek）
deepseek_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

SYSTEM_PROMPT = """
你是一个个人知识库助手。

你的任务是根据提供的知识库内容，帮助用户快速理解和解决问题。

回答规则：
1. 优先使用知识库中的内容。
2. 如果知识库内容足够回答问题，就不要额外扩展。
3. 可以使用你的通用知识进行解释、总结、举例或推理，但不要偏离用户的问题。
4. 先给出结论，再进行必要的解释。
5. 回答尽量简洁，一般控制在3～5句话。
6. 如果需要分点，最多使用3点。
7. 不要重复用户的问题。
8. 不要进行无关的扩展。
9. 如果知识库没有相关内容，请明确告诉用户“知识库中没有相关内容”，然后可以补充你的通用知识。
10. 不要编造知识库中不存在的内容。

请根据以上规则回答用户的问题。
"""

# 用户输入这些词时退出循环
EXIT_WORDS = {"exit", "quit", "q", "退出"}

# 对话历史：多轮对话的关键，必须放在循环外
history = []

# 只保留最近 12 条消息（约 6 轮），防止 prompt 无限变长
MAX_HISTORY_MESSAGES = 12


def ask(question: str) -> str:
    """执行一轮完整的 RAG 问答：问题向量化 -> 检索 -> 调用大模型"""

    # 1. 把问题转成向量（模型和维度要和建库时保持一致）
    response = embedding_client.embeddings.create(
        model="qwen3.7-text-embedding",
        input=question,
        dimensions=1024
    )
    question_embedding = response.data[0].embedding

    # 2. 检索最相关的 2 段知识
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=2,
        include=["documents", "distances"]
    )
    context = "\n\n".join(results["documents"][0])

    # 3. 组装本轮要发给大模型的消息
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)   # 带上之前的对话，AI 才能理解追问
    messages.append({
        "role": "user",
        "content": f"""
【知识库内容】
{context}

【用户问题】
{question}
"""
    })

    # 4. 调用 DeepSeek 生成回答
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        temperature=0.2,
        messages=messages
    )
    answer = response.choices[0].message.content

    # 5. 记录历史
    #    这里只存“原始问题”，不存带知识库内容的完整 prompt，
    #    否则历史会越滚越大，而且旧知识会反复塞给模型
    history.append({"role": "user", "content": question})
    history.append({"role": "assistant", "content": answer})

    # 6. 截断历史，只保留最近几轮
    if len(history) > MAX_HISTORY_MESSAGES:
        del history[:-MAX_HISTORY_MESSAGES]

    return answer


def main():
    print("知识库问答已启动。")
    print("输入问题开始对话；输入 exit / quit / 退出 结束。")
    print("回答过程中按 Ctrl+C 可以取消本轮；在输入提示处按 Ctrl+C 退出。\n")

    while True:
        # ---------- 第一层：输入时按 Ctrl+C = 退出程序 ----------
        try:
            question = input("你：").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n已退出。")
            break

        # 空输入直接跳过
        if not question:
            continue

        # 退出指令
        if question.lower() in EXIT_WORDS:
            print("已退出。")
            break

        # ---------- 第二层：回答过程中按 Ctrl+C = 只取消这一轮 ----------
        try:
            answer = ask(question)
            print(f"\nAI：{answer}\n")
        except KeyboardInterrupt:
            print("\n[已取消本轮回答]\n")
            continue
        except Exception as e:
            # API 报错、网络超时等不应该让整个程序退出
            print(f"\n[出错了] {type(e).__name__}: {e}\n")
            continue


if __name__ == "__main__":
    main()
