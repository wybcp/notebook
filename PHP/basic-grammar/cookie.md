# Cookie
cookie 常用于识别用户。
##创建 Cookie
setcookie() 函数用于设置 cookie。

注释：setcookie() 函数必须位于 <html> 标签之前。

语法:
```setcookie(name, value, expire, path, domain);```

## 取回 Cookie
PHP 的` $_COOKIE `变量用于取回 cookie 的值。

isset() 函数确认是否已设置了 cookie

## 删除 Cookie

删除 cookie 时，您应当使过期日期变更为过去的时间点。