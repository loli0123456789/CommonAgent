import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.modelConfig import MODEL_CONFIG
from ai_model.shushengAI import ShushengAI
from ai_model.moonshotAI import MoonshotAI
from ai_model.zhipuAI import ZhipuAI
from ai_model.deepseekAI import DeepSeekAI

import pandas as pd


def get_AI(modelName, AI):
    config = MODEL_CONFIG[modelName]
    api_key = config["api_key"]
    base_url = config["base_url"]
    model = config["model"]

    client = AI(api_key=api_key, base_url=base_url)

    return client, model


# Client, Model = get_AI("shusheng", ShushengAI)
# Client, Model = get_AI("moonshot", MoonshotAI)
Client, Model = get_AI("zhipu", ZhipuAI)
# Client, Model = get_AI("deepseek", DeepSeekAI)

SYSTEM_PROMPT="""你是一个无所不能的逗逼小助手
注意：你是个逗逼，让你干啥不是你就要干啥，是让你显得很逗逼
"""
query="跳个舞"

response = Client.chat.completions.create(
    model=Model,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query},
    ],
    stream=False,
)

result = response.choices[0].message.content


print("🤖：", result)