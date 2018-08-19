# 执行外部程序

使用 ` 反引号操作符 （backlist，位于 esc 键下方的上档键）来运行外部系统的命令和应用程序。

例如：

```php
$out=`ls -al`;
echo $out;
```

或者使用 `shell_exec()`通过 shell 环境执行命令，并且将完整的输出以字符串的方式返回:

```php
$out=shell_exec('ls -al');
echo $out;
```
