# 发布订阅

Redis 作为一个 pub/sub server，在订阅者和发布者之间起到了消息路由的功能。订阅者可以通过`subscribe`和`psubscribe`命令向 redis server 订阅自己感兴趣的消息类型，redis将消息类型称为频道(channel)。当发布者通过`publish`命令向 redis server 发送特定类型的消息时。订阅该消息类型的全部 client 都会收到此消息。这里消息的传递是多对多的。一个client可以订阅多个 channel,也可以向多个 channel 发送消息。

## 实例

终端A：

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
```

终端B:

```shell
127.0.0.1:6379> subscribe comments
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "comments"
3) (integer) 1
```

终端C：

```shell
127.0.0.1:6379> publish comments good!
(integer) 2
```

终端A:

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

终端B：

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

可以使用psubscribe通过通配符进行多个channel的订阅

## 命令

- `publish channel message`：向频道发送消息，返回订阅者个数
- `subscribe channel [channel...]`：订阅频道，进入订阅状态之后，只能接受`subscribe`、`psubscribe`、`unsubscribe`、`punsubscribe`；新开启的订阅客户端，无法接受以前的消息（没有持久化）。
- `unsubscribe [channel]`：取消订阅
- `psubscribe pattern [pattern...]`：按照模式订阅
- `punsubscribe [pattern [pattern...]]`：按照模式取消订阅
- `pubsub channels [pattern]`：查看活跃的频道，指当前频道至少有一个订阅者。
- `pubsub numsub [channel]`：查看频道订阅数
- `pubsub numpat`：查看模式订阅数