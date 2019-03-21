# Pipeline 流水线

Pipeline 将一组 Redis 命令进行打包， 一次性传送给 Redis 处理，再将执行结果按循序返回给客户端。注意，Pipeline 是非原子的。

Pipeline 打包的命令个数不宜过大，可拆分为较小的 Pipeline 分次执行，否则会增加客户端的等待时间和造成网络阻塞。

## 局限性

Pipelining 只能用于执行连续且无相关性的命令，当某个命令的生成需要依赖于前一个命令的返回时，就无法使用 Pipelining 了。
通过 Scripting 功能，可以规避这一局限性
