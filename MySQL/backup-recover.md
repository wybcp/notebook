# [备份](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)

MySQL 备份恢复数据的一般步骤：

1. 备份前读锁定涉及的表
   `mysql>LOCK TABLES tbl1 READ,tbl1 READ,…`
   　　如果，你在 mysqldump 实用程序中使用`--lock-tables`选项则不必使用如上 SQL 语句。
2. 导出数据库中表的结构和数据
   `shell>mysqldump --opt db_name>db_name.sql`
3. 启用新的更新日志
   `shell>mysqladmin flush-logs`
   这样可以记录你备份后的数据改变为恢复数据准备。
4. 解除表的读锁
   `mysql>UNLOCK TABLES;``

为了加速上述过程，你可以这样做：
`shell> mysqldump --lock-tables --opt db_name>db_name.sql; mysqladmin flush-logs`
但是这样可能会有点小问题。上命令在启用新的更新日志前就恢复表的读锁，

在更新繁忙的站点，可能有备份后的更新数据没有记录在新的日志中。

## 恢复

现在恢复上面备份的数据库

1. 对涉及的表使用写锁
   `mysql>LOCK TABLES tbl1 WRITE,tbl1 WRITE,…`
2. 恢复备份的数据
   `shell>mysql db_name < db_name.sql`
3. 恢复更新日志的内容
   `shell>mysql --one-database db_name < hostname.nnn`
   假设需要使用的日志名字为 hostname.nnn
4. 启用新的更新日志
   `shell>mysqladmin flush-logs`
5. 解除表的写锁
   `mysql>UNLOCK TABLES;`

导出

```bash
mysqldump -uroot -p -t laravel_shop admin_menu admin_permissions admin_role_menu admin_role_permissions admin_role_users admin_roles admin_user_permissions admin_users > database/admin.sql
```

导入

```bash
mysql laravel-shop < database/admin.sql
```

or

```bash
msyql>source database/admin.sql
```

## 迁移

### 相同版本 MySQL 数据库迁移

```bash
mysqldump -h source_host -uroot -ppassword dbname|mysql -h desitation-host uroot -ppassword
```

管道符号`|`
