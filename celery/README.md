# celery分布式任务
中间人选择: RabbitMQ、redis、DB等
这里使用redis作为中间人
## 创建redis docker
```
docker run -itd --name redis_celery -p 6379:6379 redis:alpine
```
注:Win10下启动可能出现以下错误，可以重新启动docker解决
```
Error response from daemon: driver failed programming external connectivity on endpoint redis_celery (eae1509c7c52eeb5f55f1831c5c64a2ea3a601b3bd5be52b33a93a252275e156): Error starting userland proxy: mkdir /port/tcp:0.0.0.0:6379:tcp:172.17.0.2:6379: input/output error.
```