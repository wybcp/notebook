# xml

[使用可扩展标记语言（XML）](https://docs.python.org/zh-cn/3/library/markup.html)

## 标准库中的xml

## ElementTree

Fredrik Lundh 的ElementTree

## [lxml(推荐)](https://lxml.de/index.html)

Stefan Behnel 的 lxml

lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高

XPath，全称XML Path Language，即XML路径语言，它是一门在XML文档中查找信息的语言，它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索

XPath的选择功能十分强大，它提供了非常简明的路径选择表达式，另外，它还提供了超过100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理等，几乎所有我们想要定位的节点，都可以用XPath来选择

XPath于1999年11月16日成为W3C标准，它被设计为供XSLT、XPointer以及其他XML解析软件使用，更多的文档可以访问其官方网站：<https://www.w3.org/TR/xpath/>

```python
from lxml import etree
```
