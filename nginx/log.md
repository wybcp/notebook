# [nginx access_log 日志](https://lanjingling.github.io/2016/03/14/nginx-access-log/)

nginx 日志主要有两条指令：

- log_format：用来设置日志格式；
- access_log：用来指定日志文件的存放路径、格式（把定义的 log_format 跟在后面）和缓存大小；如果不想启用日志则 access_log off ;

## log_format 日志格式

1、语法：
log_format name（格式名字） 格式样式（即想要得到什么样的日志内容）
示例：

```conf
log_format   main
'$remote_addr - $remote_user [$time_local] "$request" '
'$status $body_bytes_s ent "$http_referer" '
'"$http_user_agent" "$http_x_forwarded_for"'
```

2、具体可设置的参数格式及说明如下：
[![img](http://ww3.sinaimg.cn/large/72c913fbgw1f2l1htuh5yj20om0f3aac.jpg)](http://ww3.sinaimg.cn/large/72c913fbgw1f2l1htuh5yj20om0f3aac.jpg)

3、x_forwarded_for：

通常 web 服务器放在反向代理的后面，这样就不能获取到客户的 IP 地址了，通过$remote_addr 拿到的 IP 地址是反向代理服务器的 iP 地址。反向代理服务器在转发请求的 http 头信息中，可以增加 x_forwarded_for 信息，用以记录原有客户端的 IP 地址和原来客户端的请求的服务器地址。

_注_：在 server 中设置 x_forwarded_for

> proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

## access_log

用了 log_format 指令设置了日志格式之后，需要用 access_log 指令指定日志文件的存放路径；
1、语法：
access_log path(存放路径) format (自定义日志名称)
示例:

> access_log logs/access.log main;

2、设置刷盘策略：

> access_log /data/logs/nginx-access.log buffer=32k flush=5s;

buffer 满 32k 才刷盘；假如 buffer 不满 5s 钟强制刷盘。

_注_：一般 log_format 在全局设置，可以设置多个。access_log 可以在全局设置，但往往是定义在虚拟主机（server）中的 location 中。
例如：

```conf
http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                   '"$status" $body_bytes_sent "$http_referer" '
                   '"$http_user_agent" "$http_x_forwarded_for" '
                   '"$gzip_ratio" $request_time $bytes_sent $request_length';
    log_format srcache_log '$remote_addr - $remote_user [$time_local] "$request" '
                        '"$status" $body_bytes_sent $request_time $bytes_sent $request_length '
                        '[$upstream_response_time] [$srcache_fetch_status] [$srcache_store_status] [$srcache_expire]';
 open_log_file_cache max=1000 inactive=60s;
    server {
        server_name ~^(www\.)?(.+)$;
        access_log logs/$2-access.log main;
        error_log logs/$2-error.log;
        location /srcache {
            access_log logs/access-srcache.log srcache_log;
        }
    }
}
```

3、其他：
1）error_log：
配置错误日志，例如上例。

2）open_log_file_cache：
对于每一条日志记录，都将是先打开文件，再写入日志，然后关闭。可以使用 open_log_file_cache 来设置日志文件缓存(默认是 off)。
语法:

> open_log_file_cache max=N [inactive=time][min_uses=n] [valid=time];

参数注释如下：

- max:设置缓存中的最大文件描述符数量，如果缓存被占满，采用 LRU 算法将描述符关闭。
- inactive:设置存活时间，默认是 10s
- min_uses:设置在 inactive 时间段内，日志文件最少使用多少次后，该日志文件描述符记入缓存中，默认是 1 次
- valid:设置检查频率，默认 60s

```nginx
open_log_file_cache max=1000 inactive=20s valid=1m min_uses=2;
```

3）日志分析：
通过对日志格式的定义，就可以使用常见的 Linux 命令行工具进行分析了：

查找访问频率最高的 URL 和次数：

> cat access.log | awk -F ‘^A’ ‘{print $10}’ | sort | uniq -c

查找当前日志文件 500 错误的访问：

> cat access.log | awk -F ‘^A’ ‘{if($5 == 500) print $0}’

查找当前日志文件 500 错误的数量：
cat access.log | awk -F ‘^A’ ‘{if($5 == 500) print $0}’ | wc -l

查找某一分钟内 500 错误访问的数量:

> cat access.log | awk -F ‘^A’ ‘{if($5 == 500) print $0}’ | grep ’09:00’ | wc-l

查找耗时超过 1s 的慢请求：

> tail -f access.log | awk -F ‘^A’ ‘{if($6>1) print $0}’

假如只想查看某些位：

> tail -f access.log | awk -F ‘^A’ ‘{if($6>1) print $3″|”$4}’

查找 502 错误最多的 URL：

> cat access.log | awk -F ‘^A’ ‘{if($5==502) print $11}’ | sort | uniq -c

查找 200 空白页

> cat access.log | awk -F ‘^A’ ‘{if($5==200 && $8 < 100) print $3″|”$4″|”$11″|”$6}’

## 切割日志

Nginx 的日志都是写在一个文件当中的，不会自动地进行切割，如果访问量很大的话，将导致日志文件容量非常大，不便于管理和造成 Nginx 日志写入效率低下等问题。所以，往往需要要对 access_log、error_log 日志进行切割。

切割日志一般利用 USR1 信号让 nginx 产生新的日志。实例：

```bash
#!/bin/bash

logdir="/data/logs/nginx"
pid=`cat $logdir/nginx.pid`
DATE=`date -d "1 hours ago" +%Y%m%d%H`
DATE_OLD=`date -d "7 days ago" +%Y%m%d`
for i in `ls $logdir/*access.log`; do
        mv $i $i.$DATE
done
for i in `ls $logdir/*error.log`; do
        mv $i $i.$DATE
done
kill -s USR1 $pid
rm -v $logdir"/access.log."$DATE_OLD*

rm -v $logdir"/error.log."$DATE_OLD*
```

1、分析：

- 将上面的脚本放到 crontab 中，每小时执行一次（0 ），这样每小时会把当前日志重命名成一个新文件；然后发送 USR1 这个信号让 Nginx 重新生成一个新的日志。（相当于备份日志）
- 将前 7 天的日志删除；

2、说明：
在没有执行 kill -USR1 $pid 之前，即便已经对文件执行了 mv 命令而改变了文件名称，nginx 还是会向新命名的文件”\*access.log.2016032623”照常写入日志数据的。原因在于：linux 系统中，内核是根据文件描述符来找文件的。

3、logrotates：
使用系统自带的 logrotates，也可以实现 nginx 的日志分割，查看其 bash 源码，发现也是发送 USR1 这个信号。
