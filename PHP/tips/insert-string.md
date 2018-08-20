# 在字符串指定位置插入一段字符串

```php
<?php
//插入一段字符串
/*
 * @param string $str    # 待处理字符串
 * @param int    $i      # 插入位置
 * @param string $substr # 需要插入的字符串
 */
function strInsert($str, $i, $substr)
{
//    for($j=0; $j<$i; $j++){
//        $start_str .= $str[$j];
//    }
//    for ($j=$i; $j<strlen($str); $j++){
//        $last_str .= $str[$j];
//    }
    $start_str = mb_substr($str, 0, $i);
    $last_str = mb_substr($str, $i);
    return $start_str . $substr . $last_str;
}

var_dump(strInsert('hello china!', 5, ' cd'));
```
