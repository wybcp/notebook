# SQL 注入

SQL Injection

通过把 SQL 命令插入到 Web 表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的 SQL 命令。

我们永远不要信任用户的输入，我们必须认定用户输入的数据都是不安全的，我们都需要对用户输入的数据进行过滤处理。

## prepareStatement+Bind-Variable

Bind-Variable 绑定变量

## 转换函数

使用应用程序提供的对特殊字符进行转换的函数。

PHP 的 MySQL 扩展提供了 mysql_real_escape_string()函数来转义特殊的输入字符。

```php
if (get_magic_quotes_gpc())
{
 $name = stripslashes($name);
}
$name = mysql_real_escape_string($name);
mysql_query("SELECT * FROM users WHERE name='{$name}'");
```

## 自定义校验函数

## Laravel 的 SQL 查询

在 PHP 的项目里要避免 SQL 注入需要两个条件：

- 使用 Prepared Statement + 参数绑定
- 绝对不手动拼接 SQL

在 Laravel 里所有的 SQL 查询都是 Prepared Statement 模式
