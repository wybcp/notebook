# CGI、FastCGI 和 PHP-FPM 关系图解

![image](http://ou1viq65b.bkt.clouddn.com/17-8-3/4700904.jpg)

当 Web Server 收到 index.php 这个请求后，会启动对应的 CGI 程序，这里就是 PHP 的解析器。接下来 PHP 解析器会解析 php.ini 文件，初始化执行环境，然后处理请求，再以规定 CGI 规定的格式返回处理后的结果，退出进程，Web server 再把结果返回给浏览器。这就是一个完整的动态 PHP Web 访问流程，接下来再引出这些概念，就好理解多了，

CGI：是 Web Server 与 Web Application 之间数据交换的一种协议。

FastCGI：同 CGI，是一种通信协议，但比 CGI 在效率上做了一些优化。同样，SCGI 协议与 FastCGI 类似。

PHP-CGI：是 PHP （Web Application）对 Web Server 提供的 CGI 协议的接口程序。

PHP-FPM：是 PHP（Web Application）对 Web Server 提供的 FastCGI 协议的接口程序，额外还提供了相对智能一些任务管理。
WEB 中，

Web Server 一般指 Apache、Nginx、IIS、Lighttpd、Tomcat 等服务器，
Web Application 一般指 PHP、Java、Asp.net 等应用程序。
![image](http://ou1viq65b.bkt.clouddn.com/17-8-3/75019151.jpg)
Web Server 启动时载入 FastCGI 进程管理器（Apache Module 或 IIS ISAPI 等)

FastCGI 进程管理器自身初始化，启动多个 CGI 解释器进程(可建多个 php-cgi)，并等待来自 Web Server 的连接。

当客户端请求到达 Web Server 时，FastCGI 进程管理器选择并连接到一个 CGI 解释器。Web server 将 CGI 环境变量和标准输入发送到 FastCGI 子进程 php-cgi。

FastCGI 子进程完成处理后，将标准输出和错误信息从同一连接返回 Web Server。当 FastCGI 子进程关闭连接时，请求便告处理完成。FastCGI 子进程接着等待，并处理来自 FastCGI 进程管理器(运行在 Web Server 中)的下一个连接。 在 CGI 模式中，php-cgi 在此便退出了。

FastCGI 与 CGI 特点：

对于 CGI 来说，每一个 Web 请求 PHP 都必须重新解析 php.ini、重新载入全部扩展，并重初始化全部数据结构。而使用 FastCGI，所有这些都只在进程启动时发生一次。一个额外的好处是，持续数据库连接(Persistent database connection)可以工作。
由于 FastCGI 是多进程，所以比 CGI 多线程消耗更多的服务器内存，php-cgi 解释器每进程消耗 7 至 25 兆内存，将这个数字乘以 50 或 100 就是很大的内存数。
升级:
![image](http://ou1viq65b.bkt.clouddn.com/17-8-3/3145024.jpg)
