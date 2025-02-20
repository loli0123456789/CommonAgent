from typing import Any, Dict

import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ai_model.baseAI import BaseAI


class ShushengAI(BaseAI):
    def __init__(self, api_key: str, base_url: str, **kwargs: Dict[str, Any]) -> None:

        if api_key is None:
            api_key = os.environ.get("SHUSHENG_API_KEY")
        if api_key is None:
            raise ShushengAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SHUSHENG_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SHUSHENG_BASE_URL")
        if base_url is None:
            base_url = f"https://internlm-chat.intern-ai.org.cn/puyu/api/v1"

        super().__init__(api_key=api_key, base_url=base_url, **kwargs)



class ShushengAIError(Exception):
    pass