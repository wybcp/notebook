# UNION

union 将多个select语句的结果组合合成为一个结果集合，相应表对应的列数和数据类型必须相同。

- union 执行时删除重复记录，所有返回行都是唯一的
- union all ：不删除重复行也不对结果进行自动排序

```sql
select column_name... from table1
union
select column_name... from table2
```
