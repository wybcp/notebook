# z数组

数值数组 for，关联数组 foreach

## 入门

从一些处理数组键名和键值的基础数组函数开始。

### [array_combine()](http://php.net/manual/zh/function.array-combine.php)

[array_combine()](http://php.net/manual/zh/function.array-combine.php) 用于通过使用一个数组的值作为其键名，另一个数组的值作为其值来创建一个全新数组：

```php
<?php
$keys = ['sky', 'grass', 'orange'];
$values = ['blue', 'green', 'orange'];

$array = array_combine($keys, $values);

print_r($array);
// Array
// (
//     [sky] => blue
//     [grass] => green
//     [orange] => orange
// )
```

### [array_values()](http://php.net/manual/zh/function.array-values.php)，[array_keys()](http://php.net/manual/zh/function.array-keys.php)，[array_flip()](http://php.net/manual/zh/function.array-flip.php)

- [array_values()](http://php.net/manual/zh/function.array-values.php) 函数会以索引数组形式返回数组中的值，
- [array_keys()](http://php.net/manual/zh/function.array-keys.php) 则会返回给定数组的键名，
- [array_flip()](http://php.net/manual/zh/function.array-flip.php) 交换数组中的键值和键名。

```php
<?php

print_r(array_keys($array));
// ['sky', 'grass', 'orange']

print_r(array_values($array));
// ['blue', 'green', 'orange']

print_r(array_flip($array));
// Array
// (
//     [blue] => sky
//     [green] => grass
//     [orange] => orange
// )
```

## 简化代码

### [list()](http://php.net/manual/zh/function.list.php)

`list()` 函数，确切的说它不是一个函数，而是一种语言结构，可以在单次操作中将数组中的值赋值给一组变量。

```php
<?php
// 定义数组
$array = ['a', 'b', 'c'];

// 不使用 list()
$a = $array[0];
$b = $array[1];
$c = $array[2];
// 使用 list() 函数
list($a, $b, $c) = $array;
```

这个语言结构结合 preg_split() 或 [explode()](http://php.net/manual/zh/function.explode.php) 这类函数使用效果更佳，如果你无需定义其中的某些值，可以直接跳过一些参数的赋值：

```php
$string = 'hello|wild|world';

list($hello, , $world) = explode('|', $string);
echo $hello, ' ', $world;
```

另外，`list()` 还可用于 `foreach` 遍历，这种用法更能发挥这个语言结构的优势：

```php
$arrays = [[1, 2], [3, 4], [5, 6]];

foreach ($arrays as list($a, $b)) {
    $c = $a + $b;

    echo 'c is ',$c, '.',PHP_EOL;
}
// c is 3.
// c is 7.
// c is 11.
```

    `list()` 语言结构仅适用于数字索引数组，并默认索引从 0 开始，且无法用于关联数组，查看[文档](http://php.net/manual/zh/function.list.php)。

### [extract()](http://php.net/manual/zh/function.extract.php)

通过使用 `extract()` 函数，你可以将关联数组导出到变量（符号表）中。对数组中的各个元素，将会以其键名作为变量名创建，变量的值则为对应元素的值：

```php
<?php
$array = [
    'clothes' => 't-shirt',
    'size' => 'medium',
    'color' => 'blue',
];

extract($array);

echo $clothes, ' ', $size, ' ', $color;
```

注意在处理用户数据（如请求的数据）时 `extract()` 函数是一个安全的函数，所以此时最好使用更好的 标志类型 如 `EXTR_IF_EXISTS` 和 `EXTR_PREFIX_ALL`。

### [compact()](http://php.net/manual/zh/function.compact.php)

`extract()` 函数的逆操作是 `compact()` 函数，用于通过变量名创建关联数组：

```php
<?php
$clothes = 't-shirt';
$size = 'medium';
$color = 'blue';

$array = compact('clothes', 'size', 'color');
print_r($array);

// Array
// (
//     [clothes] => t-shirt
//     [size] => medium
//     [color] => blue
// )
```

## 过滤函数

### [array_filter()](http://php.net/manual/zh/function.array-filter.php)

PHP 提供一个用于过滤数组的超赞的函数，它是 `array_filter()`。将待处理数组作为函数的第一个参数，第二个参数是一个匿名函数。如果你希望数组中的元素通过验证则在匿名函数返回 `true`，否则返回 `false`：

```php
<?php

$numbers = [20, -3, 50, -99, 55];

$positive = array_filter($numbers, function ($number) {
    return $number > 0;
});

print_r($positive);
// [0 => 20, 2 => 50, 4 => 55]
```

函数不仅支持通过值过滤。你还可以使用 `ARRAY_FILTER_USE_KEY` 或 `ARRAY_FILTER_USE_BOTH` 作为第三参数指定是否将数组的键值或将键值和键名同时作为回调函数的参数。

你还可以不在 `array_filter()` 函数中定义回调函数以删除空值：

```php
<?php
$numbers = [-1, 0, 1];

$not_empty = array_filter($numbers);

print_r($not_empty);// [0 => -1, 2 => 1]
```

### [array_unique()](http://php.net/manual/zh/function.array-unique.php)

你可以使用 `array_unique()` 函数用于从数组中获取唯一值元素。注意该函数会保留唯一元素在原数组中的键名：

```php
<?php
$array = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5];

$uniques = array_unique($array);

print_r($uniques);
// Array
// (
//     [0] => 1
//     [4] => 2
//     [7] => 3
//     [8] => 4
//     [9] => 5
// )
```

### [array_column()](http://php.net/manual/en/function.array-column.php)

`array_column()` 函数可以从多维数组（multi-dimensional）中获取指定列的值，如从 SQL 数据库中获取答案或者 CSV 文件导入数据。只需要传入数组和指定的列名：

```php
<?php
$array = [
    ['id' => 1, 'title' => 'tree'],
    ['id' => 2, 'title' => 'sun'],
    ['id' => 3, 'title' => 'cloud'],
];

$ids = array_column($array, 'id');

print_r($ids);
// [1, 2, 3]
```

从 PHP 7 开始，`array_column` 功能更加强大，因为它开始支持包含对象的数组，所以在处理数组模型时变得更加容易：

```php
<?php
$cinemas = Cinema::find()->all();
$cinema_ids = array_column($cinemas, 'id');
```

## 数组遍历处理

### [array_map()](http://php.net/manual/zh/function.array-map.php)

通过使用 `array_map()`，你可以对数组中的每个元素执行回调方法。你可以基于给定的数组传入函数名称或匿名函数来获取一个新数组：

```php
<?php
$cities = ['Berlin', 'KYIV', 'Amsterdam', 'Riga'];
$aliases = array_map('strtolower', $cities);

print_r($aliases);
// ['berlin', 'kyiv, 'amsterdam', 'riga']

$numbers = [1, -2, 3, -4, 5];
$squares = array_map(function ($number) {
    return $number ** 2;
}, $numbers);

print_r($squares);
// [1, 4, 9, 16, 25]
```

对于这个函数还有个谣言，无法同时将数组的键名和键值传入到回调函数，但是我们现在要来打破它：

```php
<?php
$model = ['id' => 7, 'name' => 'James'];
$res = array_map(function ($key, $value) {
    return $key . ' is ' . $value;
}, array_keys($model), $model);

print_r($res);
// Array
// (
//     [0] => id is 7
//     [1] => name is James
// )
```

### [array_walk()](http://php.net/manual/zh/function.array-walk.php)

不过这样处理起来实在是丑陋。最好使用 `array_walk()` 函数来替代。这个函数表现上和 `array_map()` 类似，但是工作原理完全不同。第一，数组是以引用传值方式传入，所以 `array_walk()` 不会创建新数组，而是直接修改原数组。所以作为源数组，你可以将数组的值以引用传递方法传入回调函数，数组的键名直接传入就好了：

```php
<?php
$fruits = [
    'banana' => 'yellow',
    'apple' => 'green',
    'orange' => 'orange',
];

array_walk($fruits, function (&$value, $key) {
    $value = $key . ' is ' . $value;
});

print_r($fruits);
//Array
//(
//    [banana] => banana is yellow
//    [apple] => apple is green
//    [orange] => orange is orange
//)
```

## 数组连接操作

### [array_merge()](http://php.net/manual/zh/function.array-merge.php)

在 PHP 中合并数组的最佳方式是使用 `array_merge()` 函数。所有的数组选项会合并到一个数组中，具有相同键名的值会被最后一个值所覆盖；数组使用数字键名，键名相同不会覆盖，且键名会重新索引：

```php
<?php
$array1 = ['a' => 'a', 'b' => 'b', 'c' => 'c'];
$array2 = ['a' => 'A', 'b' => 'B', 'D' => 'D'];

$merge = array_merge($array1, $array2);
print_r($merge);
// Array
// (
//     [a] => A
//     [b] => B
//     [c] => c
//     [D] => D
// )
```

译注：有关合并数组操作还有一个「+」号运算符，它和 `array_merge()` 函数的功能类似都可以完成合并数组运算，但是结果有所不同，可以查看 PHP 合并数组运算符 + 与 array_merge 函数。

使用 “+” 运算符合并数组，可以保留数组的键值，如果合并的数组中含有相同的键值，后面的不会覆盖前面的键值（前面的优先）。

### [array_diff()](http://php.net/manual/zh/function.array-diff.php)

为了实现从数组中删除不在其他数组中的值（译注：计算差值），使用 array_diff()。还可以通过 `array_intersect()` 函数获取所有数组都存在的值（译注：获取交集）。接下来的示例演示它们的使用方法：

```php
<?php
$array1 = [1, 2, 3, 4];
$array2 = [3, 4, 5, 6];

$diff = array_diff($array1, $array2);
$intersect = array_intersect($array1, $array2);

print_r($diff); // 差集 [0 => 1, 1 => 2]
print_r($intersect); //交集 [2 => 3, 3 => 4]
```

## 数组的数学运算

### [array_sum()](http://php.net/manual/zh/function.array-sum.php)

- `array_sum()` 对数组元素进行求和运算，
- `array_product()` 对数组元素执行乘积运算，
- `array_reduce()` 处理自定义运算规则：

```php
<?php

$numbers = [1, 2, 3, 4, 5];

print_r(array_sum($numbers));// 15

print_r(array_product($numbers));// 120

print_r(array_reduce($numbers, function ($carry, $item) {
    return $$carry ? $carry / $item : 1;
}));// 0.0083 = 1/2/3/4/5
```

### [array_count_values()](http://php.net/manual/zh/function.array-count-values.php)

为了实现统计数组中值的出现次数，可以使用 `array_count_values()` 函数。它将返回一个新数组，新数组键名为待统计数组的值，新数组的值为待统计数组值的出现次数：

```php
<?php

$things = ['apple', 'apple', 'banana', 'tree', 'tree', 'tree'];
$values = array_count_values($things);

print_r($values);

// Array
// (
//     [apple] => 2
//     [banana] => 1
//     [tree] => 3
// )
```

## 生成数组

### [array_fill()](http://php.net/manual/zh/function.array-fill.php#115216)

需要以给定值生成固定长度的数组，可以使用 array_fill() 函数：

```php
<?php
$bind = array_fill(0, 5, '?');
print_r($bind);
/*
Array
(
    [0] => ?
    [1] => ?
    [2] => ?
    [3] => ?
    [4] => ?
)
*/
```

### [range()](http://php.net/manual/zh/function.range.php)

根据范围创建数组，如小时或字母，可以使用 range() 函数：

```php
<?php
$letters = range('a', 'z');
print_r($letters); // ['a', 'b', ..., 'z']

$hours = range(0, 23);
print_r($hours); // [0, 1, 2, ..., 23]
```

### [array_slice()](http://php.net/manual/zh/function.array-slice.php)

`array array_slice ( array $array , int $offset [, int $length = **NULL** [, bool $preserve_keys= false ]] )`

为了实现获取数组中的部分元素 - 比如，获取前三个元素 - 使用 array_slice() 函数:

```php
<?php
$numbers = range(1, 10);
$top = array_slice($numbers, 0, 3);

print_r($top);// [1, 2, 3]
```

## 排序数组

首先谨记 PHP 中有关排序的函数都是 引用传值 的，排序成功返回 true 排序失败返回 false。排序的基础函数是 `sort()` 函数，它执行排序后的结果不会保留原索引顺序。排序函数可以归类为以下几类：

- a 保持索引关系进行排序
- k 依据键名排序
- r 对数组进行逆向排序
- u 使用用户自定义排序规则排序

你可以从下表看到这些排序函数：

| a      | k      | r     | u     |
| ------ | ------ | ----- | ----- |
| asort  |        | asort | asort |
| ksort  | krsort |
| arsort | krsort | rsort |
| uasort |        |       | usort |

### 二维数组排序

```php
<?php
function arraySortByAnyRow($array_name, $row_id, $order_type){
    $array_temp=[];
    foreach($array_name as $key=>$value){
        $array_temp[$key]=$value[$row_id];
    }
    if($order_type==="ASC"){ //顺序
        asort($array_temp);
    } else {
        arsort($array_temp);
    }
    $result_array=[];
    foreach($array_temp as $key=>$value){
        $result_array[$key]=$array_name[$key];
    }

    return $result_array;
}

$arr = [
    ['num'=>5, 'value'=>6],
    ['num'=>2, 'value'=>39],
    ['num'=>36, 'value'=>29]
];

$sort_arr = arraySortByAnyRow($arr, 'num', 'DESC');
print_r($sort_arr);
```

## 数组函数的组合使用

数组处理的艺术是组合使用这些数组函数。这里我们通过 `array_filter()` 和 `array_map()`函数仅需一行代码就可以完成空字符截取和去控制处理：

```php
<?php
$values = ['say', '  bye', '', ' to', ' spaces  ', '    '];
$words = array_filter(array_map('trim', $values));

print_r($words);// ['say', 'bye', 'to', 'spaces']
```

依据模型数组创建 id 和 title 数据字典，我们可以结合使用 array_combine() 和 array_column() 函数：

```php
<?php
$models = [$model, $model, $model];

$id_to_title = array_combine(
    array_column($models, 'id'),
    array_column($models, 'title')
);

print_r($id_to_title);
```

译注：提供一个 可运行的版本。

为了实现获取出现频率最高的数组元素，我们可以使用 `array_count_values()`、`arsort()` 和 `array_slice()` 这几个函数：

```php
<?php

$letters = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd'];

$values = array_count_values($letters);
arsort($values);
$top = array_slice($values, 0, 3);

print_r($top);
```

还可以轻易的通过 `array_sum()` 和 `array_map()` 函数仅需数行就能完成计算订单的价格：

```php
<?php
$order = [
    ['product_id' => 1, 'price' => 99, 'count' => 1],
    ['product_id' => 2, 'price' => 50, 'count' => 2],
    ['product_id' => 2, 'price' => 17, 'count' => 3],
];

$sum = array_sum(array_map(function ($product_row) {
    return $product_row['price'] * $product_row['count'];
}, $order));

print_r($sum);// 250
```

## 例子

```php
<?php
/*
*
* 拆分、合并、分解、接合的数组函数
*    1.array_slice()
*    2.array_splice()//删除
*    3.array_combine()//合并
*    4.array_merge();//合并
 *    5.array_intersect();//多个数组的交集
 *    6.array_diff();//返回多个数组的差集
*/

//拆分、合并、分解、接合的数组函数

$data_6 = array("Linux", "Apache", "MySQL", "PHP");
print_r(array_slice($data_6, 1, 2));//取下标为1、2的元素
//Array ( [0] => Apache [1] => MySQL ) 下标重置从0开始
print_r(array_slice($data_6, -2, 1));//从后边的第二个开始取返回一个，不是从0开始的
//Array ( [0] => MySQL ) 下标重置从0开始
print_r(array_slice($data_6, 1, 2, true));
//Array ( [1] => Apache [2] => MySQL )  保留原有的下标

//array_combine()
$a1 = array("OS", "WebServer", "DataBase", "Language");
$a2 = array("Linux", "Apache", "MySQL", "PHP");
print_r(array_combine($a1, $a2));//第一个参数作为键名，第二个作为值来合并
//Array ( [OS] => Linux [WebServer] => Apache [DataBase] => MySQL [Language] => PHP )

//array_merge()
$a3 = array("OS", "WebServer", "DataBase", "Language");
$a4 = array("Linux", "Apache", "MySQL", "PHP");
$a5 = $a3 + $a4;
print_r($a5);//因为两个数组下标重复所以显示这样
//Array ( [0] => OS [1] => WebServer [2] => DataBase [3] => Language )
print_r(array_merge($a3, $a4));//合并并重新索引
//Array ( [0] => OS [1] => WebServer [2] => DataBase [3] => Language [4] => Linux [5] => Apache [6] => MySQL [7] => PHP )

//array_intersect()
$a7 = array("OS", "WebServer", "DataBase", "Language", 1, 2, 3);
$a8 = array("Linux", "Apache", "MySQL", "PHP", 2, 3, 4);
print_r(array_intersect($a7, $a8));//Array ( [5] => 2 [6] => 3 )

//array_diff()
$a9 = array(1, 2, 3, 4);
$a10 = array(3, 4, 5, 6);
print_r(array_diff($a9, $a10));//Array ( [0] => 1 [1] => 2 )
//返回第一个数组跟第二个相差的元素

/*
 *  数组与数据结构的函数
*   1.使用数组实现堆栈 //先进后出
*    array_push() array_pop()
*   2.使用数组实现队列 //先进先出
*    array_unshift() array_shift() unset()
 *
 */
//使用数组实现堆栈
$b = array(1, 2, 3, 4);
$b[] = "a";//入栈
//在数组的尾部添加数组元素array_push($arr,$v,$v1...)
array_push($b, "b", "c");//使用函数入栈
print_r($b);//Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => a [5] => b [6] => c )
//在数组的尾部删除元素array_pop($arr)
$value = array_pop($b);//使用函数出栈
print_r($b);//Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => a [5] => b )
echo $value . PHP_EOL;//显示出栈的元素的值 c

//使用数组实现队列
//在数组的开头插入一个元素array_unshift($arr,$v)
$c = array(1, 2, 3);
print_r($c);//Array ( [0] => 1 [1] => 2 [2] => 3 )
array_unshift($c, "abc", "bcd");//入队
print_r($c);//Array ( [0] => abc [1] => bcd [2] => 1 [3] => 2 [4] => 3 )
//将数组的第一个元素移出，并返回此元素array_shift($arr)
$values = array_shift($c);//出队
print_r($c);// Array ( [0] => bcd [1] => 1 [2] => 2 [3] => 3 )

unset($c[2]);//删除指定位置元素
print_r($c);//Array ( [0] => bcd [1] => 1 [3] => 3 )

/*
 * 其他与数组操作有关的函数
*    array_rand()
*    shuffle()
*    array_sum()
*    range()
 */
//array_rand()  随机返回数组下标
$arr = array(1, 3, 4, 5, 76, 7, 99, 6, 2, 3);
echo array_rand($arr) . PHP_EOL;//返回的是随机的数组元素的下标
echo $arr[array_rand($arr)];//随机显示数组元素的值

//shuffle()  随机重新排列数组
$arr2 = array(32, 35, 33);
shuffle($arr2);
print_r($arr2);//数组元素位置随机变换

//array_sum()  求和
$arr3 = array(1, 3, 5);
echo array_sum($arr3) . PHP_EOL; //返回9
print_r($arr3);//Array ( [0] => 1 [1] => 3 [2] => 5 )

//range(最小值，最大值，步长)
$arr4 = range(0, 100, 10);
print_r($arr4);//Array ( [0] => 0 [1] => 10 [2] => 20 [3] => 30 [4] => 40 [5] => 50 [6] => 60 [7] => 70 [8] => 80 [9] => 90 [10] => 100 )
//将数组用$separator连接成一个字符串implode($a,$arr)
print_r(implode('-', $arr4));
//检测变量是否是数组is_array($arr)
echo PHP_EOL;
print_r(is_array($arr4));
//检索$value是否在$arr中，返回布尔值in_array($v,$arr)
echo PHP_EOL;
print_r(in_array(10, $arr4));
//获得数组的键名array_keys($arr)
echo PHP_EOL;
print_r(array_keys($arr4));
//获得数组的值array_values($arr)
echo PHP_EOL;
print_r(array_values($arr4));
//检索数组$arr中，是否有$key这个键名array_key_exists($k,$arr)
echo PHP_EOL;
var_dump(array_key_exists(16, $arr4));
//检索$value是否在$arr中，若存在返回键名Array_search($value, $arr)
var_dump(array_search(20, $arr4));
//将一个数组逆向排序，如果第二个参数为true，则保持键名Array_reverse($arr, true)
var_dump(array_reverse($arr4));
var_dump(array_reverse($arr4, true));
//交换数组的键和值 Array_flip($arr)
var_dump(array_flip($arr4));
//统计数组元素的个数 Count($arr)
var_dump(count($arr4));
//统计数组中所有值的出现次数 Array_count_values($arr)
array_unshift($arr4, 10);
var_dump(array_count_values($arr4));
//移除数组中的重复值 Array_unique($arr)
var_dump(array_unique($arr4));
```



## 参考

- [PHP 数组使用之道](http://blog.phpzendo.com/?p=389) 译文
- [Working With PHP Arrays in the Right Way](https://code.tutsplus.com/tutorials/working-with-php-arrays-in-the-right-way--cms-28606) 原文
