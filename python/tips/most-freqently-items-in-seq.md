# [序列中出现次数最多的元素](https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p12_determine_most_freqently_items_in_seq.html)

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counter = Counter(words)
top_three = word_counter.most_common(3)
print(top_three)
```
