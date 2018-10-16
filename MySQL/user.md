# 用户

## 一. 创建用户

命令:

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

说明：

- username：你将创建的用户名
- host：指定该用户在哪个主机上可以登陆，如果是本地用户可用 localhost，如果想让该用户可以从任意远程主机登陆，可以使用通配符%
- password：该用户的登陆密码，密码可以为空，如果为空则该用户可以不需要密码登陆服务器
  例子：

```sql
CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456';
CREATE USER 'pig'@'192.168.1.101_' IDENDIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '';
CREATE USER 'pig'@'%';
```

## 二. 授权

```sql
GRANT privileges ON databasename.tablename TO 'username'@'host'
```

说明:

- privileges：用户的操作权限，如 SELECT，INSERT，UPDATE 等，如果要授予所的权限则使用 ALL
- databasename：数据库名
- tablename：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.\*
  例子:

```sql
GRANT SELECT, INSERT ON test.user TO 'pig'@'%';
GRANT ALL ON _._ TO 'pig'@'%';
```

注意:

用以上命令授权的用户不能给其它用户授权，如果想让该用户可以授权，用以下命令:

```sql
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

## 三.设置与更改用户密码

```sql
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
```

如果是当前登陆用户用:

```sql
SET PASSWORD = PASSWORD("newpassword");
```

例子:

```sql
SET PASSWORD FOR 'pig'@'%' = PASSWORD("123456");
```

## 四. 撤销用户权限

```sql
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
```

例子:

```sql
REVOKE SELECT ON _._ FROM 'pig'@'%';
```

注意:

假如你在给用户'pig'@'%'授权的时候是这样的（或类似的）：`GRANT SELECT ON test.user TO 'pig'@'%'`，则在使用 `REVOKE SELECT ON _._ FROM 'pig'@'%';`命令并不能撤销该用户对 test 数据库中 user 表的 SELECT 操作。相反，如果授权使用的是 `GRANT SELECT ON _._ TO 'pig'@'%';`则 `REVOKE SELECT ON test.user FROM 'pig'@'%';`命令也不能撤销该用户对 test 数据库中 user 表的 Select 权限。

具体信息可以用命令 `SHOW GRANTS FOR 'pig'@'%';` 查看。

## 五.删除用户

```sql
DROP USER 'username'@'host';
```

## 重置密码解决

### windows

- 在配置文件[mysqld]后面任意一行添加`--skip-grant-tables`用来跳过密码验证的过程
- 重启 MySQL
- 重置密码
  `use mysql; update mysql.user set authentication_string=password('123qwe') where user='root' and Host ='localhost‘;`
- 注释“skip-grant-tables”
- 重新登录

### linux

- `mysql_safe --skip-grant-tables user=mysql`or`/etc/init.d/mysql start-mysqld --skip-grant-tables`
- 重启 MySQL
- 重置密码
  `use mysql; update mysql.user set authentication_string=password('123qwe') where user='root' and Host ='localhost‘;`
- `msyql>flush privileges;`

[重置密码解决 MySQL for Linux 错误 ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)](https://www.cnblogs.com/gumuzi/p/5711495.html)
