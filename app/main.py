from fastapi import FastAPI
from app import router
app = FastAPI(title="Ollama Python API", version="1.1")

app.include_router(router.health_router, prefix="/health")
app.include_router(router.chat_router, prefix="/chat")

@app.get("/")
async def root():
    return {"message": "API is running"}