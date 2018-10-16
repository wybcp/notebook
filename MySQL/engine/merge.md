# MERGE

merge 存储引擎是一组 MyISAM 表的组合，这些 MyISAM 表结构必须完全相同，MERGE 表中并没有数据，对 MERGE 类型的表可以进行查询、更新、删除的操作，这些操作实际上是对内部的 MyISAM 表进行操作。对于对 MERGE 表进行的插入操作，是根据 INSERT_METHOD 子句定义的插入的表，可以有 3 个不同的值，first 和 last 值使得插入操作被相应的作用在第一个或最后一个表上，不定义这个子句或者为 NO，表示不能对这个 MERGE 表进行插入操作。可以对 MERGE 表进行 drop 操作，这个操作只是删除 MERGE 表的定义，对内部的表没有任何影响。MERGE 在磁盘上保留 2 个以 MERGE 表名开头文件：.frm 文件存储表的定义；.MRG 文件包含组合表的信息，包括 MERGE 表由哪些表组成，插入数据时的依据。可以通过修改.MRG 文件来修改 MERGE 表，但是修改后要通过 flush table 刷新。
