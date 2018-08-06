# 持久化

Redis支持RDB和AOF两种持久化，持久化功能有效避免因进程退出造成的数据丢失。

## RDB

把当前进程数据生成快照保存在硬盘，采用LZF算法。

适合灾难恢复备份，加载速度快。

### 触发机制

#### 手动触发

- save：阻塞当前 Redis 服务器，直到 RDB 完成，不建议线上使用。
- bgsave：redis 进程执行 fork 创建子进程，Redis 持久化过程有子进程负责，建议。

#### 自动触发

- 默认情况下shutdown，
- 使用 save 相关配置，`save  m n`，表示 m 秒数据集存在 n 次修改是自动触发 bgsave。
- 执行 debug reload 重新加载 Redis时。

## AOF

append only file ，以独立日志的方式记录每次写命令，重启时重新执行 AOF 文件的命令恢复数据，解决数据持久化的实时性问题，主流方案。

默认不开启 AOF，设置：`appendonly`。查询`config get appendonly`

### 1.命令写入 append

AOF命令写入的内容直接是文本协议格式。

### 2.文件同步 sync

appendfsync参数：

- always：不建议，磁盘速度太慢。
- no：提升性能，但无法保证安全。
- everysec：默认配置，建议使用。

### 3.文件重写 rewrite

压缩文件体积，以便更快的被 Redis 加载。

- 进程内超时的数据不再写入文件。
- 旧的 AOF 无效命令清除
- 多条写命令合为一条，过大则拆分为多条。


### 4.重启加载 load
