https://laravel-china.org/topics/10243/mysql-8-new-features-required-by-10-developers

### 2. 默认字符集为 utf8mb4

将默认的字符集从 latin-1 转为 utf8mb4。 MySQL支持最新的 Unicode 9.0 基于 DUCET 的新分类。

### 3. **JSON 强化**

MySQL 带来了一些新的 JSON 相关变更：

- 新增  `->>` 表达式，作用等于 `JSON_UNQUOTE(JSON_EXTRACT())`
-  新的聚合函数`JSON_ARRAYAGG()`和`JSON_OBJECTAGG()`
-  新增`JSON_PRETTY()`
-  新的 JSON 工具函数如 `JSON_STORAGE_SIZE()`,`JSON_STORAGE_FREE()`

MySQL 8.0 中 JSON 最重要的优化之一，是提供了一个 `JSON_TABLE()`函数。此函数接受 JSON 格式的数据，然后将其转化为关系型数据表。字段和数据的格式都可以被指定。你也可以对 `JSON_TABLE()`以后的数据使用正常的 SQL 查询，如 JOINS, 聚合查询等, ... 你可以查阅 [@stoker 的博文](http://elephantdolphin.blogspot.be/2017/12/jsontable.html)，当然你也可以阅读 [官方文档](https://dev.mysql.com/doc/refman/8.0/en/json-table-functions.html#function_json-table)。

需要注意的是，这不仅仅影响到开发者的使用，MySQL 的执行性能也会受到影响。在老系统中，更新 JSON 时系统会删除老数据并写入新的数据，在新系统中，如果你要更新 JSON 数据里的某个字段，正确的做法是直接对 JSON 里的某个字段进行更新，这样执行效率更佳，并且数据库主从复制（Replication）性能也会受益。

### 4. 公共表格表达式 (CTEs)

MySQL 8.0 新增了 CTEs 功能（译者注：Common Table Expresssions 公共表格表达式）。CTE 是一个命名的临时结果集，仅在单个 SQL 语句的执行范围内存在，可以是自引用，也可以在同一查询中多次引用。
### 10. InnoDB 引擎 NO WAIT 与 SKIP LOCKED 

MySQL 8.0 的 InnoDB 引擎现在可以更好的处理热行争抢。 InnoDB 支持 `NOWAIT` 和 `SKIP\
LOCKED` 选项与 `SELECT ... FOR\
SHARE` 和 `SELECT ... FOR\
UPDATE` 锁定读取语句。 `NOWAIT` 会在请求行被其他事务锁定的情况下立即返回语句。 `SKIP LOCKED` 从结果集中删除被锁定的行。 参见 [使用 NOWAIT 和 SKIP LOCKED 锁定并发读取](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html#innodb-locking-reads-nowait-skip-locked "Locking Read Concurrency with NOWAIT and SKIP LOCKED").

当然好的 MySQL 8.0 特性列表不会在这里结束， 例如 [**支持正则表达式** ](https://dev.mysql.com/doc/refman/8.0/en/regexp.html) 也是一个刚刚出现在 [8.0.4] 版本中的有趣的特性 (https://mysqlserverteam.com/the-mysql-8-0-4-release-candidate-is-available/)。 新的 SQL `GROUPING()` 功能，  IPV6 和 UUID 操作新业务，更多优化器提示...