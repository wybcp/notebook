# 慢查询分析

Redis 执行一条命令的过程：

1. 发送命令
2. 排队
3. 执行命令
4. 返回结果

慢查询只统计步骤 3 的时间，所以慢查询并不代表客户端没有超时问题。

## 参数

- `slowlog-log-slower-than`：预设阈值，单位微秒，默认值 10000，如果值为 0，记录所有命令，小于 0，所有的都不记录。
- `slowlog-max-len`：慢日志最多存储的条数，列表结构。

## 修改配置

### 修改配置文件

redis.conf

### 动态修改

`config set`：将动态修改持久化到本地配置文件，使用`config rewrite`

```shell
127.0.0.1:6379> config set slowlog-log-slower-than 20000
OK
127.0.0.1:6379> config set slowlog-max-len 2000
OK
127.0.0.1:6379> config rewrite
OK
127.0.0.1:6379> config get slowlog-max-len
1) "slowlog-max-len"
2) "2000"
```

## 查询慢日志

- `slowlog get [n]`：返回当前 redis 的慢查询
- `slowlog len`：返回当前 redis 的慢日志的长度
- `slowlog reset`：重置慢查询日志

慢查询日志由 id、发生时间、耗时、执行命令、客户端等组成。

```shell
127.0.0.1:6379> slowlog get
1) 1) (integer) 2
   2) (integer) 1533197537
   3) (integer) 50600
   4) 1) "config"
      2) "rewrite"
   5) "127.0.0.1:57016"
   6) ""
2) 1) (integer) 1
   2) (integer) 1533197438
   3) (integer) 39651
   4) 1) "config"
      2) "set"
      3) "slowlog-max-len"
      4) "20000"
   5) "127.0.0.1:57016"
   6) ""
3) 1) (integer) 0
   2) (integer) 1533197386
   3) (integer) 41210
   4) 1) "COMMAND"
   5) "127.0.0.1:57016"
   6) ""
```

## 最佳实践

- 建议线上环境最大存储条数设为 1000 以上
- 高 QPS 场景时，将`slowlog-log-slower-than`设置为 1000
- 定期执行`slow get`将慢日志持久化到其他存储中
