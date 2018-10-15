# MySQL

MySQL 5.7

## 免密码登录

MySQL 5.6 以上版本提供 mysql_config_editor 工具用于用户安全验证。

```bash
mysql_config_editor set --login-path=client --host=localhost --user=root --password
Enter password:
# 在用户目录下生成隐藏文件 .mylogin.cnf
cat .mylogin.cnf
#显示为乱码
#登录
mysql --login-path=client
```

## 显示 MySQL 信息

```sql
mysql> \s
--------------
mysql  Ver 14.14 Distrib 5.7.20, for macos10.12 (x86_64) using  EditLine wrapper

Connection id:          23
Current database:
Current user:           root@localhost
SSL:                    Not in use
Current pager:          less
Using outfile:          ''
Using delimiter:        ;
Server version:         5.7.20 MySQL Community Server (GPL)
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    latin1
Db     characterset:    latin1
Client characterset:    utf8
Conn.  characterset:    utf8
UNIX socket:            /tmp/mysql.sock
Uptime:                 6 days 9 hours 15 min 30 sec

Threads: 3  Questions: 7949  Slow queries: 0  Opens: 376  Flush tables: 1  Open tables:354  Queries per second avg: 0.014
```

## MySQL 的连接和关闭：mysql -u -p -h -P

> -u：指定用户名
> -p：指定密码
> -h：主机
> -P：端口

## 进入 MySQL 命令行后：G、c、q、s、h、d

> G：打印结果垂直显示
> c：取消当前 MySQL 命令
> q：退出 MySQL 连接
> s：显示服务器状态
> h：帮助信息
> d：改变执行符

## 目录

- [事务](https://github.com/xianyunyh/PHP-Interview/blob/master/Mysql/%E4%BA%8B%E5%8A%A1.md)

- [存储引擎](https://github.com/xianyunyh/PHP-Interview/blob/master/Mysql/%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E.md)

- [索引](index.md)

  - [聚集索引和非聚集索引区别](https://blog.csdn.net/zc474235918/article/details/50580639)
  - [索引的分类](https://www.cnblogs.com/luyucheng/p/6289714.html)

- [mysql 优化](http://www.cnblogs.com/luyucheng/p/6323477.html)

  - [sql 优化]
    - [explain](https://github.com/xianyunyh/PHP-Interview/blob/master/Mysql/MySQL%E3%80%90explain%E3%80%91.md)
    - [慢查询](slow-query.md)
  - [配置优化](http://www.cnblogs.com/luyucheng/p/6340076.html)
  - [主从配置]
  - [索引优化](https://github.com/xianyunyh/PHP-Interview/blob/master/Mysql/MySQL%E4%BC%98%E5%8C%96.md)

- [锁](lock.md)

## 参考

-[MySQL 管理之道](https://book.douban.com/subject/26870647/)
