# 数据库编码

## 修改 mysql 配置文件 my.cnf（windows 为 my.ini）

my.cnf 一般在 etc/mysql/my.cnf 位置。找到后请在以下三部分里添加如下内容：

```conf
[client]
default-character-set = utf8mb4
[mysql]
default-character-set = utf8mb4
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init_connect=’SET NAMES utf8mb4’
```

## 重启数据库，检查变量

```sql
SHOW VARIABLES LIKE ‘character_set_%’
```

但必须保证

| 系统变量                 | 描述                         |
| ------------------------ | ---------------------------- |
| character_set_client     | (客户端来源数据使用的字符集) |
| character_set_connection | (连接层字符集)               |
| character_set_database   | (当前选中数据库的默认字符集) |
| character_set_results    | (查询结果字符集)             |
| character_set_server     | (默认的内部操作字符集)       |

这几个变量必须是 utf8mb4。

## 数据库连接的配置

数据库连接参数中:

characterEncoding=utf8 会被自动识别为 utf8mb4，也可以不加这个参数，会自动检测。而 autoReconnect=true 是必须加上的。

## 将数据库和已经建好的表也转换成 utf8mb4

更改数据库编码：

```sql
ALTER DATABASE Database_Name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

更改表编码：

```sql
ALTER TABLE
    TABLE_NAME
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;
```

如有必要，还可以更改列的编码

```sql
ALTER TABLE
    table_name
    CHANGE column_name column_name
    VARCHAR(191)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```
