from typing import Any, Dict

import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from experiment.baseAI import BaseAI


class MoonshotAI(BaseAI):
    def __init__(self, api_key: str, base_url: str, **kwargs: Dict[str, Any]) -> None:

        if api_key is None:
            api_key = os.environ.get("MOONSOT_API_KEY")
        if api_key is None:
            raise MoonshotAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MOONSOT_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MOONSOT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.moonshot.cn/v1"

        super().__init__(api_key=api_key, base_url=base_url, **kwargs)



class MoonshotAIError(Exception):
    pass