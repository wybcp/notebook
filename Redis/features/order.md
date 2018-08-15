# 排序

redis 支持对 list，set 和 sorted set 元素的排序。排序命令是 sort 完整的命令格式如下：

```shell
SORT key [BY pattern] [LIMIT start count] [GET pattern] [ASC|DESC] [ALPHA] [STORE dstkey]
```

复杂度为 O(N+M\*log(M))。(N 是集合大小，M 为返回元素的数量)

说明：

1. [ASC|DESC][alpha]: sort 默认的排序方式（asc）是从小到大排的,当然也可以按照逆序或者按字符顺序排。
2. [BY pattern] : 除了可以按集合元素自身值排序外，还可以将集合元素内容按照给定 pattern 组合成新的 key，并按照新 key 中对应的内容进行排序。例如：
3. 127.0.0.1:6379sort watch:leto by severtity:\* desc
4. [GET pattern]：可以通过 get 选项去获取指定 pattern 作为新 key 对应的值，get 选项可以有多个。例如：127.0.0.1:6379sort watch:leto by severtity:_ get severtity:_。 对于 Hash 的引用，采用->，例如：sort watch:leto get # get bug:\*->priority。
5. [LIMIT start count] 限定返回结果的数量。
6. [STORE dstkey] 把排序结果缓存起来
