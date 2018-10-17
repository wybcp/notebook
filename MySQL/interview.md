#  常见面试题

## 1：char、varchar 的区别是什么？

varchar 是变长而 char 的长度是固定的。如果你的内容是固定大小的，你会得到更好的性能。

## 2: TRUNCATE 和 DELETE 的区别是什么？

DELETE 命令从一个表中删除某一行，或多行，TRUNCATE 命令永久地从表中删除每一行。

## 3：什么是触发器，MySQL 中都有哪些触发器？

触发器是指一段代码，当触发某个事件时，自动执行这些代码。在 MySQL 数据库中有如下六种触发器：

- 1、Before Insert
- 2、After Insert
- 3、Before Update
- 4、After Update
- 5、Before Delete
- 6、After Delete

  提供给程序员和数据分析员来保证数据完整性的一种方法，它是与表事件相关的特殊的存储过程。

- 可以通过数据库中的相关表实现级联更改。
- 实时监控某张表中的某个字段的更改而需要做出相应的处理。
- 例如可以生成某些业务的编号。
- 注意不要滥用，否则会造成数据库及应用程序的维护困难。
- 大家需要牢记以上基础知识点，重点是理解数据类型 CHAR 和 VARCHAR 的差异，表存储引擎 InnoDB 和 MyISAM 的区别。

## 4：FLOAT 和 DOUBLE 的区别是什么？

- FLOAT 类型数据可以存储至多 8 位十进制数，并在内存中占 4 字节。
- DOUBLE 类型数据可以存储至多 18 位十进制数，并在内存中占 8 字节。

## 5：如何在 MySQL 种获取当前日期？

```sql
SELECT CURRENT_DATE();
```

## 6：如何查询第 n 高的工资？

```sql
SELECT DISTINCT(salary) from employee ORDER BY salary DESC LIMIT n-1,1
```

## 7：请写出下面 MySQL 数据类型表达的意义（int(0)、char(16)、varchar(16)、datetime、text）

- `1、整数类型，`包括 TINYINT、SMALLINT、MEDIUMINT、INT、BIGINT，分别表示 1 字节、2 字节、3 字节、4 字节、8 字节整数。任何整数类型都可以加上 UNSIGNED 属性，表示数据是无符号的，即非负整数。

  `长度：`整数类型可以被指定长度，例如：INT(11)表示长度为 11 的 INT 类型。长度在大多数场景是没有意义的，它不会限制值的合法范围，只会影响显示字符的个数，而且需要和 UNSIGNED ZEROFILL 属性配合使用才有意义。

  `例子，`假定类型设定为 INT(5)，属性为 UNSIGNED ZEROFILL，如果用户插入的数据为 12 的话，那么数据库实际存储数据为 00012。

- `2、实数类型，`包括 FLOAT、DOUBLE、DECIMAL。

  DECIMAL 可以用于存储比 BIGINT 还大的整型，能存储精确的小数。

  而 FLOAT 和 DOUBLE 是有取值范围的，并支持使用标准的浮点进行近似计算。

  计算时 FLOAT 和 DOUBLE 相比 DECIMAL 效率更高一些，DECIMAL 你可以理解成是用字符串进行处理。

- `3、字符串类型，`包括 VARCHAR、CHAR、TEXT、BLOB

  VARCHAR 用于存储可变长字符串，它比定长类型更节省空间。VARCHAR 使用额外 1 或 2 个字节存储字符串长度。列长度小于 255 字节时，使用 1 字节表示，否则使用 2 字节表示。VARCHAR 存储的内容超出设置的长度时，内容会被截断。

  CHAR 是定长的，根据定义的字符串长度分配足够的空间。CHAR 会根据需要使用空格进行填充方便比较。CHAR 适合存储很短的字符串，或者所有值都接近同一个长度。CHAR 存储的内容超出设置的长度时，内容同样会被截断。

  **使用策略：**

  对于经常变更的数据来说，CHAR 比 VARCHAR 更好，因为 CHAR 不容易产生碎片。

  对于非常短的列，CHAR 比 VARCHAR 在存储空间上更有效率。

  使用时要注意只分配需要的空间，更长的列排序时会消耗更多内存。

  尽量避免使用 TEXT/BLOB 类型，查询时会使用临时表，导致严重的性能开销。

- `4、枚举类型（ENUM），`把不重复的数据存储为一个预定义的集合。

  有时可以使用 ENUM 代替常用的字符串类型。

  ENUM 存储非常紧凑，会把列表值压缩到一个或两个字节。

  ENUM 在内部存储时，其实存的是整数。

  尽量避免使用数字作为 ENUM 枚举的常量，因为容易混乱。

  排序是按照内部存储的整数

- `5、日期和时间类型，`尽量使用 timestamp，空间效率高于 datetime，

  用整数保存时间戳通常不方便处理。
  如果需要存储微妙，可以使用 bigint 存储。
  看到这里，这道真题是不是就比较容易回答了。

答：int(0)表示数据是 INT 类型，长度是 0、char(16)表示固定长度字符串，长度为 16、varchar(16)表示可变长度字符串，长度为 16、datetime 表示时间类型、text 表示字符串类型，能存储大字符串，最多存储 65535 字节数据）

## 8：请说明 InnoDB 和 MyISAM 的区别

- InnoDB 支持事务，MyISAM 不支持；
- InnoDB 数据存储在共享表空间，MyISAM 数据存储在文件中；
- InnoDB 支持行级锁，MyISAM 只支持表锁；
- InnoDB 支持崩溃后的恢复，MyISAM 不支持；
- InnoDB 支持外键，MyISAM 不支持；
- InnoDB 不支持全文索引，MyISAM 支持全文索引；

## 9：innodb 引擎的特性

- 插入缓冲（insert buffer)
- 二次写(double write)
- 自适应哈希索引
- 预读(read ahead)

## 11：请说明 varchar 和 text 的区别

- varchar 可指定字符数，text 不能指定，内部存储 varchar 是存入的实际字符数+1 个字节（n<=255）或 2 个字节(n>255)，text 是实际字符数+2 个字节。
- text 类型不能有默认值。
- varchar 可直接创建索引，text 创建索引要指定前多少个字符。varchar 查询速度快于 text,在都创建索引的情况下，text 的索引几乎不起作用。
- 查询 text 需要创建临时表。

## 11：varchar(50)中 50 的含义

最多存放 50 个字符，varchar(50)和(200)存储 hello 所占空间一样，但后者在排序时会消耗更多内存，因为 order by col 采用 fixed_length 计算 col 长度(memory 引擎也一样)。

## 12：int(20)中 20 的含义

是指显示字符的长度，不影响内部存储，只是当定义了 ZEROFILL 时，前面补多少个 0

## 14：创建 MySQL 联合索引应该注意什么？

需遵循前缀原则

## 15：列值为 NULL 时，查询是否会用到索引？

在 MySQL 里 NULL 值的列也是走索引的。当然，如果计划对列进行索引，就要尽量避免把它设置为可空，MySQL 难以优化引用了可空列的查询,它会使索引、索引统计和值更加复杂。

## 16：以下语句是否会应用索引：`SELECT FROM users WHERE YEAR(adddate) < 2007;`

不会，因为只要列涉及到运算，MySQL 就不会使用索引。

## 17：MyISAM 索引实现？

MyISAM 存储引擎使用 B+Tree 作为索引结构，叶节点的 data 域存放的是数据记录的地址。MyISAM 的索引方式也叫做非聚簇索引的，之所以这么称呼是为了与 InnoDB 的聚簇索引区分。

## 17：MyISAM 索引与 InnoDB 索引的区别？

- InnoDB 索引是聚簇索引，MyISAM 索引是非聚簇索引。
- InnoDB 的主键索引的叶子节点存储着行数据，因此主键索引非常高效。
- MyISAM 索引的叶子节点存储的是行数据地址，需要再寻址一次才能得到数据。
- InnoDB 非主键索引的叶子节点存储的是主键和其他带索引的列数据，因此查询时做到覆盖索引会非常高效。

## 18：以下三条 sql 如何建索引，只建一条怎么建？

```sql
WHERE a=1 AND b=1
WHERE b=1
WHERE b=1 ORDER BY time DESC
```

以顺序 b,a,time 建立联合索引，CREATE INDEX table1_b_a_time ON index_test01(b,a,time)。因为最新 MySQL 版本会优化 WHERE 子句后面的列顺序，以匹配联合索引顺序。

## 19：有 A(id,sex,par,c1,c2),B(id,age,c1,c2)两张表，其中 A.id 与 B.id 关联，现在要求写出一条 SQL 语句，将 B 中 age>50 的记录的 c1,c2 更新到 A 表中同一记录中的 c1,c2 字段中

```sql
UPDATE A,B SET A.c1 = B.c1, A.c2 = B.c2 WHERE A.id = B.id
UPDATE A INNER JOIN B ON A.id=B.id SET A.c1 = B.c1,A.c2=B.c2
再加上B中age>50的条件：
UPDATE A,B set A.c1 = B.c1, A.c2 = B.c2 WHERE A.id = B.id and B.age > 50;
UPDATE A INNER JOIN B ON A.id = B.id set A.c1 = B.c1,A.c2 = B.c2 WHERE B.age > 50
```

## MySQL 的关联查询语句

- 交叉连接（CROSS JOIN）
- 内连接（INNER JOIN）
- 外连接（LEFT JOIN/RIGHT JOIN）
- 联合查询（UNION 与 UNION ALL）
- 全连接（FULL JOIN）
- 交叉连接（CROSS JOIN）

```sql
SELECT * FROM A,B(,C)或者SELECT * FROM A CROSS JOIN B (CROSS JOIN C)#没有任何关联条件，结果是笛卡尔积，结果集会很大，没有意义，很少使用内连接（INNER JOIN）SELECT * FROM A,B WHERE A.id=B.id或者SELECT * FROM A INNER JOIN B ON A.id=B.id多表中同时符合某种条件的数据记录的集合，INNER JOIN可以缩写为JOIN
```

内连接分为三类

- 等值连接：ON A.id=B.id
- 不等值连接：ON A.id > B.id
- 自连接：SELECT \* FROM A T1 INNER JOIN A T2 ON T1.id=T2.pid

外连接（LEFT JOIN/RIGHT JOIN）

- 左外连接：LEFT OUTER JOIN, 以左表为主，先查询出左表，按照 ON 后的关联条件匹配右表，没有匹配到的用 NULL 填充，可以简写成 LEFT JOIN
- 右外连接：RIGHT OUTER JOIN, 以右表为主，先查询出右表，按照 ON 后的关联条件匹配左表，没有匹配到的用 NULL 填充，可以简写成 RIGHT JOIN

联合查询（UNION 与 UNION ALL）

```sql
SELECT * FROM A UNION SELECT * FROM B UNION ...
```

- 就是把多个结果集集中在一起，UNION 前的结果为基准，需要注意的是联合查询的列数要相等，相同的记录行会合并
- 如果使用 UNION ALL，不会合并重复的记录行
- 效率 UNION 高于 UNION ALL

全连接（FULL JOIN）

- MySQL 不支持全连接
- 可以使用 LEFT JOIN 和 UNION 和 RIGHT JOIN 联合使用

```sql
SELECT * FROM A LEFT JOIN B ON A.id=B.id UNIONSELECT * FROM A RIGHT JOIN B ON A.id=B.id
```

**嵌套查询**用一条 SQL 语句得结果作为另外一条 SQL 语句得条件，效率不好把握 SELECT \* FROM A WHERE id IN (SELECT id FROM B)

## 20：为了记录足球比赛的结果，设计表如下：team：参赛队伍表 match：赛程表其中，match 赛程表中的 hostTeamID 与 guestTeamID 都和 team 表中的 teamID 关联，查询 2006-6-1 到 2006-7-1 之间举行的所有比赛，并且用以下形式列出：拜仁 2:0 不莱梅 2006-6-21

### 首先列出需要查询的列：

- 表 team
- teamID teamName
- 表 match
- match ID
- hostTeamID
- guestTeamID
- matchTime matchResult

### 其次列出结果列：

- 主队 结果 客对 时间

初步写一个基础的 SQL：

```sql
SELECT hostTeamID,matchResult,matchTime guestTeamID from match where matchTime between "2006-6-1" and "2006-7-1";
```

通过外键联表，完成最终 SQL：

```sql
select t1.teamName,m.matchResult,t2.teamName,m.matchTime from match as m left join team as t1 on m.hostTeamID = t1.teamID, left join team t2 on m.guestTeamID=t2.guestTeamID where m.matchTime between "2006-6-1" and "2006-7-1"
```

## 21：UNION 与 UNION ALL 的区别？

- 如果使用 UNION ALL，不会合并重复的记录行
- 效率 UNION 高于 UNION ALL

## 22：一个 6 亿的表 a，一个 3 亿的表 b，通过外键 tid 关联，你如何最快的查询出满足条件的第 50000 到第 50200 中的这 200 条数据记录。

- 1、如果 A 表 TID 是自增长,并且是连续的,B 表的 ID 为索引

```sql
select * from a,b where a.tid = b.id and a.tid>50000 limit 200;
```

- 2、如果 A 表的 TID 不是连续的,那么就需要使用覆盖索引.TID 要么是主键,要么是辅助索引,B 表 ID 也需要有索引。

```sql
select * from b , (select tid from a limit 50000,200) a where b.id = a .tid;
```

## 23：拷贝表( 拷贝数据, 源表名：a 目标表名：b)

```sql
insert into b(a, b, c) select d,e,f from a;
```

## 24： Student(S#,Sname,Sage,Ssex) 学生表 Course(C#,Cname,T#) 课程表 SC(S#,C#,score) 成绩表 Teacher(T#,Tname) 教师表 查询没学过“叶平”老师课的同学的学号、姓名

```sql
select Student.S#,Student.Snamefrom Studentwhere S# not in (select distinct( SC.S#) from SC,Course,Teacher where SC.C#=Course.C# and Teacher.T#=Course.T# and Teacher.Tname=’叶平’);
```

## 25：随机取出 10 条数据

```sql
SELECT * FROM users WHERE id >= ((SELECT MAX(id) FROM users)-(SELECT MIN(id) FROM users)) * RAND() + (SELECT MIN(id) FROM users) LIMIT 10#此方法效率比直接用SELECT * FROM users order by rand() LIMIT 10高很多
```

## 26：请简述项目中优化 SQL 语句执行效率的方法，从哪些方面，SQL 语句性能如何分析？ **考点分析：**这道题主要考察的是查找分析 SQL 语句查询速度慢的方法**延伸考点：**

- 优化查询过程中的数据访问
- 优化长难的查询语句
- 优化特定类型的查询语句

## B+树索引和哈希索引的区别\*\*

B+树是一个平衡的多叉树，从根节点到每个叶子节点的高度差值不超过 1，而且同层级的节点间有指针相互链接，是有序的

![img](https://mmbiz.qpic.cn/mmbiz_jpg/UtWdDgynLdYnMu5lfXNAYzW0PPSOB8Pss8E5IlpSXicQbuCj5p3fN1vGtKkdUgeZ4IvYBx4IlFMLI4peDFvTV2w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

哈希索引就是采用一定的哈希算法，把键值换算成新的哈希值，检索时不需要类似 B+树那样从根节点到叶子节点逐级查找，只需一次哈希算法即可,是无序的

![img](https://mmbiz.qpic.cn/mmbiz_jpg/UtWdDgynLdYnMu5lfXNAYzW0PPSOB8PsAdicCricepbjicRIBIOlKdDPWlHroEiaYVgdDgicMMWbsuIlmmA4kOEVVog/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

## B 树和 B+树的区别

1、B 树，每个节点都存储 key 和 data，所有节点组成这棵树，并且叶子节点指针为 nul，叶子结点不包含任何关键字信息。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/UtWdDgynLdYnMu5lfXNAYzW0PPSOB8PsvK1h1OM5xXxKeN8BDQXdyI3nFHQ5R0akaWtCh5m0OPv8cvARObgDicg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

2、B+树，所有的叶子结点中包含了全部关键字的信息，及指向含有这些关键字记录的指针，且叶子结点本身依关键字的大小自小而大的顺序链接，所有的非终端结点可以看成是索引部分，结点中仅含有其子树根结点中最大（或最小）关键字。 (而 B 树的非终节点也包含需要查找的有效信息)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/UtWdDgynLdYnMu5lfXNAYzW0PPSOB8Psxxd09tVHZfEOicOXwrxzGFt5JibH6j44pxIpSC1ZePOFC0stO2rpBvyw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

## 什么情况下应不建或少建索引

1、表记录太少

2、经常插入、删除、修改的表

3、数据重复且分布平均的表字段，假如一个表有 10 万行记录，有一个字段 A 只有 T 和 F 两种值，且每个值的分布概率大约为 50%，那么对这种表 A 字段建索引一般不会提高数据库的查询速度。

4、经常和主字段一块查询但主字段索引值比较多的表字段

## 什么是表分区？

表分区，是指根据一定规则，将数据库中的一张表分解成多个更小的，容易管理的部分。从逻辑上看，只有一张表，但是底层却是由多个物理分区组成。

### 表分区与分表的区别

分表：指的是通过一定规则，将一张表分解成多张不同的表。比如将用户订单记录根据时间成多个表。

分表与分区的区别在于：分区从逻辑上来讲只有一张表，而分表则是将一张表分解成多张表。

### 表分区好处

1、分区表的数据可以分布在不同的物理设备上，从而高效地利用多个硬件设备。 和单个磁盘或者文件系统相比，可以存储更多数据

2、优化查询。在 where 语句中包含分区条件时，可以只扫描一个或多个分区表来提高查询效率；涉及 sum 和 count 语句时，也可以在多个分区上并行处理，最后汇总结果。

3、分区表更容易维护。例如：想批量删除大量数据可以清除整个分区。

4、可以使用分区表来避免某些特殊的瓶颈，例如 InnoDB 的单个索引的互斥访问，ext3 问价你系统的 inode 锁竞争等。

### 分区表的限制因素

1、一个表最多只能有 1024 个分区

2、在 MySQL5.5 中提供了非整数表达式分区的支持。

3、如果分区字段中有主键或者唯一索引的列，那么多有主键列和唯一索引列都必须包含进来。即：分区字段要么不包含主键或者索引列，要么包含全部主键和索引列。

4、分区表中无法使用外键约束

5、MySQL 的分区适用于一个表的所有数据和索引，不能只对表数据分区而不对索引分区，也不能只对索引分区而不对表分区，也不能只对表的一部分数据分区。

### 如何判断当前 MySQL 是否支持分区？

命令：`show variables like '%partition%'` 运行结果:

```sql
mysql> show variables like '%partition%';
+-------------------+-------+| Variable_name | Value |+-------------------+-------+| have_partitioning | YES |+-------------------+-------+1 row in set (0.00 sec)
```

have_partintioning 的值为 YES，表示支持分区。

### 分区类型

1、RANGE 分区： 这种模式允许将数据划分不同范围。例如可以将一个表通过年份划分成若干个分区

2、LIST 分区： 这种模式允许系统通过预定义的列表的值来对数据进行分割。按照 List 中的值分区，与 RANGE 的区别是，range 分区的区间范围值是连续的。

3、HASH 分区 ：这中模式允许通过对表的一个或多个列的 Hash Key 进行计算，最后通过这个 Hash 码不同数值对应的数据区域进行分区。例如可以建立一个对表主键进行分区的表。

4、KEY 分区 ：上面 Hash 模式的一种延伸，这里的 Hash Key 是 MySQL 系统产生的。

## 十六、四种隔离级别

1、Serializable (串行化)：可避免脏读、不可重复读、幻读的发生。

2、Repeatable read (可重复读)：可避免脏读、不可重复读的发生。

3、Read committed (读已提交)：可避免脏读的发生。

4、Read uncommitted (读未提交)：最低级别，任何情况都无法保证。

## MVVC

MySQL InnoDB 存储引擎，实现的是基于多版本的并发控制协议——MVCC (Multi-Version Concurrency Control) (注：与 MVCC 相对的，是基于锁的并发控制，Lock-Based Concurrency Control)。MVCC 最大的好处：读不加锁，读写不冲突。在读多写少的 OLTP 应用中，读写不冲突是非常重要的，极大的增加了系统的并发性能，现阶段几乎所有的 RDBMS，都支持了 MVCC。

1、LBCC：Lock-Based Concurrency Control，基于锁的并发控制。

2、MVCC：Multi-Version Concurrency Control，基于多版本的并发控制协议。纯粹基于锁的并发机制并发量低，MVCC 是在基于锁的并发控制上的改进，主要是在读操作上提高了并发量。

## 在 MVCC 并发控制中，读操作

1、快照读 (snapshot read)：读取的是记录的可见版本 (有可能是历史版本)，不用加锁（共享读锁 s 锁也不加，所以不会阻塞其他事务的写）。

2、当前读 (current read)：读取的是记录的最新版本，并且，当前读返回的记录，都会加上锁，保证其他事务不会再并发修改这条记录。

## Mysql 中 MyISAM 和 InnoDB 的区别有哪些？

1、InnoDB 支持事务，MyISAM 不支持，对于 InnoDB 每一条 SQL 语言都默认封装成事务，自动提交，这样会影响速度，所以最好把多条 SQL 语言放在 begin 和 commit 之间，组成一个事务；

2、InnoDB 支持外键，而 MyISAM 不支持。对一个包含外键的 InnoDB 表转为 MYISAM 会失败；

3、InnoDB 是聚集索引，数据文件是和索引绑在一起的，必须要有主键，通过主键索引效率很高。但是辅助索引需要两次查询，先查询到主键，然后再通过主键查询到数据。因此，主键不应该过大，因为主键太大，其他索引也都会很大。而 MyISAM 是非聚集索引，数据文件是分离的，索引保存的是数据文件的指针。主键索引和辅助索引是独立的。

4、InnoDB 不保存表的具体行数，执行 `select count(*) from table` 时需要全表扫描。而 MyISAM 用一个变量保存了整个表的行数，执行上述语句时只需要读出该变量即可，速度很快；

5、Innodb 不支持全文索引，而 MyISAM 支持全文索引，查询效率上 MyISAM 要高；

如何选择：

1、是否要支持事务，如果要请选择 innodb，如果不需要可以考虑 MyISAM；

2、如果表中绝大多数都只是读查询，可以考虑 MyISAM，如果既有读写也挺频繁，请使用 InnoDB。

3、系统奔溃后，MyISAM 恢复起来更困难，能否接受；

4、MySQL5.5 版本开始 Innodb 已经成为 Mysql 的默认引擎(之前是 MyISAM)，说明其优势是有目共睹的，如果你不知道用什么，那就用 InnoDB，至少不会差。

## 二十四、数据库表创建注意事项

- 剔除关系不密切的字段；
- 字段命名要有规则及相对应的含义（不要一部分英文，一部分拼音，还有类似 a.b.c 这样不明含义的字段）；
- 字段命名尽量不要使用缩写（大多数缩写都不能明确字段含义）；
- 字段不要大小写混用（想要具有可读性，多个英文单词可使用下划线形式连接）；
- 字段名不要使用保留字或者关键字；
- 保持字段名和类型的一致性；
- 慎重选择数字类型；
- 给文本字段留足余量；

1. **Myisam 和 innodb 的差别**

存储结构。myisam 一个表，三个文件。结构、数据、索引

innodb 两个文件。索引、数据保持在一个文件。

innodb 支持事务、myiam 不支持

innodb 支持外键、支持行锁

## 参考

- [企业面试题｜最常问的 MySQL 面试题集合（一）](https://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247486211&idx=1&sn=c8bbf47e3dd892443142ba9b33c37321&chksm=e91b6e1fde6ce7095709efd81614c72fcde19b00524e680a65458b25a181c73b227daa150506&scene=21#wechat_redirect)
- [企业面试题｜最常问的 MySQL 面试题集合（二)](https://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247486284&idx=1&sn=5f8ed7d5985d7feb202bdcbd3343125c&chksm=e91b6e50de6ce746831e2744188a30d99d6729be7f1344ef4c5b6add4a2b456c1acf8f4a5f58#rd)
- [面试中有哪些经典的数据库问题](https://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247486600&idx=1&sn=ffe2f7e8650db98bb1dfe874447b6863&scene=19#wechat_redirect)
