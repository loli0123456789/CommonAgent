# 使用官方 Python 3.10 运行时作为父镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于 /app 的工作目录下
COPY . /app

# 安装 requirements.txt 中指定的任何所需包
RUN pip install --no-cache-dir -r rs.txt

# 暴露容器的端口
EXPOSE 8000

# 定义环境变量
# ENV NAME World
ENV DATABASE_URL mysql+asyncmy://myagent:oHkbvF8r4F7eju9K@mysql2.sqlpub.com:3307/myagent
ENV ENV production

# 在容器启动时运行 main.py
CMD ["python", "main.py"]
