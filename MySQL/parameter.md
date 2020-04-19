# 参数

- 全局变量：适用于所有新连接
- 会话变量：仅适用于当前连接

```sql
#当前所有连接适用
set global long_query_time=1;
#持久化，保存在data目录的mysqld-auto.cnf
set persist long_query_time=1;
#当前会话适用
set session long_query_time=1;
```

linux的datadir默认`/var/lib/mysql`。
