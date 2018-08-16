# PHP

PHP 缩写最初的来源“Personal Home Page”（个人主页），逐渐成为了现在的“PHP：超文本预处理器”。

2015 年 PHP 发布了里程碑式的版本 PHP 7.0，极大的提升了 Zend 引擎的性能，并降低了 PHP 的整体内存使用率。

## 目录

- [2018 PHP](PHP-2018.md)
- [composer 包管理及常见扩展包](composer/README.md)
- [官方文档](http://php.net/manual/zh/langref.php)
- [函数](./function/README.md)
- [优化](./optimization/README.md)
- [PSR 规范](https://github.com/PizzaLiu/PHP-FIG)

### 面向对象

1. 封装性：

   也称为信息隐藏，就是将一个类的使用和实现分开，只保留部分接口和方法与外部联系，或者说只公开了一些供开发人员使用的方法。于是开发人员只需要关注这个类如何使用，而不用去关心其具体的实现过程，这样就能实现 MVC 分工合作，也能有效避免程序间相互依赖，
   实现代码模块间松藕合。

2. 继承性：

   就是子类自动继承其父级类中的属性和方法，并可以添加新的属性和方法或者对部分属性和方法进行重写。继承增加了代码的可重用性。

   php 只支持单继承，也就是说一个子类只能有一个父类。

3. 多态性：

   子类继承了来自父级类中的属性和方法，并对其中部分方法进行重写。

   于是多个子类中虽然都具有同一个方法，但是这些子类实例化的对象调用这些相同的方法后却可以获得完全不同的结果，这种技术就是多态性。

   多态性增强了软件的灵活性。

### 访问权限修饰符

- public 公开的。任何地方都能访问
- protected 保护的、只能在本类和子类中访问
- private 私有的。只能在本类调用
- final 最终的。被修饰的方法或者类，不能被继承或者重写
- static 静态

### 接口和抽象类区别

- 接口使用 interface 声明，抽象类使用 abstract
- 抽象类可以包含属性方法。接口不能包含成员属性、
- 接口不能包含非抽象方法

### CGI、FastCGI、FPM

CGI 全称是“公共网关接口”(Common Gateway Interface)，HTTP 服务器与你的或其它机器上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。

CGI 是 HTTP Server 和一个独立的进程之间的协议，把**HTTP Request 的 Header 设置成进程的环境变量**，HTTP Request 的正文设置成进程的标准输入，而进程的标准输出就是 HTTP Response 包括 Header 和正文。

FastCGI 像是一个常驻(long-live)型的 CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去 fork 一次（这是 CGI 最为人诟病的 fork-and-execute 模式）。它还支持分布式的运算，即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。

Fpm 是一个实现了 Fastcgi 协议的程序,用来管理 Fastcgi 起的进程的,即能够调度 php-cgi 进程的程序。

#### FastCGI 特点

1. FastCGI 具有语言无关性。
2. FastCGI 在进程中的应用程序，独立于核心 web 服务器运行，提供了一个比 API 更安全的环境。APIs 把应用程序的代码与核心的 web 服务器链接在一起，这意味着在一个错误的 API 的应用程序可能会损坏其他应用程序或核心服务器。 恶意的 API 的应用程序代码甚至可以窃取另一个应用程序或核心服务器的密钥。
3. FastCGI 技术目前支持语言有：C/C++、Java、Perl、Tcl、Python、SmallTalk、Ruby 等。相关模块在 Apache, ISS, Lighttpd 等流行的服务器上也是可用的。
4. FastCGI 的不依赖于任何 Web 服务器的内部架构，因此即使服务器技术的变化, FastCGI 依然稳定不变。

#### FastCGI 的工作原理

1. Web Server 启动时载入 FastCGI 进程管理器（IIS ISAPI 或 Apache Module)
2. FastCGI 进程管理器自身初始化，启动多个 CGI 解释器进程(可见多个 php-cgi)并等待来自 Web Server 的连接。
3. 当客户端请求到达 Web Server 时，FastCGI 进程管理器选择并连接到一个 CGI 解释器。Web server 将 CGI 环境变量和标准输入发送到 FastCGI 子进程 php-cgi。
4. FastCGI 子进程完成处理后将标准输出和错误信息从同一连接返回 Web Server。当 FastCGI 子进程关闭连接时，请求便告处理完成。FastCGI 子进程接着等待并处理来自 FastCGI 进程管理器(运行在 Web Server 中)的下一个连接。 在 CGI 模式中，php-cgi 在此便退出了。
