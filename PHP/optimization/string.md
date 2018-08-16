# 字符串

## 少用正则表达式

能用 PHP 内部字符串操作函数 的情况下，尽量用他们，不要用正则表达式， 因为其效率高于正则，正则最耗性能。

`str_replace`函数要比`preg_replace`快得多，`strtr`函数又比`str_replace`来得快。

例如：[strpbrk()](http://php.net/manual/zh/function.strpbrk.php)、[strncasecmp()](http://php.net/manual/zh/function.strncasecmp.php)、[strpos()](http://php.net/manual/zh/function.strpos.php)、[strrpos()](http://php.net/manual/zh/function.strrpos.php)、[stripos()](http://php.net/manual/zh/function.stripos.php)、[strripos()](http://php.net/manual/zh/function.strripos.php)。

## 字符替换

如果需要转换的全是单个字符，用字符串作为 [strtr()](http://php.net/manual/zh/function.strtr.php)函数完成替换，而不是数组：

```php
$addr='abcdefgaa';
$addr = strtr($addr, "abcd", "efgh");       // 建议
$addr = strtr($addr, ['a' => 'e',]);  // 不建议
//efghefgee
```

另外，不要做无谓的替换，即使没有替换，`str_replace`也会为其参数分配内存。

用 `strpos` 先查找（非常快）判断是否需要替换。

## 压缩大的字符串

使用 [gzcompress()](http://php.net/manual/zh/function.gzcompress.php) 和 [gzuncompress()](http://php.net/manual/zh/function.gzuncompress.php) 对容量大的字符串进行压缩和解压，再## 存入和取出数据库## 。

这种内置的函数使用 gzip 算法，能压缩字符串`90%`。

## echo 输出

`echo` 字符串用逗号代替点连接符更快些。虽然，`echo`是一种语言结构，不是真正的函数。

但是，它可以把逗号隔开的多个字符串当作“函数”参数传入，所以速度会更快。

```php
echo $str1, $str2;       // 速度快
echo $str1 . $str2;      // 速度稍慢
```

## 尽量用单引号

PHP 引擎允许使用单引号和双引号来封装字符串变量，但是它们的速度是有很大的差别的！

使用双引号的字符串会告诉 PHP 引擎，首先去读取字符串内容，查找其中的变量，并改为变量对应的值。

一般来说字符串是没有变量的，使用双引号会导致性能不佳。

最好使用字符串连接，而不是双引号字符串。

```php
$output = "This is a plain string";  // 不好的实践
$output = 'This is a plain string';  // 好的实践

$type = "mixed";                     // 不好的实践
$output = "This is a $type string";

$type = 'mixed';                     // 好的实践
$output = 'This is a ' . $type . ' string';
```

## 使用 isset 代替 strlen

在检验字符串长度时，我们第一想法会使用 [strlen()](http://php.net/manual/zh/function.strlen.php) 函数。

此函数执行起来相当快，因为它不做任何计算，只返回在`zval`结构（C 的内置数据结构，用于存储 PHP 变量）中存储的已知字符串长度。

但是，由于`strlen()`是函数，多多少少会有些慢，因为函数调用会经过诸多步骤，如字母小写化、哈希查找，会跟随被调用的函数一起执行。

在某些情况下，你可以使用 [isset()](http://php.net/manual/zh/function.isset.php) 技巧加速执行你的代码。例如：

```php
if (strlen($foo) < 5) {
    echo "Foo is too short";
}

// 使用isset()
if (!isset($foo{5})) {
    echo "Foo is too short";
}
```

## 用 split 分割字符串

在分割字符串时，`split()`要比`explode()`快。

## echo 效率高于 print

因为`echo`没有返回值，`print`返回一个整型。

注意：`echo`输出大字符串的时候，如果没有调整就会严重影响性能。
