# 字符串转为二进制

```php
<?php
//字符串转为二进制
function asc2bin($temp)
{
    $data = '';
    $len = strlen($temp);//获取字符串长度
    for ($i = 0; $i < $len; $i++) {
        //返回一个格式化字符串(返回字符的 ASCII 码值(返回字符串的子串))
        $data .= sprintf("%08b", ord(substr($temp, $i, 1)));
    }
    return $data;
}

//二进制转字符串
function bin2asc($temp)
{
    $data = '';
    $len = strlen($temp);//获取字符串长度
    for ($i = 0; $i < ($len / 8); $i++) {
        //返回字符的 ASCII 码值(获取变量的整数值(返回字符串的子串))
        $data .= chr(intval(substr($temp, $i * 8, 8), 2));
    }
    return $data;
}

$e = asc2bin('逐风博客');
echo $e;
//输出：111001101011100010000101111010011010001110001110111001011000110110011010111001011010111010100010
echo bin2asc($e);
//输出：逐风博客
```
