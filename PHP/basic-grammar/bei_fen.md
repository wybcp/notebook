# 备份

第一种方法：在复制数据文件时使用lock tables命令锁定表。
```
lock tables table lock_type；
```
lock_type可以是READ或WRITE。