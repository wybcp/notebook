# 哨兵

Redis Sentinel 是 Redis 高可用实现方案。

当主节点出现故障，Redis Sentinel 能自动发现故障和故障转移，并通知应用方。

sentinel 节点是独立的 Redis 节点，只不过不存储数据，只能执行部分命令。

## 安装及部署

### master

`redis-6379.conf`:

```conf
port 6379
logfile '6379.log'
dirfilename 'dump-6379.rdb'
dir '/opt/soft/redis/data/'#redis工作目录（存放持久化和日志文件）
daemonize yes # 是否以进程守护的方式启动redis
```

启动 master：`redis-server redis-6379.conf`

### slave

`redis-6380.conf`:

```conf
port 6380
logfile '6380.log'
dirfilename 'dump-6380.rdb'
dir '/opt/soft/redis/data/'#redis工作目录（存放持久化和日志文件）
daemonize yes # 是否以进程守护的方式启动redis
slaveof 127.0.0.1 6379
```

启动 slave：`redis-server redis-6380.conf`

同样的方式启动 6381 slave。

### sentinel

`redis-sentinel-26379.conf`:

```conf
port 26379
dir "/private/tmp"
sentinel monitor mymaster 127.0.0.1 6379 2

sentinel down-after-milliseconds mymaster 30000
#
# Number of milliseconds the master (or any attached slave or sentinel) should
# be unreachable (as in, not acceptable reply to PING, continuously, for the
# specified period) in order to consider it in S_DOWN state (Subjectively
# Down).
#
# Default is 30 seconds.

sentinel parallel-syncs mymaster 1
#
# How many slaves we can reconfigure to point to the new slave simultaneously
# during the failover. Use a low number if you use the slaves to serve query
# to avoid that all the slaves will be unreachable at about the same
# time while performing the synchronization with the master.

sentinel failover-timeout mymaster 180000
#
# Specifies the failover timeout in milliseconds. It is used in many ways:
#
# - The time needed to re-start a failover after a previous failover was
#   already tried against the same master by a given Sentinel, is two
#   times the failover timeout.
#
# - The time needed for a slave replicating to a wrong master according
#   to a Sentinel current configuration, to be forced to replicate
#   with the right master, is exactly the failover timeout (counting since
#   the moment a Sentinel detected the misconfiguration).
#
# - The time needed to cancel a failover that is already in progress but
#   did not produced any configuration change (SLAVEOF NO ONE yet not
#   acknowledged by the promoted slave).
#
# - The maximum time a failover in progress waits for all the slaves to be
#   reconfigured as slaves of the new master. However even after this time
#   the slaves will be reconfigured by the Sentinels anyway, but not with
#   the exact parallel-syncs progression as specified.
#
# Default is 3 minutes.
```

启动 sentinel ：`redis-sentinel redis-sentinel-26379.conf`或`redis-server redis-sentinel-26379.conf --sentinel`。

需要注意的是，配置文件在 sentinel 运行期间是会被动态修改的，例如当发生主备切换时候，配置文件中的 master 会被修改为另外一个 slave。这样，之后 sentinel 如果重启时，就可以根据这个配置来恢复其之前所监控的 redis 集群的状态。

`monitor`：定期监控主节点，quorum 参数用于发现故障和判断，一般设置为 sentinel 节点的一半加 1。

`down-after-milliseconds`：sentinel 会向 master 发送心跳 PING 来确认 master 是否存活，如果 master 在“一定时间范围”内不回应 PONG 或者是回复了一个错误消息，那么这个 sentinel 会主观地(单方面地)认为这个 master 已经不可用了(subjectively down，也简称为 SDOWN)。而这个 down-after-milliseconds 就是用来指定这个“一定时间范围”的，单位是毫秒。

`parallel-syncs`：当新 master 产生时，同时进行“slaveof”到新 master 并进行“SYNC”的 slave 个数，默认为 1，建议保持默认值，在 salve 执行 salveof 与同步时，将会终止客户端请求。

`failover-timeout`：故障转移超时时间，failover 过期时间，当 failover 开始后，在此时间内仍然没有触发任何 failover 操作，当前 sentinel 将会认为此次 failoer 失败。

## API

- `sentinel masters` ：列出所有被监视的主节点，以及这些主节点的当前状态。
- `sentinel slaves <master name>` ：列出给定主节点的所有从节点，以及这些从节点的当前状态。
- `sentinel sentinels <master name>` ：列出给定主节点的所有 sentinel 节点。
- `sentinel get-master-addr-by-name <master name>` ： 返回给定名字的主节点的 IP 地址和端口号。 如果这个主节点正在执行故障转移操作， 或者针对这个主节点的故障转移操作已经完成， 那么这个命令返回新的主节点的 IP 地址和端口号。
- `sentinel reset <pattern>` ： 重置所有名字和给定模式 `pattern` 相匹配的主节点。 `pattern` 参数是一个 Glob 风格的模式。 重置操作清除主节点目前的所有状态， 包括正在执行中的故障转移， 并移除目前已经发现和关联的， 主节点的所有从节点和 Sentinel 。
- `sentinel failover <master name>` ： 当主节点失效时， 在不询问其他 Sentinel 意见的情况下， 强制开始一次自动故障迁移 （不过发起故障转移的 Sentinel 会向其他 Sentinel 发送一个新的配置，其他 Sentinel 会根据这个配置进行相应的更新）。
- `sentinel ckquorum <master name>`：检测当前的 sentinel 节点是否满足 quorum 的要求。
- `sentinel flushconfig`：将当前的 sentinel 配置强制刷到磁盘。
- `sentinel remove <master name>`：移除对指定 master 节点的监控。
- `sentinel monitor <master name> ip port quorum`：监控指定主节点
