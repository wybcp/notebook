# 错误处理

在 PHP 中，默认的错误处理很简单。一条错误消息会被发送到浏览器，这条消息带有文件名、行号以及描述错误的消息。

PHP中提供了一个错误控制运算符“@”，对于一些可能会在运行过程中出错的表达式时，我们不希望出错的时候给客户显示错误信息，这样对用户不友好。于是，可以将@放置在一个PHP表达式之前，该表达式可能产生的任何错误信息都被忽略掉。

## 基本的错误处理：使用 die() 函数
## 创建自定义错误处理器

创建一个自定义的错误处理器非常简单。我们很简单地创建了一个专用函数，可以在 PHP 中发生错误时调用该函数。

该函数必须有能力处理至少两个参数 (error level 和 error message)，但是可以接受最多五个参数（可选的：file, line-number 和 error context）：
语法
`error_function(error_level,error_message,
error_file,error_line,error_context)`

|参数 | 描述 |
| -- | -- |
|error_level|	必需。为用户定义的错误规定错误报告级别。必须是一个数字。参见下面的表格：错误报告级别。
|error_message|	必需。为用户定义的错误规定错误消息。
|error_file	|可选。规定错误发生的文件名。
|error_line	|可选。规定错误发生的行号。
|error_context	|可选。规定一个数组，包含了当错误发生时在用的每个变量以及它们的值。



|值	|常量	|描述|
||||
2	E_WARNING	非致命的 run-time 错误。不暂停脚本执行。
8	E_NOTICE	run-time 通知。在脚本发现可能有错误时发生，但也可能在脚本正常运行时发生。
256	E_USER_ERROR	致命的用户生成的错误。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_ERROR。
512	E_USER_WARNING	非致命的用户生成的警告。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_WARNING。
1024	E_USER_NOTICE	用户生成的通知。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_NOTICE。
4096	E_RECOVERABLE_ERROR	可捕获的致命错误。类似 E_ERROR，但可被用户定义的处理程序捕获。（参见 set_error_handler()）
8191	E_ALL	所有错误和警告。（在 PHP 5.4 中，E_STRICT 成为 E_ALL 的一部分）

