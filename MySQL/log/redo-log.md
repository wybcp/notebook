# [redo log 重做日志]()

InnoDB 引擎特有的日志

## [`innodb_flush_log_at_trx_commit`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit)

`show variables like 'innodb%';`

1. 如果 innodb_flush_log_at_trx_commit 设置为 0，log buffer 将每秒一次地写入 log file 中，并且 log file 的 flush(刷到磁盘)操作同时进行。该模式下，在事务提交的时候，不会主动触发写入磁盘的操作。
2. 如果 innodb_flush_log_at_trx_commit 设置为 1，每次事务提交时 MySQL 都会把 log buffer 的数据写入 log file，并且 flush(刷到磁盘)中去.
3. 如果 innodb_flush_log_at_trx_commit 设置为 2，每次事务提交时 MySQL 都会把 log buffer 的数据写入 log file。但是 flush(刷到磁盘)操作并不会同时进行。该模式下,MySQL 会每秒执行一次 flush(刷到磁盘)操作。

建议参数设置成 1 ，每次事务的 redo log 都直接持久化到磁盘。

## WAL

Write-Ahead Logging，先写日志，再写磁盘

具体来说，当有一条记录需要更新的时候，InnoDB 引擎就会先把记录写到 redo log 里面并更新内存，这个时候更新就算完成了。同时，InnoDB 引擎会在适当的时候，将这个操作记录更新到磁盘里面，而这个更新往往是在系统比较空闲的时候做。

InnoDB 的 redo log 是固定大小的，比如可以配置为一组 4 个文件，每个文件的大小是 1GB。从头开始写，写到末尾就又回到开头循环写。

两个指针记录：

write pos 是当前记录的位置，一边写一边往后推移并且循环。

checkpoint 是当前要擦除的位置，也是往后推移并且循环的，擦除记录前要把记录更新到数据文件。

write pos 和 checkpoint 之间还空着的部分，可以用来记录新的操作。如果 write pos 追上 checkpoint，这时候不能再执行新的更新，得停下来先擦掉一些记录，把 checkpoint 推进一下。

有了 redo log，InnoDB 就可以保证即使数据库发生异常重启，之前提交的记录都不会丢失，这个能力称为 crash-safe。
