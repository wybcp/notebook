# 负载均衡

nginx可以实现简单的负载均衡功能。

## 例子

假设这样一个应用场景：将应用部署在 192.168.1.11:80、192.168.1.12:80、192.168.1.13:80 三台linux环境的服务器上。网站域名叫 www.helloworld.com，公网IP为 192.168.1.11。在公网IP所在的服务器上部署 nginx，对所有请求做负载均衡处理。

nginx.conf 配置如下：

```nginx
http {
    #设定mime类型,类型由mime.type文件定义
   include       /etc/nginx/mime.types;
   default_type  application/octet-stream;
   #设定日志格式
   access_log    /var/log/nginx/access.log;

   #设定负载均衡的服务器列表
   upstream load_balance_server {
       #weigth参数表示权值，权值越高被分配到的几率越大
       server 192.168.1.11:80   weight=5;
       server 192.168.1.12:80   weight=1;
       server 192.168.1.13:80   weight=6;
   }

  #HTTP服务器
  server {
       #侦听80端口
       listen       80;
       
       #定义使用www.xx.com访问
       server_name  www.helloworld.com;

       #对所有请求进行负载均衡请求
       location / {
           root        /root;                 #定义服务器的默认网站根目录位置
           index       index.html index.htm;  #定义首页索引文件的名称
           proxy_pass  http://load_balance_server ;#请求转向load_balance_server 定义的服务器列表

           #以下是一些反向代理的配置(可选择性配置)
           #proxy_redirect off;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           #后端的Web服务器可以通过X-Forwarded-For获取用户真实IP
           proxy_set_header X-Forwarded-For $remote_addr;
           proxy_connect_timeout 90;          #nginx跟后端服务器连接超时时间(代理连接超时)
           proxy_send_timeout 90;             #后端服务器数据回传时间(代理发送超时)
           proxy_read_timeout 90;             #连接成功后，后端服务器响应时间(代理接收超时)
           proxy_buffer_size 4k;              #设置代理服务器（nginx）保存用户头信息的缓冲区大小
           proxy_buffers 4 32k;               #proxy_buffers缓冲区，网页平均在32k以下的话，这样设置
           proxy_busy_buffers_size 64k;       #高负荷下缓冲大小（proxy_buffers*2）
           proxy_temp_file_write_size 64k;    #设定缓存文件夹大小，大于这个值，将从upstream服务器传
           
           client_max_body_size 10m;          #允许客户端请求的最大单文件字节数
           client_body_buffer_size 128k;      #缓冲区代理缓冲用户端请求的最大字节数
       }
   }
}
```

## 有多个webapp的配置

当一个网站功能越来越丰富时，往往需要将一些功能相对独立的模块剥离出来，独立维护。这样的话，通常，会有多个 webapp。

举个例子：假如 www.helloworld.com 站点有好几个webapp，finance（金融）、product（产品）、admin（用户中心）。访问这些应用的方式通过上下文(context)来进行区分:

- www.helloworld.com/finance/
- www.helloworld.com/product/
- www.helloworld.com/admin/

我们知道，http的默认端口号是80，如果在一台服务器上同时启动这3个 webapp 应用，都用80端口，肯定是不成的。所以，这三个应用需要分别绑定不同的端口号。

那么，问题来了，用户在实际访问 www.helloworld.com 站点时，访问不同 webapp，总不会还带着对应的端口号去访问吧。所以，你再次需要用到反向代理来做处理。

配置也不难，来看看怎么做吧：

```javascript
http {
   #此处省略一些基本配置
   
   upstream product_server{
       server www.helloworld.com:8081;
   }
   
   upstream admin_server{
       server www.helloworld.com:8082;
   }
   
   upstream finance_server{
       server www.helloworld.com:8083;
   }

   server {
       #此处省略一些基本配置
       #默认指向product的server
       location / {
           proxy_pass http://product_server;
       }

       location /product/{
           proxy_pass http://product_server;
       }

       location /admin/ {
           proxy_pass http://admin_server;
       }
       
       location /finance/ {
           proxy_pass http://finance_server;
       }
   }
}
```

## https反向代理配置

一些对安全性要求比较高的站点，可能会使用 HTTPS（一种使用ssl通信标准的安全HTTP协议）。

这里不科普 HTTP 协议和 SSL 标准。但是，使用 nginx 配置 https 需要知道几点：

- HTTPS 的固定端口号是 443，不同于 HTTP 的 80 端口
- SSL 标准需要引入安全证书，所以在 nginx.conf 中你需要指定证书和它对应的 key

其他和 http 反向代理基本一样，只是在 Server 部分配置有些不同。

```javascript

```

#### 静态站点配置

有时候，我们需要配置静态站点(即 html 文件和一堆静态资源)。

举例来说：如果所有的静态资源都放在了 /app/dist 目录下，我们只需要在 nginx.conf 中指定首页以及这个站点的 host 即可。

配置如下：

```javascript
worker_processes  1;

events {
   worker_connections  1024;
}

http {
   include       mime.types;
   default_type  application/octet-stream;
   sendfile        on;
   keepalive_timeout  65;

   gzip on;
   gzip_types text/plain application/x-javascript text/css application/xml text/javascript application/javascript image/jpeg image/gif image/png;
   gzip_vary on;

   server {
       listen       80;
       server_name  static.zp.cn;

       location / {
           root /app/dist;
           index index.html;
           #转发任何请求到 index.html
       }
   }
}
```

然后，添加 HOST：

127.0.0.1 static.zp.cn，此时，在本地浏览器访问 static.zp.cn ，就可以访问静态站点了。

#### 跨域解决方案

web 领域开发中，经常采用前后端分离模式。这种模式下，前端和后端分别是独立的 web 应用程序，例如：后端是 Java 程序，前端是 React 或 Vue 应用。

各自独立的 web app 在互相访问时，势必存在跨域问题。解决跨域问题一般有两种思路：

##### CORS

在后端服务器设置 HTTP 响应头，把你需要运行访问的域名加入加入 Access-Control-Allow-Origin 中。

##### jsonp

把后端根据请求，构造json数据，并返回，前端用 jsonp 跨域。

这两种思路，本文不展开讨论。

需要说明的是，nginx 根据第一种思路，也提供了一种解决跨域的解决方案。

举例：www.helloworld.com 网站是由一个前端 app ，一个后端 app 组成的。前端端口号为 9000， 后端端口号为 8080。

前端和后端如果使用 http 进行交互时，请求会被拒绝，因为存在跨域问题。来看看，nginx 是怎么解决的吧：

首先，在 enable-cors.conf 文件中设置 cors ：

```javascript
# allow origin list
set $ACAO '*';

# set single origin
if ($http_origin ~* (www.helloworld.com)$) {
 set $ACAO $http_origin;
}

if ($cors = "trueget") {
   add_header 'Access-Control-Allow-Origin' "$http_origin";
   add_header 'Access-Control-Allow-Credentials' 'true';
   add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
   add_header 'Access-Control-Allow-Headers' 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
}

if ($request_method = 'OPTIONS') {
 set $cors "${cors}options";
}

if ($request_method = 'GET') {
 set $cors "${cors}get";
}

if ($request_method = 'POST') {
 set $cors "${cors}post";
}
```

接下来，在你的服务器中 include enable-cors.conf 来引入跨域配置：

```javascript
# ----------------------------------------------------
# 此文件为项目 nginx 配置片段
# 可以直接在 nginx config 中 include（推荐）
# 或者 copy 到现有 nginx 中，自行配置
# www.helloworld.com 域名需配合 dns hosts 进行配置
# 其中，api 开启了 cors，需配合本目录下另一份配置文件
# ----------------------------------------------------
upstream front_server{
 server www.helloworld.com:9000;
}
upstream api_server{
 server www.helloworld.com:8080;
}

server {
 listen       80;
 server_name  www.helloworld.com;

 location ~ ^/api/ {
   include enable-cors.conf;
   proxy_pass http://api_server;
   rewrite "^/api/(.*)$" /$1 break;
 }

 location ~ ^/ {
   proxy_pass http://front_server;
 }
}
```