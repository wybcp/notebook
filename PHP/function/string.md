# [String 函数](http://www.runoob.com/php/php-ref-string.html)

## strlen()

strlen() 函数返回字符串的长度（字符数），常用在循环和其他函数中，确定字符串何时结束。

## strstr(),strchr(),strrchr(),stristr()

返回字符串，多个目标则返回首个目标的位置。

### 查找位置

strpos() 函数用于在字符串内查找一个字符或一段指定的文本。
`int strpos(haystack, needle)`

如果在字符串中找到匹配，该函数会返回第一个匹配的字符位置；如果未找到匹配，则返回 FALSE。带来一个新问题，false 在 PHP 中等于 0，也就是字符串第一个位置。使用"==="判断

```php
<?php
$result=strpos("Hello world!","wld");

if ($result===false) {
    echo("not found");
}else {
    echo("found at position:".$result);
}
```

## 连接分割字符串

`explode(delimiter, string)`分割全部字符串;

`strtok(str, token)`一次从字符串取出一段片段；

`join()`和`implode(delimiter, string)`连接字符串。

```php
<?php
$email="Wyb123@qq.com";
$email_array=explode("@", $email);
echo $email_array[0]."<br>";

echo strtok($email, "@");

$new_email=join("@",$email_array);
echo $new_email;
```

`substr(string, start,length)`提取 start 开始的 length 个字符串。

## 字符串比较

`int strcmp(str1, str2)`相等返回 0，按字典顺序 str1 在 str2 后面返回正数，区分大小写。'int strcasecmp(str1, str2)'不区分大小写。

`strnatcmp()`按自然排序。 ##替换子字符串

`str_replace($search, $replace, $subject);`
