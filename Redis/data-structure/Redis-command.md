# redis 数据常见操作

Redis 常用命令参考。

## 一、key

- `keys pattern`:redis 允许模糊查询 key,有 3 个通配符`*、?、[]`。生产环境禁止使用，使用 scan 代替。因为 keys 命令会一次性遍历这个数据库，所以数据库键值对越多，查询越慢。
- `randomkey`：返回随机 key
- `dbsize`：返回当前数据库中键的总和，不需要遍历所有键，直接读取 Redis 内置的键总数变量
- `type key`：返回 key 存储的类型，不存在返回 none
- `exists key`：判断某个 key 是否存在，返回 1 表示存在，0 不存在
- `del key1 key2 ….keyN`：删除 key，返回 1 表示存在，0 不存在
- `rename key newkey`：改名,如果键值比较大，可能存在阻塞情况
- `renamenx key newkey`：如果 newkey 不存在则修改成功
- `move key db`：将 key 移动到 db 数据库，不建议使用
- `ttl key`：查询 key 的生命周期（秒）,三种情况：大于等于 0 的整数，-1 表示没有设置过期时间，-2 表示键不存在。
- `expire key seconds`：设置 key 的生命周期以秒为单位，返回 1 成功，0 表示 key 已经设置过过期时间或者不存在。
- `pexpire key milliseconds`：设置 key 的生命周期以毫秒为单位
- `expireat key seconds-timestamp`：设置 key 在秒时间戳时过期
- `pexpireat key milliseconds-timestamp`：设置 key 在毫秒时间戳时过期
- `pttl key`：查询 key 的生命周期（毫秒）
- `perisist key`：把指定 key 设置为永久有效，即清除过期时间
- `object encoding key`:查看数据结构的内部编码
- `scan cursor`：遍历。以渐进的方式，分多次遍历整个数据库。

  redis-cli 下的扫描:`redis-cli –scan –pattern ‘chenqun_*’`。
  这是用 scan 命令扫描 redis 中的 key，–pattern 选项指定扫描的 key 的 pattern。相比 keys *pattern*模式,不会长时间阻塞 redis 而导致其他客户端的命令请求一直处于阻塞状态。

其实时间在 redis 内部实现的时候都是基于毫秒，对于字符串类型键，**执行 set 时候清除过期时间**，当 client 主动访问 key 会先对 key 进行超时判断，过时的 key 会立刻删除。

如果 clien 永远都不再 get 那条 key 呢？ 它会在 Master 的后台，每秒 10 次的执行如下操作： 随机选取 100 个 key 校验是否过期，如果有 25 个以上的 key 过期了，立刻额外随机选取下 100 个 key(不计算在 10 次之内)。可见，如果过期的 key 不多，它最多每秒回收 200 条左右，如果有超过 25%的 key 过期了，它就会做得更多，但只要 key 不被主动 get，它占用的内存什么时候最终被清理掉只有天知道。

在主从复制环境中，由于上述原因存在已经过期但是没有删除的 key，在主 snap shot 时并不包含这些 key，因此在 slave 环境中我们往往看到 dbsize 较 master 是更小的。

## 二、string 字符串类型的操作

- `set key value [ex seconds][px milliseconds] [nx/xx]`

  如果 ex 和 px 同时写，则以后面的有效期为准

  nx：添加，如果 key 不存在则建立，not exist

  xx：更新，如果 key 存在则修改其值

- `setnx key value`：当多个客户端同时执行`setnx key value`，由于单线程机制，队列执行，根据 setnx 的特性，只有一个客户端能够成功，setnx 可以作为分布式锁的一种实现方式。
- `setex key time value`：设置 key 对应的值 value，并设置有效期为 time 秒
- `get key`：取值，不存在返回 nil
- `mset key1 value1 key2 value2`： 一次设置多个值
- `msetnx key1 value1 … keyN valueN`：一次设置多个值，键不存在时生效
- `mget key1 key2`：一次获取多个值
- `setrange key offset value`：把字符串的 offset 偏移字节改成 value。如果偏移量 > 字符串长度，该字符自动补 0x00。不存在的 key 当作空白字符串处理，可以用作 append。
- `append key value` ：把 value 追加到 key 的原值上，返回新字符串值的长度。
- `getrange key start stop`：获取字符串中[start, stop]范围的值
  对于字符串的下标，左数从 0 开始，右数从-1 开始

注意：当 start>length，则返回空字符串；当 stop>=length，则截取至字符串尾；如果 start 所处位置在 stop 右边，则返回空字符串

- `getset key new_value`：获取并返回旧值，在设置新值，可配合`setnx`可实现分布式锁。
- `incr key`：自增，返回新值，如果 incr 一个不是 int 的 value 则返回错误，incr 一个不存在的 key，则设置 key 为 1
- `decr key`：自减，返回新值，如果 incr 一个不是 int 的 value 则返回错误，incr 一个不存在的 key，则设置 key 为-1
- `incrby key integer`：加指定值 ，key 不存在时候会设置 key，并认为原来的 value 是 0
- `decrby key integer`： 减指定值。decrby 完全是为了可读性，我们完全可以通过 incrby 一个负值来实现同样效果，反之一样。
- `incrbyfloat by floatnumber`： 自增浮点数
- `setbit key offset value`：设置 offset 对应二进制上的值，返回该位上的旧值
  注意：如果 offset 过大，则会在中间填充 0，offset 最大到 2^32-1，即可推出最大的字符串为 512M
- `bitop operation destkey key1 [key2..]`：对 key1 key2 做 opecation 并将结果保存在 destkey 上，opecation 可以是`AND OR NOT XOR`
- `strlen key`：取指定 key 的 value 值的长度

## 三、list 链表操作

Redis 的 list 类型其实就是一个每个子元素都是 string 类型的双向链表，链表的最大长度是 2^32。list 既可以用做栈，也可以用做队列。

list 的 pop 操作还有阻塞版本，主要是为了避免轮询

- `lpush key value [value...]`：把值插入到链表头部
- `lpushx key value`：list 存在则执行，不存在返回 0
- `rpush key value [value...]`：把值插入到链表尾部
- `lpop key` ：返回并删除链表头部元素
- `rpop key`： 返回并删除链表尾部元素
- `lrange key start stop`：返回链表中[start, stop]中的元素；`lrange key 0 -1`列表的所有元素
- `lrem key count value`：从链表中删除 value 值，删除 count 的绝对值个 value 后结束
  count > 0 从表头删除　　 count < 0 从表尾删除　　 count=0 全部删除
- `ltrim key start stop`：剪切 key 对应的链接，切[start, stop]一段并把改制重新赋给 key
- `lindex key index`：返回 index 索引上的值
- `llen key`：计算链表的元素个数
- `linsert key after|before search value`：在 key 链表中寻找 search，并在 search 值之前|之后插入 value
- `rpoplpush source destination`：把 source 的末尾拿出，放到 destination 头部，并返回单元值
  应用场景： task + bak 双链表完成安全队列
  业务逻辑： rpoplpush task bak
  接收返回值并做业务处理
  如果成功则 rpop bak 清除任务，如果不成功，下次从 bak 表取任务

- `lset key index newValue`：修改指定的索引下标的值
- `brpop，blpop key timeout`：等待弹出 key 的尾/头元素、timeout 为等待超时时间，如果 timeout 为 0 则一直等待下去

  应用场景：长轮询 ajax，在线聊天时能用到

  BLPOP/BRPOP 的先到先服务原则

  如果有多个客户端同时因为某个列表而被阻塞，那么当有新值被推入到这个列表时，服务器会按照先到先服务（first in first service）原则，优先向最早被阻塞的客户端返回新值。举个例子，假设列表 lst 为空，那么当客户端 X 执行命令 BLPOP lst timeout 时，客户端 X 将被阻塞。在此之后，客户端 Y 也执行命令 BLPOP lst timeout ，也因此被阻塞。如果这时，客户端 Z 执行命令 RPUSH lst "hello" ，将值 "hello" 推入列表 lst ，那么这个 "hello" 将被返回给客户端 X ，而不是客户端 Y ，因为客户端 X 的被阻塞时间要早于客户端 Y 的被阻塞时间。

## 四、hash 哈希类型操作

Redis hash 是一个 string 类型的 field 和 value 的映射表，它的添加、删除操作都是 O(1)（平均），哈希类型是指键值本身又是一个键值对结构。
hash 特别适用于存储对象，将一个对象存储在 hash 类型中会占用更少的内存，并且可以方便的存取整个对象。

配置：

```config
hash_max_zipmap_entries 64 #配置字段最多64个
hash_max_zipmap_value 512 #配置value最大为512字节
```

- `hset myhash field value`：设置 myhash 的 field 为 value
- `hsetnx myhash field value`：不存在的情况下设置 myhash 的 field 为 value
- `hmset myhash field1 value1 field2 value2`：同时设置多个 field
- `hget myhash field`：获取指定的 hash field
- `hmget myhash field1 field2`：一次获取多个 field
- `hincrby myhash field integer`：指定的 hash field 加上 integer
- `hincrbyfloat myhash field float`：指定的 hash field 加上 float
- `hexists myhash field`：测试指定的 field 是否存在，存在 1，不存在 0
- `hlen myhash`：返回 hash 的 field 数量
- `hdel myhash field [field2...]`：删除指定的 field，返回删除个数
- `hkeys myhash`：返回 hash 所有的 field
- `hvals myhash`：返回 hash 所有的 value
- `hgetall myhash`：获取某个 hash 中全部的 field 及 value；如果哈希元素个数较多，可能存在阻塞 redis 的可能，这时，建议使用 hscan
- `hstrlen myhash field`：获取 hash 的 field 的 value 的长度。

## 五、Set 集合结构操作

特点：无序性、确定性、唯一性

- `sadd key value`：往集合里面添加元素
- `smembers key`：获取集合所有的元素，集合很大时会阻塞，禁止在生产环境使用,sscan 替代
- `srem key value [value...]`：删除集合某个元素，
- `spop key [count]`：返回并删除集合中 1 个随机元素（可以坐抽奖，不会重复抽到某人)
- `srandmember key [count]`：随机取一个元素
- `sismember key value`：判断集合是否有某个值
- `scard key`：返回集合元素的个数
- `smove source destination value`：把 source 的 value 移动到 destination 集合中
- `sinter key1 key2 key3`：求 key1 key2 key3 的交集
- `sinterstore destination key1 key2`：求 key1 key2 的交集并存在 destination 里
- `sunion key1 key2`：求 key1 key2 的并集
- `sunionstore destination key1 key2`：求 key1 key2 的并集
- `sdiff key1 key2`：求 key1 key2 的差集
- `sdiffstore dstkey key1...keyN`：求 key1 key2 的差集并将结果保存于 dstkey

## 六、Sorted Set 有序集合

概念：它是在 set 的基础上增加了一个顺序属性，这一属性在添加修改元素的时候可以指定，每次指定后，zset 会自动按新的值调整顺序。

sorted set 是 string 类型元素的集合，不同的是每个元素都会关联一个 double 型的 score。sorted set 的实现是 skip list 和 hash table 的混合体。

当元素被添加到集合中时，一个元素到 score 的映射被添加到 hash table 中，所以给定一个元素获取 score 的开销是 O(1)。另一个 score 到元素的映射被添加的 skip list，并按照 score 排序，所以就可以有序地获取集合中的元素。添加、删除操作开销都是 O(logN)和 skip list 的开销一致，redis 的 skip list 实现是双向链表，这样就可以逆序从尾部去元素。sorted set 最经常使用方式应该就是作为索引来使用，我们可以把要排序的字段作为 score 存储，对象的 ID 当元素存储。

- `zadd key [NX|XX] [CH] [INCR] score member [score member ...]`：添加元素
  - nx：添加，如果 key 不存在则建立，not exist
  - xx：更新，如果 key 存在则修改其值
  - ch：返回此操作后，有序集合元素和分数发生变化的个数
  - incr：对 score 做增加，相当于 zincrby
- `zrange key start stop [withscore]`：把集合排序后,返回名次[start,stop]的元素 默认是升续排列 withscores 是把 score 也打印出来
- `zrevrange key start stop [withscore]`：把集合排序后,返回名次[start,stop]的元素 默认是降序排列 withscores 是把 score 也打印出来
- `zrank key member`：查询 member 的排名（升序 0 名开始）
- `zrevrank key member`：查询 member 排名（降序 0 名开始）
- `zrangebyscore key min max [withscores] [limit offset N]`：集合（升序）排序后取 score 在[min, max]内的元素，并跳过 offset 个，取出 N 个
- `zrevrangebyscore key max min [withscores] [limit offset N]`：集合（降序）排序后取 score 在[min, max]内的元素，并跳过 offset 个，取出 N 个
- `zremrangebyscore key min max`：按照 score 来删除元素，删除 score 在[min, max]之间
- `zrem key value1 [value2...]`：删除集合中的元素
- `zremrangebyrank key start end`：按排名删除元素，删除名次在[start, end]之间的
- `zincrby key score member`：增加对应 member 的 score 值，然后移动元素并保持 skip list 保持有序。返回更新后的 score 值，可以为负数递减。
- `zcard key`：返回集合元素的个数
- `zcount key min max`：返回[min, max]区间内元素数量
- `zscore key element`：返回指定元素的是 score
- `zinterstore destination numkeys key1 [key2..][weights weight1 [weight2...]] [aggregate SUM|MIN|MAX]`：求 key1，key2 的交集，key1，key2 的权值分别是 weight1，weight2 聚合方法用 sum|min|max 聚合结果 保存子 destination 集合内

- `zunionstore destination numkeys key [key ...][weights weight] [aggregate SUM|MIN|MAX]`：并集计算

注意：weights,aggregate 如何理解？

答：如果有交集，交集元素又有 score，score 怎么处理？aggregate num->score 相加，min 最小 score，max 最大 score，另外可以通过 weights 设置不同的 key 的权重，交集时 score\*weight

## 七、Bitmaps

bitmaps 事实上并不是一种新的数据类型，而是基于字符串位操作的集合，由于字符串是二进制安全的，并且最长可支持 512M，所以它们可以用来存储 2 的 32 次方（ `512*1024*1024*8` ）不同位的数据。

bitmaps 的位操作分成两组：1.固定时间的单个位操作，比如把字符串的某个位设置为 1 或者 0，或者获取某个位上的值 2.对于一组位的操作，对给定的比特范围内，统计设定值为 1 的数目。

bitmaps 最大的优势是在存储**大**数据时可以极大的节省空间，比如在一个项目中采用自增长的 id 来标识用户，就可以仅用 512M 的内存来记录 4 亿用户的信息（比如用户是否希望收到新的通知，用 1 和 0 标识）。

因为许多应用的用户 id 从一个指定数字（例如 1000）开始，直接对应造成一定浪费，可以提前将用户 id 减去指定数字。

- `setbit key offset value`
- `getbit key offset`：没有 offset 也返回 0
- `bitcount key [start] [end]`：返回指定范围内 1 的个数
- `bitop operation destkey key [key...]`：operation 代表 and，or，not，xor 操作，将结果保存于 destkey
- `bitpos key targetBit [start] [end]`：计算第一个为 targetBit 的偏移量

## 八、HyperLogLog

HyperLogLog 主要解决大数据应用中的非精确计数（可能多也可能少，但是会在一个合理的范围）操作，它可以接受多个元素作为输入，并给出输入元素的基数估算值，基数指的是集合中不同元素的数量，一种计数算法。比如 {'apple', 'banana', 'cherry', 'banana', 'apple'} 的基数就是 3 。

HyperLogLog 的优点是，即使输入元素的数量或者体积非常非常大，计算基数所需的空间总是固定的、并且是很小的。在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

关于这个数据类型的误差：在一个大小为 12k 的 key 所存储的 Hyperloglog 集合基数计算的误差是 0.81%。

- `pfadd key element [element...]`：添加元素，成功返回 1
- `pfcount key [key...]`：计算独立元素个数
- `pfmerge destkey sourcekey [sourcekey...]`：求并集保存到 destkey

## 七、服务器相关命令

- ping：测定连接是否存活
- echo：在命令行打印一些内容
- select index：选择数据库
- quit：退出连接
- dbsize：返回当前数据库中 key 的数目
- info：获取服务器的信息和统计
- monitor：实时转储收到的请求
- config get 配置项：获取服务器配置的信息
- flushdb：删除当前选择数据库中所有的 key
- flushall：删除所有数据库中的所有的 key
- time：显示服务器时间，时间戳（秒），微秒数
- bgrewriteaof：后台保存 rdb 快照
- bgsave：后台保存 rdb 快照
- save：保存 rdb 快照
- lastsave：上次保存时间
- shutdown [save/nosave]

注意：如果不小心运行了 flushall，立即 shutdown nosave，关闭服务器，然后手工编辑 aof 文件，去掉文件中的 flushall 相关行，然后开启服务器，就可以倒回原来是数据。如果 flushall 之后，系统恰好 bgwriteaof 了，那么 aof 就清空了，数据丢失。

- dump+restore：实现不同 redis 实例之间进行数据迁移。

  - 源 redis 上使用 dump 命令将键值序列化，RDB 格式`dump key`
  - 目标 redis 上，restore 命令将上面的序列化的数据复原`restore key ttl value`

- `migrate host port key|" " destination-db timeout [COPY] [REPLACE] [KEYS key]`:redis 数据库之间进行数据迁移，具有原子性。

如果要使用多个数据库功能，建议在一个机器上面部署多个 Redis 实例，通过不同的端口区分，现在计算器有多个 cpu，这样有利于使用 CPU 资源。

如果在一个实例上面使用多个数据库，由于单线程，可能会受影响，不利于维护运营，难以定位，有的客户端不支持。
