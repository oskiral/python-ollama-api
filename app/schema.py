from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500, examples=["Why is the sky blue?"])
    model_name: Optional[str] = Field(default="mistral", examples=["mistral"])
    temperature: Optional[float] = Field(default=.7, ge=0, le=2, examples=[.7])
    max_tokens: Optional[int] = Field(default=500, gt=0, examples=[500])


class ChatResponse(BaseModel):
    message: str