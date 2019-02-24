# redis shell

Redis 提供的 shell 工具。

## reids-cli

- `redis-cli --stat` ：实时获取信息
- `redis-cli -h host -p port` ：连接 redis
- `redis-cli --raw`： 返回格式化的结果，能正常显示中文
- `redis-cli --bigkeys`：对 redis 中的 key 进行采样，寻找较大的 keys。不用担心会阻塞 redis 很长时间不能处理其他的请求。执行的结果可以用于分析 redis 的内存的使用状态，每种类型 key 的平均大小。
- `redis-cli --latency`：测试客户端到目标 Redis 的网络延迟`redis-cli -h 127.0.0.1 -p 6379 --latency`,执行一次，取平均
- `redis-cli --latency-history`：测试客户端到目标 Redis 的网络延迟`redis-cli -h 127.0.0.1 -p 6379 --latency-history`,分时段执行多次，取平均

    min: 0, max: 1, avg: 0.17 (1344 samples) -- 15.00 seconds range
    min: 0, max: 1, avg: 0.16 (1337 samples) -- 15.01 seconds range
    min: 0, max: 2, avg: 0.13 (1341 samples) -- 15.01 seconds range

- `redis-cli --latency-dist`：测试客户端到目标 Redis 的网络延迟`redis-cli -h 127.0.0.1 -p 6379 --latency-dist`,分时段执行多次，取平均,输出统计图表。

## redis-server

`redis-server --test-memory 1024` 当前系统能否稳定分配指定容量（1024MB）的内存给 Redis，避免 Redis 崩溃，检测时间较长。

## redis-benchmark

基准测试参数：

- -r（random）：指的是使用随机 key 的范围。
- -n（num）：代表客户端请求总数。
- -c（clients）：代表客户端并发数量（默认 50）。
- -q：显示 requests per second 信息。
- -t：对指定命令执行测试。
- -p：每个请求的 pipeline 数据量（默认 1）
- -k：代表客户端是否使用 keeppalive
- --csv：将测试结果按照 csv 输出

比如：开 100 条线程(默认 50)，SET GET 1 千万次(key 在 0-1 千万间随机)，key 长 21 字节，value 长 256 字节的数据。

```shell
redis-benchmark -t SET,GET -c 100 -n 10000000 -r 10000000 -d 256
```

注意：Redis-Benchmark 的测试结果提供了一个保证你的 Redis-Server 不会运行在非正常状态下的基准点，但是你永远不要把它作为一个真实的“压力测试”。压力测试需要反应出应用的运行方式，并且需要一个尽可能的和生产相似的环境。
