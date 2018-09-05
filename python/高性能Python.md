运行环境：python3.6.4

## 合理使用内置数据类型


```
test_range = range(10000)
test_set = set(test_range)


def func_2(n, data):
    return n in data
```
IPython环境运行：

```
%timeit func_2(100,test_range)
# 213 ns ± 10.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

```
%timeit func_2(100,test_set)
# 137 ns ± 0.654 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```
## 列表迭代 vs for循环


```
test_range = range(10000)

def func_3(data):
    result = []
    for i in data:
        if i % 2 == 0:
            result.append(i)
    return result


def func_4(data):
    return [i for i in data if i % 2 == 0]
```
IPython环境运行：
```
%timeit func_3(test_range)
# 1.05 ms ± 10.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit func_4(test_range)
# 744 µs ± 2.44 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
列表迭代接近map循环速度。
## 函数调用开销

```
def func_5(x):
    return x * 2


def func_6():
    for i in test_range:
        v = func_5(i)


def func_7():
    for i in test_range:
        v = i * 2
```
IPython环境运行：
```
%timeit func_6()
#1.43 ms ± 23.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit func_7()
#613 µs ± 4.92 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
在很大的循环中，尽量使用inline
## 充分利用内建优秀模块

例如：`deque/collections/bisect`

```
from collections import deque


def func_8():
    test_list = deque()
    for i in range(10000):
        test_list.appendleft(i)


def func_9():
    test_list = []
    for i in range(10000):
        test_list.insert(0, i)
```
IPython环境运行：
```
%timeit func_8()
# 987 µs ± 30.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit func_9()
# 35 ms ± 155 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```
