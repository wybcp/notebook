# MEMORY 存储引擎

如果临时存放数据，数据量不大，且不需要较高的数据安全性，可以选用 Memory。

Memory 存储引擎使用存在于内存中的内容来创建表。每个 memory 表只实际对应一个磁盘文件，格式是.frm。memory 类型的表访问非常的快，因为它的数据是放在内存中的，并且默认使用 HASH 索引，但是一旦服务关闭，表中的数据就会丢失掉。

MEMORY 存储引擎的表可以选择使用 BTREE 索引或者 HASH 索引，两种不同类型的索引有其不同的使用范围

Hash 索引优点：Hash 索引结构的特殊性，其检索效率非常高，索引的检索可以一次定位，不像 B-Tree 索引需要从根节点到枝节点，最后才能访问到页节点这样多次的 IO 访问，所以 Hash 索引的查询效率要远高于 B-Tree 索引。

Hash 索引缺点：那么不精确查找呢，也很明显，因为 hash 算法是基于等值计算的，所以对于“like”等范围查找 hash 索引无效，不支持；

Memory 类型的存储引擎主要用于哪些内容变化不频繁的代码表，或者作为统计操作的中间结果表，便于高效地对中间结果进行分析并得到最终的统计结果，。对存储引擎为 memory 的表进行更新操作要谨慎，因为数据并没有实际写入到磁盘中，所以一定要对下次重新启动服务后如何获得这些修改后的数据有所考虑。

memory 使用存在内存中的内容来创建表。每个 MEMORY 表实际对应一个磁盘文件，格式是.frm。MEMORY 类型的表访问非常快，因为它到数据是放在内存中的，并且默认使用 HASH 索引，但是一旦服务器关闭，表中的数据就会丢失，但表还会继续存在。

默认情况下，memory 数据表使用散列索引，利用这种索引进行“相等比较”非常快，但是对“范围比较”的速度就慢多了。因此，散列索引值适合使用在"="和"<=>"的操作符中，不适合使用在"<"或">"操作符中，也同样不适合用在 order by 字句里。如果确实要使用"<"或">"或 betwen 操作符，可以使用 btree 索引来加快速度。

存储在 MEMORY 数据表里的数据行使用的是长度不变的格式，因此加快处理速度，这意味着不能使用 BLOB 和 TEXT 这样的长度可变的数据类型。VARCHAR 是一种长度可变的类型，但因为它在 MySQL 内部当作长度固定不变的 CHAR 类型，所以可以使用。

```sql
create table tab_memory engine=memory select id,name,age,addr from man order by id;
```

使用 USING HASH/BTREE 来指定特定到索引。

```sql
create index mem_hash using hash on tab_memory(city_id);
```

在启动 MySQL 服务的时候使用--init-file 选项，把 insert into...select 或 load data infile 这样的语句放入到这个文件中，就可以在服务启动时从持久稳固的数据源中装载表。

服务器需要足够的内存来维持所在的在同一时间使用的 MEMORY 表，当不再使用 MEMORY 表时，要释放 MEMORY 表所占用的内存，应该执行 DELETE FROM 或 truncate table 或者删除整个表。

每个 MEMORY 表中放置到数据量的大小，受到 max_heap_table_size 系统变量的约束，这个系统变量的初始值是 16M，同时在创建 MEMORY 表时可以使用 MAX_ROWS 子句来指定表中的最大行数。
