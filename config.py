import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

SILICON_FLOW_API_KEY = os.getenv("SILICON_FLOW_API_KEY", "")
SILICON_FLOW_BASE_URL = os.getenv("SILICON_FLOW_BASE_URL", "https://api.siliconflow.cn/v1")
SILICON_FLOW_MODEL = os.getenv("SILICON_FLOW_MODEL", "Qwen/Qwen2.5-7B-Instruct")

WECHAT_APP_ID = os.getenv("WECHAT_APP_ID", "")
WECHAT_APP_SECRET = os.getenv("WECHAT_APP_SECRET", "")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
