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
        prompt = f"""你是一个专业的公众号文章写手。请根据以下主题生成一篇高质量的公众号文章。

主题: {topic}

请生成以下格式的内容（JSON格式返回）：
{{
    "title": "文章标题",
    "author": "作者名称",
    "digest": "文章摘要（50字以内）",
    "content": "文章正文内容（HTML格式，可以包含<p>、<h2>等标签）",
    "cover_description": "封面图片描述（用于生成或搜索封面图）"
}}

要求：
1. 文章内容要专业、有深度
2. 使用HTML标签格式化内容
3. 标题要吸引人
4. 内容要有实际价值
5. 返回纯JSON格式，不要有其他内容
"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 4000,
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
