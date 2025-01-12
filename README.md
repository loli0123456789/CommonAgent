# CommonAgent 项目

## 项目概述
CommonAgent 是一个通用智能体平台，旨在为开发者提供构建AI应用的统一框架和工具集。

A lightweight framework for a simple agent, which is utilized for studying AI and, at the same time, for acquiring knowledge about frontend and backend development.

## 技术栈
- 后端：FastAPI + Uvicorn
- 前端：Vue 3 + TypeScript
- 数据库：MySQL
- 环境管理：Conda
- 部署：Docker + Kubernetes

## 项目结构
```
CommonAgent/
├── docker/             # docker相关文件
├── docs/               # 项目文档
├── frontend/           # 前端源代码
├── src/                # 后端源代码
├── tests/              # 测试代码
├── README.md           # 项目说明
└── requirements.txt    # Python依赖
```

## 快速开始
- 后端

cd src

conda create -n commonagent

conda activate commonagent

pip install -r requirements.txt

python main.py

- 前端

cd frontend

npm install

npm run dev

**注意**：

    在frontend下.env文件配置后端api地址：VITE_DEV_API_URL=http://localhost:8000/api

## docker部署
- 后端

cd src

docker build -t backend:01 .

docker run -d -p 8000:8000 --name backend backend:01

**注意**：

    在src下dockerfile定义了docker构建信息，需要修改相关配置

- 前端

cd frontend

docker build -t frontend:01 .

docker run -d -p 8080:8080 --name -v frontend\nginx\conf.d:/etc/nginx/conf.d frontend frontend:01

**注意**：
    
    在frontend下dockerfile定义了docker构建信息，需要修改相关配置

    在frontend下nginx\conf.d\default.conf定义了nginx配置，需要修改相关配置，以便动态设置后端api代理地址

    -v 参数中宿主机路径在windows下需要是磁盘完整路径

## docker镜像制作

为了方便讲docker部署到服务器，可以制作docker镜像

docker save backend:01 -o backend-01.tar

docker save frontend:01 -o frontend-01.tar

将镜像上传到服务器后

docker load -i backend-01.tar

docker load -i frontend-01.tar

同时把frontend下nginx\conf.d\my.conf中的api地址修改为服务器地址

然后执行

docker run -d -p 8000:8000 --name backend backend:01

docker run -d -p 8080:8080 --name -v ~/nginx/conf.d:/etc/nginx/conf.d frontend frontend:01

**注意**：

    -v 参数中宿主机路径在Linux下不需要是磁盘完整路径


## 其他资源
数据库mysql，使用 https://sqlpub.com/
