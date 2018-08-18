# 优化

##设计优化

数据越小越好。使用最小化冗余设计思想实现。

尽可能使NULL最小，使主键尽可能短。

避免使用可变长度列（VARCHAR/TEXT/BLOB）。

但如果字段长度固定，速度更快，但要占用跟多的空间。

##表的优化

修复支离破碎的表
`optimize table tablename;`或者`myisamchk -r table;`

## 使用索引
