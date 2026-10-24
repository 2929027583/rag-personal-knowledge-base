import os
import re
from html import unescape
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

# 从项目根目录的 .env 读取 API Key
# 默认不会覆盖已存在的真实环境变量，所以 PyCharm 运行配置里配的密钥优先级更高
load_dotenv(Path(__file__).with_name(".env"))

# =========================
# 1. 全局初始化（进程启动时只做一次）
# =========================

_chroma_client = chromadb.PersistentClient(
    path=str(Path(__file__).resolve().parent / "chroma_db")
)
collection = _chroma_client.get_collection(name="my_knowledge")

# 阿里云百炼：负责生成问题向量
_embedding_client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# DeepSeek：负责生成回答
_chat_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 系统提示词
SYSTEM_PROMPT = """
你是一个个人知识库助手。

回答规则：
1. 有笔记来源时，优先基于笔记回答，不要复述原文。
2. 如果【知识库内容】以【本轮无笔记来源】开头，先用一句话说明"以下回答基于通用知识，未引用笔记"，再正常回答；不要因此缩短回答。
3. 只有当你确实不知道时，才说"我不确定"。
4. 先给结论，再作必要解释；全文控制在 5 句话以内，需要分点时最多 3 点；
   用户明确要求详细展开时除外。
5. 禁止使用表格、多级标题、分隔线。
6. 不要编造笔记中的原文、代码片段或具体细节。
"""
# 单次回答最大 token 数，作为长度兜底
MAX_ANSWER_TOKENS = 500
# 检索结果的距离阈值：超过就认为与问题无关，丢弃不用
# 注意：Chroma 默认是 L2 距离（不是余弦相似度），这个值需要用真实问题打印 distance 分布来校准
RELEVANT_DISTANCE = 1.0
# 最多保留 12 条历史消息，约 6 轮对话
MAX_HISTORY_MESSAGES = 12


def clean_note_markdown(text: str) -> str:
    """
    把笔记里的 Markdown / 文档工具语法清洗成可读纯文本。

    建库时 chunk 保留了原始笔记排版，直接返回给前端会看到
    ":::info"、"+ 列表" 这类标记，所以展示前先洗一遍。
    """
    # 1. 去掉 :::info / :::warning / ::: 这类提示块标记（整行）
    text = re.sub(r"^\s*:::\s*\w*\s*$", "", text, flags=re.MULTILINE)

    # 2. 把 "+ 列表" 统一成 "- 列表"
    text = re.sub(r"^\s*\+\s+", "- ", text, flags=re.MULTILINE)

    # 3. 去掉加粗、行内代码、引用符号
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)

    # 4. 去掉笔记工具导出的 HTML 标签（如 <font style="...">）并还原 &nbsp; 等实体
    text = re.sub(r"</?[a-zA-Z][^>]*>", "", text)
    text = unescape(text)

    # 5. source 摘要不需要保留排版，把换行/多空格压成单个空格
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_images(text: str) -> str:
    """
    去掉图片标签，避免把 CDN 链接当正文发给模型。

    笔记里的操作步骤很多是截图，模型读不到图片内容，
    所以这里留一句提示，避免它假装看过截图。
    """
    if "<img" not in text:
        return text

    text = re.sub(r"<img[^>]*>", "", text)
    return text.rstrip() + "\n（本段包含图片，图片中的文字当前无法读取）"


def to_source(chunk: str, distance: float, max_len: int = 120) -> dict:
    """把检索到的原始 chunk 转成前端友好的 source：标题 + 短摘要 + 距离。"""
    title = "未命名片段"
    body = chunk

    # 建库时每段 chunk 都以 "标题路径：xxx" 开头，这里拆出来当标题
    match = re.match(r"^标题路径：(.+?)\s*\n+", chunk)
    if match:
        title = match.group(1).strip()
        body = chunk[match.end():]

    snippet = clean_note_markdown(body)
    if not snippet:
        # 正文只有截图时，清洗后会变成空字符串
        snippet = "（仅图片，无可读文字）" if "<img" in body else ""
    elif len(snippet) > max_len:
        snippet = snippet[:max_len].rstrip() + "…"

    return {
        "title": title,
        "snippet": snippet,
        "distance": round(distance, 4),
    }


# 追问里常见的指代 / 省略标记；命中这些才把上一轮问题拼进检索查询
REFERENCE_MARKERS = (
    "它", "他", "她", "它们", "他们",
    "这个", "那个", "这些", "那些", "这种", "那种",
    "上面", "上述", "刚才", "之前", "前面",
)


def needs_history_context(question: str) -> bool:
    """判断当前问题是否依赖上一轮上下文。"""
    text = question.strip()

    # 代词、指示词、指代上文的说法
    if any(marker in text for marker in REFERENCE_MARKERS):
        return True

    # “那 HLOOKUP 呢”“还有呢”这类省略问法
    if text.startswith("那") or text.endswith("呢"):
        return True

    # “为什么”“怎么做”这种极短追问，通常省略了主语
    if len(text) <= 4:
        return True

    return False


def build_search_query(question: str, history: list[dict]) -> str:
    """
    有历史时，把上一轮用户问题拼到当前问题前面，供检索使用。

    多轮追问经常只有代词，比如“他有什么好处”，单独 embedding
    会丢失指代对象；拼上上一轮问题后，检索更容易命中正确片段。
    注意：这只影响检索，发给模型的仍然是原始 question。
    """
    if not history or not needs_history_context(question):
        return question

    last_user = next(
        (
            message["content"]
            for message in reversed(history)
            if message["role"] == "user"
        ),
        None,
    )
    if not last_user:
        return question

    return f"{last_user}。{question}"


def _embed_text(text: str) -> list[float]:
    response = _embedding_client.embeddings.create(
        model="qwen3.7-text-embedding",
        input=text,
        dimensions=1024,
    )
    return response.data[0].embedding


def _query_candidates(embedding: list[float], limit: int):
    """返回 [(chunk_id, document, distance), ...]。"""
    results = collection.query(
        query_embeddings=[embedding],
        n_results=limit,
        include=["documents", "distances"],
    )
    return list(
        zip(
            results["ids"][0],
            results["documents"][0],
            results["distances"][0],
        )
    )


REWRITE_PROMPT = """
你是一个检索查询改写器。

根据对话历史，把用户最后一句话改写成不依赖上下文、适合向量检索的完整问题。

要求：
1. 补全代词和省略的主语，例如"它"指代上一轮讨论的对象。
2. 保留专有名词、函数名、命令名。
3. 如果最后一句话本身已经完整，原样返回。
4. 只输出改写后的问题，不要解释，不要加引号。
"""

# 改写时最多带最近 6 条消息，约 3 轮对话
MAX_REWRITE_HISTORY = 6


def rewrite_query(question: str, history: list[dict]) -> str:
    """
    用最近几轮历史把追问改写成独立问题。

    只在问题明显依赖上下文时调用；失败时退回原问题，
    不让改写成为整条链路的新故障点。
    """
    if not history or not needs_history_context(question):
        return question

    recent = history[-MAX_REWRITE_HISTORY:]
    history_lines = []
    for message in recent:
        role = "用户" if message["role"] == "user" else "助手"
        history_lines.append(f"{role}：{message['content']}")

    try:
        response = _chat_client.chat.completions.create(
            model="deepseek-chat",
            temperature=0,
            max_tokens=64,
            messages=[
                {"role": "system", "content": REWRITE_PROMPT},
                {
                    "role": "user",
                    "content": (
                        "对话历史：\n"
                        + "\n".join(history_lines)
                        + f"\n\n最后一句话：{question}"
                    ),
                },
            ],
        )
        rewritten = response.choices[0].message.content or ""
    except Exception:
        return question

    rewritten = rewritten.strip().strip('"\'“”‘’')
    if not rewritten or len(rewritten) > 100:
        return question

    return rewritten


def ask(
    question: str,
    history: list[dict] | None = None,
    top_k: int = 2,
) -> tuple[str, list[dict], list[dict]]:
    """
    执行一轮 RAG 问答。

    返回：
        answer      —— AI 回答
        sources     —— 本轮检索到的知识片段（已清洗，供前端展示）
        new_history —— 更新后的对话历史
    """
    history = history or []

    # 有历史且当前问题是追问时，额外生成一个“上一轮问题 + 当前问题”的检索 query
    search_query = build_search_query(question, history)
    queries = [question]
    if search_query != question:
        queries.append(search_query)

    # 再用 LLM 把追问改写成完整问题，作为第三路检索
    rewritten = rewrite_query(question, history)
    if rewritten not in queries:
        queries.append(rewritten)

    # 每个 query 单独检索，再按 chunk id 合并，保留距离更小的那条。
    # 候选池取 max(top_k, 5)，最终仍只保留 top_k 条，响应数量不变。
    candidate_k = max(top_k, 5)
    candidates: dict[str, tuple[str, float]] = {}

    for query_text in queries:
        embedding = _embed_text(query_text)
        for chunk_id, doc, dist in _query_candidates(embedding, candidate_k):
            if chunk_id not in candidates or dist < candidates[chunk_id][1]:
                candidates[chunk_id] = (doc, dist)

    ranked = sorted(candidates.values(), key=lambda item: item[1])

    # 向量检索永远会返回最近邻，不相关时也会“硬凑”出结果，
    # 所以这里按距离再做一次相关性过滤：检出来 ≠ 用得上
    pairs = [
        (doc, dist)
        for doc, dist in ranked
        if dist <= RELEVANT_DISTANCE
    ][:top_k]

    if pairs:
        # 给模型看的上下文：保留原始 Markdown，但把图片链接替换成提示
        context = "\n\n".join(strip_images(doc) for doc, _ in pairs)
        # 给前端看的 sources：清洗后只保留标题 + 短摘要
        sources = [to_source(doc, dist) for doc, dist in pairs]
    else:
        # 没有相关片段时不塞入无关笔记，并明确标记本轮无来源
        context = "【本轮无笔记来源】（请直接用通用知识回答，并按系统提示在开头说明）"
        sources = []

    # 3. 组装消息：系统提示 + 历史对话 + 本轮问题
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({
        "role": "user",
        "content": f"""
【知识库内容】
{context}

【用户问题】
{question}
""",
    })

    # 4. 调用大模型
    response = _chat_client.chat.completions.create(
        model="deepseek-chat",
        temperature=0.2,
        max_tokens=MAX_ANSWER_TOKENS,
        messages=messages,
    )
    answer = response.choices[0].message.content

    # 5. 更新对话历史
    #    只存原始问题和回答，不存带知识库内容的完整 prompt，
    #    否则历史会越滚越大
    new_history = history + [
        {"role": "user", "content": question},
        {"role": "assistant", "content": answer},
    ]
    new_history = new_history[-MAX_HISTORY_MESSAGES:]

    return answer, sources, new_history
