# InnoDB 存储引擎

该存储引擎提供了具有提交、回滚和崩溃恢复能力的事务安全。但是对比 MyISAM 引擎，写的处理效率会差一些，并且会占用更多的磁盘空间以保留数据和索引。

InnoDB 存储引擎的特点：支持自动增长列，支持外键约束，支持事务。

InnoDB 中，创建的表的表结构存储在`.frm`文件中。数据和索引存储在 `innodb_data_home_dir` 和 `innodb_data_file_path` 定义的表空间中。MySQL 8.0 版本，允许把表结构定义放在系统数据表中。因为表结构定义占用的空间很小。

InnoDB：支持事务和行级锁，是 innodb 的最大特色。行锁大幅度提高了多用户并发操作的新能。

- 默认事务型引擎，最重要最广泛的存储引擎，性能非常优秀。
- 数据存储在共享表空间，可以通过配置分开。也就是多个表和索引都存储在一个表空间中，可以通过配置文件改变此配置。
- 对主键查询的性能高于其他类型的存储引擎。
- 内部做了很多优化，从磁盘读取数据时会自动构建 hash 索引，插入数据时自动构建插入缓冲区。
- 通过一些机制和工具支持真正的热备份。
- 支持崩溃后的安全恢复。
- 支持行级锁。
- 支持外键。

InnoDB 不创建目录，MySQL 在 MySQL 数据目录下面创建一个名为 ibdata1 的 10MB 大小的自动扩展数据文件和两个日志文件 ib_logfile0、ib_logfile1。

## 回收空间

删除表之后空间回收。

`innodb_file_per_table`
这项设置告知 InnoDB 是否需要将所有表的数据和索引存放在共享表空间里（innodb_file_per_table = OFF）或者为每张表的数据单独放在一个`.ibd` 文件（innodb_file_per_table = ON,从 MySQL 5.6.6 开始，默认值 ON）,每张表一个文件允许你在 drop、truncate 或者 rebuild 表时回收磁盘空间这对于一些高级特性也是有必要的，比如数据压缩,但是它不会带来任何性能收益

推荐将`innodb_file_per_table`设置为 ON。因为，一个表单独存储为一个文件更容易管理，而且在你不需要这个表的时候，通过 drop table 命令，系统就会直接删除这个文件。而如果是放在共享表空间中，即使表删掉了，空间也是不会回收的。

## 性能

- 磁盘 I/O:

  - 可以使用 SSD 提升性能
  - innodb_io_capacity 加大每秒刷新脏页的数量，设置成磁盘的 IOPS。磁盘的 IOPS 可以通过 fio 这个工具来测试`fio -filename=$filename -direct=1 -iodepth 1 -thread -rw=randrw -ioengine=psync -bs=16k -size=500M -numjobs=10 -runtime=10 -group_reporting -name=mytest`

- 内存 buffer_pool 缓存池，innodb_buffer_pool_size 尽可能最大，

一旦一个查询请求需要在执行过程中先 flush 掉一个脏页时，这个查询就可能要比平时慢了。而 MySQL 中的一个机制，可能让你的查询会更慢：在准备刷一个脏页的时候，如果这个数据页旁边的数据页刚好是脏页，就会把这个“邻居”也带着一起刷掉；而且这个把“邻居”拖下水的逻辑还可以继续蔓延，也就是对于每个邻居数据页，如果跟它相邻的数据页也还是脏页的话，也会被放到一起刷。

在 InnoDB 中，innodb_flush_neighbors 参数就是用来控制这个行为的，值为 1 的时候会有上述的“连坐”机制，值为 0 时表示不找邻居，自己刷自己的。

找“邻居”这个优化在机械硬盘时代是很有意义的，可以减少很多随机 IO。机械硬盘的随机 IOPS 一般只有几百，相同的逻辑操作减少随机 IO 就意味着系统性能的大幅度提升。

而如果使用的是 SSD 这类 IOPS 比较高的设备的话，我就建议你把 innodb_flush_neighbors 的值设置成 0。因为这时候 IOPS 往往不是瓶颈，而“只刷自己”，就能更快地执行完必要的刷脏页操作，减少 SQL 语句响应时间。

在 MySQL 8.0 中，innodb_flush_neighbors 参数的默认值已经是 0 了。
