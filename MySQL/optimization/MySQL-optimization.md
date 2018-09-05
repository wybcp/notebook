# mysql 优化

- 不要查询不需要的列
- 不要在多表关联返回全部的列
- 不要 `select *`
- 不要重复查询，应当写入缓存
- 尽量使用关联查询来替代子查询。
- 尽量使用索引优化。如果不使用索引。mysql 则使用临时表或者文件排序。如果不关心结果集的顺序，可以使用 order by null 禁用文件排序。
- 优化分页查询，最简单的就是利用覆盖索引扫描。而不是查询所有的列
- 应尽量避免在 where 子句中使用 !=或<> 操作符，否则将引擎放弃使用索引而进行全表扫描。
- 对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引

- 尽量不要使用前缀%

  ```sql
  select * from user where name like '%a'
  ```

- 应尽量避免在 where 子句中对字段进行表达式操作
- 应尽量避免在 where 子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描
- 很多时候用 exists 代替 in 是一个好的选择：
- 对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引。
- 应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描，如：

    ```sql
    select id from t where num is null;# 可以在num上设置默认值0，确保表中num列没有null值，然后这样查询：select id from t where num=
    ```
- 4.应尽量避免在 where 子句中使用 or 来连接条件，否则将导致引擎放弃使用索引而进行全表扫描，如：

    ```sql
    select id from t where num=10 or num=20;
    #可以这样查询：
    select id from t where num=10 union all select id from t where num=20;
    ```
