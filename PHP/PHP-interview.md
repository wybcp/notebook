# PHP 面试题

## 问题：请用最简单的语言告诉我 PHP 是什么？

回答：PHP 全称：Hypertext Preprocessor，是一种用来开发动态网站的服务器脚本语言。

## 问题：什么是 MVC？

回答：MVC 由 Model（模型）, View（视图）和 Controller（控制器）组成，PHP MVC 可以更高效地管理好 3 个不同层的 PHP 代码。
Model：数据信息存取层。
View：view 层负责将应用的数据以特定的方式展现在界面上。
Controller：通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

## 问题：在页面中引用 CSS 有几种方式？

回答：在页面中使用 CSS 有 3 中方式：
引用外部 CSS 文件
内部定义 Style 样式
内联样式

## 问题：PHP 支持多继承吗？

回答：不可以。PHP 类只能继承一个父类，并用关键字“extended”标识。

## 问题：请问 PHP 中 echo 和 print 有什么区别？

这两个看起来很相似，因为它们都是将一些值打印在屏幕上。但是 echo 和 print 的本质区别在于：echo 用来输出字符串，显示多个值的时候可以用逗号隔开。只支持基本类型，print 不仅可以打印字符串值，而且可以打印函数的返回值。

## 问题：请问 GET 和 POST 方法有什么区别？

回答：我们再网页上填写的表单信息都可以通过这两个方法将数据传递到服务器上，当我们使用 GET 方法是，所有的信息都会出现在 URL 地址中，并且使用 GET 方法最多只能传递 1024 个字符，所以如果在传输量小或者安全性不那么重要的情况下可以使用 GET 方法。说到 POST 方法，最多可以传输 2MB 字节的数据，而且可以根据需要调节。

## 问题：PHP 中获取图像尺寸大小的方法是什么？

回答：getimagesize () 获取图片的尺寸
Imagesx () 获取图片的宽度
Imagesy () 获取图片的高度

## 问题：PHP 中的 PEAR 是什么？

回答：PEAR 也就是为 PHP 扩展与应用库（PHP Extension and Application Repository），它是一个 PHP 扩展及应用的一个代码仓库。

## 问题：如何用 PHP 和 MySQL 上传视频？

回答：我们可以在数据库中存放视频的地址，而不需要将真正的视频数据存在数据库中。可以将视频数据存放在服务器的指定文件夹下，上传的默认大小是 2MB，但是我们也可以在 php.ini 文件中修改 max_file size 选项来改变。

## 问题：PHP 中的错误类型有哪些？

回答：PHP 中遇到的错误类型大致有 3 类。
提示：这都是一些非常正常的信息，而非重大的错误，有些甚至不会展示给用户。比如访问不存在的变量。
警告：这是有点严重的错误，将会把警告信息展示给用户，但不会影响代码的输出，比如包含一些不存在的文件。
错误：这是真正的严重错误，比如访问不存在的 PHP 类。

## 问题：如何在 PHP 中定义常量？

回答：PHP 中使用 Define () 来定义常量。
define (“Newconstant”, 30);

## 问题：如何不使用 submit 按钮来提交表单？

如果我们不想用 submit 按钮来提交表单，我们也可以用超链接来提交，我们可以这样写代码：
<a href=”javascript: document.myform.submit();”>Submit Me</a>

## 什么是 CGI？

CGI 是一种通用网关协议。为了解决不同的语言解释器(如 php、python 解释器)与 WebServer 的通信而产生的一种协议。只要遵守这种协议就能实现语言与 WebServer 通讯。CGI 是规定了要传什么数据／以什么格式传输给 php 解析器的协议。

## 什么是 FastCGI?

是一种对 CGI 协议升华的一种协议。FastCGI 像是一个常驻(long-live)型的 CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去 fork 一次(这是 CGI 最为人诟病的 fork-and-execute 模式)。它还支持分布式的运算, 即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。。

## 什么是 PHP-FPM?

(PHP FastCGI Process Manager)，PHP-FPM 是一个实现了 Fastcgi 协议的程序,用来管理 Fastcgi 起的进程的,即能够调度 php-cgi 进程的程序。并提供了进程管理的功能。进程包含 master 进程和 worker 进程两种进程。master 进程只有一个，负责监听端口(默认 9000)，接收来自 WebServer 的请求，而 worker 进程则一般有多个(具体数量根据实际需要配置)，每个进程内部都嵌入了一个 PHP 解释器，是 PHP 代码真正执行的地方。

## FastCGI 好在哪里？

Fastcgi 则会先 fork 一个 master，解析配置文件，初始化执行环境，然后再 fork 多个 worker。当请求过来时，master 会传递给一个 worker，然后立即可以接受下一个请求。这样就避免了重复的劳动，效率自然是高。而且当 worker 不够用时，master 可以根据配置预先启动几个 worker 等着；当然空闲 worker 太多时，也会停掉一些，这样就提高了性能，也节约了资源。这就是 Fastcgi 的对进程的管理。大多数 Fastcgi 实现都会维护一个进程池。注：swoole 作为 httpserver，实际上也是类似这样的工作方式。

## Nginx 与 PHP 交互过程

我们以用户访问 index.php 为，服务器环境为 LNMP:

1. 用户请求 index.php 时，首先到 Nginx
1. Nginx 流程步骤：
   - 根据配置查找路由
   - 加载 nginx 的 fast-cgi 模块(FastCGI 的 Client),将根据 fastcgi.conf 文件中 fastcgi\_\*配置参数值也一并加入转发任务中
   - 根据 nginx.conf 文件 fastcgi_pass 配置将请求转发到 127.0.0.1:9000。
1. PHP-FPM 操作：
   - PHP-FPM 的 master 进程监听 9000 端口。
   - 收到请求后调用子进程来处理逻辑，PHP 解释器解释 PHP 语法并返回给 Nginx。
1. Nginx 操作：
   将响应返回给用户

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
