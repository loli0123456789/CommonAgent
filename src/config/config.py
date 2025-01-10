import os

# 判断当前环境
env = os.getenv("ENV", "development")  # 默认是开发环境

if env == "production":
    pass
    
else:
    # 开发环境：从 .env 文件加载
    from dotenv import load_dotenv
    load_dotenv()

print(env)

# 数据库配置
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+asyncmy://root:password@localhost/commonagent")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")
