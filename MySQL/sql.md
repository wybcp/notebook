# 常用 mysql 语句

## 1. 增

- 增加数据库

  ```sql
  create database test;
  ```

- 增加一张表

  ```sql
  CREATE TABLE `table_name`(
    ...
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
  ```

- 增加记录

  ```sql
  INSERT INTO `table_name`(`column_name`)
  VALUES ('your_value_one'),('your_value_two');
  ```

- 增加字段

  ```sql
  ALTER TABLE `table_name`
  ADD `column_name` <数据类型>
  AFTER `column_name`;
  ```

- 增加索引

  - 主键

    ```sql
    ALTER TABLE `table_name`
    ADD PRIMARY KEY your_index_name(your_column_name);
    ```

  - 唯一索引
    ```sql
    ALTER TABLE `table_name`
    ADD UNIQUE your_index_name(your_column_name);
    ```
  - 普通索引
    ```sql
    ALTER TABLE `table_name`
    ADD INDEX your_index_name(your_column_name);
    ```
  - 全文索引
    ```sql
    ALTER TABLE `table_name`
    ADD FULLTEXT your_index_name(your_column_name);
    ```

## 2. 删

- 逐行删除

  ```sql
  DELETE FORM `table_name`
  WHERE ...;
  ```

- 清空整张表

  ```sql
  TRUNCATE TABLE `table_name`;
  ```

- 删除数据库

  ```sql
  DROP DATABASE `database_name`;
  ```

- 删除表

  ```sql
  DROP TABLE [if exists]`table_name`;
  ```

- 删除字段

  ```sql
  ALTER TABLE `table_name`
  DROP `column_name`;
  ```

- 删除索引

  ```sql
  ALTER TABLE `table_name`
  DROP INDEX your_index_name(your_column_name);
  ```

- 删除外键约束

  ```sql
  ALTER TABLE `table_name`
  DROP foreign key foreign_key_name;
  ```

## 3. 改

- 更改表名

  ```sql
  alter table table_name rename user_2;
  ```

- 更改存储引擎

  ```sql
  alter table table_name engine= engine_name;
  ```

- 变更数据

  ```sql
  UPDATE `table_name`
  SET column_name=your_value
  WHERE ...;
  ```

- 改变字段数据类型

  ```sql
  alter table table_name modify column_name <数据类型>;
  ```

- 变更字段名

  ```sql
  ALTER TABLE `table_name`
  CHANGE `old_column_name` `new_column_name` <数据类型>;
  ```

- 变更字段值为另一张表的某个值

  ```sql
  UPDATE `table_name`
  AS a
  JOIN `another_table_name`
  AS b
  SET a.column = b.anther_column
  WHERE a.id = b.a_id...;
  ```

## 4. 查

- 普通查询

  ```sql
  SELECT `column_name_one`, `column_name_two`
  FROM `table_name`;
  ```

- 关联查询

  ```sql
  SELECT *
  FROM `table_name`
  AS a
  JOIN `your_anther_table_name`
  AS b
  WHERE a.column_name = b.column_name...;
  ```

- 合计函数条件查询：WHERE 关键字无法与合计函数一起使用

  ```sql
  SELECT aggregate_function(column_name)
  FROM table_name
  GROUP BY column_name
  HAVING aggregate_function(column_name)...;
  ```

- 同一个实例下跨库查询

  ```sql
  SELECT *
  FROM database_name.table_name
  AS a
  JOIN another_database_name.your_another_table_name
  AS b
  WHERE a.column_name = b.column_name...;
  ```

- mysql 查询一个数据库中的所有的表名

  ```sql
  select table_name
  from information_schema.tables
  where table_schema='当前数据库'
  ```

- 双表关联

  ```sql
  select orders.orderid, customers.city
  from orders, customers
  where customers.city="cq"
  and customers.customerid=orders.orderid;
  ```

  如果列的名称不具有唯一性，则使用点号表明从属于哪个表。

- 特定顺序

  ORDER BY 关键词用于对记录集中的数据进行排序,默认对记录进行升序排序。
  如果降序排序，使用 DESC 关键字。

  ```sql
  SELECT column_name(s)
  FROM table_name
  ORDER BY column_name(s) ASC|DESC
  ```

## 5. 复制

- 复制一张表结构

  ```sql
  CREATE `table_name`
  LIKE `destination_table_name`;
  ```

- 完全复制一张表：表结构+全部数据

  ```sql
  CREATE TABLE `table_name`
  LIKE `destination_table_name`;

  INSERT INTO `table_name`
  SELECT *
  FROM `destination_table_name`;
  ```

## 选择要返回的行

`limit`子句，带有两个参数：起始行号和返回行数。

## 附录：mysql 常用命令

- 登陆： `mysql -h host -u username -p`
- 列出数据库：`SHOW DATABESES`;
- 列出表:`SHOW TABLES`;
- 列出表结构:`DESC table_name`
- 使用一个数据库：`USE database_name`;
- 导入：`source 'file'`;
- 导出：`mysqldump -h 127.0.0.1 -u root -p "database_name" "table_name" --where="condition" > file_name.sql`;
- 查看慢日志：`mysqldumpslow -s [c:按记录次数排序/t:时间/l:锁定时间/r:返回的记录数] -t [n:前 n 条数据] -g "正则" /path`

```sql
use database_name;
//创建数据表
create table table_name(
column_name data_type,
...
);
//查看表结构
show columns from table_name;

//insert table () values();
```

- select version():显示服务器版本号
- select database();//查看当前数据库
- select now():当前时间
- select user():当前用户
- show tables;//查看数据表列表
- SHOW DATABASES; 显示所有数据库
- SHOW index from table; 显示表的索引，
- SHOW WARNINGS:
- SHOW CREATE DATABASE X:查看数据库表基本信息
- SHOW CREATE table X:查看创建表基本信息
- select least(value_1...value_n)：选取最小值
- select greatest(value_1...value_n)：选取最大值

```sql
select * from information_schema.TABLES where information_schema.TABLES.TABLE_SCHEMA = '数据库名' and information_schema.TABLES.TABLE_NAME = '表名';
```

- 去重显示数据
  select distinct a,b from test;

- 查看 MySQL 数据库大小

  ```sql
  SELECT sum(DATA_LENGTH)+sum(INDEX_LENGTH) FROM information_schema.TABLES where TABLE_SCHEMA='数据库名';
  ```

  得到的结果是以字节为单位，除 1024 为 K，除 1048576(=1024\*1024)为 M。

- 查看表的最后 mysql 修改时间

  ```sql
  select TABLE_NAME,UPDATE_TIME from information_schema.TABLES where TABLE_SCHEMA='数据库名' order by UPDATE_TIME desc limit 1;
  select TABLE_NAME,UPDATE_TIME from information_schema.TABLES where TABLE_SCHEMA='数据库名' and information_schema.TABLES.TABLE_NAME = '表名';
  ```

## group by

## having

HAVING 分组过滤条件： HAVING 后的字段必须是 SELECT 后出现过的（如“SELECT sex，age FROM users GROUP BY age HAVING age>20"，age 就出现在 SELECT 后），或放在聚合函数（包括 COUNT：计算行的数量，MAX：计算列的最大值，MIN：计算列的最小值，SUM：获取单个列的合计值，AVG：计算某个列的平均值等）中

## 将查询结果写入数据表：

将表格 users 中 age 大于 30 的数据行放入数据表 test 中的 username 数据行

```sql
INSERT test(username) SELECT username FROM users WHERE age>=30;
```

## 查询重复记录

1. 查找表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断

   ```sql
   select * from people
   where peopleId in (select peopleId from people group by peopleId having count(peopleId) > 1)
   ```

2. 删除表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断，只留有 rowid 最小的记录

   ```sql
   delete from people
   where peopleId in (select peopleId from people group by peopleId   having count(peopleId) > 1)
   and rowid not in (select min(rowid) from people group by peopleId having count(peopleId )>1)
   ```

3. 查找表中多余的重复记录（多个字段）

   ```sql
   select * from vitae a
   where (a.peopleId,a.seq) in (select peopleId,seq from vitae group by peopleId,seq having count(*) > 1)
   ```

## 参考

- [MYSQL 查询重复记录的方法](http://database.51cto.com/art/201011/235159.htm)
