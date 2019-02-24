# 面试题

## "\t" "\r" "\n" "\x20"

答：`\t tab \r 换行 \n 回车 \x20 16 进制`

## `setcookie("user","value")` `var_dump($_COOKIE['user'])`

答：null

## require include 区别

require 遇到错误会中断，include 不会

## 调用父类的方法`parent::`

## php 跳转页面

header("location:");

## 客户端 ip 整型

ip2long

## 什么是 php-fpm

FastCGI 进程管理器

## 查看 io 的状态

iostat

## 查看 cpu 的负载

top

## 聚簇索引所在的列数据是乱序的，会有什么影响。

[https://www.cnblogs.com/starhu/p/6406495.html](https://www.cnblogs.com/starhu/p/6406495.html)

## mysql 主从同步的原理，什么 sql 语句导致 mysql 的主从同步失败

mysql binlog

## 获取当前客户端的 IP 地址，并判断是否在（111.111.111.111,222.222.222.222)

注意:（111.111.111.111,222.222.222.222) 这是一个集合区间，不是数组的 array

利用 php 获取 ip 地址。 然后转成 long

```php
public function ip() {
    //strcasecmp 比较两个字符，不区分大小写。返回0，>0，<0。
    if(getenv('HTTP_CLIENT_IP') && strcasecmp(getenv('HTTP_CLIENT_IP'), 'unknown')) {
        $ip = getenv('HTTP_CLIENT_IP');
    } elseif(getenv('HTTP_X_FORWARDED_FOR') && strcasecmp(getenv('HTTP_X_FORWARDED_FOR'), 'unknown')) {
        $ip = getenv('HTTP_X_FORWARDED_FOR');
    } elseif(getenv('REMOTE_ADDR') && strcasecmp(getenv('REMOTE_ADDR'), 'unknown')) {
        $ip = getenv('REMOTE_ADDR');
    } elseif(isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], 'unknown')) {
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    $res =  preg_match ( '/[\d\.]{7,15}/', $ip, $matches ) ? $matches [0] : '';
    return $ip;
}
$ip = sprintf('%u',ip2long(ip());
$begin = sprintf('%u',ip2long('111.111.111.111'))
$end = sprintf('%u',ip2long('222.222.222.222'))
if($ip > $begin && $ip < $end) {
    echo "在这个区间里"。
}
```

## csrf 和 xss 的区别

- csrf 跨站请求攻击。验证码、token、检测 refer
- xss 跨站脚本攻击，过滤用户输入。

## 应用中我们经常会遇到在 user 表随机调取 10 条数据来展示的情况，简述你如何实现该功能。

```php
function get_random_array($min,$max,$number)
{
    $data = [];
    for($i = 0;$i<$number;$i++;)
    {
        $d = mt_rand($min,$max);
        if(in_array($d,$data)) {
            $i--;
        }else{
            $data[] = $d;
        }
    }
    return $data;
}

$sql = 'select * from user where user_id in (' .join(",",get_random_array($min,$max,$number)). ')'
```

## 从扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这 5 张牌是连续的

- [思路解析](https://blog.csdn.net/Jarvan_Song/article/details/52416039)
- [PHP 代码实现](https://github.com/xianyunyh/arithmetic-php/blob/master/package/Other/Judge.php)

## linux 的内存分配和多线程原理

- [Linux 内存分配](https://blog.csdn.net/haiross/article/details/38921135)
- [Linux 线程和进程关系](https://my.oschina.net/cnyinlinux/blog/367910)

## MYSQL 中主键与唯一索引的区别

- 主键唯一不能为空
- 唯一索引可以为空
- 一个表可以有多个唯一索引，但是只能有一个主键

## http 和 https 区别

- https 是在 http 的基础上加 ssl 层。进行了数据加密。保证传输过程中，数据加密，默认端口是 443
- http 在传输中数据是明文，默认端口 80

## http 状态码及其含意

- 2xx 表示成功 比如 200
- 3xx 资源转移 301 永久转移 304 Not Modified
- 4xx 资源没找到或禁止访问 404、403
- 5xx 服务器错误

## linux 中怎么查看系统资源占用情况

top 、free、iostat、vmstat

## SQL 注入的原理是什么？如何防止 SQL 注入

用户传入的数据没有过滤。不要相信用户的输入

## isset(null) isset(false) empty(null) empty(false)输出

false,false,true,true

## 优化 MYSQL 的方法

​ 数据库字段冗余，增添索引、优化 sql、分库分表

## 数据库中的事务是什么？

​ 是指一些操作要么同时执行成功，要么同时失败的一个过程，事务具有 acid 四个特性。

## 写一个函数，尽可能高效的从一个标准 URL 中取出文件的扩展名

```php
$arr = parse_url('http://www.sina.com.cn/abc/de/fg.php?id=1');
$result = pathinfo($arr['path']);
var_dump($result['extension']);
```

## 参数为多个日期时间的数组，返回离当前时间最近的那个时间

解题思路：让第一个时间作为哨兵。计算第一个时间和当前时间的差 diff，然后从第二个值开始遍历。如果第二个值和当前时间的值大于 diff。则继续，否则该时间离当前时间近。把 min 赋值给当前值。

```php
function ($timeArray,$now) {
    $min = $timeArray[0];
    $diff =abs($min-$now);
    $length = count($timeArray);
    for($i=1;$i<$length;$i++) {
        $diff1 = $timeArray[$i] - $now;
        if($diff1 < $diff) {
            $diff = $diff1;
            $min = timeArray[$i];
        }
    }
    return $min;
}
```

## echo、print、print_r 的区别

- echo 是一个语法结构
- print 是一个函数,有返回值
- print_r 是一个函数，用于打印复合类型变量。

## http 协议的 header 中有哪些 key 及含义

非常多，建议记住几个常见的。

[HTTP Header](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers)

## 聚簇索引，聚集索引的区别？

聚簇索引：数据行的物理顺序与列值（一般是主键的那一列）的逻辑顺序相同，一个表中只能拥有一个聚集索引。

## 数组和 hash 的区别是什么？

​hash 基于数组。数组在内存空间上是连续的地址。hash 则不连续。

## 写个函数，判断下面扩号是否闭合，左右对称即为闭合： ((()))，)(())，(())))，(((((())，(()())，()()

```php
/**
*  对于对称的结构第i个跟第n-i个相反。
*/
function close($string)
{
    if(empty($string)) {
        return false;
    }
    $length = strlen($string);
      //判断奇偶数
    if($length%2 ==1) {
        return false;
    }

    for ($i=0;$i<$length;$i++) {
        if($string[$i] == '('){
            if($string[$length-$i-1] != ')'){
                return false;
            }
        }else{
            if($string[$length-$i-1] != '('){
                return false;
            }
        }
    }
    return true;
}

var_dump(close( '(()())'));
```

## 找出数组中不重复的值[1,2,3,3,2,1,5]

```php
/**
 * 从数组中找出不重复的数字
 * @param $array
 */
function find($array)
{
    if(empty($array) || !is_array($array)) {
        return [];
    }

    $data = [];

    foreach ($array as $key=>$value) {
        if(isset($data[$value])) {
            $data[$value]++;
        }else{
            $data[$value] = 1;
        }
    }
    $result = [];
    foreach ($data as $k=>$v) {
        if($v != 1) {
            unset($data[$k]);
        }else{
            $result[] = $k;
        }
    }
    return $result;
}
var_dump(find([1,2,3,3,2,1,5]));
```

## PHP 的的这种弱类型变量是怎么实现的？

通过 zval 结构。 zval 包含变量的信息。

    zval{
        type
        value
    }

type 记录变量的类型。然后根据不同的类型，找到不同的 value。

## PHP 中发起 http 请求有哪几种方式？它们有何区别？

​ curl、fscocket、socket

## 请写出自少两个支持回调处理的 PHP 函数，并自己实现一个支持回调的 PHP 函数

preg_matacth_callback. call_user_func

## 请写出自少三种截取文件名后缀的方法或函数（PHP 原生函数和自己实现函数均可）

basename expload() strpos

## 请用 SHELL 统计 5 分钟内，nginx 日志里访问最多的 URL 地址，对应的 IP 是哪些？

## ping 一个服务器 ping 不通，用哪个命令跟踪路由包？

- linux:traceroute,
- windows:tracert

## php-fpm 各配置含义，fpm 的 daemonize 模式

- static - 子进程的数量是固定的（pm.max_children）
- ondemand - 进程在有需求时才产生（当请求时，与 dynamic 相反，pm.start_servers 在服务启动时即启动
- dynamic - 子进程的数量在下面配置的基础上动态设置：pm.max_children，pm.start_serverspm.min_spare_servers，pm.max_spare_servers

## 断开 TCP 连接时，timewait 状态会出现在发起分手的一端还是被分手的一端

出现在分手的一端。time_wait 会持续 2mls。由于网络的不稳定等因素，会导致 ack 发送失败。在 2MLS 内，可以重发。

被动关闭连接的一方在一段时间内没有收到对方的 ACK 确认数据包，会重新发送 FIN 数据包，因而主动关闭连接的一方需要停留在等待状态以处理对方重新发送的 FIN 数据包。否则他会回应一个 RST 数据包给被动关闭连接的一方，使得对方莫名其妙。

在 TIME_WAIT 状态下，不允许应用程序在当前 ip 和端口上和之前通信的 client(这个 client 的 ip 和端口号不变)建立一个新的连接。这样就能避免新的连接收到之前的 ip 和端口一致的连接残存在网络中的数据包。这也是 TIME_WAIT 状态的等待时间被设置为 2MSL 的原因，以确保网络上当前连接两个方向上尚未接收的 TCP 报文已经全部消失。
