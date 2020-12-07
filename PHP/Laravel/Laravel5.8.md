# [Laravel5.8代码中Get到的小彩蛋](https://mp.weixin.qq.com/s/AMERQbU1qkEixCQsYEq8aQ)

1、获取关联数组中指定部分键值组成的数组

项目中常常有这么一种场景，一些数据的生成需要一些其他的数据获得，但是返回给用户的不需要原始数据。比如对于一个用户数据如下:

```php
{
    "userid":10,
    "username":"abc",
    "type":1,
    "status":1,
    "system_code":"xtfy",
    "system_uid":1,
    "file_id":1
}
```

如果我最终想要返回给用户的结果如下

```php
{
    "userid":10,
    "username":"abc",
    "type":1,
    "status":1
}
```

这种情况就需要获取数组中指定的部分内容。实现方式有一下几种方式：

- unset不需要的数据字段
- 重新创建一个变量，然后一个个字段的添加到新数组中去

在Laravel5.8中Support\Arr中有一个only方法,使用php原生数组函数的键名交集，返回指定键数组的内容。实现方式如下:

```php
array_intersect_key(
 $array,
 array_flip((array) $keys)
);
```

根据这个思路，获取指定键之外的数组可以用下面的方式实现:

```php
array_diff_key(
 $array,
 array_flip((array) $keys)
)
```

2、如何判断关联数组

首先明白关联数组是什么。下面这样是关联数组

```php
$a = [3=>1,4=>'a'];
$b=['a'=>1,'b'=>2];
```

而以下内容则不是

```php
$a = [1,2,3];
$b = [0=>1,1=>2,2=>3];
```

如何判断一个数组是不是关联数组呢?之前的做法都是判断键是否都是数字，其实是不准确的。

在Laravel5.8中有一个isAssoc方法。实现方式如下:

```php
$keys = array_keys($array);

return array_keys($keys) !== $keys;
```

简单而言，如果数组key的key还是一样的，则不是关联数组。
