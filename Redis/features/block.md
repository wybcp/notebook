# 阻塞

## 内因

### 不合理使用API和数据结构

避免在大对象上执行算法复杂度超过O(n)的命令

#### 发现慢查询

`showlog get {n}`
获取最近n条慢查询命令，默认对执行超过10毫秒的命令记录到一个定长队列（默认为128），线上系统建议设置1毫秒

- 修改为低算法的命令，禁用keys、sort，修改hgetall为hmget
- 调整大对象

#### 发现大对象


```
redis-cli -h {ip} -p {port} bigkeys
```

### CPU饱和

```
redis-cli -h {ip} -p {port} --stat
```
查看当前redis情况，

### 持久化阻塞

- fork阻塞
- AOF刷盘阻塞
- Hugepage写操作阻塞

## 外因

CPU竞争、内存交换、网络问题

## 发现阻塞

线上服务收到很多Redis超时异常。
