from fastapi import FastAPI, HTTPException
from app.schema import ChatRequest, ChatResponse
from app.llm import ask_llm

app = FastAPI(title="Ollama Python API", version="1.0")

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        answer = ask_llm(req.message)
        return {"message": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))