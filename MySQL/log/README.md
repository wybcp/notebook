# 日志

## MySQL Server

有四种类型的日志：

- [Error Log](error-log.md)：错误日志，记录 mysqld 的一些错误
- [General Query Log](query-log.md)：一般查询日志，记录 mysqld 正在做的事情，非常影响性能
- [Binary Log](binlog.md)：包含了一些事件，这些事件描述了数据库的改动，如建表、数据改动等，也包括一些潜在改动，比如`DELETE FROM ran WHERE bing = luan`，然而一条数据都没被删掉的这种情况。除非使用 Row-based logging，否则会包含所有改动数据的 SQL Statement。
- [Slow Query Log](slow-query-log.md)：慢查询日志，记录一些查询比较慢的 SQL 语句

## 存储引擎

- [redo log](redo-log.md)InnoDB 引擎特有的日志

## 对比

### `redo log` vs `binlog`

- redo log 是 InnoDB 引擎特有的；binlog 是 MySQL 的 Server 层实现的，所有引擎都可以使用。
- redo log 是物理日志，记录的是“在某个数据页上做了什么修改”；binlog 是逻辑日志，记录的是这个语句的原始逻辑，比如“给 ID=2 这一行的 c 字段加 1 ”。
- redo log 是循环写的，空间固定会用完；binlog 是可以追加写入的。“追加写”是指 binlog 文件写到一定大小后会切换到下一个，并不会覆盖以前的日志。
