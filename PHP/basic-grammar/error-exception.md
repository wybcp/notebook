# 错误和异常

在编码的时候，我们无时无刻会遇到错误和异常，所以我们需要处理这些错误。

## 错误

PHP 中提供了一个错误控制运算符“@”，对于一些可能会在运行过程中出错的表达式时，我们不希望出错的时候给客户显示错误信息，这样对用户不友好。于是，可以将@放置在一个 PHP 表达式之前，该表达式可能产生的任何错误信息都被忽略掉。（不建议使用 log 记录）

在开发模式中，我们一般需要打开**error_reporting** 设置为**E_ALL**。然后把**display_errors** 设置为 on。

如果需要记录错误日志，则需要配置 log_errors.

开发者可以通过 set_error_handle()自定义的错误处理器，该函数必须有能力处理至少两个参数 (error level 和 error message)，但是可以接受最多五个参数（可选的：file, line-number 和 error context）：
语法
`error_function(error_level,error_message, error_file,error_line,error_context)`

| 参数          | 描述                                                                                   |
| ------------- | -------------------------------------------------------------------------------------- |
| error_level   | 必需。为用户定义的错误规定错误报告级别。必须是一个数字。参见下面的表格：错误报告级别。 |
| error_message | 必需。为用户定义的错误规定错误消息。                                                   |
| error_file    | 可选。规定错误发生的文件名。                                                           |
| error_line    | 可选。规定错误发生的行号。                                                             |
| error_context | 可选。规定一个数组，包含了当错误发生时在用的每个变量以及它们的值。                     |

php 的错误类型有

- E_ERROR 致命的错误。会中断程序的执行
- E_WARNING 警告。不会中断程序
- E_NOTICE 通知，运行时通知。表示脚本遇到可能会表现为错误的情况
- E_PARSE 解析错误，一般是语法错误。
- E_STRICT PHP 对代码的修改建议
- E_DEPRECATED 将会对在未来版本中可能无法正常工作的代码给出警告

```php
set_error_handle(function($errno,$errstr,$errfile,$errline){

})

/**
* throw exceptions based on E_* error types
*/
set_error_handler(function ($err_severity, $err_msg, $err_file, $err_line, array $err_context)
{
    // error was suppressed with the @-operator
    if (0 === error_reporting()) { return false;}
    switch($err_severity)
          {
              case E_ERROR:
                throw new ErrorException            ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_WARNING:
                throw new WarningException          ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_PARSE:
                throw new ParseException            ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_NOTICE:
                throw new NoticeException           ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_CORE_ERROR:
                throw new CoreErrorException        ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_CORE_WARNING:
                throw new CoreWarningException      ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_COMPILE_ERROR:
                throw new CompileErrorException     ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_COMPILE_WARNING:
                throw new CoreWarningException      ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_USER_ERROR:
                throw new UserErrorException        ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_USER_WARNING:
                throw new UserWarningException      ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_USER_NOTICE:
                throw new UserNoticeException       ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_STRICT:
                throw new StrictException           ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_RECOVERABLE_ERROR:
                throw new RecoverableErrorException ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_DEPRECATED:
                throw new DeprecatedException       ($err_msg, 0, $err_severity, $err_file, $err_line);
              case E_USER_DEPRECATED:
                throw new UserDeprecatedException   ($err_msg, 0, $err_severity, $err_file, $err_line);
          }
      });

class WarningException              extends ErrorException {}
class ParseException                extends ErrorException {}
class NoticeException               extends ErrorException {}
class CoreErrorException            extends ErrorException {}
class CoreWarningException          extends ErrorException {}
class CompileErrorException         extends ErrorException {}
class CompileWarningException       extends ErrorException {}
class UserErrorException            extends ErrorException {}
class UserWarningException          extends ErrorException {}
class UserNoticeException           extends ErrorException {}
class StrictException               extends ErrorException {}
class RecoverableErrorException     extends ErrorException {}
class DeprecatedException           extends ErrorException {}
class UserDeprecatedException       extends ErrorException {}
```

### PHP7 的错误处理

PHP 7 改变了大多数错误的报告方式。error 可以通过 exception 异常进行捕获到，不能通过 try catch 捕获，但是可以通过注册到 set_exception_handle 捕获。

- Throwable
  - Error
  - Exception

```php
try
{
   // Code that may throw an Exception or Error.
}
catch (Throwable $t)
{
   // Executed only in PHP 7, will not match in PHP 5
}
catch (Exception $e)
{
   // Executed only in PHP 5, will not be reached in PHP 7
}
```

## 异常

捕获异常可以通过 try catch 语句

```php
try{
  //异常的代码
}catch (Exception $e){
  //处理异常
}finally{
  //最后执行的
}
```
