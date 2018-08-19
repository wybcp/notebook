# 从 MySQL 数据库读取数据

1. 检查并过滤信息：过滤空白符（`trim()`），适当过滤一些控制字符，使用`get_magic_quotes_gpc()`检测是否自动完成引号，否则使用`addslashes()`处理；
2. 建立数据库连接：`mysqli`,`max_connections`参数决定同时连接的个数，通过`my.conf`更改
3. 查询数据库：`mysqli_query()`
4. 获取结果
5. 显示内容

SELECT 语句用于从数据表中读取数据:
`SELECT column_name(s) FROM table_name`

WHERE 子句用于提取满足指定标准的的记录。

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator value
```

双表关联

```sql
select orders.orderid, customers.city
from orders, customers
where customers.city="cq"
and customers.customerid=orders.orderid;
```

如果列的名称不具有唯一性，则使用点号表明从属于哪个表。

mysqli_query() 函数用于向 MySQL 连接发送查询或命令。

## 查找不匹配行

左关联是在两个表之间指定的关联条件下匹配的数据行，`left join`关键字。

## 表别名：Aliases

`table as a`使用 as 子句声明表的别名。

## 特定顺序

ORDER BY 关键词用于对记录集中的数据进行排序,默认对记录进行升序排序。
如果降序排序，使用 DESC 关键字。

```sql
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) ASC|DESC
```

## 分组和合计数据

| 名称 | 描述   |
| ---- | ------ |
| AVG  | 平均值 |

|

```sql
select avg(amount) ，customerid
from orders
group by customerid
having avg(amount)>50;
```

使用`group by` 子句获得更详细的信息。类似与`where`语句。

## 选择要返回的行

`limit`子句，带有两个参数：起始行号和返回行数。

## 子查询

子查询是一个嵌套在另一个查询内部的查询。

最常见的用法是将一个查询的结果作为另一个查询的比较条件

## 更新数据库

UPDATE 语句用于更新数据库表中已存在的记录。
语法

```sql
UPDATE table_name
SET column1=value, column2=value2,...
WHERE some_column=some_value
```

WHERE 子句规定了哪些记录需要更新。如果省去 WHERE 子句，所有的记录都会被更新！

## 修改数据库

`alter table`

## 删除

`delete`删除表内容

`drop` 删除表和数据库

DELETE FROM 语句用于从数据库表中删除记录。

```sql
DELETE FROM table_name
WHERE some_column = some_value
```

WHERE 子句规定了哪些记录需要删除。如果省去 WHERE 子句，所有的记录都会被删除！

## 显示数据库信息

`show tables from books;`查看数据库的表

`show tables from customers from books;`查看表的所有列，也可以使用`show columns from books.customers;`
