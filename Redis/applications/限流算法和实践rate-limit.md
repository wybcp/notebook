# 限流算法和实践 rate-limit

发表于 2016-12-15 | [0 Comments](https://liuzhengyang.github.io/2016/12/15/rate-limit/#comments)| 阅读次数: 1721 | 1475

实现一个限制一定时间执行次数的限制次数的工具。常用于防止攻击防刷等。
例如，1 个 ip1 分钟内最多访问 10 次。
还可分为单个应用内的次数限制以及全局的限制。

# 算法

速率限制的传统算法是令牌桶(token bucket)以及 Leaky bucket，提供一个滑动窗口控制速率。
常用于流量整形和流量控制，如带宽的限制。

## 令牌桶算法

令牌桶会以一定速率产生令牌放入桶中，满了以后会丢弃或暂停产生，数据通过时需要持有一个令牌，没有令牌说明超过了速率限制。令牌桶算法允许突发流量，如突然将桶内令牌都消耗完成。

[![令牌桶算法](http://oek9m2h2f.bkt.clouddn.com/token%20bucket.png)](http://oek9m2h2f.bkt.clouddn.com/token%20bucket.png)

## 漏桶算法

漏桶算法中，水以一定速率放到漏桶里，然后漏桶以一定的速率向外流水。所以最大的速率就是出水的速率。不能出现突发流量。

[![漏桶算法](http://oek9m2h2f.bkt.clouddn.com/leak%20bucket.png)](http://oek9m2h2f.bkt.clouddn.com/leak%20bucket.png)

# 实现

## 其他需求

RateLimit 除了基本的速率限制外还可能有一些其他的需求
如

1. 分布式，这样就可以跨进程共享;
2. 滑动窗口: 如果我们限制 1 分钟 10 个，不能出现 0 分钟 59 秒执行 10 个，1 分钟 1 秒后执行 10 个
3. 消息间的最小间隔，防止消息爆炸集中突发

## 使用 redis 实现

使用 redis 作为一个集中的远程数据管理中心，解决多机器多进程间的数据协调问题。
[Redis](https://redis.io/commands/incr#pattern-rate-limiter-2) 官网提供了一个使用例子，大体思路是添加一个计数 key，并设置它的 expire 过期时间。
根据计数器的值来断定是否超过了次数。

### 实现一

下面是一个简单的实现，限制一个 ip 只能访问 THRE_SHOLD 次，

```
String time = String.valueOf(new Date().getTime() / 1000);
String key = ip + ":" + time;
Jedis jedis = JedisFactory.getJedis();
String s = jedis.get(key);
if (StringUtils.isNotEmpty(s) && Long.parseLong(s) >= THRE_SHOLD) {
    LOGGER.info("exceed max number per interval");
} else {
    Long incr = jedis.incr(key);
    Long expire = jedis.expire(key, 3);
    LOGGER.info("Run");
}
```

如果要实现 1 分钟 10 次限制，可以将除以 1000 的地方改成除以 60\* 1000，但是不能满足上述其他需求中的第二点。

### 实现二

另一种方式为每个 ip 使用一个计数器

```
String s = jedis.get(ip);
if (StringUtils.isNotEmpty(s) && Long.parseLong(s) > 10) {
    System.out.println("Exceed max number");
} else {
    long count = jedis.incr(ip);
    if (count == 1) {
        jedis.expire(ip, 1);
    }
    System.out.println("Run");
}
```

这种方式有一个危险的地方，如果一个 client 执行了 incr 但没有执行 expire，会导致这个 key 一直不失效。

另一种方式是通过 redis 的 list 数据结构和 MULTI 事务支持, 这样的缺点是在限制次数较大时会占用很多 redis 内存

```
FUNCTION LIMIT_API_CALL(ip)
current = LLEN(ip)
IF current > 10 THEN
    ERROR "too many requests per second"
ELSE
    IF EXISTS(ip) == FALSE
        MULTI
            RPUSH(ip,ip)
            EXPIRE(ip,1)
        EXEC
    ELSE
        RPUSHX(ip,ip)
    END
    PERFORM_API_CALL()
END
```

## 使用 Guava 实现

Guava 中的 RateLimit 可以用于速率限制，和 Semaphore 不同，Semaphore 用于限制资源的并发获取数量，RateLimit 限制速率，但是并发量和速率又是有一定的关联。
acquire()方法会阻塞调用，tryAcquire()会直接返回 true 和 false 表示是否获取到的许可。
`RateLimit.create()`方法的参数表示 1 秒内允许获得的数量。RateLimiter 的实现中`SmoothRateLimiter`会限制获取的间隔时间，例如参数是 10 的 RateLimiter, T0 请求时间是 0.0s, T1 在 0.01 秒请求是会 wait 到 0.1 秒才能被执行。

```
// 创建一个1秒钟限制执行10次的RateLimitter
RateLimiter rateLimiter = RateLimiter.create(10);

for (int i = 0; i < 100; i++) {
    rateLimiter.acquire(1);
    System.out.println("acquirer success " + new Date().getTime());

}
```

从这个日志也可以看出获取的间隔时间。

## 使用 Hystrix

[Hystrix](https://github.com/Netflix/Hystrix)越来越流行了，从 15 年开始调研这个项目后公司越来越多的部门、小组都开始使用 Hystrix 为提供降级熔断隔离等功能。Hystrix 也可以作为一种限流方案，使用起来还比较简单，也有和 Spring 结合的注解方式，更多可以参考它的 wiki。

## 其他

# 参考

- <https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/>
- <https://en.wikipedia.org/wiki/Token_bucket>
- <https://en.wikipedia.org/wiki/Leaky_bucket>
- <https://redis.io/commands/incr#pattern-rate-limiter-2>
- <https://www.google.com/patents/CN1536815A?cl=zh>
