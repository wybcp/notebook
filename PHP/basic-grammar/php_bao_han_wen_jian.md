# PHP 包含文件

## include 和 require 语句

include 和 require 语句用于在执行流中插入写在其他文件中的有用的代码。

include 和 require 除了处理错误的方式不同之外，在其他方面都是相同的：
+ require 生成一个致命错误（E_COMPILE_ERROR），在错误发生后脚本会停止执行。
+ include 生成一个警告（E_WARNING），在错误发生后脚本会继续执行。

因此，如果您希望继续执行，并向用户输出结果，即使包含文件已丢失，那么请使用 include。否则，在框架、CMS 或者复杂的 PHP 应用程序编程中，请始终使用 require 向执行流引用关键文件。这有助于提高应用程序的安全性和完整性，在某个关键文件意外丢失的情况下。

