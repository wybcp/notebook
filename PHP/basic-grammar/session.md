# Session

PHP session 变量用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。Session 变量存储单一用户的信息，并且对于应用程序中的所有页面都是可用的。

会话信息是临时的。

Session 的工作机制是：为每个访客创建一个唯一的 id (UID)，并基于这个 UID 来存储变量。UID 存储在 cookie 中，或者通过 URL 进行传导。

## 开始 Session

在您把用户信息存储到 PHP session 中之前，首先必须启动会话。

注释：session_start() 函数必须位于 `<html>` 标签之前。

也可以在 php.ini 里启动`session.auto_start=1`，这样就无需每次使用 session 之前都要调用 session_start()。启用此指令的缺点是无法在会话中存储对象，因为定义要在会话开始之前加载才能重新创建对象。

## 存储 Session 变量

存储和取回 session 变量的正确方法是使用 PHP `$_SESSION` 变量

## 销毁 Session

- unset() 函数用于释放指定的 session 变量;
- session_destroy() 函数彻底销毁 session

## 配置

php.ini #配置文件中有一组会话配置选项，可以对其进行设置：

```conf
session.save_handler = files ; #如何存储session信息
session.save_path = /tmp ; #save_handler 设为文件时， session文件保存的路径
session.use_cookies = 1 ; #是否使用cookies
session.name = PHPSESSID；  #用在cookie里的session的名字
session.auto_start = 0 ; #是否自动启动session
session.cookie_lifetime = 0 ; #设置会话cookie的有效期，以秒为单位，为0时表示直到浏览器被重启
session.cookie_path = / ; #cookie的有效路径
session.cookie_domain = ; #cookie的有效域
session.cache_expire = 180 ; #设置缓存中的会话文档在 n 分钟后过时
```
