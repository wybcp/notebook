# nginx参数

## nginx日志

如果只是监控每次请求的访问时间。直接检测nginx的日志即可。在nginx的日志中有两个选项。$request_time 和 $upstream_response_time 。 这两个选项记录了响应时间。

1、$request_time 指的就是从接受用户请求的第一个字节到发送完响应数据的时间，即包括接收请求数据时间、程序响应时间、输出响应数据时间。

2、$upstream_response_time 是指从Nginx向后端(php-cgi)建立连接开始到接受完数据然后关闭连接为止的时间。

如果只是监控后端PHP服务的性能，只要更多的关注 $upstream_response_time 这个选项即可。