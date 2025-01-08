from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import os

from dotenv import load_dotenv

_=load_dotenv()

# 数据库配置
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+asyncmy://root:password@localhost/commonagent")

# 创建异步引擎
engine = create_async_engine(DATABASE_URL, echo=True)

# 创建会话工厂
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with AsyncSessionLocal() as session:
        # await session.execute(text("SELECT 1"))
        await session.execute(text("Create table test(id int)"))
        print("Database connection successful")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

import asyncio
if __name__=="__main__":
    asyncio.run(init_db())
