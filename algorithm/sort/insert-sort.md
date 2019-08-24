# 插入排序

```php
<?php
$data = [1, 43, 54, 62, 21, 66, 32, 78, 36, 76, 39];
function insertSort($data)
{
    $len = count($data);
    //区分 哪部分是已经排序好的
    //哪部分是没有排序的
    //找到其中一个需要排序的元素
    //这个元素 就是从第二个元素开始，到最后一个元素都是这个需要排序的元素
    //利用循环就可以标志出来
    //i循环控制 每次需要插入的元素，一旦需要插入的元素控制好了，
    //间接已经将数组分成了2部分，下标小于当前的（左边的），是排序好的序列
    for ($i = 1; $i < $len; $i++) {
        //获得当前需要比较的元素值。
        $tmp = $data[$i];
        //内层循环控制 比较并插入
        for ($j = $i - 1; $j >= 0; $j--) {
            //$arr[$i];需要插入的元素; $arr[$j];//需要比较的元素
            if ($tmp < $data[$j]) {
                //发现插入的元素要小，交换位置
                //将后边的元素与前面的元素互换
                $data[$j + 1] = $data[$j];
                //将前面的数设置为 当前需要交换的数
                $data[$j] = $tmp;
            } else {
                //如果碰到不需要移动的元素
                //由于是已经排序好是数组，则前面的就不需要再次比较了。
                break;
            }
        }
    }
    //将这个元素 插入到已经排序好的序列内。
    return $data;
}
```

## go

```go
package main

import "fmt"

func main() {
	numbers := []int{6, 2, 7, 3, 8, 5}

	//insertIncSort(numbers)
	insertDecSort2(numbers)

}

//插入排序

func insertIncSort(s []int) {
	for j := 1; j < len(s); j++ {
		key := s[j]
		i := j - 1
		for i >= 0 && s[i] > key {
			s[i+1] = s[i]
			i--
		}
		s[i+1] = key
	}
	fmt.Println(s)
}
func insertDecSort2(s []int) {
	for j := 1; j < len(s); j++ {
		key := s[j]
		i := j - 1
		for i >= 0 && s[i] < key {
			s[i+1] = s[i]
			i--
		}
		s[i+1] = key
	}
	fmt.Println(s)
}
```
