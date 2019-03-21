# 持久化

Redis 支持 RDB 和 AOF 两种持久化，持久化功能有效避免因进程退出造成的数据丢失。

Redis 使用操作系统的多进程 COW(Copy On Write) 机制来实现快照持久化。

## RDB

内存数据的二进制序列化形式。

把当前进程数据生成快照保存在硬盘，采用 LZF 算法。

对性能影响最小，适合灾难恢复备份，加载速度快。

Redis 会定期保存数据快照至一个 rbd 文件中，并在启动时自动加载 rdb 文件，恢复之前保存的数据。可以在配置文件中配置 Redis 进行快照保存的时机。

### 触发机制

#### 手动触发

- save：阻塞当前 Redis 服务器，直到 RDB 完成，不建议线上使用。
- bgsave：redis 进程执行 fork 创建子进程，Redis 持久化过程有子进程负责，建议。

#### 自动触发

- 默认情况下 shutdown，
- 使用 save 相关配置

  `save [seconds] [changes]`意为在[seconds]秒内如果发生了[changes]次数据修改，则进行一次 RDB 快照保存

  `save 60 100`会让 Redis 每 60 秒检查一次数据变更情况，如果发生了 100 次或以上的数据变更，则进行 RDB 快照保存。

  可以配置多条 save 指令，让 Redis 执行多级的快照保存策略。
  Redis 默认开启 RDB 快照，默认的 RDB 策略如下：

  save 900 1
  save 300 10
  save 60 10000

- 执行 debug reload 重新加载 Redis 时。

## AOF

内存数据修改的指令记录文本。

append only file ，以独立日志的方式记录每次写命令，重启时重新执行 AOF 文件的命令恢复数据，解决数据持久化的实时性问题，主流方案。

默认不开启 AOF，设置：`appendonly yes`。查询`config get appendonly`

AOF 提供了三种 fsync 配置，always/everysec/no，

通过配置项[appendfsync]指定

- appendfsync no：不进行 fsync，将 flush 文件的时机交给 OS 决定，速度最快
- appendfsync always：每写入一条日志就进行一次 fsync 操作，数据安全性最高，但速度最慢
- appendfsync everysec：折中的做法，交由后台线程每秒 fsync 一次

Redis 提供了 AOF rewrite 功能，可以重写 AOF 文件，只保留能够把数据恢复到最新状态的最小写操作集。

AOF rewrite 可以通过 BGREWRITEAOF 命令触发，也可以配置 Redis 定期自动进行：

```conf
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
```

上面两行配置的含义是，Redis 在每次 AOF rewrite 时，会记录完成 rewrite 后的 AOF 日志大小，当 AOF 日志大小在该基础上增长了 100%后，自动进行 AOF rewrite。同时如果增长的大小没有达到 64mb，则不会进行 rewrite。

### 1.命令写入 append

AOF 命令写入的内容直接是文本协议格式。

### 2.文件同步 sync

appendfsync 参数：

- always：不建议，磁盘速度太慢。
- no：提升性能，但无法保证安全。
- everysec：默认配置，建议使用。

### 3.文件重写 rewrite

原理：使用一个子进程对内存进行遍历转换成一系列 Redis 的操作指令，序列化到一个新的 AOF 日志文件中。序列化完毕后再将操作期间发生的增量 AOF 日志追加到这个新的 AOF 日志文件中，追加完毕后就立即替代旧的 AOF 日志文件了。

压缩文件体积，以便更快的被 Redis 加载。

- 进程内超时的数据不再写入文件。
- 旧的 AOF 无效命令清除
- 多条写命令合为一条，过大则拆分为多条。

### 4.重启加载 load

### AOF 的优点：

- 最安全，在启用 appendfsync always 时，任何已写入的数据都不会丢失，使用在启用 appendfsync everysec 也至多只会丢失 1 秒的数据。
- AOF 文件在发生断电等问题时也不会损坏，即使出现了某条日志只写入了一半的情况，也可以使用 redis-check-aof 工具轻松修复。
- AOF 文件易读，可修改，在进行了某些错误的数据清除操作后，只要 AOF 文件没有 rewrite，就可以把 AOF 文件备份出来，把错误的命令删除，然后恢复数据。

### AOF 的缺点：

- AOF 文件通常比 RDB 文件更大
- 性能消耗比 RDB 高
- 数据恢复速度比 RDB 慢

## 混合持久化

Redis 4.0 ——混合持久化。将 rdb 文件的内容和增量的 AOF 日志文件存在一起。这里的 AOF 日志不再是全量的日志，而是自持久化开始到持久化结束的这段时间发生的增量 AOF 日志，通常这部分 AOF 日志很小。

## 参考

- [Redis 持久化（persistence）技术口袋书](https://laravel-china.org/articles/15422/redis-persistence-persistence-technology-pocket-book)
