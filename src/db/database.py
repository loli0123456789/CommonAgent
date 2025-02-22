from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import DATABASE_URL

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
        await session.execute(text("SELECT 1"))
        print("Database connection successful")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

import asyncio
if __name__=="__main__":
    asyncio.run(init_db())
    
async def excute_sql(sql:str):
    async with AsyncSessionLocal() as session:
        result = await session.execute(text(sql))
        if result.returns_rows:
            rows = result.fetchall()
            return rows
        
        return "no data"

