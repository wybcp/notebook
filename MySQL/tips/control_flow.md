# [Control Flow](https://dev.mysql.com/doc/refman/8.0/en/control-flow-functions.html)

## CASE

Case operator

```sql
CASE value
WHEN [compare_value] THEN result [WHEN [compare_value] THEN result ...]
[ELSE result]
END
```

NULL if there is no ELSE part.

## IF()

If/else construct

`IF(expr1,expr2,expr3)`

If expr1 is TRUE (expr1 <> 0 and expr1 <> NULL), `IF()` returns expr2. Otherwise, it returns expr3.

## IFNULL()

Null if/else construct

`IFNULL(expr1,expr2)`

If expr1 is not NULL, `IFNULL()` returns expr1; otherwise it returns expr2.

## NULLIF()

Return NULL if expr1 = expr2
