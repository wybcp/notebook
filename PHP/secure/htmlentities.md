# 转义输出

将输出渲染成网页或 API，一定要转义输出。

```php
htmlentities($output, ENT_QUOTES, 'UTF-8');
```

三个参数

- 输出字符串
- ENT_QUOTES 常数，转义单引号
- 输出字符串的字符集
