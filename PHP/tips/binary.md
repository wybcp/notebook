# [PHP 二进制封包](https://blog.tanteng.me/2017/01/php-pack/)

通过 TCP/IP 协议传输数据经常会用二进制数据包的形式，在 PHP 中可使用 pack() 和 unpack() 函数进行二进制封包和解包，通过 socket 建立 TCP 连接，并将数据包传输出去。

## PHP 数据封包示例

````php
/**
 * 包头二进制封包
 * @param int $length
 * @return string
    */
private function getHeaderPack(int $length):string
{
    $header = [
        'version'     => 1,
        'seq'         => time(),
        'body_length' => $length,
    ];
    $headerPack = pack('L3', $header['version'], $header['seq'], $header['body_length']);
    //$this->unPackHeader($headerPack);
    return $headerPack;
}
```
一个 TCP 协议的接口，数据包通常是由包头和包体组成的，把包头和包体分别二进制封包拼接起来（实际上合为一体进行封包也是一样的），就是一个完整的数据包。

如包头结构体定义三个字段，分别是 version,seq,body_length，类型都是 unsigned long，那么给包头封包的 PHP 写法就是：

```php
pack('L3', $header['version'], $header['seq'], $header['body_length']);
````

同理，包体的封包方式也是一样的，有时包体里的字段本身也是一个二进制的封包，也有他的包头和包体，不过方法是一样的，这个就看具体的定义了。

值得注意的是，这种封包的方式本身也是一种数据加密的方式，你必须知道每个字段的类型和顺序，才能解析数据，所以这个协议的定义也要保密。

在项目实践中，这种封包对类型有很严格的要求，一点都不能错，否则就无法正确解析。

## PHP 数据封包格式

以下是字段类型和对应说明，摘自 PHP 官方手册。

| Code | Description                                                  |
| ---- | ------------------------------------------------------------ |
| a    | NUL-padded string                                            |
| A    | SPACE-padded string                                          |
| h    | Hex string, low nibble first                                 |
| H    | Hex string, high nibble first                                |
| c    | signed char                                                  |
| C    | unsigned char                                                |
| s    | signed short (always 16 bit, machine byte order)             |
| S    | unsigned short (always 16 bit, machine byte order)           |
| n    | unsigned short (always 16 bit, big endian byte order)        |
| v    | unsigned short (always 16 bit, little endian byte order)     |
| i    | signed integer (machine dependent size and byte order)       |
| I    | unsigned integer (machine dependent size and byte order)     |
| l    | signed long (always 32 bit, machine byte order)              |
| L    | unsigned long (always 32 bit, machine byte order)            |
| N    | unsigned long (always 32 bit, big endian byte order)         |
| V    | unsigned long (always 32 bit, little endian byte order)      |
| q    | signed long long (always 64 bit, machine byte order)         |
| Q    | unsigned long long (always 64 bit, machine byte order)       |
| J    | unsigned long long (always 64 bit, big endian byte order)    |
| P    | unsigned long long (always 64 bit, little endian byte order) |
| f    | float (machine dependent size and representation)            |
| d    | double (machine dependent size and representation)           |
| x    | NUL byte                                                     |
| X    | Back up one byte                                             |
| Z    | NUL-padded string (new in PHP 5.5)                           |
| @    | NUL-fill to absolute position                                |
