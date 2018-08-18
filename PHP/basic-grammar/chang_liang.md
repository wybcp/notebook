# 常量

常量是一个简单值的标识符，被定义后，在脚本的其他任何地方都不能被改变。
(常量名不需要加 $ 修饰符)。
注意： 常量在整个脚本中都可以使用。

设置常量语法：
```
define ( string $name , mixed $value [, bool $case_insensitive = false ] )
```

+ name：必选参数，常量名称，即标志符。
+ value：必选参数，常量的值。
+ case_insensitive ：可选参数，如果设置为 TRUE，该常量则大小写不敏感。默认是大小写敏感的。

sample：

```
<?php
// 不区分大小写的常量名
define("GREETING", "欢迎来到重庆", true);
echo greeting;  // 输出 "欢迎欢迎来到重庆"
?>
```

defined()函数判断一个常量是否已经定义，其语法格式为：

`bool defined(string constants_name)`

参数constant_name，指的是要获取常量的名称，若存在则返回布尔类型true，否则返回布尔类型false; 
