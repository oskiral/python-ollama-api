from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()
OLLAMA_URL = "http://localhost:11434/api/tags"

@router.get("")
async def get_health():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(OLLAMA_URL, timeout=2.0)
            if response.status_code == 200:
                return {"status": "healthy", "ollama": "online"}
            return {"status": "unhealthy", "ollama": "error"}
        except:
            return {"status": "unhealthy", "ollama": "offline"}