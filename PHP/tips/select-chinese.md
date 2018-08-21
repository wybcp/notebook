# 提取中文

```php
$str='skldjfa232方式打开sdag56';
preg_match_all('/[\x{4e00}-\x{9fff}]+/u',$str,$matches);
$str=join('',$matches[0]);
echo $str;
```
