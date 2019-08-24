# PHP 面试题

## 问题：请用最简单的语言告诉我 PHP 是什么？

回答：PHP 全称：Hypertext Preprocessor，是一种用来开发动态网站的服务器脚本语言。

## 问题：什么是 MVC？

MVC 是一种设计模式，由 Model（模型）， View（视图）和 Controller（控制器）组成，PHP MVC 可以更高效地管理好 3 个不同层的 PHP 代码。

- Model：数据信息存取层。
- View：负责将应用的数据以特定的方式展现在界面上。
- Controller：通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

使用 MVC 的优点：低耦合、高重用性、较低的生命周期成本、快速开发部署、可维护性、可扩展性，有利于软件工程化管理。

MVC 的缺点：没有明确的定义，完全理解并不容易。小型项目不适合用 MVC。

## 问题：在页面中引用 CSS 有几种方式？

回答：在页面中使用 CSS 有 3 中方式：

- 引用外部 CSS 文件
- 内部定义 Style 样式
- 内联样式

## 问题：PHP 支持多继承吗？

回答：不可以。PHP 类只能继承一个父类，并用关键字`extended`标识。

## echo()、print()、print_r()的区别？

- `echo()` 是 PHP 语法，可以输出多个值，多个值之间用逗号分隔，不能输出数组。
- `print()` 是 php 的语言结构，可以输出单个简单类型的变量值。如果字符串成功显示则返回 true，否则返回 false
- `print_r()` 是 php 函数，可以打印出复杂类型变量的值，如数组，对象。

拓展：var_dump()是一个函数，用来显示关于一个或多个表达式的结果信息，包括表达式的类型与值。数组将递归展开值，通过缩进显示其结构。

## 问题：PHP 中获取图像尺寸大小的方法是什么？

- getimagesize () 获取图片的尺寸
- Imagesx () 获取图片的宽度
- Imagesy () 获取图片的高度

## 问题：PHP 中的 PEAR 是什么？

PEAR 也就是为 PHP 扩展与应用库（PHP Extension and Application Repository），它是一个 PHP 扩展及应用的一个代码仓库。

## 问题：如何用 PHP 和 MySQL 上传视频？

我们可以在数据库中存放视频的地址，而不需要将真正的视频数据存在数据库中。可以将视频数据存放在服务器的指定文件夹下，上传的默认大小是 2MB，但是我们也可以在 php.ini 文件中修改 max_file size 选项来改变。

## 问题：PHP 中的错误类型有哪些？

PHP 中遇到的错误类型大致有 3 类。

- 提示：这都是一些非常正常的信息，而非重大的错误，有些甚至不会展示给用户。比如访问不存在的变量。
- 警告：这是有点严重的错误，将会把警告信息展示给用户，但不会影响代码的输出，比如包含一些不存在的文件。
- 错误：这是真正的严重错误，比如访问不存在的 PHP 类。

## 问题：如何在 PHP 中定义常量？

PHP 中使用 Define () 来定义常量。 `define (“Newconstant”， 30);`

## 问题：如何不使用 submit 按钮来提交表单？

用超链接来提交 `<a href=”javascript: document.myform.submit();”>Submit Me</a>`

## 什么是 CGI？

CGI 是一种通用网关协议。为了解决不同的语言解释器(如 php、python 解释器)与 WebServer 的通信而产生的一种协议。只要遵守这种协议就能实现语言与 WebServer 通讯。CGI 是规定了要传什么数据／以什么格式传输给 php 解析器的协议。

## 什么是 FastCGI

是一种对 CGI 协议升华的一种协议。FastCGI 像是一个常驻(long-live)型的 CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去 fork 一次(这是 CGI 最为人诟病的 fork-and-execute 模式)。它还支持分布式的运算，即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。

## 什么是 PHP-FPM

(PHP FastCGI Process Manager)，PHP-FPM 是一个实现了 Fastcgi 协议的程序，用来管理 Fastcgi 的进程的，即能够调度 php-cgi 进程的程序，并提供了进程管理的功能。进程包含 master 进程和 worker 进程两种进程。master 进程只有一个，负责监听端口(默认 9000)，接收来自 WebServer 的请求，而 worker 进程则一般有多个(具体数量根据实际需要配置)，每个进程内部都嵌入了一个 PHP 解释器，是 PHP 代码真正执行的地方。

## FastCGI 好在哪里？

Fastcgi 则会先 fork 一个 master，解析配置文件，初始化执行环境，然后再 fork 多个 worker。当请求过来时，master 会传递给一个 worker，然后立即可以接受下一个请求。这样就避免了重复的劳动，效率自然是高。而且当 worker 不够用时，master 可以根据配置预先启动几个 worker 等着；当然空闲 worker 太多时，也会停掉一些，这样就提高了性能，也节约了资源。这就是 Fastcgi 的对进程的管理。大多数 Fastcgi 实现都会维护一个进程池。注：swoole 作为 httpserver，实际上也是类似这样的工作方式。

## Nginx 与 PHP 交互过程

1. 用户请求 index.php 时，首先到 Nginx
2. Nginx 流程步骤：
   - 根据配置查找路由
   - 加载 nginx 的 fast-cgi 模块(FastCGI 的 Client)，将根据 fastcgi.conf 文件中 `fastcgi_*`配置参数值也一并加入转发任务中
   - 根据 nginx.conf 文件 fastcgi_pass 配置将请求转发到 `127.0.0.1:9000`。
3. PHP-FPM 操作：
   - PHP-FPM 的 master 进程监听 9000 端口。
   - 收到请求后调用子进程来处理逻辑，PHP 解释器解释 PHP 语法并返回给 Nginx。
4. Nginx 操作：将响应返回给用户

## 访问权限修饰符

- public 公开的。任何地方都能访问
- protected 保护的、只能在本类和子类中访问
- private 私有的。只能在本类调用
- final 最终的。被修饰的方法或者类，不能被继承或者重写
- static 静态

## 接口和抽象类区别

- 接口使用 interface 声明，抽象类使用 abstract
- 抽象类可以包含属性方法。接口不能包含成员属性
- 接口不能包含非抽象方法

## CGI、FastCGI、FPM

CGI 全称是“公共网关接口”(Common Gateway Interface)，HTTP 服务器与你的或其它机器上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。

CGI 是 HTTP Server 和一个独立的进程之间的协议，把**HTTP Request 的 Header 设置成进程的环境变量**，HTTP Request 的正文设置成进程的标准输入，而进程的标准输出就是 HTTP Response 包括 Header 和正文。

FastCGI 像是一个常驻(long-live)型的 CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去 fork 一次（这是 CGI 最为人诟病的 fork-and-execute 模式）。它还支持分布式的运算，即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。

Fpm 是一个实现了 Fastcgi 协议的程序，用来管理 Fastcgi 起的进程的，即能够调度 php-cgi 进程的程序。

当 Web Server 收到 index.php 这个请求后，会启动对应的 CGI 程序，这里就是 PHP 的解析器。接下来 PHP 解析器会解析 php.ini 文件，初始化执行环境，然后处理请求，再以规定 CGI 规定的格式返回处理后的结果，退出进程，Web server 再把结果返回给浏览器。这就是一个完整的动态 PHP Web 访问流程.

Web Server 启动时载入 FastCGI 进程管理器（Apache Module 或 IIS ISAPI 等)

FastCGI 进程管理器自身初始化，启动多个 CGI 解释器进程(可建多个 php-cgi)，并等待来自 Web Server 的连接。

当客户端请求到达 Web Server 时，FastCGI 进程管理器选择并连接到一个 CGI 解释器。Web server 将 CGI 环境变量和标准输入发送到 FastCGI 子进程 php-cgi。

FastCGI 子进程完成处理后，将标准输出和错误信息从同一连接返回 Web Server。当 FastCGI 子进程关闭连接时，请求便告处理完成。FastCGI 子进程接着等待，并处理来自 FastCGI 进程管理器(运行在 Web Server 中)的下一个连接。 在 CGI 模式中，php-cgi 在此便退出了。

FastCGI 与 CGI 特点：

对于 CGI 来说，每一个 Web 请求 PHP 都必须重新解析 php.ini、重新载入全部扩展，并重初始化全部数据结构。而使用 FastCGI，所有这些都只在进程启动时发生一次。一个额外的好处是，持续数据库连接(Persistent database connection)可以工作。

由于 FastCGI 是多进程，所以比 CGI 多线程消耗更多的服务器内存，php-cgi 解释器每进程消耗 7 至 25 兆内存，将这个数字乘以 50 或 100 就是很大的内存数。

### FastCGI 特点

1. FastCGI 具有语言无关性。
2. FastCGI 在进程中的应用程序，独立于核心 web 服务器运行，提供了一个比 API 更安全的环境。APIs 把应用程序的代码与核心的 web 服务器链接在一起，这意味着在一个错误的 API 的应用程序可能会损坏其他应用程序或核心服务器。 恶意的 API 的应用程序代码甚至可以窃取另一个应用程序或核心服务器的密钥。
3. FastCGI 技术目前支持语言有：C/C++、Java、Perl、Tcl、Python、SmallTalk、Ruby 等。相关模块在 Apache， ISS， Lighttpd 等流行的服务器上也是可用的。
4. FastCGI 的不依赖于任何 Web 服务器的内部架构，因此即使服务器技术的变化， FastCGI 依然稳定不变。

### FastCGI 的工作原理

1. Web Server 启动时载入 FastCGI 进程管理器（IIS ISAPI 或 Apache Module)
2. FastCGI 进程管理器自身初始化，启动多个 CGI 解释器进程(可见多个 php-cgi)并等待来自 Web Server 的连接。
3. 当客户端请求到达 Web Server 时，FastCGI 进程管理器选择并连接到一个 CGI 解释器。Web server 将 CGI 环境变量和标准输入发送到 FastCGI 子进程 php-cgi。
4. FastCGI 子进程完成处理后将标准输出和错误信息从同一连接返回 Web Server。当 FastCGI 子进程关闭连接时，请求便告处理完成。FastCGI 子进程接着等待并处理来自 FastCGI 进程管理器(运行在 Web Server 中)的下一个连接。 在 CGI 模式中，php-cgi 在此便退出了。

## include 与 require 的区别，require 和 require_once 的效率哪个高？

PHP 在遇到 include 时就解释一次，如果页面中出现 10 次 include，php 就解释 10 次，而 php 遇到 require 时只解释一次，即使页面出现多次 require 也只解释一次，因此 require 的执行效率比 include 高。

PHP 使用 require 包含文件时将被包含的文件当成当前文件的一个组成部分，如果被包含的文件中有语法错误或者被包含的文件不存在，则 php 脚本将不再执行，并提示错误。

PHP 使用 include 包含文件时相当于指定了这个文件的路径，当被包含的文件有语法错误或者被包含的文件不存在时给出警告，不影响本身脚本的运行。

Include 在包含文件时可以判断文件是否包含，而 require 则不管任何情况都包含进来。

Require 的效率比 require_once 的效率更高，因为 require_once 在包含文件时要进行判断文件是否已经被包含。

## Cookie 和 session 的区别，禁止了 cookie 后 session 能正常使用吗？session 的缺点是什么？session 在服务器端是存在哪里的？是共有的还是私有的？

COOKIE 保存在客户端，用户通过手段可以进行修改，不安全，单个 cookie 允许的最大值是 3k。而 SESSION 保存在服务器端，相对比较安全，大小没有限制。禁用了 cookie 之 session 不能正常使用。

Session 的缺点：保存在服务器端，每次读取都从服务器进行读取，对服务器有资源消耗。

Session 保存在服务器端的文件或数据库中，默认保存在文件中，文件路径由 php 配置文件的 session.save_path 指定。

Session 文件是公有的。

[都 9102 年了，还问 Session 和 Cookie 的区别](https://segmentfault.com/a/1190000018058541)

## cookie、session 的联系和区别，多台 web 服务器如何共享 session？

cookie 在客户端保存状态，session 在服务器端保存状态。但是由于在服务器端保存状态的时候，在客户端也需要一个标识，所以 session 也可能要借助 cookie 来实现保存标识位的作用。

cookie 包括名字，值，域，路径，过期时间。路径和域构成 cookie 的作用范围。cookie 如果不设置过期时间，则这个 cookie 在浏览器进程存在时有效，关闭时销毁。如果设置了过期时间，则 cookie 存储在本地硬盘上，在各浏览器进程间可以共享。

session 存储在服务器端，服务器用一种散列表类型的结构存储信息。当一个连接建立的时候，服务器首先搜索有没有存储的 session id，如果没有，则建立一个新的 session，将 session id 返回给客户端，客户端可以选择使用 cookie 来存储 session id。也可以用其他的方法，比如服务器端将 session id 附在 URL 上。

两者区别：

1. cookie 在本地，session 在服务器端
2. cookie 不安全，容易被欺骗，session 相对安全
3. session 在服务器端，访问多了会影响服务器性能
4. cookie 有大小限制，为 3K

多服务器共享 session 可以尝试将 session 存储在 redis 中

## php 中 web 上传文件的原理是什么，如何限制上传文件的大小？

PHP 上传文件默认大小为 2M，设置上传大小的配置项是 `upload_max_filesize`，`post_max_size` 设置一次，POST 中 PHP 能接收的最大数据量，应该比 upload_max_filesize 大。

## http 协议中的 post 和 get 有何区别？

1. GET 用于获取信息，不应该用于修改信息，POST 可用于更新修改信息。
2. GET 可传输数据大小和 URL 有关，而 POST 没有限定大小，大小和服务器配置有关。
3. GET 放在 URL 中，因此不安全，而 POST 传输数据对于用户来说是不可见的，所以相对安全。
4. 在 ajax 中：post 不被缓存，get 被缓存所以一般在请求结尾加 Math.random();
5. SERVER 端接收：因为在 submit 提交的时候是按不同方式进行编码的，所以服务端在接受的时候会按照不同的方式进行接收。
6. 编码方式：如果传递数据是非-ASCII，那么 GET 一般是不适应的，所以在传递的时候会做编码处理！

表单信息都可以通过这两个方法将数据传递到服务器上，GET 方法，所有的信息都会出现在 URL 地址中，并且使用 GET 方法最多只能传递 1024 个字符，所以如果在传输量小或者安全性不那么重要的情况下可以使用 GET 方法。POST 方法，最多可以传输 2MB 字节的数据，而且可以根据需要调节。

## 怎么防止 sql 注入

1. 过滤掉一些常见的数据库操作关键字：select，insert，update，delete，and 等或者通过系统函数：addslashes(需要被过滤的内容)来进行过滤。
1. 在 PHP 配置文件中 Register_globals=off;设置为关闭状态 //作用将注册全局变量关闭。比如：接收 POST 表单的值使用`$_POST['user']`，如果将 register_globals=on;直接使用\$user 可以接收表单的值。
1. SQL 语句书写的时候尽量不要省略小引号(tab 键上面那个)和单引号
1. 提高数据库命名技巧，对于一些重要的字段根据程序的特点命名，取不易被猜到的
1. 对于常用的方法加以封装，避免直接暴漏 SQL 语句
1. 开启 PHP 安全模式 Safe_mode=on;
1. 打开 magic_quotes_gpc 来防止 SQL 注入 Magic_quotes_gpc=off;默认是关闭的，它打开后将自动把用户提交的 sql 语句的查询进行转换，把'转为\'，这对防止 sql 注入有重大作用。因此开启：magic_quotes_gpc=on;
1. 控制错误信息关闭错误提示信息，将错误信息写到系统日志。
1. 使用 mysqli 或 pdo 预处理。

## 数据库索引有几类

普通索引、主键索引、唯一索引

并非所有的数据库都以相同的方式使用索引，作为通用规则，只有当经常查询列中的数据时才需要在表上创建索引。

## 引用传值和非引用传值的区别，什么时候该用引用传值?什么时候该用非引用传值

按值传递：函数范围内对值的改变在函数外都会被忽略。

按引用传递：函数范围内对值的任何改变在函数外也将反应出这些修改。

按值传递时，php 必须复制值，如果操作的是大型的对象和字符串，这将是一个代价很大的操作。按引用传递不需要复制值，因此对性能的提高有好处。

当需要在函数内改变源变量的值时用引用传递，如果不想改变原变量的值用传值。

## 魔术方法并说明作用

- `__call()`当调用不存在的方法时会自动调用的方法
- `__autoload()`在实例化一个尚未被定义的类是会自动调用次方法来加载类文件
- `__set()`当给未定义的变量赋值时会自动调用的方法
- `__get()`当获取未定义变量的值时会自动调用的方法
- `__construct()`构造方法，实例化类时自动调用的方法
- `__destroy()`销毁对象时自动调用的方法
- `__unset()`当对一个未定义变量调用 unset()时自动调用的方法
- `__isset()`当对一个未定义变量调用 isset()方法时自动调用的方法
- `__clone()`克隆一个对象
- `__tostring()`当输出一个对象时自动调用的方法

## `$_REQUEST`、`$_POST`、`$_GET`、`$_COOKIE`、`$_SESSION`、`$_FILE` 的意思是什么

它们都是 PHP 预定义变量。

- `$_REQUEST` 用来获取 post 或 get 方式提交的值
- `$_POST` 用来获取 post 方式提交的值
- `$_GET` 用来获取 get 方式提交的值
- `$_COOKIE` 用来获取 cookie 存储的值
- `$_SESSION`用来获取 session 存储的值
- `$_FILE` 用来获取上传文件表单的值

## 数组中下标最好是什么类型的

数组的下标最好是数字类型的，数字类型的处理速度快。

## `++i`和`i++`哪一个效率高

++i 效率比 i++的效率更高，因为++i 少了一个返回 i 的过程。

## magic_quotes_gpc()、magic_quotes_runtime()的意思是什么？

Magic_quotes_gpc()是 php 配置文件中的，如果设置为 on 则会自动 POST，GET，COOKIE 中的字符串进行转义，在'之前加\

Magic_quotes_runtime()是 php 中的函数，如果参数为 true 则会数据库中取出来的单引号、双引号、反斜线自动加上反斜杠进行转义。

## 框架中什么是单一入口和多入口，单一入口的优缺点

多入口就是通过访问不同的文件来完成用户请求。

单一入口只 web 程序所有的请求都指向一个脚本文件的。

单一入口更容易控制权限，方便对 http 请求可以进行安全性检查。

缺点：URL 看起来不那么美观，特别是对搜索引擎来说不友好。

## 打印一个用`.`链接的字符串时候，还可以用什么代替`.`链接效率更高些

可以用`,`代替`.`效率更高。

## 提示类型 200、404、502 是什么意思

200 是请求成功，404 是文件未找到，502 是服务器内部错误。

## 函数提取这段路径的的后缀名。

```php
function geturltype($url){
    $info=parse_url($url);
   // return end(explode('.'，$info['path']));
    //return explode('.'，$info['path']);
    return $info;
}
var_dump(geturltype("Www/hello/test.php.html?a=3&b=4"));
```

## Memcache 的理解

Memcache 是一种缓存技术，在一定的时间内将动态网页经过解析之后保存到文件，下次访问时动态网页就直接调用这个文件，而不必在重新访问数据库。使用 memcache 做缓存的好处是：提高网站的访问速度，减轻高并发时服务器的压力。

Memcache 的优点：稳定、配置简单、多机分布式存储、速度快

## 有 mail.log 的一个文档，内容为若干邮件地址，其中用’\n’将邮件地址分隔。要求从中挑选出 sina.com 的邮件地址（包括从文件读取、过滤到列印出来）。

```php
$mail = file_get_contents('mail.log');
$pattern = "/\S+sina\.com/";
$rpattern = "/\\n/";
preg_filter($rpattern，""，$mail);
if(preg_match_all($pattern，$mail，$matches))
{
    print_r($matches);
}
```

## const 的含义及实现机制，比如：const int i，是怎么做到 i 只可读的

含义：const 用来说明所定义的变量是只读的。

实现机制：这些在编译期间完成，编译器使用常数直接替换掉对此变量的引用。

## tcp 三次握手的过程，accept 发生在三次握手哪个阶段

accept 发生在三次握手之后。

- 第一次握手：客户端发送 syn 包(syn=j)到服务器。
- 第二次握手：服务器收到 syn 包，必须确认客户的 SYN(ack=j+1)，同时自己也发送一个 ASK 包(ask=k)。
- 第三次握手：客户端收到服务器的 SYN+ACK 包，向服务器发送确认包 ACK(ack=k+1)。

三次握手完成后，客户端和服务器就建立了 tcp 连接。这时可以调用 accept 函数获得此连接。

## 用 UDP 协议通讯时怎样得知目标机是否获得了数据包？

可以在每个数据包中插入一个唯一的 ID，比如 timestamp 或者递增的 int。发送方在发送数据时将此 ID 和发送时间记录在本地。接收方在收到数据后将 ID 再发给发送方作为回应。发送方如果收到回应，则知道接收方已经收到相应的数据包;如果在指定时间内没有收到回应，则数据包可能丢失，需要重复上面的过程重新发送一次，直到确定对方收到。

## 统计论坛在线人数分布：假设有一个论坛，其注册 ID 有两亿个，每个 ID 从登陆到退出会向一个日志文件中记下登陆时间和退出时间，要求写一个算法统计一天中论坛的用户在线分布，取样粒度为秒。

分析及答案：一天总共有 `3600*24 = 86400` 秒。定义一个长度为 86400 的整数数组 int delta[86400]，每个整数对应这一秒的人数变化值，可能为正也可能为负。开始时将数组元素都初始化为 0。然后依次读入每个用户的登录时间和退出时间，将与登录时间对应的整数值加 1，将与退出时间对应的整数值减 1。这样处理一遍后数组中存储了每秒中的人数变化情况。定义另外一个长度为 86400 的整数数组 int online_num[86400]，每个整数对应这一秒的论坛在线人数。假设一天开始时论坛在线人数为 0，则第 1 秒的人数 online_num[0] = delta[0]。第 n+1 秒的人数 online_num[n] = online_num[n-1] + delta[n]。这样我们就获得了一天中任意时间的在线人数。

## 状态码 200 301 304 403 404 500 的含义

- 200 - 服务器成功返回网页
- 301(永久移动)请求的网页已永久移动到新位置。
- 304(未修改)自从上次请求后，请求的网页未修改过
- 403(禁止)服务器拒绝请求
- 404 - 请求的网页不存在
- 503 - 服务器超时

## 请描述 PHP(或其他语言) Session 的运行机制，大型网站中 Session 方面应注意什么？

运行机制:客户端将 session id 传递到服务器，服务器根据 session id 找到对应的文件，读取的时候对文件内容进行反序列化就得到 session 的值，保存的时候先序列化再写入

注意:

1. session 在大访问量网站上确实影响系统性能，影响性能的原因之一由文件系统设计造成，在同一个目录下超过 10000 个文件时，文件的定位将非常耗时，可以通过修改 php.ini 中 session.save_path 设置两级子目录 ，session 将存储在两级子目录中，每个目录有 16 个子目录[0~f]，不过好像 PHP session 不支持创建目录，你需要事先把那么些目录创建好 。
2. 还有一个问题就是小文件的效率问题，可以通过存储方式中的 redis 来解决 I/O 效率低下的问题
3. session 同步问题，session 同步有很多种，如果你是存储在 memcached 或者 MySQL 中，那就很容易了，指定到同样的位置即可，还有一种方法就是在负载均衡那一层保持会话，把访问者绑定在某个服务器上，他的所有访问都在那个服务器上就不需要 session 同步了

## 简单描述 mysql 中，索引，主键，唯一索引，联合索引的区别，对数据库的性能有什么影响(从读写两方面)

- 索引就相当于对指定的列进行排序，排序有利于对该列的查询，可以大大增加查询效率
- 建立索引也是要消耗系统资源，所以索引会降低写操作的效率
- 主键，唯一，联合都属于索引
- 主键属于唯一索引，且一个表只能有一个主键，主键列不允许空值
- 唯一索引可以一个表中可以有多个，而且允许为空，列中的值唯一
- 多个字段的多条件查询多使用联合索引

## 解释 MySQL 外连接、内连接与自连接的区别

- Mysql 外连接分为左连接(left join....on)和右连接(right join.... on)，左连接是以左表作为条件查询关联右表数据，无对应数据则补空，右连接则相反
- Mysql 内连接(inner join.....on)是做关联查询时，内连接的特性是只显示符合连接条件的记录
- Mysql 自连接:在 FROM clause（子句）中我们可以给这个表取不同的别名， 然后在语句的其它需要使用到该别名的地方用 dot（点）来连接该别名和字段名

## count()

count — 计算数组中的单元数目或对象中的属性个数

`int count ( mixed $var [， int $mode ] )`， 如果 var 不是数组类型或者实现了 Countable 接口的对象，将返回 1，有一个例外，如果 var 是 NULL 则结果是 0。

## error_reporting(2047)什么作用？

答：PHP 显示所有错误 E_ALL

## 打开 php.ini 中的 Safe_mode，会影响哪些函数？至少说出 6 个。

1. 用户输入输出函数(fopen() file() require()，只能用于调用这些函数有相同脚本的拥有者)
2. 创建新文件(限制用户只在该用户拥有目录下创建文件)
3. 用户调用 popen() systen() exec()等脚本，只有脚本处在 safe_mode_exec_dir 配置指令指定的目 录中才可能
4. 加强 HTTP 认证，认证脚本拥有者的 UID 的划入认证领域范围内，此外启用安全模式下，不会设置 PHP_AUTH
5. mysql 服务器所用的用户名必须与调用 mysql_connect()的文件的拥有者用户名相同
6. 受影响的函数变量以及配置命令达到 40 个

   chmod() 检查被操作的文件或目录是否与正在执行的脚本有相同的 UID（所有者）。另外，不能设置 SUID、SGID 和 sticky bits mkdir() 检查被操作的目录是否与正在执行的脚本有相同的 UID（所有者）。 touch() 检查被操作的文件是否与正在执行的脚本有相同的 UID（所有者）。检查被操作的目录是否与正在执行的脚本有相同的 UID（所有者）。 chown()、chgrp()、chdir()、fopen()、rmdir()、copy()、link()、exec()等 检查被操作的文件或目录是否与正在执行的脚本有相同的 UID（所有者）。检查被操作的目录是否与正在执行的脚本有相同的 UID（所有者）。

## 写个函数来解决多线程同时读写一个文件的问题。

答：flock(\$hander，LOCK_EX);

## 设置当前内容的 Content-Type

```php
//定义编码
header(“Content-type:text/html;charset=utf-8”);
//CSS
header(“Content-type:text/css”);
//JavaScript
header(“Content-type:text/javascript”);
//JPEG Image
header(“Content-type:image/jpeg”);
//GIF Image
header(“Content-type:image/gif”);
//PNG Image
header(“Content-type:image/png”);
//JSON
header(“Content-type:application/json”);
//PDF
header(“Content-type:application/pdf”);
//XML
header(“Content-type:text/xml”);
//ok
header(“HTTP/1.1 200 OK”);
//404头
header(‘HTTP/1.1 404 Not Found’);
//设置地址被永久的重定向
header(‘HTTP/1.1 301 Moved Permanently’);
//转到一个新地址
header(‘Location:http://www.example.org/’);
//文件延迟转向
header(‘Refresh:10;url=http://www.example.org/’);
print ‘You will be redirected in 10 seconds’;
//纯文本格式
header(‘Content-type:text/plain’);
```

## mysql 中 varchar 的最大长度是多少？用什么类型的字段存储大文本？date 和 datetime 和 timestamp 什么区别？怎么看数据库中有哪些 sql 正在执行？

- 65535
- text
- date 只保留日期，不保留时分秒。
- datetime 保留日期和时分秒，MySQL 检索且以‘YYYY-MM-DD HH:MM:SS’格式显示 datetime 值，支持的范围是‘1000-01-01 00:00:00’到‘9999-12-31 23:59:59’。
- timestamp 的格式与 datetime 相同，但其取值范围小于 datetime，使用 timestamp 可以自动地用当前的日期和时间标记 INSERT 或 UPDATE 的操作，如果有多个 timestamp 列，只有第一个自动更新。
- show processlist;

## 写一段代码保证多个进程同时写入成功

```php
#加锁
function write($filepath，$data) {
     $fp = fopen( $filepath， 'a' );   //以追加的方式打开文件，返回的是指针
 do{
 　　 usleep( 100 ); 　　　　　　//暂停执行程序，参数是以微秒为单位的
 }while( !flock( $fp， LOCK_EX ) );　　//以独享写入的方式锁定文件，成功则返回TRUE，否则FALSE
}
 $res = fwrite( $fp， $data."/n" );　　// 以追加的方式写入数据到打开的文件
 flock( $fp， LOCK_UN );　　　　　　//解锁，以让别的进程进行锁定
 fcloce( $fp );　　　　　　　　　　　//关闭打开的文件指针
 return $res;　　　　　　　　　　　　//返回写入结果
}
```

[https://www.cnblogs.com/gengyi/p/6399206.html](https://www.cnblogs.com/gengyi/p/6399206.html)

## 打出前一天的时间

```php
date('Y-m-d H:i:s'， strtotime('-1 day'))
```

## 翻转字符【包含中文】

```php
 function strRev($str，$encoding='utf-8'){
        $result = '';
        $len = mb_strlen($str);
        for($i=$len-1; $i>=0; $i--){
            $result .= mb_substr($str，$i，1，$encoding);
        }
        return $result;
    }
```

## 遍历一个文件夹下的所有文件和子文件

```php
function my_dir($dir) {
    $files = array();
    if(@$handle = opendir($dir)) { //注意这里要加一个@，不然会有warning错误提示：）
        while(($file = readdir($handle)) != = false) {
            if($file != ".." && $file != ".") { //排除根目录；
                if(is_dir($dir."/".$file)) { //如果是子文件夹，就进行递归
                    $files[$file] = my_dir($dir."/".$file);
                } else { //不然就将文件的名字存入数组；
                    $files[] = $file;
                }
            }
        }
        closedir($handle);
        return $files;
    }
}
```

## 不适用第三个变量交换两个变量的值

```php
function swap (int &$a， int &$b){
     // 20 10
    $a = $a+$b; // 30
    $b = $a-$b; //20 a
    $a = $a-$b;
}
```

<https://blog.tanteng.me/2018/04/php-interview-2/#more-12086>

## 用 PHP 获取当前时间并打印,打印格式:2006-5-10 22:21:21

```php
date_default_timezone_set('PRC');//设置中国区域
echo date('Y-n-d H:i:s'); // 2019-3-21 16:26:15
echo date('Y-m-d H:i:s'); // 2019-03-21 16:26:15
```

## 字符串转数组,数组转字符串,字符串截取,字符串替换,字符串查找的函数分别是什么

```php
// 字符串转数组
$str='www.baidu.com';
print_r(str_split($str));//第一种按照长度去切割字符串变成数组
var_dump(explode('.',$str));//第二种 用explode 按照某个字符串去切割这个字符串变为数组
// 数组转字符串
$arr=array("aaa","bbb","ccc");
print_r(implode('',$arr)); //join() 这个函数不知道小伙伴们用过没有 其实join() 函数是 implode() 函数的别名 没什么区别！
// 字符串截取

substr($str,1,10);
mb_substr($str,1,3);
// 字符串替换

$bodytag = str_replace("%body%", "black", "<body text='%body%'>");

//函数搜索字符串在另一字符串中的第一次出现。并返回字符串的剩余部分：
echo strstr("I love Shanghai!","Shanghai");
// strpos()
//函数查找字符串在另一字符串中第一次出现的位置 记住返回是int 就是索引的位置
// strrpos()
//函数查找字符串在另一字符串中最后一次出现的位置 记住返回是int 就是索引的位置
```

## 防止盗链

1. 服务器上防止

   Apache 和 nginx 做 rewrite 基于源来做判断阻止盗链

   ```conf
   # 设置防盗链文件类型
   location ~* \.(gif|jpg|png|jpeg)$ {
   expires     30d;
   #白名单，允许文件链出的域名白名单，域名与域名之间使用空格隔开！
   valid_referers *.hugao8.com www.hugao8.com m.hugao8.com *.baidu.com *.google.com;
   #这个图片是盗链返回的图片。这个图片要放在没有设置防盗链的网站上，因为防盗链的作用，这个图片如果也放在防盗链网站上就会被当作防盗链显示不出来了，盗链者的网站所盗链图片会显示X符号。
   if ($invalid_referer) {
   rewrite ^/ http://ww4.sinaimg.cn/bmiddle/051bbed1gw1egjc4xl7srj20cm08aaa6.jpg;
   #return 404;
       }
   }
   ```

2. 代码防止,设置 Referer

   Referer 是 HTTP Header 的一部分，当浏览器向网站 Web 服务器发送请求的时候，通常会带上 Referer，告诉服务器此次请求的链接来源。 `$_SERVER[HTTP_REFERER]`

## php 数组中 如果有一个人下标没标注 那么就是这个数组中最大的下标+1

```php
<?php
$a = array(1=>5,5=>8,22,2=>'8',81);
echo $a[7];
echo $a[6];
echo $a[3];
print_r($a);

// 8122<br />
// <b>Notice</b>:  Undefined offset: 3 in <b>[...][...]</b> on line <b>5</b><br />
// Array
// (
//     [1] => 5
//     [5] => 8
//     [6] => 22
//     [2] => 8
//     [7] => 81
// )
```
