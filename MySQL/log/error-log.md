# 错误日志

MySQL 的 error log 用于记录错误信息的 log，但 error 记录的不仅仅是错误信息，有关服务进程的错误信息也会被记录（critical 级别）；如果 mysqld 进程发现某些表需要自动检查或者修复的话，也会抛出相关信息到该 log。
