# 函数

有效的函数名以字母或下划线打头，后面跟字母，数字或下划线。

函数名是大小写无关的。

```php
function 函数名字(参数){
  //函数体
}
```

## 函数参数

可以通过参数传递外部的信息到函数内部。

```php
$a = 100;
function fn($arg) {
echo $arg;
}
fn($a);//100
```

- 引用传值
    ```php
    function fn(&$arg){
    $arg = 10;
    }
    fn($a);
    echo $a;//10;
    ```
- 默认参数
    ```php
    # 默认值
    $a = 100;
    function fn($arg = 10){
    echo $arg;
    }
    fn($a);//100
    fn();//10
    ```
- 可变参数

    PHP 在用户自定义函数中支持可变数量的参数列表。在 PHP 5.6 及以上的版本中，由  *...*  语法实现

    ```php
    function fn(...$arg){
    foreach($arg as $v){
        echo $v;
    }
    }
    fn(1,2,3,4);
    ```

## 函数类型声明

类型声明允许函数在调用时要求参数为特定类型。 如果给出的值类型不对，那么将会产生一个错误

目前支持的类型有类名、接口名、self、array、callable、bool、int、float、string

```php
function fn(int $a){
  echo $a;
}
$c = "hello";
fn($c);//error
```

### 严格类型

```php
declare(strict_types=1);
function fn(int $a){
  echo $a;
}
$c = '1';//string
fn($c);//
```

### 返回值类型

可以限制返回值的类型

```php
declare(strict_types=1);
function($a):float {
  return 1.1;
}
```

## 可变函数

PHP 支持可变函数的概念。这意味着如果一个变量名后有圆括号，PHP 将寻找与变量的值同名的函数，并且尝试执行它。可变函数可以用来实现包括回调函数

```php
function f(){
  echo "1";
}
$a = 'f';

$a();//1
```

### 匿名函数

匿名函数（Anonymous functions），也叫闭包函数（_closures_），允许 临时创建一个没有指定名称的函数。最经常用作回调函数 参数的值。当然，也有其它应用的情况。

闭包可以从父作用域中继承变量。 任何此类变量都应该用  *use*  语言结构传递进去

```php
(function (){
  echo '匿名函数';
})();

#传递参数

$a = function ($arg) {
 echo $arg;
}
$arg = 'hello';

$a($arg);//hello;

# 传递外部作用域变量
$arg = 'arg';
$f = function() use($arg){
  echo $arg;
}
$f();
```

## 目录

- [文件](file.md)
- [数组](array.md)
- [字符串](string.md)
- [魔术方法](magic-function.md)
- [执行外部程序](shell-exec.md)
