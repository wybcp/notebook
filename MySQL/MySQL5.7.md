# MySQL5.7

## 服务增强

### 初始化方式变更

### 支持为表增加计算列

[计算列](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html)：由表的其他数据列计算得到。

之前使用触发器实现相关功能。

```mysql
col_name data_type [GENERATED ALWAYS] AS (expression)
  [VIRTUAL | STORED] [UNIQUE [KEY]] [COMMENT comment]
  [[NOT] NULL] [[PRIMARY] KEY]
```

### JSON

json列类型

JSON函数：json_开头

## Replication增强

+ 支持多源复制

+ 基于库或逻辑的多线程复制

+ 在线变更复制模式



## Innodb增强
+ 支持缓冲池大小在线变更
+ 增加innodb_buffer_pool导入导出功能
+ 支持为innodb表建立表空间


## 安全及管理增强

+ 移除old_password认证
+ 增加账号默认过期时间
+ 账号管理
+ sys管理数据库
