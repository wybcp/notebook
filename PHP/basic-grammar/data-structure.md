# 数据类型

## 四种标量类型

- [boolean](http://php.net/manual/zh/language.types.boolean.php)（布尔型）
- [integer](http://php.net/manual/zh/language.types.integer.php)（整型）
- [float](http://php.net/manual/zh/language.types.float.php)（浮点型，也称作  [double](http://php.net/manual/zh/language.types.float.php))
- [string](http://php.net/manual/zh/language.types.string.php)（字符串）

### 整型 int

整型值可以使用十进制，十六进制，八进制或二进制表示，前面可以加上可选的符号（- 或者 +）

自 PHP 5.0.5 后，整型最大值可以用常量  **PHP_INT_MAX**  来表示，最小值可以在 PHP 7.0.0 及以后的版本中用常量  **PHP_INT_MIN**

```php
123
-123
0123 #八进制
0x123 #十六进制
```

给定的一个数超出了  [integer](http://php.net/manual/zh/language.types.integer.php)  的范围，将会被解释为  [float](http://php.net/manual/zh/language.types.float.php)。同样如果执行的运算结果超出了  [integer](http://php.net/manual/zh/language.types.integer.php)  范围，也会返回  [float](http://php.net/manual/zh/language.types.float.php)

从其他类型转换成整型

- 布尔值转整型 **false** 产生 0 **true** 产生 1
- 从浮点型转换 向下取整 0.5 转换成 0
- 字符串转整型
  > 如果该字符串没有包含 '.'，'e' 或 'E' 并且其数字值在整型的范围之内（由  **PHP_INT_MAX**  所定义），该字符串将被当成  [integer](http://php.net/manual/zh/language.types.integer.php)  来取值。其它所有情况下都被作为  [float](http://php.net/manual/zh/language.types.float.php)  来取值。该字符串的开始部分决定了它的值。如果该字符串以合法的数值开始，则使用该数值。否则其值为 0（零）。合法数值由可选的正负号，后面跟着一个或多个数字（可能有小数点），再跟着可选的指数部分。指数部分由 'e' 或 'E' 后面跟着一个或多个数字构成

## 浮点数 float

浮点数，也就是我们说的小数。由于浮点数的精度有限。尽管取决于系统，PHP 通常使用 IEEE 754 双精度格式，则由于取整而导致的最大相对误差为 1.11e-16

    **永远不要比较两个浮点数的值**

## 字符串 string

字符串由一些字符组成。

字符串有四种表示方法

- 单引号

  单引号是最简单的表示方法。在 C 语言中 单个字符用单引号表示。单引号的变量不解析.表达一个单引号自身，需在它的前面加个反斜线（\*\*）来转义

  ```php
  $a = 'abc';
  $b = '$a';//$a
  $c = "$a"; //abc
  ```

- 双引号

  双引号非转义任何其它字符都会导致反斜线被显示出来。\*\\{$var}\*  中的反斜线还不会被显示出来。

- heredoc

  heredoc 结构是一种提供一个开始标记和一个结束标记。方便书写大段的字符串。结束标记必须**顶格写**。

  类似双引号。单引号不转义。变量解析

  ```php
  <?php
   $heredoc = <<<START
   FDSFDSFS
   SDFSDTHIS DDSFS
   任意字符
   SF
  START
  ```

- nowdoc

  Nowdoc 结构是类似于单引号字符串的。Nowdoc 结构很象 heredoc 结构，但是 nowdoc 中不进行解析操作 nowdoc 前需要加上单引号。

  ```php
  <?php
  $str = <<<'EOD'
  Example of string
  spanning multiple lines
  using nowdoc syntax.
  EOD;
  ```

  string 中的字符可以通过一个从 0 开始的下标，用类似  array 结构中的方括号包含对应的数字来访问和修改

  **字符串的链接**

  字符串的连接使用.（点）转成字符串

  布尔值 true 转成 1 。false 转成 “”

  数组 array 转成 "array"

  object 总是被转换成字符串  *"Object"*，

### 布尔类型 Boolean

布尔类型只有 true 和 false 两个值

以下的值会认为是 false。其他之外的都是 true

- [布尔值](http://php.net/manual/zh/language.types.boolean.php)  **FALSE**  本身
- [整型值](http://php.net/manual/zh/language.types.integer.php) 0（零）
- [浮点型值](http://php.net/manual/zh/language.types.float.php) 0.0（零）
- [空字符串](http://php.net/manual/zh/language.types.string.php)，以及[字符串](http://php.net/manual/zh/language.types.string.php) "0"
- [空数组](http://php.net/manual/zh/language.types.array.php)
- 特殊类型  [NULL](http://php.net/manual/zh/language.types.null.php)（包括尚未赋值的变量）
- 从空标记生成的  [SimpleXML](http://php.net/manual/zh/ref.simplexml.php)  对象

```php
var_dump((bool)'false') //true #字符串false
var_dump((bool) false) //false #布尔值false
```

## 三种复合类型

- [array](http://php.net/manual/zh/language.types.array.php)（数组）
- [object](http://php.net/manual/zh/language.types.object.php)（对象）
- [callable](http://php.net/manual/zh/language.types.callable.php)（可调用）

### 数组 array

php 中的数组和 C 语言中的数组还有区别。它是一种 hash 的类型。通过 key=>value.通过数组可以实现丰富的数据类型，如字典、列表、集合、栈等。

定义数组

```php
$arr = array(1,2,3);
//简写 php5.4+
$arr2 = [1,2,3];
$arr2[1];
$arr3 = ["key"=>"value"];

$arr3["key"];
```

PHP 将自动使用之前用过的最大  INT 键名加上 1 作为新的键名.PHP 实际并不区分索引数组和关联数组。

### 对象 object

创建一个新的对象的时候，使用 new 关键字

```php
class obj {}
$a = new obj();
```

### 回调 callback

```php
function test(){
  echo "echo";
}
call_user_function('test');
```

## 两种特殊类型

- [resource](http://php.net/manual/zh/language.types.resource.php)（资源）
- [NULL](http://php.net/manual/zh/language.types.null.php)（无类型）

### 资源类型 resource

资源类型是保持外部的一个引用。如数据库的链接，文件的句柄等。

```php
$fp = fopen("./a.log");//resource
```

### NULL 类型

当一个变量没有被赋值，那么该变量的值就是 null。以下的情况是一个变量被认为是 null

- 被赋值成 null
- 未赋值
- 被 unset

```php
$a = null // null
$b;//var_dump($b); null
$c = 1;
unset($c);//var_dump($c); null
```

## 变量

php 中的变量是以 `$` 开头的。变量名区分大小写。合法的变量名是字母或者下划线开头，后面跟着任意数量的字母，数字，或者下划线

在此所说的字母是 a-z，A-Z，以及 ASCII 字符从 127 到 255（_0x7f-0xff_）

变量默认总是传值赋值

```php
$a $_a $张三 // 合法的
$2aaa //非法的
$a = 123;
````

### 变量的作用域

在最外层定义的是全局变量。在全局都有效。在函数内部的成为局部变量。只有函数内部可以访问。使用 static 修饰的变量，是静态变量。静态变量不会被销毁。只有等程序运行结束后才被回收.

**$this 是一个特殊的变量。不能定位成 this 变量**

```php
<?php
$a = 123;//全局
function f1(){
  $b = 234;//局部变量
}
echo $b;//未定义


function f2(){
  global $a;
  echo $a;
}
f2();// 123;

function s(){
  static $c = 1;
  $c++;
}

s();//2
s();//3

  ?>
```

确定变量的类型。php 提供了以下函数

```php
gettype() is_bool() is_string() is_object() is_array();
```

## 常量

常量一般是定义之后不能再更改的变量。传统上使用大写字母来定义常量.合法的常量命名跟变量一致。只是不需要加 `$` 符号。

```php
IS_DEBUG;
define("IS_DEBUG",0);
```

### 魔术常量

魔术常量是 php 内置的。可能跟着代码的变化而变化。一般魔术常量 以双下划线开始 双下划线结束。

```php
__LINE__
__DIR__
__FILE__
__CLASS__
```

