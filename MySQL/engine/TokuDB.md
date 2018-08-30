TokuDB是一个支持事务的“新”引擎，有着出色的数据压缩功能，由美国TokuTek公司(http://www.tokutek.com/) 研发，该公司于2015年4月份被Percona收购。

## 优点


出色的数据压缩功能，较低的IOPS消耗，如果您的数据量比较大，强烈建议您使用TokuDB，以节省空间成本，而且有着与InnoDB相当的性能。

+ 使用fractal树索，插入性能快20~80倍；
+ 压缩数据减少存储空间；
+ 使用bulk loader，数据量可以扩展到几个TB；
+ 不会产生索引碎片；
+ hot scheme modification，支持在线创建索引和添加、删除
+ 支持hot column addition ， hot indexing， mvcc；


## 注意点

不支持外键(foreign key)功能，如果您的表有外键，切换到TokuDB引擎后，此约束将被忽略!!!



##压缩算法

 tokudb_zlib:表启用zlib压缩，压缩效果偏中，CPU消耗偏中，建议使用(默认)；
 tokudb_quicklz:表启用quicklz压缩，压缩效果差，CPU消耗低；
 tokudb_lzma:表启用lzma压缩，压缩效果好，CPU消耗高。

TokuDB默认压缩算法为zlib，建议您不要做修改，因为zlib压缩的性价比非常高。

## 使用

1.如果要存储blob，不要使用tokuDB，因为他的记录不能太大；
2.如果记录数过亿，使用tokuDB；
3.如果注重update的性能，不要使用tokuDB，他没有innodb快；
4.如果要存储旧的记录，使用tokuDB；
5.如果要缩小数据占用的存储空间，使用tokuDB；
日志数据

