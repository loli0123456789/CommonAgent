from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
from typing import List, Dict


import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config.modelConfig import MODEL_CONFIG

from zhipuAI import ZhipuAI
from shushengAI import ShushengAI

router = APIRouter(prefix="/api", tags=["users"])

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# 请求响应模型
class ChatRequest(BaseModel):
    message: str
    model: str = "zhipu"
    conversation_id: str = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str = None

# 对话上下文管理
conversations: Dict[str, List[Dict]] = {}

@router.post("/chat")
def chat_endpoint(request: ChatRequest) -> ChatResponse:
    try:
        # 参数校验
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="消息内容不能为空")
            
        # 获取模型配置
        config = MODEL_CONFIG.get(request.model)
        if not config:
            raise HTTPException(status_code=400, detail="不支持的模型类型")
            
        # 初始化对话上下文
        if not request.conversation_id:
            request.conversation_id = os.urandom(16).hex()
            
        if request.conversation_id not in conversations:
            conversations[request.conversation_id] = [
                {"role": "system", "content": "你是一个有帮助的助手。"}
            ]
            
        # 添加用户消息
        conversations[request.conversation_id].append({
            "role": "user",
            "content": request.message
        })
        
        # 调用模型
        client = ZhipuAI(mod,api_key=config["api_key"], base_url=config["base_url"])
        completion = client.chat.completions.create(
            model=config["model"],
            messages=conversations[request.conversation_id]
        )
        
        # 添加助手回复
        response = completion.choices[0].message.content
        conversations[request.conversation_id].append({
            "role": "assistant",
            "content": response
        })
        
        return ChatResponse(
            response=response,
            conversation_id=request.conversation_id
        )
        
    except Exception as e:
        logger.error(f"对话请求失败: {str(e)}")
        raise HTTPException(status_code=500, detail="服务端错误")
