
safe-update 选项，避免没有 WHERE 条件的全表数据被修改；

MySQL 在沒有 WHERE 或 LIMIT 條件下會拒絕執行 UPDATE 或 DELETE querey，即使是沒有 KEY column 的 WHERE 條件也會拒絕執行。

```
show variables like 'SQL_SAFE_UPDATES';查看开关状态。
```


要解決就是將 MySQL 的 Safe Update Mode 關閉:


```
SET SQL_SAFE_UPDATES=0;
```

如果要重新啟用 Safe Update Mode，只要執行:

SET SQL_SAFE_UPDATES=1;