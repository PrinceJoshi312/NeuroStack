from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.agents.orchestrator import AgentOrchestrator
from app.core.config import get_settings

router = APIRouter(prefix="/agent", tags=["agent"])

class ChatRequest(BaseModel):
    session_id: str
    message: str
    provider: Optional[str] = "gemini"

class ChatResponse(BaseModel):
    response: str
    session_id: str
    actions_taken: List[Dict[str, Any]]
    plan: List[Dict[str, Any]]

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        orchestrator = AgentOrchestrator(provider_name=request.provider)
        result = await orchestrator.handle_user_request(
            session_id=request.session_id,
            user_input=request.message
        )
        return {
            "response": result["response"],
            "session_id": request.session_id,
            "actions_taken": result["actions_taken"],
            "plan": result["plan"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/session/{session_id}")
async def clear_session(session_id: str):
    from app.memory.tiered_memory import ShortTermMemory
    memory = ShortTermMemory()
    memory.clear_context(session_id)
    return {"message": f"Session {session_id} cleared"}
