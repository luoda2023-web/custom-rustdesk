#!/bin/bash
set -e

echo "=== 开始构建LUODA Windows客户端 ==="

# 构建Docker镜像
echo "1. 构建Docker镜像..."
docker build -t luoda-builder -f Dockerfile.windows .

# 运行容器并编译
echo "2. 在Docker容器中编译..."
docker run --rm -v $(pwd):/build luoda-builder

# 复制编译结果
echo "3. 复制编译结果..."
mkdir -p /tmp/luoda-build-output
cp target/x86_64-pc-windows-gnu/release/luoda.exe /tmp/luoda-build-output/

echo "4. 构建完成！EXE文件位置：/tmp/luoda-build-output/luoda.exe"
