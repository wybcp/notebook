# socket

## [fscokopen()](https://secure.php.net/manual/zh/function.fsockopen.php)函数

fsockopen()支持 socket 编程，可以使用 fsockopen 实现邮件发送等 socket 程序等等,使用 fcockopen 需要自己手动拼接出 header 部分

使用示例如下：

```php
<?php
$fp = fsockopen("www.taobao.com", 80, $error_no, $error_str, 30);

if (!$fp) {
    echo "$error_str ($error_no)<br />\n";
} else {
    $out = "GET /index.php / HTTP/1.1\r\n";
    $out .= "Host: www.taobao.com\r\n";
    $out .= "Connection: Close\r\n\r\n";
    fwrite($fp, $out);
    while (!feof($fp)) {
        echo fgets($fp, 128);
    }
    fclose($fp);
}
```

## [pfsockopen()](https://secure.php.net/manual/zh/function.pfsockopen.php)

打开一个持久的网络连接或者 Unix 套接字连接。

`resource pfsockopen ( string $hostname [, int $port = -1 [, int &$errno [, string &$errstr [, float $timeout = ini_get("default_socket_timeout") ]]]] )`
