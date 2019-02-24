# 外键约束

保持数据的一致性，完整性。实现数据表的一对一，一对多的关系。

1. 父表（子表所参照的表）和子表（具有外键列的表）必须使用相同的存储引擎，而且禁止使用临时表。
2. 数据表的存储引擎只能为 InnoDB
3. 外键列（曾经加过 foreign 关键词的那一列）和参照列（外键列所参照的那列）必须具有相似的数据类型(字符，整型，日期时间等）。其中数字的长度或是否有符号位（如整型有无符号(unsigned)和有符号(signed)两种类型;）必须相同；而字符的长度则可以不同。比如说父表里面有一个参数 id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,子表里面就要写作 pid SMALLINT UNSIGNED(符号位和数据类型要相似)
4. 外键列和参照列必须创建索引。如果外键列不存在索引的话，MySQL 将自动创建索引。

```sql
FOREIGN KEY (pid)REFERENCES 父表名(id)
```

也就是 users 表中有两个索引（id pid）

- 外键列：pid （可自定义）
- 参照列：id （可自定义）

查看索引：

```sql
SHOW INDEXES FROM table_name;
```

以网格方式来查看索引：

```sql
SHOW INDEXES FROM table_name\G;
```
