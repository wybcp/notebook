# 案例应用

- 记录帖子的点赞数、评论数和点击数 (hash)。
- 记录用户的帖子 ID 列表 (排序)，便于快速显示用户的帖子列表 (zset)。
- 记录帖子的标题、摘要、作者和封面信息，用于列表页展示 (hash)。
- 记录帖子的点赞用户 ID 列表，评论 ID 列表，用于显示和去重计数 (zset)。
- 缓存近期热帖内容 (帖子内容空间占用比较大)，减少数据库压力 (hash)。
- 记录帖子的相关文章 ID，根据内容推荐相关帖子 (list)。
- 如果帖子 ID 是整数自增的，可以使用 Redis 来分配帖子 ID(计数器)。
- 收藏集和帖子之间的关系 (zset)。

- 缓存用户行为历史，进行恶意行为过滤 (zset,hash)。

## 目录

- [缓存用户信息](cache-user-info.md)
- [抽奖](lottery.md)
- [排序](order.md)
- [分布式锁](distribution-lock.md)