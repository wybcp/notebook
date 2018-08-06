# Redis 客户端

- java：jedis,Redisson
- python：redis-py

## 客户端API

- `client list`：列出相连的所有客户端连接信息。
- `client setName name`：给客户端设置名字。
- `client getName`：获取当前客户端的名字。
- `client kill ip:port` ：杀死指定的ip和端口的客户端。
- `client pouse timeout`：阻塞客户端的timeout毫秒数。
- `monitor`：监控Redis正在执行的命令，如果redis 并发量太大，monitor的输出缓存就会暴涨，占用大量内存。
- `info clients`：客户端统计信息

qbuf 输出缓冲不能超过1 G，否则该客户端将被关闭，不受 maxmemory 控制，可能造成数据丢失等问题。输出缓冲区过大主要是 Redis 处理速度跟不上输入缓存区的输入速度，且进入输入缓冲区的命令中包含大量的 bigkey。

监控输入缓冲区的异常：

- 定期执行 `client list` 查看 qbuf 和 qbuf-free。
- 通过 `info clients` 获得 client_biggest_input_buf 最大输入缓冲区，设置报警。