# 冒泡算法

## PHP

```php
<?php
/**
 *  思路分析：就是像冒泡一样，每次从数组当中冒一个最大的数出来。
 *  比如：2,4,1    // 第一次 冒出的泡是4
 *        2,1,4    // 第二次 冒出的泡是 2
 *        1,2,4    // 最后就变成这样
 */
$data = [1, 43, 54, 62, 21, 66, 32, 78, 36, 76, 39];
function bubble($data)
{
    $len = count($data);
    //设置一个空数组 用来接收冒出来的泡
    //该层循环控制 需要冒泡的轮数
    for ($i = 1; $i < $len; $i++) { //该层循环用来控制每轮 冒出一个数 需要比较的次数
        for ($k = 0; $k < $len - $i; $k++) {
            if ($data[$k] > $data[$k + 1]) {
                $tmp = $data[$k + 1];
                $data[$k + 1] = $data[$k];
                $data[$k] = $tmp;
            }
        }
    }
    return $data;
}

var_dump(bubble($data));
```

## go

```go
package main

import "fmt"

func main() {
	values := []int{4, 93, 84, 85, 80, 37, 81, 93, 27,12}
	fmt.Println(values)
	BubbleIncSort(values)
	BubbleDecSort(values)
}

func BubbleIncSort(values []int) {
	for i := 0; i < len(values)-1; i++ {
		for j := i+1; j < len(values); j++ {
			if  values[i]>values[j]{
				values[i],values[j] = values[j],values[i]
			}
		}
	}
	fmt.Println(values)
}

func BubbleDecSort(values []int) {
	for i := 0; i < len(values)-1; i++ {
		for j := i+1; j < len(values); j++ {
			if  values[i]<values[j]{
				values[i],values[j] = values[j],values[i]
			}
		}
	}
	fmt.Println(values)
}
```
