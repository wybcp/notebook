# 超级全局变量
http://www.runoob.com/php/php-superglobals.html

超级全局变量在PHP 4.1.0之后被启用, 是PHP系统中自带的变量，在一个脚本的全部作用域中都可用。


##$GLOBALS
$GLOBALS 是一个包含了全部变量的全局组合数组。变量的名字就是数组的键。

```
<?php 
$x = 75; 
$y = 25;
 
function addition() 
{ 
$GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y']; 
}
 
addition(); 
echo $z; 
?>
```

##$_SERVER
$_SERVER 是一个包含了诸如头信息(header)、路径(path)、以及脚本位置(script locations)等等信息的数组。这个数组中的项目由 Web 服务器创建。不能保证每个服务器都提供全部项目；服务器可能会忽略一些，或者提供一些没有在这里列举出来的项目。

##$_REQUEST

PHP $_REQUEST 用于收集HTML表单提交的数据。

##$_POST
PHP $_POST 被广泛应用于收集表单数据，在HTML form标签的指定该属性："method="post"。

##$_GET

PHP $_GET 同样被广泛应用于收集表单数据，在HTML form标签的指定该属性："method="get"。
$_GET 也可以收集URL中发送的数据。