# 锁

## 乐观锁

```mysql
update table table_name
set column_name = value, version=version+1
where version = version;
```

## 悲观锁

```mysql
update table table_name set column_name = value for update;
```

## 共享锁

x 锁

- 脏读：一个事务内修改了数据，另一个事务读取并使用了这个数据；
- 幻读：一个事务内修改了涉及全表的数据，另一个事务往这个表里面插入了新的数据，第一个事务出现幻读；
- 不可重复读：一个事务内连续读了两次数据，中间另一个事务修改了这个数据，导致第一个事务前后两次读的数据不一致；
- 更新丢失：一个事务内变更了数据，另一个事务修改了这个数据，最后前一个事务 commit 导致另一个事务的变更丢失；
