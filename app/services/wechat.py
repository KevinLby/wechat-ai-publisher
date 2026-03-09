import requests
import json
from typing import Optional, Dict, Any
import config

class WeChatClient:
    def __init__(self):
        self.app_id = config.WECHAT_APP_ID
        self.app_secret = config.WECHAT_APP_SECRET
        self.access_token: Optional[str] = None
        self.token_expires_at = 0
    
    def get_access_token(self) -> str:
        import time
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token
        
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        response = requests.get(url)
        data = response.json()
        
        if "access_token" in data:
            self.access_token = data["access_token"]
            self.token_expires_at = time.time() + data.get("expires_in", 7200) - 300
            return self.access_token
        else:
            raise Exception(f"获取 access_token 失败: {data}")
    
    def upload_image(self, image_url: str) -> str:
        token = self.get_access_token()
        image_data = requests.get(image_url).content
        
        url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"
        files = {"media": ("cover.jpg", image_data, "image/jpeg")}
        response = requests.post(url, files=files)
        data = response.json()
        
        if "media_id" in data:
            return data["media_id"]
        elif "url" in data:
            return data["url"]
        else:
            raise Exception(f"上传图片失败: {data}")
    
    def add_draft(self, title: str, author: str, content: str, cover_url: str = "", digest: str = "") -> str:
        token = self.get_access_token()
        
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
        
        article = {
            "title": title,
            "author": author,
            "content": content
        }
        
        payload = {"articles": [article]}
        print(f"[DEBUG] add_draft payload: {json.dumps(payload)}")
        response = requests.post(url, json=payload)
        data = response.json()
        print(f"[DEBUG] add_draft response: {data}")
        
        if "media_id" in data:
            return data["media_id"]
        else:
            raise Exception(f"添加草稿失败: {data}")

wechat_client = WeChatClient()
