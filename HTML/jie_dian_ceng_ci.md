# 节点层次

## Node 类型

appendChild()用于向 childNodes 末尾添加一个节点，返回新增的节点，如果添加的节点是文档的一部分，那该节点从原位置移动到新位置。

insertBefore()插入特定的位置，接收两个参数：要插入的节点和作为参照的节点(若参照节点为 null，则等同于 appendChild())。

replaceChild()接受两个参数：要插入的节点和要替换的节点。

removeChild()

cloneNode()接受一个布尔值参数：

- true，深复制，即复制节点及其整个字节点树；
- false，只复制节点本身。

## Document 类型

document.documentElement 取得<html>的引用。

document.body 取得对<body>的引用。

document.title 取得文档标题。

document.URL 取得完整的 URL。

document.domain 取得域名，子域设置相同 domain 则可以通过 JavaScript 通讯。

getElementById

getElementsByTagName():返回多个元素的 NodeList，通过方括号语法或者 item()方法访问这些元素，传递星号（\*）返回文档的所有元素。

getElementsByName():

### DOM 一致性检测

document.implementation.hasFeature("DOM 功能名称","版本号"):检测浏览器实现 DOM 的功能。

### 文档写入

write()，原样写入字符串。

writeln()：写入字符串同时在末尾添加换行符(\n)

open()

close()

## Element 类型

getAttribute()

setAttrribute()

removeAttribute()

document.createElement()创建新元素

## Text 类型

### 操作节点中的文本

- appendData(text):将 text 添加到节点的末尾；
- deleteData(offset,count):从 offset 位置开始删除 count 个字符；
- insertData(offset,text )：在 offset 指定的位置插入 text；
- replaceData(offset,count,text)：用 text 替代从 offset 开始替代 count 个字符；
- splitText(offset )：从 offset 位置一分为二；
- substringData(offset,count)：提取 count 个字符从 offset 开始。

### 创建文本节点

document.createTextNode(text)

```
var element = document.createElement("div");
    element.className = "message";

var textNode = document.createTextNode("Hello world!");
    element.appendChild(textNode);

    document.body.appendChild(element);
```

### 规范化文本节点

父元素 normalize()可以将相连的文本节点合并。

```js
function addNode() {
  var element = document.createElement("div");
  element.className = "message";

  var textNode = document.createTextNode("Hello world!");
  element.appendChild(textNode);

  var anotherTextNode = document.createTextNode("Yippee!");
  element.appendChild(anotherTextNode);

  document.body.appendChild(element);

  alert(element.childNodes.length); //2

  element.normalize();
  alert(element.childNodes.length); //1
  alert(element.firstChild.nodeValue); //"Hello World!Yippee!"
}
```

## commet 类型

注释节点

## Attr 类型

getAttribute()

setAttribute()

removeAttribute()
