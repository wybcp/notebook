# 大小交替排列

有一组数，28、32、43、14、53、67、42、54、46、31 写程序排列这组数（要求：第一个是最大的，第二个是最小的，第三个是剩下中最大的，第四个是剩下最小的，第五个是剩下中最大的，第六个是剩下中最小的，依次向下排列。

```php
<?php
function getArray(array $data){

    rsort($data);        //对数组顺向排序
    $num = count($data);        //计算数组中的单元数目或对象中的属性个数
    echo $num.PHP_EOL;
    print_r($data);
    $result_data=[];
    // 奇数
    $is_odd = ($num%2===0)?false:true;

    if($num%2===0){
        $half_num=$num/2;
        for($i=0; $i<$half_num; $i++) {
            $result_data[$i*2] = $data[$i];//把最大的放在第一位
            $result_data[$i*2+1] = $data[$num-$i-1];//把最小的放在第二位上
        }
    }else{
         $half_num=($num-1)/2;
        for($i=0; $i<$half_num; $i++) {
            $result_data[$i*2] = $data[$i];;//把最大的放在第一位
            $result_data[$i*2+1] = $data[$num-$i-1];//把最小的放在第二位上
        }
        $result_data[$num-1]=$data[$half_num];
    }

    return $result_data;
}
$data= [28, 32, 43, 14, 53, 67, 42, 54, 46, 31];
print_r(getArray($data));
```
