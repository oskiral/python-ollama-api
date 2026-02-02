from fastapi import APIRouter, HTTPException
from app.schema import ChatRequest, ChatResponse
from app.llm import ask_llm

router = APIRouter()

@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        answer = ask_llm(req.message)
        return {"message": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))