# 调用 explain

explain 可以查看查询计划的信息，

如果 sql 语句中包含子查询，mysql 依然会执行子查询，将结果放到一个临时表中。然后完成外层的优化查询

## 支持的命令

MySQL 5.6 以上的版本支持对 select、update、delete 命令使用 explain 查看 SQL 执行情况。

## EXPLAIN 中的列

explain 中总是有相同的列。

| id  | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra |
| --- | ----------- | ----- | ---------- | ---- | ------------- | ---- | ------- | ---- | ---- | -------- | ----- |
| 1   | SIMPLE      | links | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 10   | 100.00   | NULL  |

### id 列

这个 id 包含一个标号，标识 select 所属的行。如果语句中没有子查询或者联合，id 唯一。否则，内层的 select 语句一般会顺序编号，对应于其在原始语句中的位置。

mysql 将查询分为简单查询和复杂查询，复杂查询分为子查询、派生表（FROM 中的子查询）、union 查询。

### select_type 列

这一列显示对应的行是简单查询还是复杂查询。如果是简单查询就是 simple。如果是复杂查询，则是以下的几种值：

1. SUBQUERY

   包含在 select 列表中的 select

   ```sql
   select (select id from user) from user
   ```

1. DERIVED

   DERIVED 值用来表示包含在 from 子查询中的 select。

   ```sql
   select id from (select id from user where id >100);
   ```

1. UNION

   在 union 中的第二个值和 select 都被标记为 union

1. union result

   用来从临时表检索结果的 select 被标记为 union result

### table 列

对应访问的表。

### partitions

匹配的分区。

### type 列

mysql 决定查找表中的行

- all

  全表扫描，这个类型的查询是性能最差的查询之一，通常来说，我们的查询不应该出现ALL类型的查询，因为这样的查询在数据量大的情况下，对数据库的性能是巨大的灾难，一般可以用索引来避免。

- index

  表示全索引扫描（full index scan），扫描所有的索引，而不扫描数据。优点避免了排序，缺点就是按照整个索引读取整个表的开销。

- range

  范围扫描。就是一个有限制的索引扫描，开始于索引的一点，结束到匹配的值。比如where 带有范围的条件, =, <>, >, >=, <, <=, IS NULL, <=>, BETWEEN, IN() 操作

- ref

  这是一种索引访问，返回匹配到某个单个值的行，一般是非唯一索引或者非唯一索引的前缀索引。此类型通常出现在多表的join查询，针对于非唯一或非主键索引，或者使用了最左前缀规则索引的查询

- eq_ref

  使用这种索引查找，一般是通过唯一索引或者主键索引查找的时候看到

- const、system

  mysql 对查询的部分进行优化转成一个常量的时候，比如把一行中的主键放入到 where 条件中

  ```sql
  select * from user where name = id ;
  ```

- null

  mysql 在优化阶段分解查询语句，在执行阶段不用访问表或者访问索引。

type类型的性能比较

`ALL < index < range ≈ index_merge < ref < eq_ref < const < system`

### possible_keys

这列显示的是 mysql 可以使用的索引

### key 列

决定了 mysql 采用哪个索引来对表的访问。

### key_len 列

mysql 在索引使用的字节数，这个字段可以评估组合索引是否完全被使用，或只有最左部分字段被使用到。根据数据类型所占字节数计算出来。

- 字符串
  - char(n): n 字节长度
  - varchar(n): 如果是 utf8 编码，则是`3n+2`字节; 如果是 utf8mb4 编码，则是`4n+2`字节。
- 数值类型:
  - TINYINT: 1 字节
  - SMALLINT: 2 字节
  - MEDIUMINT: 3 字节
  - INT: 4 字节
  - BIGINT: 8 字节
- 时间类型
  - DATE: 3 字节
  - TIMESTAMP: 4 字节
  - DATETIME: 8 字节
- 字段属性: NULL 属性占用一个字节。如果一个字段是 NOT NULL 的，则没有此属性。

### ref 列

显示之前的表在 key 列记录的索引中，查找值所用的列或常量。

### rows 列

mysql 查询优化器根据统计信息，估算 SQL 要查找到结果集需要扫描读取的数据行数。这个值非常直观显示 SQL 的效率好坏，原则上 rows 越少越好。

### fiteread 列

查询记录和总记录的一个百分比

### extra 列

额外的信息

- using index 使用覆盖索引，表示查询在索引树中就可以查询到所需数据，不用扫描表数据问题，往往说明性能挺好。
- using where
- using temproary 使用临时表，一般出现于排序，分组和多表 join 的情况，查询效率不高，建议优化。
- using filesort 使用文件排序，表示 mysql 需额外的排序操作，不能通过索引顺序达到排序效果，一般有 Using filesort，都建议优化去掉，因为这样的查询 CPU 资源消耗大。
