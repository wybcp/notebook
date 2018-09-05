# json

在 JavaScript 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等，但是对象和数组是比较特殊且常用的两种类型，下面简要介绍一下它们。

- 对象：它在 JavaScript 中是使用花括号{}包裹起来的内容，数据结构为{key1：value1, key2：value2, ...}的键值对结构。在面向对象的语言中，key 为对象的属性，value 为对应的值。键名可以使用整数和字符串来表示。值的类型可以是任意类型。
- 数组：数组在 JavaScript 中是方括号[]包裹起来的内容，数据结构为["java", "javascript", "vb", ...]的索引结构。在 JavaScript 中，数组是一种比较特殊的数据类型，它也可以像对象那样使用键值对，但还是索引用得多。同样，值的类型可以是任意类型。

所以，一个 JSON 对象可以写为如下形式：

```json
[
  {
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
  },
  {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
  }
]
```

由中括号包围的就相当于列表类型，列表中的每个元素可以是任意类型，这个示例中它是字典类型，由大括号包围。

JSON 可以由以上两种形式自由组合而成，可以无限次嵌套，结构清晰，是数据交换的极佳方式。

JSON 的数据需要用双引号来包围，不能使用单引号。

如果想保存 JSON 的格式，可以再加一个参数 indent，代表缩进字符个数。

```python
json.dumps(data, indent=2)
```

```python
with open('female_codon_scan.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(female_codon_scan_structure, indent = 2, ensure_ascii = False))
```
