# 排序

zset 有序集合，取 TOP N 操作

以某个条件为权重获取数据，比如按顶的次数排序，这时候就需要我们的 sorted set 数据结构，将你要排序的值设置成 sorted set 的 score，将具体的数据设置成相应的 value，每次只需要执行一条 ZADD 命令即可。

```bash
127.0.0.1:6379> zadd top_app 1 wechat
1
127.0.0.1:6379> zadd top_app 1 QQ
1
127.0.0.1:6379> zadd top_app 2 taobao
1
127.0.0.1:6379> zincrby top_app 1 taobao
3
127.0.0.1:6379> zincrby top_app 3 wechat
4
127.0.0.1:6379> zrank top_app QQ
0
127.0.0.1:6379> zrank top_app taobao
1
127.0.0.1:6379> zrank top_app wechat
2
127.0.0.1:6379> zrange top_app 0 -1
QQ
taobao
wechat
```

zset 可以用来存粉丝列表，value 值是粉丝的用户 ID，score 是关注时间。我们可以对粉丝列表按关注时间进行排序。

zset 还可以用来存储学生的成绩，value 值是学生的 ID，score 是他的考试成绩。我们可以对成绩按分数进行排序就可以得到他的名次。

记录帖子的点赞用户 ID 列表，评论 ID 列表，用于显示和去重计数 (zset)。

记录热榜帖子 ID 列表，总热榜和分类热榜 (zset)。

## 精准设定过期时间的应用

利用 sorted set 数据结构，把的 sorted set 的 score 值设置成过期时间的时间戳，那么就可以简单地通过过期时间排序，定时清除过期数据了，不仅是清除 Redis 中的过期数据，你完全可以把 Redis 里这个过期时间当成是对数据库中数据的索引，用 Redis 来找出哪些数据需要过期删除，然后再精准地从数据库中删除相应的记录。

## 取最新 N 个数据的操作

以时间为权重获取数据。

比如获取网站的最新文章，通过下面方式，我们可以将最新的 5000 条评论的 ID 放在 Redis 的 List 集合中，并将超出集合部分从数据库获取。

使用`LPUSH latest.comments`命令，向 list 集合中插入数据 插入完成后再用 `LTRIM latest.comments 0 5000` 命令使其永远只保存最近 5000 个 ID，然后我们在客户端获取某一页评论时可以用下面的逻辑:

```php
function get_latest_comments(start,num_items){
 $id_list = redis.lrange("latest.comments",start,start+num_items-1);
 if(id_list.length < num_items) {
    $id_list = SQL_DB("SELECT ... ORDER BY time LIMIT ...");
 }
 return $id_list;
}
```

如果你还有不同的筛选维度，比如某个分类的最新 N 条，那么你可以再建一个按此分类的 List，只存 ID 的话，Redis 是非常高效的。
