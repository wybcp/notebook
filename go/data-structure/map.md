# 

# 哈希表

键值对，工作方式就是：定义键和值，并且可以获取，设置和删除其中的值。

`for` 组合 `range` 关键字迭代映射：

```go
for key, value := range lookup {
  ...
}
```

迭代映射是没有顺序的。每次迭代查找将会随机返回键值对。

map中所有的key都有相同的类型，所有的value也有着相同的类型，但是key和value之间可以是不同的数据类型。

内置的make函数可以创建一个map：

```Go
ages := make(map[string]int) // mapping from strings to ints
```

另一种创建空的map的表达式是`map[string]int{}`



禁止对map元素取址的原因是map可能随着元素数量的增长而重新分配更大的内存空间，从而可能导致之前的地址无效。

## key 不存在

如果key在map中是存在的，那么将得到与key对应的value；如果key不存在，那么将得到value对应类型的零值。

这个规则很实用，但是有时候可能需要知道对应的元素是否真的是在map之中。例如，如果元素类型是一个数字，你可能需要区分一个已经存在的0，和不存在而返回零值的0，可以像下面这样测试：

```Go
age, ok := ages["bob"]
if !ok { /* "bob" is not a key in this map; age == 0. */ }
```

你会经常看到将这两个结合起来使用，像这样：

```Go
if age, ok := ages["bob"]; !ok { /* ... */ }
```

在这种场景下，map的下标语法将产生两个值；第二个是一个布尔值，用于报告元素是否真的存在。布尔变量一般命名为ok，特别适合马上用于if条件判断部分。

## 顺序遍历map

如果要按顺序遍历key/value对，必须显式地对key进行排序，可以使用sort包的Strings函数对字符串slice进行排序。下面是常见的处理方式：

```Go
import "sort"

var names []string
for name := range ages {
    names = append(names, name)
}
sort.Strings(names)
for _, name := range names {
    fmt.Printf("%s\t%d\n", name, ages[name])
}
```

## 相等值判断

要判断两个map是否包含相同的key和value，我们必须通过一个循环实现：

```Go
func equal(x, y map[string]int) bool {
    if len(x) != len(y) {
        return false
    }
    for k, xv := range x {
        if yv, ok := y[k]; !ok || yv != xv {
            return false
        }
    }
    return true
}
```

