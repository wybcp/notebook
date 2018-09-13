# [保留最后 N 个元素](https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p03_keep_last_n_items.html)

队列

在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

last_5 = collections.deque(maxlen = 5)
[last_5.append(i) for i in range(10)]
print(last_5)
```

在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 。
