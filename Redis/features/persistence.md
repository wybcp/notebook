# 持久化

Redis 支持 RDB 和 AOF 两种持久化，持久化功能有效避免因进程退出造成的数据丢失。

Redis 使用操作系统的多进程 COW(Copy On Write) 机制来实现快照持久化。

## RDB

内存数据的二进制序列化形式。

把当前进程数据生成快照保存在硬盘，采用 LZF 算法。

适合灾难恢复备份，加载速度快。

### 触发机制

#### 手动触发

- save：阻塞当前 Redis 服务器，直到 RDB 完成，不建议线上使用。
- bgsave：redis 进程执行 fork 创建子进程，Redis 持久化过程有子进程负责，建议。

#### 自动触发

- 默认情况下 shutdown，
- 使用 save 相关配置，`save m n`，表示 m 秒数据集存在 n 次修改是自动触发 bgsave。
- 执行 debug reload 重新加载 Redis 时。

## AOF

内存数据修改的指令记录文本。

append only file ，以独立日志的方式记录每次写命令，重启时重新执行 AOF 文件的命令恢复数据，解决数据持久化的实时性问题，主流方案。

默认不开启 AOF，设置：`appendonly`。查询`config get appendonly`

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

## 混合持久化

Redis 4.0 ——混合持久化。将 rdb 文件的内容和增量的 AOF 日志文件存在一起。这里的 AOF 日志不再是全量的日志，而是自持久化开始到持久化结束的这段时间发生的增量 AOF 日志，通常这部分 AOF 日志很小。

## 参考

- [Redis 持久化（persistence）技术口袋书](https://laravel-china.org/articles/15422/redis-persistence-persistence-technology-pocket-book)
