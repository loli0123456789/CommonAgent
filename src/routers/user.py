from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import sys
import os
import time

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import User
from db.database import get_db
from schemas.user import UserCreate, UserLogin
from utils.security import get_password_hash, verify_password

router = APIRouter(prefix="/api", tags=["users"])

@router.post("/users/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # 检查用户名是否已存在
    existing_user = await db.execute(
        select(User).where(User.username == user.username)
    )
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # 创建新用户
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return {
        "code": 200,
        "message": "User registered successfully",
        "data": {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        },
        "timestamp": int(time.time())
    }

@router.post("/users/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    # 验证用户
    result = await db.execute(
        select(User).where(User.username == user.username)
    )
    db_user = result.scalar()
    
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 生成token（待实现）
    return {
        "code": 200,
        "message": "Login successful",
        "data": {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        },
        "timestamp": int(time.time())
    }

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return {
        "code": 200,
        "message": "Success",
        "data": [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_time": user.created_time.isoformat() if user.created_time else None
            }
            for user in users
        ],
        "timestamp": int(time.time())
    }
