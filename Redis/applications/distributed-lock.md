# 分布式锁

setnx(set if not exists) 指令：`setnx key value`

## `setnx key value`

上锁的一般情况：

```bash
127.0.0.1:6379[8]> setnx test:lock true
(integer) 1
127.0.0.1:6379[8]> get test:lock
"true"
127.0.0.1:6379[8]> del test:lock
(integer) 1
127.0.0.1:6379[8]> get test:lock
(nil)
```

有个问题，如果逻辑执行到中间出现异常了，可能会导致 del 指令没有被调用，这样就会陷入死锁，锁永远得不到释放。

所以说一般要给锁加上过期时间。

```bash
127.0.0.1:6379[8]> setnx test:lock true
(integer) 1
127.0.0.1:6379[8]> expire test:lock 100
(integer) 1
127.0.0.1:6379[8]> ttl test:lock
(integer) 80
127.0.0.1:6379[8]> del test:lock
(integer) 1
127.0.0.1:6379[8]> ttl test:lock
(integer) -2
```

如果在 setnx 和 expire 之间服务器进程突然挂掉了，可能是因为机器掉电或者是被人为杀掉的，就会导致 expire 得不到执行，也会造成死锁。
拿到锁之后，再给锁加上一个过期时间，比如 5s，这样即使中间出现异常也可以保证 5 秒之后锁会自动释放。

这种问题的根源就在于 setnx 和 expire 是两条指令而不是原子指令。如果这两条指令可以一起执行就不会出现问题。也许你会想到用 Redis 事务来解决。但是这里不行，因为 expire 是依赖于 setnx 的执行结果的，如果 setnx 没抢到锁，expire 是不应该执行的。事务里没有 if-else 分支逻辑，事务的特点是一口气执行，要么全部执行要么一个都不执行。

Redis 2.8 版本中作者加入了 set 指令的扩展参数，使得 setnx 和 expire 指令可以一起执行，彻底解决了分布式锁的乱象。

`SET key value [expiration EX seconds|PX milliseconds] [NX|XX]`

- `EX` _seconds_ -- Set the specified expire time, in seconds.
- `PX` _milliseconds_ -- Set the specified expire time, in milliseconds.
- `NX` -- Only set the key if it does not already exist.
- `XX` -- Only set the key if it already exist.

```bash
set test:lock true ex 100 nx
```

## 超时问题

Redis 的分布式锁不能解决超时问题，如果在加锁和释放锁之间的逻辑执行的太长，以至于超出了锁的超时限制，就会出现问题。因为这时候锁过期了，第二个线程重新持有了这把锁，但是紧接着第一个线程执行完了业务逻辑，就把锁给释放了，第三个线程就会在第二个线程逻辑执行完之间拿到了锁。

为了避免这个问题，Redis 分布式锁不要用于较长时间的任务。

安全一点的方案是为 set 指令的 value 参数设置为一个随机数，释放锁时先匹配随机数是否一致，然后再删除 key，这是为了确保当前线程占有的锁不会被其它线程释放，除非这个锁是过期了被服务器自动释放的。 但是匹配 value 和删除 key 不是一个原子操作，Redis 也没有提供类似于 delifequals 这样的指令，这就需要使用 Lua 脚本来处理了，因为 Lua 脚本可以保证连续多个指令的原子性执行。

## 参考

[应用 1：千帆竞发 —— 分布式锁](https://juejin.im/book/5afc2e5f6fb9a07a9b362527/section/5afc35fb6fb9a07abf72b477)
