# 日志

MySQL Server 有四种类型的日志：

- [Error Log](error-log.md)：错误日志，记录 mysqld 的一些错误
- [General Query Log](query-log.md)：一般查询日志，记录 mysqld 正在做的事情，非常影响性能
- [Binary Log](binlog.md)：包含了一些事件，这些事件描述了数据库的改动，如建表、数据改动等，也包括一些潜在改动，比如`DELETE FROM ran WHERE bing = luan`，然而一条数据都没被删掉的这种情况。除非使用 Row-based logging，否则会包含所有改动数据的 SQL Statement。
- [Slow Query Log](slow-query-log.md)：慢查询日志，记录一些查询比较慢的 SQL 语句
