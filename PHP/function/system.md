# 系统相关函数

## 定义变量列表 get_defined_vars()

该函数返回一个包含所有已定义变量列表的多维数组，这些变量包括环境变量、服务器变量和用户定义的变量。

```php
print_r(get_defined_vars());
```

## 代码语法高亮

当需要在一个网站中展示 PHP 代码时，highlight_string()函数就变的非常有用了。该函数通过使用 PHP 语法高亮程序中定义的颜色，输出或返回给定的 PHP 代码的语法高亮版本。

```php
highlight_string('<?php phpinfo(); ?>');
```
