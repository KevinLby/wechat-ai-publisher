from fastapi import APIRouter, HTTPException
from app.models.article import ArticleGenerateRequest, ArticleGenerateResponse, HealthResponse
from app.services.ai_generator import ai_generator
from app.services.wechat import wechat_client
import httpx

router = APIRouter()

DEFAULT_COVER_URL = "https://picsum.photos/800/400"

@router.post("/generate", response_model=ArticleGenerateResponse)
async def generate_article(request: ArticleGenerateRequest):
    try:
        article_data = ai_generator.generate_article(request.topic)
        
        title = article_data.get("title", "无标题")
        author = request.author or article_data.get("author", "AI助手")
        content = article_data.get("content", "")
        digest = article_data.get("digest", "")[:50]
        
        cover_url = DEFAULT_COVER_URL
        try:
            uploaded_url = wechat_client.upload_image(cover_url)
            cover_url = uploaded_url
        except Exception as e:
            print(f"上传封面图失败，使用默认封面: {e}")
        
        draft_id = wechat_client.add_draft(
            title=title,
            author=author,
            content=content,
            cover_url=cover_url,
            digest=digest
        )
        
        return ArticleGenerateResponse(
            success=True,
            message="文章已成功添加到草稿箱",
            draft_id=draft_id,
            title=title,
            author=author,
            cover_url=cover_url
        )
        
    except Exception as e:
        return ArticleGenerateResponse(
            success=False,
            message=f"生成失败: {str(e)}"
        )

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok", message="服务运行正常")
