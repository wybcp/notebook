# 文件

PHP 具有丰富的文件操作函数。

## 读取文件

最简单的读取文件的函数为[file_get_contents](http://php.net/manual/zh/function.file-get-contents.php)，可以将整个文件读取到一个字符串中。

```php
$content = file_get_contents('./test.txt');
```

PHP 也提供类似于 C 语言操作文件的方法，使用`fopen，fgets，fread`等方法。

`fgets`可以从文件指针中读取一行：

```php
$fp = fopen('./text.txt', 'rb');
while(!feof($fp)) {
    echo fgets($fp); //读取一行
}
fclose($fp);
```

`freads`可以读取指定长度的字符串。

```php
$fp = fopen('./text.txt', 'rb');
$contents = '';
while(!feof($fp)) {
    $contents .= fread($fp, 4096); //一次读取4096个字符
}
fclose($fp);
```

使用 `fopen` 打开的文件，`fclose` 关闭文件指针。

## 判断文件

一般情况下在对文件进行操作的时候需要先判断文件是否存在，PHP 中常用来判断文件存在的函数:

- `file_exists` 不仅可以判断文件是否存在，也可以判断目录是否存在
- `is_file` 判断给定的路径是否是一个文件。

更加精确的可以使用 `is_readable` 与 `is_writeable` 在文件是否存在的基础上，判断文件是否可读与可写。

```php
$filename = './test.txt';
if (is_writeable($filename)) {
file_put_contents($filename, 'test');
}
if (is_readable($filename)) {
echo file_get_contents($filename);
}
```
