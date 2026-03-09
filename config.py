import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

SILICON_FLOW_API_KEY = os.getenv("SILICON_FLOW_API_KEY", "sk-oojwioxyfcvgsctpyzapzxvbvaaqdcfgwitvtopnkjxhiago")
SILICON_FLOW_BASE_URL = os.getenv("SILICON_FLOW_BASE_URL", "https://api.siliconflow.cn/v1")
SILICON_FLOW_MODEL = os.getenv("SILICON_FLOW_MODEL", "deepseek-ai/DeepSeek-R1")

WECHAT_APP_ID = os.getenv("WECHAT_APP_ID", "wxbb663df28cf205b9")
WECHAT_APP_SECRET = os.getenv("WECHAT_APP_SECRET", "5e2a4b05d58b855d771da65ae752a073")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
