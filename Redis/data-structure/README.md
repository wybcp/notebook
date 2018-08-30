# 数据结构

Redis 常见数据结构和命令。

list/set/hash/zset 这四种数据结构是容器型数据结构，它们共享下面两条通用规则：

1. create if not exists

   如果容器不存在，那就创建一个，再进行操作。比如 rpush 操作刚开始是没有列表的，Redis 就会自动创建一个，然后再 rpush 进去新元素。

2. drop if no elements

   如果容器里元素没有了，那么立即删除元素，释放内存。这意味着 lpop 操作到最后一个元素，列表就消失了。

## 目录

- [常见命令参考](Redis-command.md)
- [Redis 数据结构内部编码](Redis-encoding.md)
