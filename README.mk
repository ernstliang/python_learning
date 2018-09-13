# python练习笔记

## 搭建Python virtualenv环境
```
$ python3 -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
```

## grpc
1. 创建python的虚拟环境
2. 安装gRPC和gRPC tools
```
$ python -m pip install grpcio
$ python -m pip install grpcio-tools googleapis-common-protos
```
3. 创建proto文件 test_grpc.proto
4. 编译生成python的pb文件
```
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. test_grpc.proto
```
-I:指定搜索目录<br>
--python_out:指定python pb文件输出目录<br>
--grpc_python_out:指定python grpc pb文件输出目录<br>

5. 创建server和client

## concurrent性能测试
