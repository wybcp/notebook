# 触发器

触发器是一种与表操作有关的数据库对象，当触发器所在表上出现指定事件时，将调用该对象，即表的操作事件触发表上的触发器的执行。

触发器尽量少的使用，因为不管如何，它还是很消耗资源，如果使用的话要谨慎的使用，确定它是非常高效的：触发器是针对每一行的；对增删改非常频繁的表上切记不要使用触发器，因为它会非常消耗资源。

```sql
CREATE
    [DEFINER = { user | CURRENT_USER }]
TRIGGER trigger_name
trigger_time trigger_event
ON tbl_name FOR EACH ROW
　　[trigger_order]
trigger_body

trigger_time: { BEFORE | AFTER }

trigger_event: { INSERT | UPDATE | DELETE }

trigger_order: { FOLLOWS | PRECEDES } other_trigger_name
```

- BEFORE 和 AFTER 参数指定了触发执行的时间，在事件之前或是之后。

- FOR EACH ROW 表示任何一条记录上的操作满足触发事件都会触发该触发器，也就是说触发器的触发频率是针对每一行数据触发一次。

- tigger_event：

  - INSERT 型触发器：插入某一行时激活触发器，可能通过 INSERT、LOAD DATA、REPLACE 语句触发(LOAD DAT 语句用于将一个文件装入到一个数据表中，相当与一系列的 INSERT 操作)；

  - UPDATE 型触发器：更改某一行时激活触发器，可能通过 UPDATE 语句触发；

  - DELETE 型触发器：删除某一行时激活触发器，可能通过 DELETE、REPLACE 语句触发。

- trigger_order 是 MySQL5.7 之后的一个功能，用于定义多个触发器，使用 follows(尾随)或 precedes(在…之先)来选择触发器执行的先后顺序。

## 查看 trigger

```sql
show triggers;
```

or

```sql
select * from information_schema.triggers where condition;
```

## 删除trigger

```sql
drop trigger [schema_name.]trigger_name;
```

## 常见用途

检查插入到表中的值，或者对更新涉及的值进行计算。
