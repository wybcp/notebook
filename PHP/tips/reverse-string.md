# 翻转字符串

翻转字符串中的单词，字符串仅包含大小写字母和空格，单词间使用空格分隔。

```php
<?php
function reverseString($str){
    $arr = explode(' ',$str);
    $num = count($arr);
    for($i = 0; $i < $num/2; $i++){
        $temp = $arr[$i];
        $arr[$i] = $arr[$num-$i-1];
        $arr[$num-$i-1] = $temp;
    }
    return implode(' ',$arr);
}
$str = 'This is PHP i yi';
echo reverseString($str);
```
