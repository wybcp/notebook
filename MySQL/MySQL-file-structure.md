# [MySQL 安装文件结构](https://juejin.im/book/5bffcbc9f265da614b11b731/section/5bffcbc9f265da61553a8bc9)

## bin 目录下的可执行文件

- mysqld：
  MySQL 服务器程序，运行直接启动一个服务器进程。但这个命令不常用

- mysqld_safe：
  一个启动脚本，它间接的调用 mysqld，而且还顺便启动了另外一个监控进程，这个监控进程在服务器进程挂了的时候，可以帮助重启它。另外，使用 mysqld_safe 启动服务器程序时，它会将服务器程序的出错信息和其他诊断信息重定向到某个文件中，产生出错日志，这样可以方便我们找出发生错误的原因。

- mysql.server：
    一个启动脚本，间接的调用 mysqld_safe，在调用 mysql.server 时在后边指定 start 参数就可以启动服务器程序了，`mysql.server start`，关闭正在运行的服务器程序`mysql.server stop`
- mysqld_multi
  其实我们一台计算机上也可以运行多个服务器实例，也就是运行多个 MySQL 服务器进程。mysql_multi 可执行文件可以对每一个服务器进程的启动或停止进行监控。