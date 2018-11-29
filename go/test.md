# 测试源码

名称以`_test.go`为后缀。其中至少有一个函数的名称以 Test 或 Benchmark 为前缀。该函数接受一个类型为
`*testing.T`或`*testing.B`的参数

```golang
func TestFind(t *testing.T){
    //省略若干条语句
    }
func BenchmarkFind(b *testing.B){
    //省略若干条语句
    }
```
