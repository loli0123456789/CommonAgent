
from typing import Any, Dict
from openai import OpenAI

class BaseAI(OpenAI):
    """
    AI基类
    """
    
    def __init__(self,api_key: str, base_url: str, **kwargs: Dict[str, Any]) -> None:

        super().__init__(api_key=api_key, base_url=base_url, **kwargs)

