# [Monolog](https://github.com/Seldaek/monolog)：PHP 日志记录工具

Monolog是php下比较全又容易扩展的记录日志组件。目前有包括Symfony 、Laravel、 CakePHP等诸多知名php框架都内置了Monolog。

Monolog可以把你的日志发送到文件，sockets，收件箱，数据库和各种web服务器上。一些特殊的组件可以给你带来特殊的日志策略。

## 使用例子

```php
<?php

use Monolog\Logger;
use Monolog\Handler\StreamHandler;

// create a log channel
$log = new Logger('name');
$log->pushHandler(new StreamHandler('path/to/your.log', Logger::WARNING));

// add records to the log
$log->addWarning('Foo');
$log->addError('Bar');
```

## 核心概念

每个Logger实例都有一个通道和日志处理器栈。每当你添加一条日志记录，它会被发送到日志处理器栈。 你可以创建很多`Logger，`每个Logger定义一个通道（db，请求，路由），每个Logger有很多日志处理器。这些通道会过滤日志。

每个日志处理器都有一个Formatter（内置的日志显示格式处理器）。你还可以设定日志级别。

## 日志级别

1.  DEBUG：详细的debug信息
2. INFO：感兴趣的事件。像用户登录，SQL日志
3. NOTICE：正常但有重大意义的事件。
4. WARNING**：**发生异常，使用了已经过时的API。
5. ERROR：运行时发生了错误，错误需要记录下来并监视，但错误不需要立即处理。
6. CRITICAL：关键错误，像应用中的组件不可用。
7. ALETR：需要立即采取措施的错误，像整个网站挂掉了，数据库不可用。这个时候触发器会通过SMS通知你，