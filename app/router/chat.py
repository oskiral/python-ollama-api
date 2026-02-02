from fastapi import APIRouter, HTTPException
from app.schema import ChatRequest, ChatResponse
from app.llm import ask_llm

router = APIRouter()

@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        answer = ask_llm(
            message=req.message,
            model_name=req.model_name,
            temperature=req.temperature,
            max_tokens=req.max_tokens,
        )
        return {"message": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))