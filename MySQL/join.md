# 连接查询

## inner join 内连接

在 MySQL 中 JOIN,INNER JOIN,CROSS JOIN 是等价的

交集 仅显示 A、B 两表符合连接条件的记录。不符合连接条件的记录不显示。类似于取 AB 的交集。

![image](http://img.mukewang.com/58e371d60001e9b512800720.jpg)

## left join

LEFT JOIN：显示左表全部和左右符合连接条件的记录

## RIGHT JOIN

显示左右符合连接条件的记录和右表全部记录

## 自身连接

实现无限极分类表设计框架：字段 1：类型 id 字段 2：类型名字段 3：父类 id create table 无限极表名

```sql
(
 type_id smallint unsigned primary key auto_increment,
 type_name vachar(20) NOT NULL,
 parent_id smallint unsigned NOT NULL DEFAULT 0
);
```

从设计上看，父类和子类、子子类同在一个表。通过最后一个字段(parent_id)确认父类,从而实现无限极分类。

如何利用 select 语句查询该表，查询出需要的分类呢？利用“连接”还是“自身连接”，将自身通过别名实现一个父表，一个子表。

```sql
select 父.type_id,父.type_name,子.type_name from 子表 as 子 left join 父表 as  父 on 子.parent_id = 父.type_id;
```

左连接是子表，查询数据完整。左连接是父表，子表中相同父类 id 只显示一个，数据不完整。也可以使用右连接：

```sql
select 父.type_id,父.type_name,子.type_name from 父表 as  父 right join 子表 as 子 on 子.parent_id = 父.type_id;
```

## 多表删除：

delete 语句无法进行多表删除数据操作，不过可以建立多表连接，在两个表之间删除满足条件的记录。

例：

```sql
delete from tbl_name1,tbl_name2 where condition on condition;
```

删除 tbl_name1 表和 tbl_name2 表中条件满足 where 条件和 on 条件的记录。通过子查询变成逻辑上的两张表多表删除实例

```sql
DELETE t1 FROM tdb_goods AS t1 INNER JOIN (SELECT goods_id,goods_name FROM tdb_goods GROUP BY goods_name HAVING count(goods_name)>=2) AS t2 ON t1.goods_name = t2.goods_name WHERE t1.goods_id > t2.goods_id;
```

删除 tdb_goods 表中的商品名相同的多余的部分。
