# 使用官方 nginx 镜像作为基础镜像
FROM nginx:alpine

# api主机名
# 默认为 host.docker.internal
# ENV API_HOST host.docker.internal

# 设置工作目录
WORKDIR /usr/share/nginx/html


# 复制打包好的前端文件到工作目录
COPY dist/ .

# 替换 nginx 的默认配置文件（如果需要）
# COPY my.conf /etc/nginx/conf.d/my.conf

# 暴露端口 80
EXPOSE 80
