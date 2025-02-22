import sys
import os
import argparse
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add project root and src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import init_db

# Import core modules
from models import *
from tools import *
from agents import *
from utils import *

app = FastAPI()

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")
parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind the server to")

async def retry_init_db(retry_times=3):
    for i in range(retry_times):
        try:
            await init_db()
            break
        except Exception as e:
            print(f"Failed to connect to database, retrying... ({i+1}/{retry_times})")
            time.sleep(1)

@app.on_event("startup")
async def startup():
    await retry_init_db()

from routers import user
from experiment import chat

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册用户路由
app.include_router(user.router)

# 注册chat路由
app.include_router(chat.router)

@app.get("/api/")
async def root():
    return {
        "code": 200,
        "message": "Hello World",
        "data": None,
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    import uvicorn
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
