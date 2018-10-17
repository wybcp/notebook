# MySQL 复制

主要用于主服务器和从服务器之间的数据异步复制操作。

网络延迟是产生 MySQL 主从不同步的主要原因，推荐使用 InnoDB 存储引擎，主机开启 sysc_binlog，设置主从服务器的 `max_allowed_packet=5M`

## 复制有哪些用途

- 读写分离
- 灾备
- 高可用
- 线下统计
- 备份

## 复制是如何工作的

![img](https://user-gold-cdn.xitu.io/2017/3/29/9e38d215a38df0042e3b75992d6855f7?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

复制的主要步骤：

1. master 将改变记录到二进制日志 binary log 中
2. slave 上的 IO 线程将主库上的日志复制到自己的 relay log 的最后面，并将 master 的文件名和位置记录到 master-info 文件中
3. slave 上 SQL 线程回放中继日志的内容，使 slave 上的数据与 master 达到一致

binlog 二进制日志文件，用于记录 MySQL 的数据变更。

relay-log 中继日志文件，slave 的 I/O 线程读取 master 的 binlog，记录到 relay-log 中，然后 SQL 线程会读取 relay-log 日志的内容并应用到 slave 服务器。

## 创建复制账号

replication slave 权限

```bash
mysql>grant replication slave on *.* to 'rep_1'@'host' identified by 'password';
mysql>flush privileges;
```

流程

```bash
# 设置锁定
mysql>flush tables with read lock;
#查询master当前的二进制日志名和偏移量
mysql>show master status;
# 生成备份文件dump，从服务器加载
#解锁
mysql>unlock tables;
# 修改从服务器配置文件，增加server_id等参数，唯一server_id

# 从服务器上使用--skip-slave-start启动服务器，这样不会立即启动从服务器上的复制过程，等待配置服务
mysqld_safe --skip-slave-start
# 从服务器设置
msyql>stop slave;
mysql>change master to
->master_host='',
->master_user='rep_1',
->master_password='password',
->master_log_file='mysql-bin.00001',
->master_log_pos=11;
# 启动slave线程
mysql>start slave;
```

## binlog 记录的格式

STATEMENT（记录操作的 SQL 语句）

- 优点 减少了 binlog 日志量，节约 IO，提高性能，易于理解
- 缺点 不是所有的 DML 语句都能被复制，有些函数 UUID() 、FOUND_ROWS()、USER() 也无法被复制

ROW（记录操作的每一行数据的变化信息，RC 隔离级别，必须是 row 格式）

- 优点 任何情况都可以被复制，ROW 模式是最安全可靠的
- 缺点 产生大量的日志，特别是 copy data 的 DDL 会让日志暴涨
- 建议表一定要有主键

MIXED （混合模式）

- 先使用 STATEMENT 模式记录 binlog ，对于 STATEMENT 模式无法复制的操作使用 ROW 模式保存 binlog，MySQL 会根据执行的 SQL 语句选择日志记录方式。Bug 较多，不建议使用。

## binlog Events

我们都知道　 binlog 日志用于记录所有对 MySQL 的操作的变更，而这每一个变更都会对应的事件，也就是 Event，index 文件记录了所有的 binlog 位置，每个 binlog 会有 header event，rotate 三个 event，binlog 的结构如下。

![img](https://user-gold-cdn.xitu.io/2017/3/29/4a6a030e217be904de9bbe4cbb4c9f9c?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

常见的 Event 如下：

- Format_desc：全新的 binlog 日志文件
- Rotate ：日志分割
- Table_map：表，列等元数据
- Query：查询
- Write_rows: 插入
- Update_rows：更新
- Delete_rows：删除

![img](https://user-gold-cdn.xitu.io/2017/3/29/e58b4977697eb91e39cc37b8bf0bd4d5?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

### 事务是如何提交的？事务提交先写 binlog 还是 redo log？

![img](https://user-gold-cdn.xitu.io/2017/3/29/3af97e52b55f7af559446998ea68c21b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

以上的图片中可以看到，事务的提交主要分三个主要步骤：

1. InnoDB 层写 prepare log，此时 SQL 已经成功执行，并生成 xid 信息及 redo 和 undo 的内存日志，写入 redo log file
2. MySQL Server 层写 binlog （write --》 fsync）
3. InnoDB 层写 commit log， InnoDB 存储引擎内提交，使 undo 和 redo 永久写入磁盘

### 为什么 MySQL 有 binlog，还有 redo log

这个是因为 MySQL 体系结构的原因，MySQL 是多存储引擎的，不管使用那种存储引擎，都会有 binlog，而不一定有 redo log，简单的说，binlog 是 MySQL Server 层的，redo log 是 InnoDB 层的。

### 如何保证这两部分的日志做到一致性？

事务提交的过程上面已经说到，需要写 redo log 还要写 binlog，那么如何保证数据的一致性呢，如果不能保证写这两个文件在同一事务中，那么就会造成数据不一致，这个不一致包括 MySQL crash 时和主从复制的数据不一致。

面试时经常会问的一个问题，影响 MySQL 写入性能、数据一致性的参数有哪些？无疑是 双一参数 innodb_flush_log_at_trx_commit 和 sync_binlog， 这两个参数是控制 MySQL 磁盘写入策略以及数据安全性的关键参数，MySQL 为了保证 master 和 slave 的数据一致性，就必须保证 binlog 和 InnoDB redo 日志的一致性。

参数说明如下：

innodb_flush_log_at_trx_commit（redo）

- 0 log buffer 每秒一次地写入 log file 中，且进行 flush 操作
- 1 每次事务提交时都会把 log buffer 的数据写入 log file，并进行 flush 操作
- 2 每次事务提交时 MySQL 都会把 log buffer 的数据写入 log file，不进行 flush 操作

sync_binlog （binlog）

- 0 刷新 binlog_cache 中的信息到磁盘由 os 决定
- N 每 N 次事务提交刷新 binlog_cache 中的信息到磁盘

那么如何保证 binlog 和 InnoDB redo 日志的一致性，MySQL 使用内部分布式事物来保证一致性，MySQL 在 prepare 阶段会生成 xid，xid 会写入 prepare log 中，也会写入到 binlog 中，当恢复时会对比此事务的 xid 在两个文件中是否都有，如果都存在该 xid 对应的事物会提交，反之会 rollback 此事务，下面是几种情况分析：

1. 当事务在 prepare 阶段 crash，将该事务 rollback。
2. 当事务在 binlog 阶段 crash，此时日志还没有成功写入到磁盘中，启动时会 rollback 此事务
3. 当事务在 binlog 日志已经 fsync() 到磁盘后 crash，但是 InnoDB 没有来得及 commit,此时 MySQL 启动时会重新将该事务重做并 commit，使 InnoDB 存储引擎的 redo log 和 binlog 始终保持一致。

总结起来说就是如果一个事物在 prepare log 阶段中落盘成功，并在 MySQL Server 层中的 binlog 也写入成功，那这个事务必定 commit 成功。

## 组提交

现在回头看事务是如何提交的那张图，会发现 innodb 层每个事务是并行的，但是在写 binlog 时，MySQL Server 层就变成了串行，这是因为每次提交都会去申请 prepare_commit_mutex 这把锁造成的，在 MySQL 5.6 版本中，提供了 Binary Log Group Commit 也就是组提交，Group Commit 分为了三个阶段。

![img](https://user-gold-cdn.xitu.io/2017/3/29/2b04897f7ca02deb0eb1df0ea09dd9fb?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

- Flush stage：Leader 线程遍历 FLUSH_STAGE 链表，写入 binary log 缓存
- Sync stage ：将 binlog 缓存 sync 到磁盘，当 sync_binlog=1 时所有该队列事务的二进制日志缓存永久写入磁盘
- Commit stage: leader 根据顺序让 InnoDB 存储引擎完成 Commit

下面是我们测试组提交的一张图，可以看到组提交的 TPS 高不少。

![img](https://user-gold-cdn.xitu.io/2017/3/29/869f5e43498c2b7ebce1f6769c1e114d?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

## 1062、1053 复制错误

可能 DBA 在使用 MySQL Replication 的过程中，在 slave 宕机或异常时，会遇到 1062 等错误，大家都是使用以下方式解决。

- SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1
- GTID 通过空事务方式

但为什么数据会冲突呢？我们分解下复制的步骤，这里有张图很好，图片来自于网络。

![img](https://user-gold-cdn.xitu.io/2017/3/29/e54e3fb1c513f78358ce8482a4fcaf14?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

我们可以看到这里有保存 Replication matadata 的两个文件，

- **relay-info.log**保存了 SQL 线程回放到的 Relay_log_name 和 Relay_log_pos，以及对应的 Master 的 Master_log_name 和 Master_log_pos。
- **master-info.log**保存了连接 master 的用户，密码，端口，Master_log_name 和 Master_log_pos 等信息。

如下图，如果 SQL 线程正在回放，回放完后，还没来的及写到 Replication matadata 的文件中，就宕机了，此时重启 slave 后，就会出现 1062 错误。

![img](https://user-gold-cdn.xitu.io/2017/3/29/344cf9b245bee85701ac2b3817efbcba?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

在 MySQL 5.6 中，提供了 SQL/IO thread crash-safe 特性。通过将 relay_log_info_repository=TABLE，relay-info 将信息写入到 mysql.slave_relay_log_info 这张表中，不但可以保证一致性（写文件变成同一事物的原子操作），还提高了写入性能。 ![img](https://user-gold-cdn.xitu.io/2017/3/29/6666ccab47ebba41f0cf918899b2daab?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

如上图。IO thread 同理，稍有不同的是 relay-log-recover 设置为 1 后，slave 的 IO thread 读取 events 时，会根据从 SQL thread 回放到的位置重新读取。

## 复制参数

### 从服务器

- `log-slave-updates`：配置从服务器的更新是否写入二进制日志，默认关闭
- `master-connect-retry`：连接丢失时重连的时间间隔，默认为 60s
- `read-only`：限制普通用户对从数据库的更新操作
- `slave-skip-errors`：复制过程中从服务器自动跳过错误，my.cnf`slave-skip-errors=1007,1051,1062`

### 主服务器

- `binlog-do-db=test`需要复制的数据库
- `binlog-ignore-db=test` 复制时忽略的数据库
- `binlog-do-table=test.test` 需要复制的数据库表
- `binlog-ignore-table=test.test` 复制时忽略的数据库表

### 复制最优的参数配置

上面讲了这么多，其实就是得出 MySQL Replication 的最可靠的参数配置。

master：

```config
binlog_format = ROW
transaction-isolation = READ-COMMITTE
Dexpire_logs_days = 30

server-id = 327
sync_binlog = 1
innodb_flush_log_at_trx_commit = 1
innodb_support_xa = 1
# 需要复制的数据库
binlog-do-db=test
# 复制忽略的数据库
binlog-ignore-db=test

## 需要复制的数据库表
#binlog-do-table=test.test
## 复制忽略的数据库表
#binlog-ignore-table=test.test
```

slave：

```config
log_slave_updates=1
server-id = 328
relay_log_recover = 1
relay_log_info_repository = TABLE
master_info_repository = TABLE
read_only = 1
```

重启 msyql 服务

## 查看复制进度

通过`show processlist;`列表中 slave_sql_running 线程的 time 值。

## 如何提高复制效率？

MySQL 5.6 提供了并行复制,但是这种并行只是基于 database 的。如果是基于单 database 的依然无法做到真正的并行回放，这个阶段很多 DBA 将数据库进行垂直拆分，将一个 database 拆分成几个 database，通过设置 slave_parallel_workers=n，可以进行 database 级别的并行复制，但对于热点业务复制延迟依然无法解决。

![img](http://mmbiz.qpic.cn/mmbiz_png/s9EktjKpKwLpEPlX4ME6ycykkdBtPfgOfTgzI8rXx6yGsricmlMFFcZ06fcCsQQGMWWIOYq1AK2Q08C8sp8kGgw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

MySQL 5.6 版本中还引入了 GTID，不但降低了主从 failover 时，寻找 filename，position 的难度，更是加入到了组提交中，这也造就了 MySQL 5.7 版本中的 Multi-Threaded Slave 的出现。如下图，一组中的事务，可以并行回放。

![img](http://mmbiz.qpic.cn/mmbiz_png/s9EktjKpKwLpEPlX4ME6ycykkdBtPfgOpL7EFmNbVgEiaZ2h7abUDm9hVQX4Kuh6Gbru09NicBlyZaSCkDSpbRibA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://user-gold-cdn.xitu.io/2017/3/29/a86b3a0ecb9cc9b01fcaf2ca792be717?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

在下图的测试中，MySQL 5.7 的多线程复制极大的提升了延迟效率，在 30 个线程并发操作的时候还能保证平均延迟 5.9 秒左右，而单线程复制的延迟率基本一直在上升。

![img](https://user-gold-cdn.xitu.io/2017/3/29/1b220a4ba932c5f4f4697d21b73e3aec?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

Multi-Threaded Slave 相关参数

```config
slave-parallel-type= DATABASE /LOGICAL_CLOCK
-- DATABASE -- 基于库级别的并行复制 与5.6相同
-- LOGICAL_CLOCK -- 逻辑时钟，主上怎么并行执行，从上怎么回放。

slave-parallel-workers=16
-- 并行复制的线程数

slave_preserve_commit_order=1
--commit的顺序保持一致
```

## 半同步

我们都知道，默认的 MySQL Replication 复制为异步模式，异步也就说明会有丢失数据的可能性，MySQL 在 5.5 版本中提供了 semi-sync replication，也就是半同步，但半同步只能说减少数据丢失的风险，所以在 MySQL 5.7 版本中，MySQL 提供了 lossless semi-sync replication，也就是无损复制，可最低限度的减少数据丢失（无损复制会和半同步一样在出问题时会切换为异步复制）。

![img](http://mmbiz.qpic.cn/mmbiz_png/s9EktjKpKwLpEPlX4ME6ycykkdBtPfgO0Nkk6x2Dic4Spt2LGosAVnTE1ialpBENiaYEUfs5Ho8YYUtCKhYicxPjAw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在半同步中，至少有一个 Slave 节点收到 binlog 后再返回，不能完全避免数据丢失，超时后，切回异步复制。在事物提交的过程中，在 InnoDB 层的 commit log 阶段后，Master 节点需要收到至少一个 Slave 节点回复的 ACK 后，才能继续下一个事物。

### **无损复制**

![img](https://user-gold-cdn.xitu.io/2017/3/29/87359d8129296fe3cca0adea3de41901?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

在无损复制中，master 把 binlog 发送给 slave，只有在 slave 把 binlog 写到本地的 relay-log 里，master 才会将事务提交到存储引擎层，然后把请求返回给客户端，客户端才可以看见刚才提交的事务。在一个事物提交的过程中，在 MySQL Server 层的 binlog 阶段后，Master 节点需要收到至少一个 Slave 节点回复的 ACK 后，才能继续下一个事物。

### 半同步复制与无损复制的对比

ACK 的时间点不同

- 半同步复制在 InnoDB 层的 Commit Log 后，等待 ACK。
- 无损复制在 MySQL Server 层的 Write binlog 后，等待 ACK。

主从数据一致性

- 半同步复制意味着在 Master 节点上，这个刚刚提交的事物对数据库的修改，对其他事物是可见的。
- 无损复制在 write binlog 完成后，就传输 binlog，但还没有去写 commit log，意味着当前这个事物对数据库的修改，其他事物也是不可见的。

### 半同步相关参数

```config
rpl_semi_sync_master_enabled=1
rpl_semi_sync_slave_enabled=1
rpl_semi_sync_master_timeout=1000
rpl_semi_sync_master_wait_for_slave_count=1
rpl_semi_sync_master_wait_point=AFTER_SYNC
rpl_semi_sync_master_wait_for_slave_count=1
```

### 半同步相关事件统计

```config
Rpl_semi_sync_master_tx_avg_wait_time
--开启Semi_sync，平均需要额外等待的时间
Rpl_semi_sync_master_net_avg_wait_time
--事务进入等待队列后，到网络平均等待时间Semi-sync的网络消耗有多大。
Rpl_semi_sync_master_status
-- 则表示当前Semi-sync是否正常工作
Rpl_semi_sync_master_no_times
--可以知道一段时间内，Semi-sync是否有超时失败过，记录了失败次数。
```

### **multi-source**

然而在 MySQL 5.7 版本中，提供了多源复制，多源复制的出现对于分库分表的业务提供了极大的便利，目前我们已经部署了多套多源复制供统计使用。

![img](http://mmbiz.qpic.cn/mmbiz_png/s9EktjKpKwLpEPlX4ME6ycykkdBtPfgOVpHUE4qNlFNJfgnNEnRZKJicU0Lx1WRuTbvyia3ibL9SUVhORonEgLRrg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如上图，多源复制采用多通道的模式，和普通的复制相比，就是使用 FOR CHANNEL 进行了分离。

```
CHANGE MASTER TO .... FOR CHANNEL ‘m1';
CHANGE MASTER TO .... FOR CHANNEL ‘m2';
```

上面我们也说到，为了提高复制效率，很多 DBA 会根据业务进行 DB 拆分，但拆分后又面临一个新的问题，就是 join，join 绝对是关系型数据库中最常用一个特性，然而在分布式的环境中，join 是最难解决的一个问题，使用多源复制就能很好的解决这个问题。

如果数据库，表名一致如何使用多源复制？，其实只要解决了数据冲突的问题就可以使用。

![img](https://user-gold-cdn.xitu.io/2017/3/29/19517cf041208e4263fb3b44658ec5f1?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

如上图的分库分表架构，可以使用以下参数实现奇偶插入的方式去解决。

```
auto_increment_offset=1…n
auto_increment_increment=n
```

但这种方式需要提前考虑扩展性。

## 切换主从服务器

```bash
# 确保所有的从数据库都已经执行relay log 中的更新，check从数据库的status转态has read all relay log
mysql>stop slave IO_THREAD;
mysql>show processlist;
# 停止slave服务
mysql>shop slave;
# 重置reset master成为主数据库
mysql>reset master;
# 接着重新配置主从服务器
```

## 参考

[浅析 MySQL Replication](https://mp.weixin.qq.com/s/t06xpSGk65cPih9ujbzArg?)
