# PHP

## 目录

- [2018 PHP](PHP-2018.md)
- [官方文档](http://php.net/manual/zh/langref.php)
- [数组函数]()
- [字符串函数]()
- [垃圾回收机制]()
- [面向对象]()
  - 封装
  - 继承
  - 多态
- [zval结构]()
- [魔术方法]()
- [抽象类和接口]()
- [MVC]()
- [访问修饰符]()
- [正则表达式]()
- [FPM、FastCGI]()
- [PSR规范](https://github.com/PizzaLiu/PHP-FIG)
  - **PSR 1 基本代码规范**
  - **PSR 2 代码风格指南**
  - **PSR 3 日志接口**
  - **PSR 4 改进的自动加载**

### 面向对象

1. 封装性：

    也称为信息隐藏，就是将一个类的使用和实现分开，只保留部分接口和方法与外部联系，或者说只公开了一些供开发人员使用的方法。于是开发人员只需要关注这个类如何使用，而不用去关心其具体的实现过程，这样就能实现MVC分工合作，也能有效避免程序间相互依赖，
    实现代码模块间松藕合。

2. 继承性：

    就是子类自动继承其父级类中的属性和方法，并可以添加新的属性和方法或者对部分属性和方法进行重写。继承增加了代码的可重用性。

    php只支持单继承，也就是说一个子类只能有一个父类。

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

- 接口使用interface声明，抽象类使用abstract
- 抽象类可以包含属性方法。接口不能包含成员属性、
- 接口不能包含非抽象方法

### CGI、FastCGI、FPM

CGI全称是“公共网关接口”(Common Gateway Interface)，HTTP服务器与你的或其它机器上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。

CGI是HTTP Server和一个独立的进程之间的协议，把**HTTP Request的Header设置成进程的环境变量**，HTTP Request的正文设置成进程的标准输入，而进程的标准输出就是HTTP Response包括Header和正文。  

FastCGI像是一个常驻(long-live)型的CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去fork一次（这是CGI最为人诟病的fork-and-execute 模式）。它还支持分布式的运算，即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。

Fpm是一个实现了Fastcgi协议的程序,用来管理Fastcgi起的进程的,即能够调度php-cgi进程的程序。

#### FastCGI特点

1. FastCGI具有语言无关性。
2. FastCGI在进程中的应用程序，独立于核心web服务器运行，提供了一个比API更安全的环境。APIs把应用程序的代码与核心的web服务器链接在一起，这意味着在一个错误的API的应用程序可能会损坏其他应用程序或核心服务器。 恶意的API的应用程序代码甚至可以窃取另一个应用程序或核心服务器的密钥。
3. FastCGI技术目前支持语言有：C/C++、Java、Perl、Tcl、Python、SmallTalk、Ruby等。相关模块在Apache, ISS, Lighttpd等流行的服务器上也是可用的。
4. FastCGI的不依赖于任何Web服务器的内部架构，因此即使服务器技术的变化, FastCGI依然稳定不变。

#### FastCGI的工作原理

1. Web Server启动时载入FastCGI进程管理器（IIS ISAPI或Apache Module)
2. FastCGI进程管理器自身初始化，启动多个CGI解释器进程(可见多个php-cgi)并等待来自Web Server的连接。
3. 当客户端请求到达Web Server时，FastCGI进程管理器选择并连接到一个CGI解释器。Web server将CGI环境变量和标准输入发送到FastCGI子进程php-cgi。
4. FastCGI子进程完成处理后将标准输出和错误信息从同一连接返回Web Server。当FastCGI子进程关闭连接时，请求便告处理完成。FastCGI子进程接着等待并处理来自FastCGI进程管理器(运行在Web Server中)的下一个连接。 在CGI模式中，php-cgi在此便退出了。