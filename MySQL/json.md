# json

从 MySQL 5.7 原生支持 json 格式。

## 使用

插入接送数据：

```sql
insert into user values(1,{'name':'xxx','age':20}),(2,{'name':'xx','age':21});
```

获取 key-value：

```sql
select id ,JSON_EXTRACT(context,'$.name') name,JSON_EXTRACT(context,'$.age') age from user;
```

获取所有的键：

```sql
select id,json_keys(context) from user;
```

增加 key-value：

```sql
update user set context=JSON_INSERT(context,'$.address','cd') where id =21;
```

更改 key-value：

```sql
update user set context=JSON_SET(context,'$.address','cq') where id =21;
```

删除 key-value：

```sql
update user set context=JSON_REMOVE(context,'$.address') where id =21;
```
