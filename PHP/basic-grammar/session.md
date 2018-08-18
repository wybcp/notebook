# Session

PHP session 变量用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。Session 变量存储单一用户的信息，并且对于应用程序中的所有页面都是可用的。
##开始 PHP Session
在您把用户信息存储到 PHP session 中之前，首先必须启动会话。

注释：session_start() 函数必须位于 <html> 标签之前：

## 存储 Session 变量
存储和取回 session 变量的正确方法是使用 PHP $_SESSION 变量

##销毁 Session

+ unset() 函数用于释放指定的 session 变量;
+  session_destroy() 函数彻底销毁 session