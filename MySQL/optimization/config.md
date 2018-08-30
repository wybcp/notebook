# 配置文件

```config
[client]
no-beep
port=3306
[mysql]
default-character-set=utf8
[mysqld]
# The TCP/IP Port the MySQL Server will listen on
port=3306
# Path to installation directory. All paths are usually resolved relative to this.
# basedir="C:/Program Files/MySQL/MySQL Server 5.7/"
# Path to the database root
datadir=C:/ProgramData/MySQL/MySQL Server 5.7\Data
character-set-server=utf8
```

## innodb_buffer_pool_size

配置 Innodb 的缓冲池，如果数据库中只有 Innodb 表，推荐配置为总内存的 75%。

## innodb_buffer_pool_instances

MySQL5.5 控制缓冲池的个数，默认情况下只有一个缓冲池。

## innodb_log_pool_size

innodb log 缓冲大小，由于日志最长每秒都会刷新所以一般不用太大。

## innodb_flush_log_at_yrx_commit

关键参数，对 Innodb 的 IO 效率影响较大，默认值 1，可选值 0.1.2，一般建议 2，如果安全性要求比较高使用 1。

## mysql 大小写敏感配置

MySQL 大小写敏感配置相关的两个参数，lower_case_file_system 和 lower_case_table_names。

```sql
mysql> show global variables like '%lower_case%';
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| lower_case_file_system | ON    |
| lower_case_table_names | 2     |
+------------------------+-------+
2 rows in set (0.01 sec)
```

### lower_case_file_system

表示当前系统文件是否大小写敏感，只读参数，无法修改。

- ON 大小写不敏感
- OFF 大小写敏感

### lower_case_table_names

表示表名是否大小写敏感，可以修改。

- lower_case_table_names = 0 时，mysql 会根据表名直接操作，大小写敏感。
- lower_case_table_names = 1 时，mysql 会先把表名转为小写，再执行操作。
- lower_case_table_names = 1 时，表名和数据库名在硬盘上使用CREATE TABLE或CREATE DATABASE语句指定的大小写字母进行保存，但MySQL将它们转换为小写在查找表上。名称比较对大小写不敏感，即按照大小写来保存，按照小写来比较。注释：只在对大小写不敏感的文件系统上适用! innodb表名用小写保存。

### 设置 lower_case_table_names 的值

打开 my.cnf 文件，加入以下语句后重启。

```config
lower_case_table_names = 0 
```

### 设置 lower_case_table_names=1 时，原来在 lower_case_table_names=0 时创建的表提示不存在的解决方法

在 lower_case_table_names=0 时使用大小写混用创建表名，再设置 lower_case_table_names=1 后，原创建的表使用时会提示不存在。

解决方法：

如果要将 lower_case_table_names 从 0 修改为 1 时，应先对旧数据表的表名进行处理，把所有数据库的表名先改为小写，最后再设置 lower_case_table_names 为 1，否则会出现上述的问题。

## max_allowed_packet

传输的包有大小限制。所以要注意 SQL 语句的长度度。过长会被抛异常。

可以调整`max_allowed_packet`

查看

```sql
mysql> show variables like 'max_allowed_packet';
+--------------------+---------+
| Variable_name      | Value   |
+--------------------+---------+
| max_allowed_packet | 4194304 |
+--------------------+---------+
1 row in set (0.03 sec)
```

设置

```sql
SET GLOBAL max_allowed_packet=16777216;
```

## 参考

- [mysql 大小写敏感配置](https://blog.csdn.net/fdipzone/article/details/73692929)
- [Packet Too Large](https://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html)
