# style

任何支持 style 特性的 HTML 元素在 JavaScript 有一个对应的 style 属性。使用短划线的 css 属性需要转化为驼峰大小写形式。

CSSText()

getPropertyValue()

removeProperty()：移除这个属性，应用该属性的默认值；

## 创建规则

跨浏览器方式向样式表插图规则：

```js
function insertRule(sheet, selectorText, cssText, position) {
  if (sheet.insertRule) {
    sheet.insertRule(selectorText + "{" + cssText + "}", position);
  } else if (sheet.addRule) {
    sheet.addRule(selectorText, cssText, position);
  }
}
```

## 删除规则跨浏览器删除规则：

```js
function deleteRule(sheet, index) {
  if (sheet.deleteRule) {
    sheet.deleteRule(index);
  } else if (sheet.removeRule) {
    sheet.removeRule(index);
  }
}
```

## 偏移量某个元素在页面的偏移量:

```js
function getElementLeft(element) {
  var actualLeft = element.offsetLeft;
  var current = element.offsetParent;

  while (current !== null) {
    actualLeft += current.offsetLeft;
    current = current.offsetParent;
  }

  return actualLeft;
}

function getElementTop(element) {
  var actualTop = element.offsetTop;
  var current = element.offsetParent;

  while (current !== null) {
    actualTop += current.offsetTop;
    current = current.offsetParent;
  }

  return actualTop;
}
```

## 滚动大小

scrollHeight

scrollWidth

scrollLeft

scrollTop
