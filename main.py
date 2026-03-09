from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import config
from app.api import routes

app = FastAPI(
    title="微信公众号AI发布助手",
    description="自动生成文章并添加到微信公众号草稿箱",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api", tags=["文章生成"])

@app.get("/")
async def root():
    return {"message": "微信公众号AI发布助手", "docs": "/docs"}

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
