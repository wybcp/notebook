# 分区

分区是指根据一定规则，数据库将一个表分解成多个更小、更容易管理的部分。

分区有利于管理非常大的表，采取“分而治之”的逻辑，引入分区键（partition key），分区键用于根据某个区间值、特定值列表或 HASH 函数值执行数据的聚集，让数据根据规则分布在不同的分区。

## 优点

- 存储更多数据
- 优化查询
- 快速删除对应的数据
- 跨多个磁盘来分散数据查询，提高查询吞吐量

## 分区类型

- RANGE 分区：基于属于一个给定连续区间的列值，把多行分配给分区。
- LIST 分区：类似于按 RANGE 分区，区别在于 LIST 分区是基于列值匹配一个离散值集合中的某个值来进行选择。
- HASH 分区：基于用户定义的表达式的返回值来进行选择的分区，该表达式使用将要插入到表中的这些行的列值进行计算。这个函数可以包含 MySQL 中有效的、产生非负整数值的任何表达式。
- KEY 分区：类似于按 HASH 分区，区别在于 KEY 分区只支持计算一列或多列，且 MySQL 服务器提供其自身的哈希函数。必须有一列或多列包含整数值。

### RANGE 分区

基于属于一个给定连续区间的列值，把多行分配给分区。这些区间要连续且不能相互重叠，使用 VALUES LESS THAN 操作符来进行定义。

```
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT NOT NULL,
    store_id INT NOT NULL
)
partition BY RANGE (store_id) (
    partition p0 VALUES LESS THAN (6),
    partition p1 VALUES LESS THAN (11),
    partition p2 VALUES LESS THAN (16),
    partition p3 VALUES LESS THAN (21)
);
```

每个分区都是按顺序进行定义，从最低到最高。这是 PARTITION BY RANGE 语法的要求。

改进
`
PARTITION p3 VALUES LESS THAN MAXVALUE

`
MAXVALUE 表示最大的可能的整数值。

RANGE 分区应用：

1. 当需要删除一个分区上的“旧的”数据时,只删除分区即可。
2. 想要使用一个包含有日期或时间值，或包含有从一些其他级数开始增长的值的列。
3. 经常运行直接依赖于用于分割表的列的查询。

### LIST 分区

LIST 分区是基于列值匹配一个离散值集合中的某个值来进行选择。

LIST 分区通过使用“PARTITION BY LIST(expr)”来实现，其中“expr” 是某列值或一个基于某个列值、并返回一个整数值的表达式，然后通过“VALUES IN (value_list)”的方式来定义每个分区，其中“value_list”是一个通过逗号分隔的整数列表。

```
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT,
    store_id INT
)
PARTITION BY LIST(store_id)
    PARTITION pNorth VALUES IN (3,5,6,9,17),
    PARTITION pEast VALUES IN (1,2,10,11,19,20),
    PARTITION pWest VALUES IN (4,12,13,14,18),
    PARTITION pCentral VALUES IN (7,8,15,16)
)；
```

【要点】：如果试图插入列值（或分区表达式的返回值）不在分区值列表中的一行时，那么“INSERT”查询将失败并报错。将要匹配的任何值都必须在值列表中找到。

LIST 分区除了能和 RANGE 分区结合起来生成一个复合的子分区，与 HASH 和 KEY 分区结合起来生成复合的子分区也是可能的。

### HASH 分区

基于用户定义的表达式的返回值来进行选择的分区，该表达式使用将要插入到表中的这些行的列值进行计算。这个函数可以包含 MySQL 中有效的、产生非负整数值的任何表达式。

要使用 HASH 分区来分割一个表，要在 CREATE TABLE 语句上添加一个“PARTITION BY HASH (expr)”子句，其中“expr”是一个返回一个整数的表达式。它可以仅仅是字段类型为 MySQL 整型的一列的名字。此外，你很可能需要在后面再添加一个“PARTITIONS num”子句，其中 num 是一个非负的整数，它表示表将要被分割成分区的数量。

```
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT,
    store_id INT
)
PARTITION BY HASH(store_id)
PARTITIONS 4；
```

如果没有包括一个 PARTITIONS 子句，那么分区的数量将默认为 1。

#### LINER HASH

MySQL 还支持线性哈希功能，线性哈希功能使用的一个线性的 2 的幂（powers-of-two）运算法则，而常规哈希使用的是求哈希函数值的模数。

线性哈希分区和常规哈希分区在语法上的唯一区别在于，在“PARTITION BY” 子句中添加“LINEAR”关键字。

```
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT,
    store_id INT
)
PARTITION BY LINEAR HASH(YEAR(hired))
PARTITIONS 4；
```

线性哈希分区：

- 优点在于增加、删除、合并和拆分分区将变得更加快捷，有利于处理含有极其大量（1000 吉）数据的表
- 缺点在于，与使用常规 HASH 分区得到的数据分布相比，各个分区间数据的分布不大可能均衡。

### KSY 分区

类似于按 HASH 分区，区别在于 KEY 分区只支持计算一列或多列，且 MySQL 服务器提供其自身的哈希函数。必须有一列或多列包含整数值。

```
CREATE TABLE tk (
    col1 INT NOT NULL,
    col2 CHAR(5),
    col3 DATE
)
PARTITION BY LINEAR KEY (col1)
PARTITIONS 3;
```

在 KEY 分区中使用关键字 LINEAR 和在 HASH 分区中使用具有同样的作用，分区的编号是通过 2 的幂（powers-of-two）算法得到，而不是通过模数算法。
