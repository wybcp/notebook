# 进程

## 用 PHP 玩转进程

- [用 PHP 玩转进程之一 — 基础](https://www.fanhaobai.com/2018/08/process-php-basic-knowledge.html)
- [用 PHP 玩转进程之二 — 多进程 PHPServer](https://www.fanhaobai.com/2018/09/process-php-multiprocess-server.html)

## 进程和线程的区别

进程是一次程序运行的活动。进程有自己的 pid，堆栈空间等资源。

线程是进程里面的一个实体。是 CPU 调度的基本单位。它比进程更小。线程本身不拥有系统资源。只拥有自己的程序计数器、堆栈、寄存器。和同一个进程中的其他线程共享进程中的内存。

线程开销小。进程切换开销比较大。进程切换，上下文。

进程是 cpu 资源分配的最小单位，线程是 cpu 调度的最小单位。
