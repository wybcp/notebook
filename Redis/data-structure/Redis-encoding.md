# 内部编码

```shell
object encoding key
```

查看数据结构内部编码的方式。

通过不同的编码方式实现效率和空间的平衡。

## string 字符串

- int：8 byte 的长整型
- embstr：小于等于 39 byte 的字符串
- raw：大于 39 byte 的字符串

## hash 哈希

- ziplist（压缩列表）：当列表的元素个数小于`hash-max-ziplist-entries`（默认 512 个），且每个元素的小于`hash-max-ziplist-value`（默认 64byte），使用 ziplist 作为列表内部实现。
- hashtable（哈希表）：非 ziplist 时。

## list 列表

- ziplist（压缩列表）：当列表的元素个数小于`list-max-ziplist-entries`（默认 512 个），且每个元素的小于`zset-max-ziplist-value`（默认 64byte），使用 ziplist 作为列表内部实现。
- linkedlist（链表）：非 ziplist 时。

## set 集合

- intset（整数集合）：当集合的元素是整数且个数小于`set-max-intset-entries`（默认 512 个），使用 ziplist 作为列表内部实现。
- hashtable（哈希表）：非 intset 时。

## sorted set 有序集合

- ziplist（压缩列表）：当有序集合的元素个数小于`zset-max-ziplist-entries`（默认 128 个），且每个元素的小于`zset-max-ziplist-value`（默认 64byte），使用 ziplist 作为有序集合内部实现。
- skiplist（跳跃表）：非 ziplist 时。
