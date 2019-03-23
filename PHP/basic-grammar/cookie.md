# Cookie

cookie 常用于识别用户。cookie 是一种服务器留在用户计算机上的小文件。每当同一台计算机通过浏览器请求页面时，这台计算机将会发送 cookie。通过 PHP，您能够创建并取回 cookie 的值。

## 创建 Cookie

`setcookie()` 函数用于设置 cookie。

注释：`setcookie()` 函数必须位于 `<html>` 标签之前。

语法:`setcookie(name, value, expire, path, domain);`

## 取回 Cookie

PHP 的`$_COOKIE`变量用于取回 cookie 的值。

isset() 函数确认是否已设置了 cookie。

## 删除 Cookie

删除 cookie 时，您应当使过期日期变更为过去的时间点。

## 如果浏览器不支持 Cookie

如果是不支持 cookie 的浏览器，采取其他方式传递信息。例如通过表单传递数据。
