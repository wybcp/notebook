# mysql 优化

- 不要查询不需要的列
- 不要在多表关联返回全部的列
- 不要 `select *`
- 不要重复查询，应当写入缓存
- 尽量使用关联查询来替代子查询。
- 尽量使用索引优化。如果不使用索引。mysql 则使用临时表或者文件排序。如果不关心结果集的顺序，可以使用 order by null 禁用文件排序。
- 优化分页查询，最简单的就是利用覆盖索引扫描。而不是查询所有的列
- 应尽量避免在 where 子句中使用 !=或<> 操作符，否则将引擎放弃使用索引而进行全表扫描。
- 对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引
- 应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描，如：

```sql
select * from user where name is null
```

- 尽量不要使用前缀%

```sql
select * from user where name like '%a'
```

- 应尽量避免在 where 子句中对字段进行表达式操作

- 应尽量避免在 where 子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描

- 很多时候用 exists 代替 in 是一个好的选择：

1、开启查询缓存，优化查询

2、explain 你的 select 查询，这可以帮你分析你的查询语句或是表结构的性能瓶颈。EXPLAIN 的查询结果还会告诉你你的索引主键被如何利用的，你的数据表是如何被搜索和排序的

3、当只要一行数据时使用 limit 1，MySQL 数据库引擎会在找到一条数据后停止搜索，而不是继续往后查少下一条符合记录的数据

4、为搜索字段建索引

5、使用 ENUM 而不是 VARCHAR，如果你有一个字段，比如“性别”，“国家”，“民族”，“状态”或“部门”，你知道这些字段的取值是有限而且固定的，那么，你应该使用 ENUM 而不是 VARCHAR。

6、Prepared StatementsPrepared Statements 很像存储过程，是一种运行在后台的 SQL 语句集合，我们可以从使用 prepared statements 获得很多好处，无论是性能问题还是安全问题。Prepared Statements 可以检查一些你绑定好的变量，这样可以保护你的程序不会受到“SQL 注入式”攻击

7、垂直分表

8、选择正确的存储引擎

## btree 索引

B-TREE 索引适合全键值、键值范围、前缀查找。

全值匹配，是匹配所有的列进行匹配、

匹配最左前缀。比如 a=1&b=2 那么会用到 a 的索引

匹配列前缀。 比如 abc abcd %abc

匹配范围 比如 in(3,5)

### 限制

- 如果不是左前缀开始查找，无法使用索引 比如 %aa

- 不能跳过索引的列。

- 需要中，含有某个列的范围查找，后面的所有字段都不会用到索引

### 索引的优点

1、减少服务器扫描表的次数

2、避免排序和临时表

3、将随机 io 变成顺序 io

### 高性能索引策略

- 1、使用独立的列，而不是计算的列

where num+1 =10 //bad

where num = 9 //good

- 2、使用前缀索引
- 3、多列索引，应该保证左序优先
- 4、覆盖索引
- 5、选择合适的索引顺序

不考虑排序和分组的情况。在选择性最高的列上，放索引，

- 6、使用索引扫描来排序

mysql 有两种方式生成有序的结果，一种是排序操作，一种是按索引顺序扫描，如果 explain 处理的 type 列的值是 index。则说明 mysql 使用了索引

只有当索引的列顺序和 order by 子句的顺序一致的时候，并且所有的顺序都一致的时候。mysql 才能使用索引进行排序。

### 不能使用索引的情况

- 1.查询使用了两种排序方向

```sql
select * from user where login_time > '2018-01-01' order by id des ,username asc #
```

- 2.order by 中含有了一个没有 索引的列

```sql
select * from user where name = '11' order by age desc; //age 没有索引
```

- 3.where 和 order by 无法形成最左前缀

- 索引列的第一列是范围条件

- 在索引列上有多个等于条件，这也是一种范围。不能使用索引


- 1.对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引。
- 2.应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描，如：

```
select id from t where num is null可以在num上设置默认值0，确保表中num列没有null值，然后这样查询：select id from t where num=
```

- 3.应尽量避免在 where 子句中使用!=或<>操作符，否则引擎将放弃使用索引而进行全表扫描。
- 4.应尽量避免在 where 子句中使用 or 来连接条件，否则将导致引擎放弃使用索引而进行全表扫描，如：

```
select id from t where num=10 or num=20可以这样查询：select id from t where num=10 union all select id from t where num=20
```

- 5.in 和 not in 也要慎用，否则会导致全表扫描，如：

```
select id from t where num in(1,2,3) 对于连续的数值，能用 between 就不要用 in 了：select id from t where num between 1 and 3
```

- 6.下面的查询也将导致全表扫描：select id from t where name like ‘%李%’若要提高效率，可以考虑全文检索。
- \7. 如果在 where 子句中使用参数，也会导致全表扫描。因为 SQL 只有在运行时才会解析局部变量，但优化程序不能将访问计划的选择推迟到运行时；它必须在编译时进行选择。然 而，如果在编译时建立访问计划，变量的值还是未知的，因而无法作为索引选择的输入项。如下面语句将进行全表扫描：

```
select id from t where num=@num可以改为强制查询使用索引：select id from t with(index(索引名)) where num=@num
```

- 8.应尽量避免在 where 子句中对字段进行表达式操作，这将导致引擎放弃使用索引而进行全表扫描。如：

```
select id from t where num/2=100应改为:select id from t where num=100*2
```

- 9.应尽量避免在 where 子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描。如：

```
select id from t where substring(name,1,3)=’abc’ ，name以abc开头的id应改为:select id from t where name like ‘abc%’
```

- 10.不要在 where 子句中的“=”左边进行函数、算术运算或其他表达式运算，否则系统将可能无法正确使用索引。

[原文](https://blog.csdn.net/samjustin1/article/details/52212421)
