# 发布订阅

Redis 作为一个 pub/sub server，在订阅者和发布者之间起到了消息路由的功能。订阅者可以通过`subscribe`和`psubscribe`命令向 redis server 订阅自己感兴趣的消息类型，redis 将消息类型称为频道(channel)。当发布者通过`publish`命令向 redis server 发送特定类型的消息时。订阅该消息类型的全部 client 都会收到此消息。这里消息的传递是多对多的。一个 client 可以订阅多个 channel,也可以向多个 channel 发送消息。

如果 Redis 停机重启，PubSub 的消息是不会持久化的，所有的消息直接被丢弃。

Redis5.0 新增了 Stream 数据结构，这个功能给 Redis 带来了持久化消息队列，从此 PubSub 可以消失了。

## 实例

终端 A：

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
```

终端 B:

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
```

终端 C：

```shell
127.0.0.1:6379> publish comments good!
(integer) 2
```

终端 A:

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
1) "message"
2) "comments"
3) "good!"
```

终端 B：

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
1) "message"
2) "comments"
3) "good!"
```

可以使用 psubscribe 通过通配符进行多个 channel 的订阅

## 命令

- `publish channel message`：向频道发送消息，返回订阅者个数
- `subscribe channel [channel...]`：订阅频道，进入订阅状态之后，只能接受`subscribe`、`psubscribe`、`unsubscribe`、`punsubscribe`；新开启的订阅客户端，无法接受以前的消息（没有持久化）。
- `unsubscribe [channel]`：取消订阅
- `psubscribe pattern [pattern...]`：按照模式订阅
- `punsubscribe [pattern [pattern...]]`：按照模式取消订阅
- `pubsub channels [pattern]`：查看活跃的频道，指当前频道至少有一个订阅者。
- `pubsub numsub [channel]`：查看频道订阅数
- `pubsub numpat`：查看模式订阅数

## 例子

消费者：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis

client = redis.StrictRedis()
client.publish("codehole", "python comes")
client.publish("codehole", "java comes")
client.publish("codehole", "golang comes")
```

生产者：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import redis

client = redis.StrictRedis()
p = client.pubsub()
p.subscribe("codehole")
# 轮询
# while True:
#     msg = p.get_message()
#     if not msg:
#         time.sleep(1)
#         print('sleep 1s!')
#         continue
#     print(msg)

# listen 来阻塞监听消息
for msg in p.listen():
    print(msg)
```

先启动消费者监听频道，再启动生产者。