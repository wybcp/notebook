# [魔术变量](http://www.phpxs.com/j/php/1000051/)

PHP 向它运行的任何脚本提供了大量的预定义常量。

不过很多常量都是由不同的扩展库定义的，只有在加载了这些扩展库时才会出现，或者动态加载后，或者在编译时已经包括进去了。

有八个魔术常量它们的值随着它们在代码中的位置改变而改变。

## `__LINE__`

文件中的当前行号。

## `__FILE__`

文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。

实例:

```php
<?php
echo '该文件位于 “ '  . __FILE__ . ' ” ';
```

以上实例输出结果为：`该文件位于 “ E:\wamp\www\test\index.php ”`

## `__DIR__`

文件所在的目录。如果用在被包括文件中，则返回被包括的文件所在的目录。
它等价于 dirname(**FILE**)。除非是根目录，否则目录中名不包括末尾的斜杠。

## `__FUNCTION__`

自 PHP 5 起本常量返回该函数被定义时的名字（区分大小写）。

## `__CLASS__`

自 PHP 5 起本常量返回该类被定义时的名字（区分大小写）。

## `__TRAIT__`

自 PHP 5.4.0 起，PHP 实现了代码复用的一个方法，称为 traits。
Trait 名包括其被声明的作用区域（例如 Foo\Bar）。
从基类继承的成员被插入的 SayWorld Trait 中的 MyHelloWorld 方法所覆盖。其行为 MyHelloWorld 类中定义的方法一致。
优先顺序是当前类中的方法会覆盖 trait 方法，而 trait 方法又覆盖了基类中的方法。

```php
<?php
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}

trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}

class MyHelloWorld extends Base {
    use SayWorld;
}

$o = new MyHelloWorld();
$o->sayHello();
```

以上例程会输出：
`Hello World!`

## `__METHOD__`

类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）。
实例:

```php
<?php
function test() {
    echo  '函数名为：' . __METHOD__ ;
}
test();
```

以上实例输出结果为：
函数名为：test

## `__NAMESPACE__`

当前命名空间的名称（区分大小写）。此常量是在编译时定义的（PHP 5.3.0 新增）。
实例:

```php
<?php
namespace MyProject;

echo '命名空间为："', __NAMESPACE__, '"'; // 输出 "MyProject"
```

以上实例输出结果为：

`命名空间为："MyProject"`
