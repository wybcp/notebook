# 子查询

子查询（Subquery）是指出现在其他 sql 语句内的 select 字句，子查询指嵌套在查询内部，且必须始终出现在圆括号内。

MySQL 通过内部的优化器将子查询改写成关联查询，支持 select。

通常情况下，希望由内到外，先完成内表的查询，在查询外表。

- 子查询可以包换多个关键字或条件 如 distinct，group by，order by，limit，函数等。
- 子查询的外层查询可以是 select insert update set do。
- 子查询的外层查询并不单指是查找，而是所有 sql 语句的统称。
- 子查询返回多条记录，ANY ,SOME, ALL 修饰的比较运算符
  ![image](http://img.mukewang.com/590bd62c000103e912800720.jpg)
- IN 、 NOT IN

  IN 等价于 =ANY \ =SOME

  NOT IN 等价于 !=ALL \ <>ALL
- 如果子查询返回任何行，EXISTS 将返回 TRUE,否则为 FALSE.
- exists   关键词，对子查询判断是否返回行`select * from table_name where exists (子查询)`
