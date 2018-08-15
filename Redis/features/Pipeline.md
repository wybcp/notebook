# Pipeline 流水线

Pipeline 将一组 Redis 命令进行打包， 一次性传送给 Redis 处理，再将执行结果按循序返回给客户端。注意，Pipeline 是非原子的。

Pipeline 打包的命令个数不宜过大，可拆分为较小的 Pipeline 分次执行，否则会增加客户端的等待时间和造成网络阻塞。
