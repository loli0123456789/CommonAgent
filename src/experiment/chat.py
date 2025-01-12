from openai import OpenAI

from dotenv import load_dotenv
import os

from zhipuAI import ZhipuAI

load_dotenv()

api_key = os.getenv("ZHIPU_API_KEY")
base_url = os.getenv("ZHIPU_BASE_URL")
model="GLM-4-Flash"

# print(api_key, base_url)


def chat():
    client = OpenAI(api_key=api_key, base_url=base_url)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁啊"},
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    print(completion.choices[0].message.content)


def chat_zhipu():
    client = ZhipuAI(api_key=api_key, base_url=base_url)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁啊"},
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    print(completion.choices[0].message.content)


chat_zhipu()
