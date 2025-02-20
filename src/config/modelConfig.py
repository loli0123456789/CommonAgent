
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

# 初始化配置
load_dotenv()

# 模型配置
MODEL_CONFIG = {
    "zhipu": {
        "api_key": os.getenv("ZHIPU_API_KEY"),
        "base_url": os.getenv("ZHIPU_BASE_URL"),
        "model": "GLM-4-Flash"
    },
    "shusheng": {
        "api_key": os.getenv("SHUSHENG_API_KEY"),
        "base_url": os.getenv("SHUSHENG_BASE_URL"),
        "model": "internlm3-latest"
    },
    "moonshot": {
        "api_key": os.getenv("MOONSHOT_API_KEY"),
        "base_url": os.getenv("MOONSHOT_BASE_URL"),
        "model": "moonshot-v1-32k"
    },
    "deepseek": {
        "api_key": os.getenv("DEEPSEEK_API_KEY"),
        "base_url": os.getenv("DEEPSEEK_BASE_URL"),
        "model": "deepseek-chat"
    }
}