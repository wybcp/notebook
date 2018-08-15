# client 和 nginx 简易交互过程

- step1:client 发起 http 请求
- step2:dns 服务器解析域名得到主机 ip
- step3:默认端口为 80，通过 ip+port 建立 tcp/ip 链接
- step4:建立连接的 tcp/ip 三次握手，建立成功发送数据包
- step5:nginx 匹配请求
  - case .html: 静态内容，分发静态内容响应
  - case .php: php 脚本，转发请求内容到 php-fpm 进程，分发 php-fpm 返回的内容响应
- step6:断开连接的 tcp/ip 四次握手，断开连接

## nginx 和 php 简易交互过程

- 背景：web server 和服务端语言交互依赖的是 cgi(Common Gateway Interface)协议，由于 cgi 效率不高，
  后期产生了 fastcgi 协议(一种常驻型的 cgi 协议),php-cgi 实现了 fastcgi，但是相比 php-cgi,php-fpm 提供了
  更好的 PHP 进程管理方式，可以有效控制内存和进程、可以平滑重载 PHP 配置
- 流程：
  - step1:nginx 接收到一条 http 请求，会把环境变量，请求参数转变成 php 能懂的 php 变量
  ```
  // nginx 配置资料
  location ~ \.php$ {
        include snippets/fastcgi-php.conf; //step1
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;
  }
  ```
  - step2:nginx 匹配到.php 结尾的访问通过 fastcgi_pass 命令传递给 php-fpm.sock 文件，其实这里
    的 ngnix 发挥的是反向代理的角色，把 http 协议请求转到 fastcgi 协议请求
  ```
  // nginx 配置资料
  location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;// step2
  }
  ```
  - step3:php-fpm.sock 文件会被 php-fpm 的 master 进程所引用，这里 nginx 和 php-fpm 使用的是
    linux 的进程间通信方式 unix domain socks，是一种基于文件而不是网络底册协议的通信方式
  - step4:php-fpm 的 master 进程接收到请求后，会把请求分发到 php-fpm 的子进程，每个 php-fpm
    子进程都包含一个 php 解析器
  - step5:php-fpm 进程处理完请求后返回给 nginx
