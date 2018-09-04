# 限流

实现一个限制一定时间执行次数的限制次数的工具。常用于防止攻击防刷等。

还可分为单个应用内的次数限制以及全局的限制。

## 算法

速率限制的传统算法是令牌桶(token bucket)以及 Leaky bucket，提供一个滑动窗口控制速率。
常用于流量整形和流量控制，如带宽的限制。

### 令牌桶算法

令牌桶会以一定速率产生令牌放入桶中，满了以后会丢弃或暂停产生，数据通过时需要持有一个令牌，没有令牌说明超过了速率限制。令牌桶算法允许突发流量，如突然将桶内令牌都消耗完成。

[![令牌桶算法](http://oek9m2h2f.bkt.clouddn.com/token%20bucket.png)](http://oek9m2h2f.bkt.clouddn.com/token%20bucket.png)

### 漏斗算法

漏桶算法中，水以一定速率放到漏桶里，然后漏桶以一定的速率向外流水。所以最大的速率就是出水的速率。不能出现突发流量。

[![漏桶算法](http://oek9m2h2f.bkt.clouddn.com/leak%20bucket.png)](http://oek9m2h2f.bkt.clouddn.com/leak%20bucket.png)

## 实现

RateLimit 除了基本的速率限制外还可能有一些其他的需求
如：

1. 分布式，这样就可以跨进程共享;
2. 滑动窗口: 如果我们限制 1 分钟 10 个，不能出现 0 分钟 59 秒执行 10 个，1 分钟 1 秒后执行 10 个
3. 消息间的最小间隔，防止消息爆炸集中突发

## 使用 redis 实现

首先我们来看一个常见 的简单的限流策略。

系统要限定用户的某个行为在指定的时间里只能允许发生 N 次，如何使用 Redis 的数据结构来实现这个限流的功能？

指定用户 user_id 的某个行为 action_key 在特定的时间内 period 只允许发生一定的次数 max_count。

### 调用这个接口 , 一分钟内只允许最多回复 5 个帖子

解决方案:

这个限流需求中存在一个滑动时间窗口，想想 zset 数据结构的 score 值，是不是可以通过 score 来圈出这个时间窗口来。而且我们只需要保留这个时间窗口，窗口之外的数据都可以砍掉。那这个 zset 的 value 填什么比较合适呢？它只需要保证唯一性即可，用 uuid 会比较浪费空间，那就改用毫秒时间戳吧。

为节省内存，我们只需要保留时间窗口内的行为记录，同时如果用户是冷用户，滑动时间窗口内的行为是空记录，那么这个 zset 就可以从内存中移除，不再占用空间。

通过统计滑动窗口内的行为数量与阈值 max_count 进行比较就可以得出当前的行为是否允许。

用代码表示如下：

```python
# coding: utf8

import time
import redis

client = redis.StrictRedis()

def is_action_allowed(user_id, action_key, period, max_count):
    key = 'hits:%s:%s' % (user_id, action_key)
    now_ts = int(time.time() * 1000)  # 毫秒时间戳
    with client.pipeline() as pipe:  # client 是 StrictRedis 实例
        # 记录行为
        pipe.zadd(key, now_ts, now_ts)  # value 和 score 都使用毫秒时间戳
        # 移除时间窗口之前的行为记录，剩下的都是时间窗口内的
        pipe.zremrangebyscore(key, 0, now_ts - period * 1000)
        # 获取窗口内的行为数量
        pipe.zcard(key)
        # 设置 zset 过期时间，避免冷用户持续占用内存
        # 过期时间应该等于时间窗口的长度，再多宽限 1s
        pipe.expire(key, period + 1)
        # 批量执行
        _, _, current_count, _ = pipe.execute()
    # 比较数量是否超标
    return current_count <= max_count


if __name__ == '__main__':
    for i in range(20):
        print(is_action_allowed("laoqian", "reply", 60, 5))
```

整体思路：每一个行为到来时，都维护一次时间窗口。将时间窗口外的记录全部清理掉，只保留窗口内的记录。zset 集合中只有 score 值非常重要，value 值没有特别的意义，只需要保证它是唯一的就可以了。

因为这几个连续的 Redis 操作都是针对同一个 key 的，使用 pipeline 可以显著提升 Redis 存取效率。但这种方案也有缺点，因为它要记录时间窗口内所有的行为记录，如果这个量很大，比如限定 60s 内操作不得超过 100w 次这样的参数，它是不适合做这样的限流的，因为会消耗大量的存储空间。

## 参考

- <https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/>
- <https://en.wikipedia.org/wiki/Token_bucket>
- <https://en.wikipedia.org/wiki/Leaky_bucket>
- <https://redis.io/commands/incr#pattern-rate-limiter-2>
- <https://www.google.com/patents/CN1536815A?cl=zh>
- [应用 6：断尾求生 —— 简单限流](https://juejin.im/book/5afc2e5f6fb9a07a9b362527/section/5b4477416fb9a04fa259c496)
- [应用 7：一毛不拔 —— 漏斗限流](https://juejin.im/book/5afc2e5f6fb9a07a9b362527/section/5b44aaf75188251a9f248c4c)
