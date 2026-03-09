import httpx
import json
from typing import Dict, Any
import config

class AIGenerator:
    def __init__(self):
        self.api_key = config.SILICON_FLOW_API_KEY
        self.base_url = config.SILICON_FLOW_BASE_URL
        self.model = config.SILICON_FLOW_MODEL
    
    def generate_article(self, topic: str) -> Dict[str, Any]:
        prompt = f"""根据主题"{topic}"生成一篇简短的公众号文章。

要求（JSON格式返回，仅返回JSON）：
{{
    "title": "标题",
    "author": "作者",
    "digest": "摘要50字",
    "content": "正文HTML格式，3-4段话"
}}

只返回JSON，不要其他内容。"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 1500,
            "temperature": 0.7
        }
        
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code != 200:
                raise Exception(f"API调用失败: {response.text}")
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            try:
                article_data = json.loads(content)
                return article_data
            except json.JSONDecodeError:
                start = content.find('{')
                end = content.rfind('}') + 1
                if start >= 0 and end > start:
                    article_data = json.loads(content[start:end])
                    return article_data
                raise Exception("无法解析AI返回的内容")

ai_generator = AIGenerator()
