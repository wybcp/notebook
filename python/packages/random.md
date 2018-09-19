# `random`

`random` 模块有大量的函数用来产生随机数和随机选择元素。 比如，要想从一个序列中随机的抽取一个元素，可以使用 `random.choice()` ：

```bash
>>> import random
>>> values = [1, 2, 3, 4, 5, 6]
>>> random.choice(values) #一个序列中随机的抽取一个元素
2
>>> random.sample(values, 2) #提取出N个不同元素的样本
[6, 2]
>>> random.shuffle(values) #打乱序列中元素的顺序
>>> values
[2, 4, 6, 5, 3, 1]
>>> random.randint(0,10) #生成随机整数
2
>>> random.random() #生成0到1范围内均匀分布的浮点数
0.9406677561675867
```

`random.uniform()` 计算均匀分布随机数， `random.gauss()` 计算正态分布随机数。

`random` 模块使用 _Mersenne Twister_ 算法来计算生成随机数。这是一个确定性算法。
