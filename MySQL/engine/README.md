# MySQL 存储引擎

引擎执行流程:

    SQL命令 》MySQL引擎 进行语法分析-》语法正确-》可识别的命令-》执行-》执行结果-》返回-》客户端

存储过程是 SQL 语句和控制语句的预编译集合，以一个名称存储并作为一个单元处理.

存储过程的优点：

- 第一，增强 SQL 语句的功能和灵活性；
- 第二，实现较快的执行的速度；第三，减少网络流量

MySQL5.5 以后默认使用 InnoDB 存储引擎，其中 InnoDB 和 BDB 提供事务安全表，其它存储引擎都是非事务安全表。

若要修改默认引擎，可以修改配置文件中的`default-storage-engine`。

`show variables like 'default_storage_engine';`查看当前数据库到默认引擎。

`show engines`和`show variables like 'have%'`可以列出当前数据库所支持到引擎。其中 Value 显示为 disabled 的记录表示数据库支持此引擎，而在数据库启动时被禁用。

```sql
mysql> show engines \G;
*************************** 1. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 2. row ***************************
      Engine: MRG_MYISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 3. row ***************************
      Engine: MEMORY
     Support: YES
     Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 4. row ***************************
      Engine: BLACKHOLE
     Support: YES
     Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 5. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 6. row ***************************
      Engine: CSV
     Support: YES
     Comment: CSV storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 7. row ***************************
      Engine: ARCHIVE
     Support: YES
     Comment: Archive storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 8. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 9. row ***************************
      Engine: FEDERATED
     Support: NO
     Comment: Federated MySQL storage engine
Transactions: NULL
          XA: NULL
  Savepoints: NULL
9 rows in set (0.00 sec)

ERROR:
No query specified
```

在 MySQL5.1 以后，INFORMATION_SCHEMA 数据库中存在一个 ENGINES 的表，它提供的信息与 show engines;语句完全一样，可以使用下面语句来查询哪些存储引擎支持事物处理：`select engine from information_chema.engines where transactions = 'yes';`

可以通过 engine 关键字在创建或修改数据库时指定所使用到引擎。

在创建表到时候通过 engine=...或 type=...来指定所要使用到引擎。

`show table status from DBname`来查看指定表到引擎。

## MERGE 存储引擎

Merge 存储引擎是一组 MyISAM 表的组合，这些 MyISAM 表必须结构完全相同，merge 表本身并没有数据，对 merge 类型的表可以进行查询，更新，删除操作，这些操作实际上是对内部的 MyISAM 表进行的。

## 其他表引擎

Archive、Blackhole、CSV、Memory

## 目录
