# 文件处理

## 打开文件

fopen() 函数用于在 PHP 中打开文件。
此函数的第一个参数含有要打开的文件的名称，第二个参数规定了使用哪种模式来打开文件：
http://www.runoob.com/php/php-file.html

## 关闭文件

fclose() 函数用于关闭打开的文件：

## 检测文件末尾（EOF）

feof() 函数检测是否已到达文件末尾（EOF）。
在循环遍历未知长度的数据时，feof() 函数很有用。
注释：在 w 、a 和 x 模式下，您无法读取打开的文件！

## 逐行读取文件

fgets()
函数用于从文件中逐行读取文件。
注释：在调用该函数之后，文件指针会移动到下一行。
实例
下面的实例逐行读取文件，直到文件末尾为止：

```<?php
$file = fopen("welcome.txt", "r") or exit("无法打开文件!");
// 读取文件每一行，直到文件结尾
while(!feof($file))
{
    echo fgets($file). "<br>";
}
fclose($file);
?>
```

## 逐字符读取文件

fgetc() 函数用于从文件中逐字符地读取文件。
注释：在调用该函数之后，文件指针会移动到下一个字符。

## 文件上传

### $\_FILES

通过使用 PHP 的全局数组 $\_FILES，你可以从客户计算机向远程服务器上传文件。

第一个参数是表单的 input name，第二个下标可以是 "name"、"type"、"size"、"tmp_name" 或 "error"。如下所示：

- `$_FILES["file"]["name"]`- 上传文件的名称
- `$_FILES["file"]["type"]`- 上传文件的类型
- `$_FILES["file"]["size"]`- 上传文件的大小，以字节计
- `$_FILES["file"]["tmp_name"]`- 存储在服务器的文件的临时副本的名称
- `$_FILES["file"]["error"]`- 由文件上传导致的错误代码
