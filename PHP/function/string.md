# [String 函数](http://www.runoob.com/php/php-ref-string.html)

## strlen()

strlen() 函数返回字符串的长度（字符数），常用在循环和其他函数中，确定字符串何时结束。

## mb_strlen()

使用`mb_strlen()`函数获取字符串中中文长度。

```php
$str = "我爱你";
echo mb_strlen($str,"UTF8");
```

## strstr(),strchr(),strrchr(),stristr()

返回字符串，多个目标则返回首个目标的位置。

## strpos()查找位置

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

## 字符串比较

`int strcmp(str1, str2)`相等返回 0，按字典顺序 str1 在 str2 后面返回正数，区分大小写。`int strcasecmp(str1, str2)`不区分大小写。

`strnatcmp()`按自然排序。

## 去除字符串首尾的空格

PHP 中有三个函数可以去掉字符串的空格:

- trim 去除一个字符串两端空格。
- rtrim 是去除一个字符串右部空格，其中的 r 是 right 的缩写。
- ltrim 是去除一个字符串左部空格，其中的 l 是 left 的缩写。

## 字符串合并函数 implode()

函数说明：implode(分隔符[可选], 数组)

返回值：把数组元素组合为一个字符串

例子：

```php
$arr = ['Hello', 'World!'];
$result = implode(' ', $arr);
print_r($result);//结果显示Hello World!
```

## php 字符串分隔函数 explode()

函数说明：explode(分隔符[可选], 字符串) `explode(delimiter, string)`

返回值：函数返回由字符串组成的数组

例子：

```php
$str = 'apple,banana';
$result = explode(',', $str);
print_r($result);
```

## str_getcsv()

php 提供了 str_getcsv() 方法，可以把字符串作为 csv 格式来处理，这样方便解析为数组。

str_getcsv 解析 csv 字符串为数组
`array str_getcsv ( string $input [, string $delimiter = "," [, string $enclosure = '"' [, string $escape = "\\" ]]] )`

参数：

- input 待解析的字符串
- delimiter 设定字段界定符(仅单个字符)
- enclosure 设定字段包裹字符（仅单个字符）
- escape 设置转义字符（仅单个字符），默认为反斜线（\）

实例：

```php
<?php
$str = "中国,广东省,广州市,天河区,'113.329884,23.154799',1,'2016-01-01 12:00:00','1,2,3,4,5,6'";
$arr = str_getcsv($str, ',', "'");
print_r($arr);
// Array(
//     [0] => 中国
//     [1] => 广东省
//     [2] => 广州市
//     [3] => 天河区
//     [4] => 113.329884,23.154799
//     [5] => 1
//     [6] => 2016-01-01 12:00:00
//     [7] => 1,2,3,4,5,6)
```

## 字符串的截取函数

### 英文 substr()

函数说明：substr(字符串变量,开始截取的位置，截取个数）

例如：

```php
$str='i love you';
//截取love这几个字母
echo substr($str, 2, 4);//为什么开始位置是2呢，因为substr函数计算字符串位置是从0开始的，也就是0的位置是i,1的位置是空格，l的位置是2。从位置2开始取4个字符，就是love。
```

### 中文 mb_substr()

字符串的截取函数说明：mb_substr(字符串变量,开始截取的位置，截取个数, 网页编码）
例如：

```php
$str='我爱你，中国';

//截取中国两个字

echo mb_substr($str, 4, 2, 'utf8');
//mb_substr函数计算汉字位置是从0开始的，也就是0的位置是我,1的位置是爱，4的位置是中。从位置4开始取2个汉字，就是中国。中文编码一般是utf8格式
```

## 替换字符串 str_replace()

函数说明：str_replace(要查找的字符串, 要替换的字符串, 被搜索的字符串, 替换进行计数[可选]);`str_replace($search, $replace, $subject);`

## 格式化字符串函数 sprintf()

函数说明：sprintf(格式, 要转化的字符串)
返回：格式化好的字符串
例子：

```php
$str = '99.9';
$result = sprintf('%01.2f', $str);
echo $result;//结果显示99.90
```

解释例子中的格式%01.2f:

1. 这个 % 符号是开始的意思， 也就是 "起始字符", 直到出现 "转换字符" 为止，就算格式终止。
2. 跟在 % 符号后面的是 0， 是 "填空字元" ，表示如果位置空着就用 0 来填满。
3. 在 0 后面的是 1，这个 1 是规定整个所有的字符串占位要有 1 位以上(小数点也算一个占位)。
   如果把 1 改成 6，则 $result 的值将为 099.90
4. 在 %01 后面的 .2 （点 2）意思是，小数点后的数字必须占 2 位。如果$str 的值为 9.234,则 $result 的值将为 9.23.
5. 最后，以 f "转换字符" 结尾。

## 字符串单词的个数 str_word_count()

该函数必须要传递一个参数，根据参数类型返回单词的个数。如下面的所示：

```php
<?php
$str = "How many words do I have?";
echo str_word_count($str); //Outputs 6
```
