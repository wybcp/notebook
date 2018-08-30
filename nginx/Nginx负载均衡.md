
负载均衡（load balance）是将负载分摊到不同的服务单元，既保证服务的可用性，又保证响应足够快，给用户很好的体验。

nginx的负载均衡策略可以划分为两大类：内置策略和扩展策略。内置策略包含加权轮询和ip hash，在默认情况下这两种策略会编译进nginx内核，只需在nginx配置中指明参数即可。扩展策略有很多，如fair、通用hash、consistent hash等，默认不编译进nginx内核。

首先给大家说下upstream这个配置的，这个配置是写一组被代理的服务器地址，然后配置负载均衡的算法。这里的被代理服务器地址有2中写法。


```
upstream mysvr {   
server 192.168.10.121:3333;   
server 192.168.10.122:3333;  
    
} 
server {    
....    
location ~*^.+$ {

proxy_pass http://mysvr; #请求转向mysvr 定义的服务器列表        
    
} 
upstream mysvr {   
server http://192.168.10.121:3333;   
server http://192.168.10.122:3333;  
    
} 
server {    
....    
location ~*^.+$ {          
proxy_pass mysvr; #请求转向mysvr 定义的服务器列表       
}
```


1、热备：如果你有2台服务器，当一台服务器发生事故时，才启用第二台服务器给提供服务。服务器处理请求的顺序：AAAAAA突然A挂啦，BBBBBBBBBBBBBB.....

```
upstream mysvr {   
server 127.0.0.1:7878;   
server 192.168.10.121:3333 backup; #热备    
    
}
```


2、 加权轮询（weighted round robin）：nginx默认就是轮询其权重都默认为1，服务器处理请求的顺序：ABABABABAB....

```
upstream mysvr {   
server 127.0.0.1:7878;   
server 192.168.10.121:3333;      
}
```
![image](http://ou1viq65b.bkt.clouddn.com/17-8-30/7300152.jpg)

第一，如果可以把加权轮询算法分为先深搜索和先广搜索，那么nginx采用的是先深搜索算法，即将首先将请求都分给高权重的机器，直到该机器的权值降到了比其他机器低，才开始将请求分给下一个高权重的机器；第二，当所有后端机器都down掉时，nginx会立即将所有机器的标志位清成初始状态，以避免造成所有的机器都处在timeout的状态，从而导致整个前端被夯住。

3、加权轮询：跟据配置的权重的大小而分发给不同服务器不同数量的请求。如果不设置，则默认为1。下面服务器的请求顺序为：ABBABBABBABBABB....

```
upstream mysvr {   
server 127.0.0.1:7878 weight=1;   
server 192.168.10.121:3333 weight=2; }
```

4、ip_hash:nginx会让相同的客户端ip请求相同的服务器。


```
upstream mysvr {   
server 127.0.0.1:7878;   
server 192.168.10.121:3333;   
ip_hash;  
    
}
```
![](http://ou1viq65b.bkt.clouddn.com/17-8-30/69178371.jpg)

关于nginx负载均衡配置的几个状态参数讲解。

- down，表示当前的server暂时不参与负载均衡。
- backup，预留的备份机器。当其他所有的非backup机器出现故障或者忙的时候，才会请求backup机器，因此这台机器的压力最轻。
- max_fails，允许请求失败的次数，默认为1。当超过最大次数时，返回proxy_next_upstream 模块定义的错误。
- fail_timeout，在经历了max_fails次失败后，暂停服务的时间。max_fails可以和fail_timeout一起使用。

```
upstream mysvr {   
server 127.0.0.1:7878 weight=2 max_fails=2 fail_timeout=2;   
server 192.168.10.121:3333 weight=1 max_fails=2 fail_timeout=1;    
    
}
```
