# 内部编码

```shell
object encoding key
```

查看数据结构内部编码的方式。

## string字符串

- int：8 byte的长整型
- embstr：小于等于39 byte的字符串
- raw：大于39 byte的字符串

## hash哈希

- ziplist（压缩列表）：当列表的元素个数小于`hash-max-ziplist-entries`（默认512个），且每个元素的小于`hash-max-ziplist-value`（默认64byte），使用ziplist作为列表内部实现。
- hashtable（哈希表）：非ziplist时。

## list列表

- ziplist（压缩列表）：当列表的元素个数小于`list-max-ziplist-entries`（默认512个），且每个元素的小于`zset-max-ziplist-value`（默认64byte），使用ziplist作为列表内部实现。
- linkedlist（链表）：非ziplist时。

## set集合

- intset（整数集合）：当集合的元素是整数且个数小于`set-max-intset-entries`（默认512个），使用ziplist作为列表内部实现。
- hashtable（哈希表）：非intset时。

## sorted set有序集合

- ziplist（压缩列表）：当有序集合的元素个数小于`zset-max-ziplist-entries`（默认128个），且每个元素的小于`zset-max-ziplist-value`（默认64byte），使用ziplist作为有序集合内部实现。
- skiplist（跳跃表）：非ziplist时。
