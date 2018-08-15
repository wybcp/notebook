# Debug

redis 一般问题处理方法。

## 探测服务是否可用

```shell
127.0.0.1:6379> ping
```

返回 PONG 说明正常。

## 探测服务延迟

```shell
redis-cli --latency
```

显示的单位是 milliseconds，作为参考，千兆网一跳一般延迟为 0.16ms 左右。

## 监控正在请求执行的命令

在 cli 下执行 monitor，**生产环境慎用**

## 查看统计信息

在 cli 下执行`info [section]`，可只查看部分信息：

```shell
127.0.0.1:6379> info
# Server
redis_version:4.0.10
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:57de23d05bb58291
redis_mode:standalone
os:Darwin 18.0.0 x86_64
arch_bits:64
multiplexing_api:kqueue ###调用epoll算法
atomicvar_api:atomic-builtin
gcc_version:4.2.1
process_id:424
run_id:b23e56f483fe0dc56ebf19f7c8ec3ea2a35e7720 ###Redis的随机标识符(用于sentinel和集群)
tcp_port:6379
uptime_in_seconds:188350 ###Redis运行时长(s为单位)
uptime_in_days:2 ###Redis运行时长(天为单位
hz:10
lru_clock:6131865 ###以分钟为单位的自增时钟,用于LRU管理
executable:/usr/local/opt/redis/bin/redis-server
config_file:/usr/local/etc/redis.conf

# Clients
connected_clients:1 ###已连接客户端的数量（不包括通过从属服务器连接的客户端）
client_longest_output_list:0 ###当前连接的客户端中最长的输出列表
client_biggest_input_buf:0 ###当前连接的客户端中最大的。输出缓存
blocked_clients:0 ###正在等待阻塞命令（BLPOP、BRPOP、BRPOPLPUSH）的客户端的数量，需监控

# Memory
used_memory:4881680 ###由 Redis 分配器分配的内存总量，以字节（byte）为单位
used_memory_human:4.66M
used_memory_rss:692224 ###从操作系统的角度，返回 Redis 已分配的内存总量（俗称常驻集大小）。这个值和 top 、 ps 等命令的输出一致，包含了used_memory和内存碎片。
used_memory_rss_human:676.00K
used_memory_peak:4932032 ### Redis 的内存消耗峰值
used_memory_peak_human:4.70M
used_memory_peak_perc:98.98%
used_memory_overhead:1031174
used_memory_startup:980736
used_memory_dataset:3850506
used_memory_dataset_perc:98.71%
total_system_memory:17179869184
total_system_memory_human:16.00G
used_memory_lua:37888
used_memory_lua_human:37.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:0.14 ###   =used_memory_rss /used_memory 这两个参数都包含保存用户k-v数据的内存和redis内部不同数据结构需要占用的内存，并且RSS指的是包含操作系统给redis实例分配的内存，这里面还包含不连续分配所带来的开销。因此在理想情况下， used_memory_rss 的值应该只比 used_memory 稍微高一点儿。当 rss > used ，且两者的值相差较大时，表示存在（内部或外部的）内存碎片。内存碎片的比率可以通过 mem_fragmentation_ratio 的值看出。当 used > rss 时，表示 Redis 的部分内存被操作系统换出到交换空间了，在这种情况下，操作可能会产生明显的延迟。可以说这个值大于1.5或者小于1都是有问题的。当大于1.5的时候需要择机进行服务器重启。当小于1的时候需要对redis进行数据清理
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0

# Persistence
loading:0 ###记录服务器是否正在载入持久化文件，1为正在加载
rdb_changes_since_last_save:0 ###距离最近一次成功创建持久化文件之后，产生了多少次修改数据集的操作
rdb_bgsave_in_progress:0 ###记录了服务器是否正在创建 RDB 文件，1为正在进行
rdb_last_save_time:1532769697 ###最近一次成功创建 RDB 文件的 UNIX 时间戳
rdb_last_bgsave_status:ok ###最近一次创建 RDB 文件的结果是成功还是失败,失败标识为err，这个时候写入redis 的操作可能会停止，因为默认stop-writes-on-bgsave-error是开启的，这个时候如果需要尽快恢复写操作，可以手工将这个选项设置为no。
rdb_last_bgsave_time_sec:0 ###最近一次创建 RDB 文件耗费的秒数
rdb_current_bgsave_time_sec:-1 ###如果服务器正在创建 RDB 文件，那么这个域记录的就是当前的创建操作已经耗费的秒数
rdb_last_cow_size:0
aof_enabled:0 ###AOF 是否处于打开状态，1为启用
aof_rewrite_in_progress:0 ###服务器是否正在创建 AOF 文件
aof_rewrite_scheduled:0 ###RDB 文件创建完毕之后，是否需要执行预约的 AOF 重写操作
aof_last_rewrite_time_sec:-1 ###最近一次创建 AOF 文件耗费的时长
aof_current_rewrite_time_sec:-1  ###如果服务器正在创建 AOF 文件，那么这个域记录的就是当前的创建操作已经耗费的秒数
aof_last_bgrewrite_status:ok ###最近一次创建 AOF 文件的结果是成功还是失败
aof_last_write_status:ok
aof_last_cow_size:0

# Stats
total_connections_received:112 ###服务器已接受的连接请求数量，注意这是个累计值。
total_commands_processed:2454  ###服务器已执行的命令数量，这个数值需要持续监控，如果在一段时间内出现大范围波动说明系统要么出现大量请求，要么出现执行缓慢的操作。
instantaneous_ops_per_sec:0 ###服务器每秒钟执行的命令数量
total_net_input_bytes:74953
total_net_output_bytes:663493
instantaneous_input_kbps:0.01
instantaneous_output_kbps:3.56
rejected_connections:0 ###因为最大客户端数量限制而被拒绝的连接请求数量
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:3 ###因为过期而被自动删除的数据库键数量
expired_stale_perc:0.00
expired_time_cap_reached_count:0
evicted_keys:0 ###因为最大内存容量限制而被驱逐（evict）的键数量。这个数值如果不是0则说明maxmemory被触发，并且evicted_keys一直大于0，则系统的latency增加，此时可以临时提高最大内存，但这只是临时措施，需要从应用着手分析。
keyspace_hits:107 ###查找数据库键成功的次数。
keyspace_misses:4 ###查找数据库键失败的次数。
pubsub_channels:0 ###目前被订阅的频道数量
pubsub_patterns:0 ###目前被订阅的模式数量
latest_fork_usec:327 ###最近一次 fork() 操作耗费的毫秒数
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0

# Replication
role:master ###如果当前服务器没有在复制任何其他服务器，那么这个域的值就是 master ；否则的话，这个域的值就是 slave 。
connected_slaves:0
master_replid:3be71606796f64fef04fa8dfbb9f92d90dbf38fe
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0 ###关闭缓冲复制区
repl_backlog_size:1048576 ###缓冲区最大长度
repl_backlog_first_byte_offset:0 ###起始偏移量，计算当前缓冲区可用范围
repl_backlog_histlen:0 ###已保存数据的有效长度

# CPU
used_cpu_sys:8.45  ###Redis 服务器耗费的系统 CPU
used_cpu_user:3.63  ###Redis 服务器耗费的用户 CPU
used_cpu_sys_children:0.06 ###后台进程耗费的系统 CPU
used_cpu_user_children:0.27 ###后台进程耗费的用户 CPU

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=13,expires=1,avg_ttl=33815865350
db2:keys=1,expires=0,avg_ttl=0 ###keyspace 部分记录了数据库相关的统计信息，比如数据库的键数量、数据库过期键数量等。
```

重新统计`config resetstat`。

## 获取慢查询

`SLOWLOG GET 10`结果为查询 ID、发生时间、运行时长和原命令

```shell
1 ###查询ID
1532858522 ### 发生时间
31298 ###运行时长
info ###原命令
127.0.0.1:51053

0
1532768796
18609
zadd
top_app
1
wechat
127.0.0.1:58826
```

默认 10 毫秒，默认只保留最后的 128 条。单线程的模型下，一个请求占掉 10 毫秒是件大事情，注意设置和显示的单位为微秒，注意这个时间是不包含网络延迟的。

- `slowlog get`：获取慢查询日志
- `slowlog len`：获取慢查询日志条数
- `slowlog reset`：清空慢查询

## 查看客户端

- `client list`：列出所有连接
- `client kill`：杀死某个连接， 例如`CLIENT KILL 127.0.0.1:43501`
- `client getname`：获取连接的名称 默认 nil
- `client setname "名称"`：设置连接名称,便于调试

## 查看日志

日志位置在/redis/log 下，redis.log 为 redis 主日志，sentinel.log 为 sentinel 监控日志。

## 并发延迟检查

top 看到单个 CPU 100%时，就是垂直扩展的时候了。如果需要让 CPU 使用率最大化，可以配置 Redis 实例数对应 CPU 数, Redis 实例数对应端口数(8 核 Cpu, 8 个实例, 8 个端口), 以提高并发。
