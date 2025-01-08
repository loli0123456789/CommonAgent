# import datetime
import datetime
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    
    # 添加关系（如果需要）
    # items = relationship("Item", back_populates="owner")
