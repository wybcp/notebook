# 函数

## 信息函数

- SELECT CONNECTION_ID(); 连接 ID，登录当天几次就是 ID 号
- select DATEBASE(); 当前数据库
- select LAST_INSERT_ID(); 当天最后插入几次记录的就是 ID 号
- select USER(); 当前用户，如 root
- select VERSION(); 版本信息
- select MD5()：信息摘要算法，为以后的 Web 页面做准备，尽量使用 MD5()

  举例： SELECT MD5('admin');
- select PASSWORD()：密码算法，通过 PASSWORD()修改当前用户和其他用户的密码，修改客户端自己的密码

## 时间函数

- NOW(); 当前时间 2018-08-29 22:59:39
- CURDATE(); 当前日期 2018-08-29
- CURTIME(); 当前时间 22:59:39
- SELECT DATE_ADD('2017-4-21',INTERVAL 365 DAY); 日期变化；2018-4-21 与（1 YEAR）等价
- SELECT DATEDIFF('2013-2-12','2014-2-12') 日期之差：-365
- SELECT DATE_FORMAT(NOW(),'%m/%d/%Y'); 定义时间格式

## 比较运算符函数

- [NOT]BETWEEN...AND... //是否[不]在数字 1 与数字 2 之间。
- [NOT]IN() //是否[不]在列出值范围内。例 "10 IN(5,10,15,20)" 得到 1
- IS [NOT] NULL //是否[不]为空。

  SELECT \* FROM test WHERE first_name IS NULL; //查找 test 表中 first_name 字段里为空的记录。

## 数字函数

- SELECT CEIL(3.01); 进一取整：4
- SELECT FLOOR(3.99); 舍一取整：3
- SELECT 9 DIV 4; 整数除法:2(注意结果是整数)与除法/等价
- SELECT 5 MOD 3; 取余数(模)
- SELECT POWER(3，3) 幂运算，表示三个 3 次方：27
- SELECT ROUND(7.7); 四舍五入法：8
- TRUNCATE(125.89,1) //数字截取 截取小数点后 1 位，即 125.8 ;截取位可为负数，例如-1，即得到 120

## 字符函数

- `SELECT CONCAT('A','B')` 字符连接作用：AB
- `SELECT CONCAT_WS('-','A','B','C')` 使用指定的分隔符进行连接：A-B-C
- `SELECT FORMAT(1234.734,2)` 1,234.73(四舍五入法)
- `SELECT LOWER()` 转小写
- `SELECT UPPER()` 转大写
- `SELECT LEFT('ABCEF',3)` 在左边获取几个字符：ABC
- `SELECT RIGHT('ABCEF',3)` 在右边获取几个字符：ECF
- ltrim() 删除前导空格
- rtrim()删除后导空格
- trim() 删除全部空格
- `SELECT REPLACE('??MySQL???','?','')` 替换字符串中的某些字符:
- `SELECT SUBSTRING('MySQL',1,2);` 利用 SUBSTRING()截取字符串中的一部分字符串
- `SELECT * FROM test WHERE first_name LIKE '%1%%' ESCAPE '1';` 利用 LIKE 查找含特定字符的字符串

意思是查找字段 first_name 中含字符%的记录

## 自定义函数

自定义函数：UDF 是对 MySQL 扩展的途径，其用法与内置函数相同。

必要条件：返回值（必须），参数（非必须）

MySQL 中参数的数量不能超过 1024 个
创建自定义函数：

```
CREATE FUNCTION function_name(参数) RETURNS 返回值类型

{STRING|INTEGER|REAL|DECIMAL}

RETURN 返回值
```

routine_body 函数体

1. 函数体由合法的 SQL 语句构成；
2. 函数体可以是简单的 SELECT 或 INSERT 语句；
3. 函数体如果为复合结构则使用 BEGIN...END 语句；
4. 复合结构可以包含声明，循环，控制结构；

删除函数：

```sql
DROP FUNCTION [IF EXISTS] function_name;
```

---

CREATE FUNCTION 函数名称(参数列表)
　　 RETURNS 返回值类型
　　函数体
删除自定义函数:
　　 DROP FUNCTION function_name
调用自定义函数语法:
　　 SELECT function_name(parameter_value,...)
自定义函数中定义局部变量语法:
DECLARE 变量 1[,变量 2,... ]变量类型 [DEFAULT 默认值];
为变量赋值语法:
SET parameter_name = value[,parameter_name = value...];
