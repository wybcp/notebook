# [HTMLPurifier](http://htmlpurifier.org/)

运用『白名单机制』对 HTML 文本信息进行 XSS 过滤。

这里的『白名单机制』指的是，使用配置信息来定义『HTML 标签』、『标签属性』和『CSS 属性』数组，在执行 `clean()` 方法时，只允许配置信息『白名单』里出现的元素通过，其他都进行过滤。

如配置信息：

```php
'HTML.Allowed' => 'div,em,a[href|title|style],ul,ol,li,p[style],br',
'CSS.AllowedProperties'    => 'font,font-size,font-weight,font-style,font-family',
```

用户提交：

```html
<a someproperty="somevalue" href="http://example.com" style="color:#ccc;font-size:16px">
    文章内容<script>alert('Alerted')</script>
</a>
```

会被解析为：

```html
<a href="http://example.com" style="font-size:16px">
    文章内容
</a>
```

以下内容因为未指定会被过滤：

1. `someproperty` 未指定的 HTML 属性
2. `color` 未指定的 CSS 属性
3. `script` 未指定的 HTML 标签

## 参考

- [使用 HTMLPurifier 来解决 Laravel 5 中的 XSS 跨站脚本攻击安全问题](https://laravel-china.org/articles/4798/the-use-of-htmlpurifier-to-solve-the-xss-xss-attacks-of-security-problems-in-laravel)