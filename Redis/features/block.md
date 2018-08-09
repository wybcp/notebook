# 阻塞

## 内因

### 1.不合理使用API和数据结构

避免在大对象上执行算法复杂度超过O(n)的命令，

#### 发现慢查询

`showlog get {n}`
获取最近n条慢查询命令，默认对执行超过10毫秒的命令记录到一个定长队列（默认为128），线上系统建议设置1毫秒：

- 修改为低算法的命令，禁用keys、sort，修改hgetall为hmget
- 调整大对象

#### 发现大对象

```shell
redis-cli -h {ip} -p {port} --bigkeys
```

### 2.CPU饱和

```shell
redis-cli -h {ip} -p {port} --stat
```

查看当前redis情况，

### 3.持久化阻塞

- fork 阻塞
- AOF 刷盘阻塞
- Hugepage 写操作阻塞

## 外因

### CPU竞争

实例与CPU绑定，降低CPU 频繁切换上下文的开销，注意对于开启持久化或参与复制的主节点不建议绑定。

### 内存交换

查看 Redis 进程号：`redis-cli -p 6379 info server | grep process_id`，根据进程号查询内存交换信息：`cat /proc/{process_id}/swaps | grep Swap`

### 网络问题

- 连接拒绝
- 网络延迟
- 网卡软中断

## 发现阻塞

线上服务收到很多Redis超时异常。

处理方法：在应用中异常统计并通过邮件、短信、微信报警及时发现问题，日志记录异常；Redis 监控系统查看关键指标异常。