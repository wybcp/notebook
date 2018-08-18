# 异常处理

异常处理用于在指定的错误（异常）情况发生时改变脚本的正常流程。这种情况称为异常。

当异常被触发时，通常会发生：
+ 当前代码状态被保存
+ 代码执行被切换到预定义（自定义）的异常处理器函数
+ 根据情况，处理器也许会从保存的代码状态重新开始执行代码，终止脚本执行，或从代码中另外的位置继续执行脚本

不同的错误处理方法：
+ 异常的基本使用
+ 创建自定义的异常处理器
+ 多个异常
+ 重新抛出异常
+ 设置顶层异常处理器

## 异常的基本使用
当异常被抛出时，其后的代码不会继续执行，PHP 会尝试查找匹配的 "catch" 代码块。


适当的处理异常代码应该包括：
+ Try - 使用异常的函数应该位于 "try" 代码块内。如果没有触发异常，则代码将照常继续执行。但是如果异常被触发，会抛出一个异常。
+ Throw - 里规定如何触发异常。每一个 "throw" 必须对应至少一个 "catch"。
+ Catch - "catch" 代码块会捕获异常，并创建一个包含异常信息的对象。


## 设置顶层异常处理器

set_exception_handler() 函数可设置处理所有未捕获异常的用户定义函数。
```<?php
function myException($exception)
{
	echo "<b>Exception:</b> " , $exception->getMessage();
}

set_exception_handler('myException');

throw new Exception('Uncaught Exception occurred');
?>
```