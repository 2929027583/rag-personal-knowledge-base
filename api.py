import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from rag import ask, collection

app = FastAPI(
    title="个人知识库 RAG API",
    description="基于 Chroma + DeepSeek 的知识库问答服务",
    version="1.0.0",
)

# 前端页面目录；页面和 /ask 同源（同协议、同主机、同端口），所以不需要 CORS
STATIC_DIR = Path(__file__).parent / "static"

# 内存会话表：session_id -> 对话历史
# 注意：服务重启后会清空；多进程运行时各进程也不共享
sessions: dict[str, list[dict]] = {}


# =========================
# 页面
# =========================

@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


# =========================
# 请求 / 响应模型
# =========================

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="用户问题")
    session_id: str | None = Field(
        default=None,
        description="会话 ID；不传则自动开启新会话",
    )
    top_k: int = Field(
        default=2,
        ge=1,
        le=10,
        description="检索多少条知识片段",
    )


class SourceItem(BaseModel):
    title: str = Field(description="笔记的标题路径")
    snippet: str = Field(description="清洗后的内容摘要")
    distance: float = Field(description="向量距离，越小越相关")


class AskResponse(BaseModel):
    answer: str
    sources: list[SourceItem]
    session_id: str


# =========================
# 接口
# =========================

@app.post("/ask", response_model=AskResponse, summary="知识库问答")
def ask_question(req: AskRequest):
    # 关键点：这里用 def，不要写 async def。
    # OpenAI SDK 和 Chroma 都是同步阻塞调用，FastAPI 会把 def 端点
    # 放进线程池执行；写成 async def 又直接调用同步 SDK，会阻塞整个事件循环。
    session_id = req.session_id or str(uuid.uuid4())
    history = sessions.get(session_id, [])

    try:
        answer, sources, new_history = ask(
            question=req.question,
            history=history,
            top_k=req.top_k,
        )
    except Exception as exc:
        # 502 表示上游服务（Embedding / DeepSeek）出错
        raise HTTPException(
            status_code=502,
            detail=f"生成回答失败：{exc}",
        ) from exc

    sessions[session_id] = new_history

    return AskResponse(
        answer=answer,
        sources=sources,
        session_id=session_id,
    )


@app.get("/health", summary="健康检查")
def health():
    return {
        "status": "ok",
        "documents": collection.count(),
    }


@app.delete("/sessions/{session_id}", summary="清空某个会话的历史")
def reset_session(session_id: str):
    sessions.pop(session_id, None)
    return {"ok": True}


@app.get("/sessions/{session_id}", summary="查看某个会话的历史")
def get_session(session_id: str):
    # 前端用它显示“当前会话第几轮”，刷新页面后也能核对是不是同一个会话
    history = sessions.get(session_id, [])
    return {
        "session_id": session_id,
        "rounds": len(history) // 2,
        "messages": history,
    }