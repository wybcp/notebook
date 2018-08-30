# information_schema 数据库

information_schema 数据库是 MySQL 自带的，它提供了访问数据库元数据的方式。什么是元数据呢？元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等。有些时候用于表述该信息的其他术语包括“数据词典”和“系统目录”。

在 MySQL 中，把 information_schema 看作是一个数据库，确切说是信息数据库。其中保存着关于 MySQL 服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权限等。在 INFORMATION_SCHEMA 中，有数个只读表。它们实际上是视图，而不是基本表，因此，你将无法看到与之相关的任何文件。

information_schema 数据库表说明:

- SCHEMATA 表：提供了当前 mysql 实例中所有数据库的信息。是 show databases 的结果取之此表。
- TABLES 表：提供了关于数据库中的表的信息（包括视图）。详细表述了某个表属于哪个 schema，表类型，表引擎，创建时间等信息。是 show tables from schemaname 的结果取之此表。
- COLUMNS 表：提供了表中的列信息。详细表述了某张表的所有列以及每个列的信息。是 show columns from schemaname.tablename 的结果取之此表。
- STATISTICS 表：提供了关于表索引的信息。是 show index from schemaname.tablename 的结果取之此表。
- USER_PRIVILEGES（用户权限）表：给出了关于全程权限的信息。该信息源自 mysql.user 授权表。是非标准表。
- SCHEMA_PRIVILEGES（方案权限）表：给出了关于方案（数据库）权限的信息。该信息来自 mysql.db 授权表。是非标准表。
- TABLE_PRIVILEGES（表权限）表：给出了关于表权限的信息。该信息源自 mysql.tables_priv 授权表。是非标准表。
- COLUMN_PRIVILEGES（列权限）表：给出了关于列权限的信息。该信息源自 mysql.columns_priv 授权表。是非标准表。
- CHARACTER_SETS（字符集）表：提供了 mysql 实例可用字符集的信息。是 SHOW CHARACTER SET 结果集取之此表。
- COLLATIONS 表：提供了关于各字符集的对照信息。
- COLLATION_CHARACTER_SET_APPLICABILITY 表：指明了可用于校对的字符集。这些列等效于 SHOW COLLATION 的前两个显示字段。
- TABLE_CONSTRAINTS 表：描述了存在约束的表。以及表的约束类型。
- KEY_COLUMN_USAGE 表：描述了具有约束的键列。
- ROUTINES 表：提供了关于存储子程序（存储程序和函数）的信息。此时，ROUTINES 表不包含自定义函数（UDF）。名为“mysql.proc name”的列指明了对应于 INFORMATION_SCHEMA.ROUTINES 表的 mysql.proc 表列。
- VIEWS 表：给出了关于数据库中的视图的信息。需要有 show views 权限，否则无法查看视图信息。
- TRIGGERS 表：提供了关于触发程序的信息。必须有 super 权限才能查看该表
