# 限流器

## [Go rate limiter](https://github.com/uber-go/ratelimit)

the leaky-bucket rate limit algorithm

漏桶速率限制算法

## [limiter](https://github.com/ulule/limiter)

Dead simple rate limit middleware for Go.

- Simple API
- "Store" approach for backend
- Redis support (but not tied too)
- Middlewares: HTTP and Gin

### redis

应用 setnx `setnx key value time`设置： 前缀+ip 为键值`key`，`incr key`计数，`time`过期时间

利用 pipeline 设置，检查过期时间，进行判断处理
