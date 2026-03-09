from pydantic import BaseModel
from typing import Optional

class ArticleGenerateRequest(BaseModel):
    topic: str
    author: Optional[str] = "AI助手"

class ArticleGenerateResponse(BaseModel):
    success: bool
    message: str
    draft_id: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    cover_url: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    message: str
