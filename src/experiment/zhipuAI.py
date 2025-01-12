from typing import Any, Dict
from openai import OpenAI

import os


class ZhipuAI(OpenAI):
    def __init__(self, api_key: str, base_url: str, **kwargs: Dict[str, Any]) -> None:

        if api_key is None:
            api_key = os.environ.get("ZHIPU_API_KEY")
        if api_key is None:
            raise ZhipuAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ZHIPU_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ZHIPU_BASE_URL")
        if base_url is None:
            base_url = f"https://open.bigmodel.cn/api/paas/v4"

        super().__init__(api_key=api_key, base_url=base_url, **kwargs)



class ZhipuAIError(Exception):
    pass