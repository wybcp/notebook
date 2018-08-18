# style

任何支持style特性的HTML元素在JavaScript有一个对应的style属性。使用短划线的css属性需要转化为驼峰大小写形式。

CSSText()

getPropertyValue()

removeProperty()：移除这个属性，应用该属性的默认值；

##创建规则

跨浏览器方式向样式表插图规则：
```
function insertRule(sheet, selectorText, cssText, position){
if (sheet.insertRule){
sheet.insertRule(selectorText + "{" + cssText + "}", position);
} else if (sheet.addRule){
sheet.addRule(selectorText, cssText, position);
}
}

```

##删除规则
跨浏览器删除规则：
```
function deleteRule(sheet, index){
if (sheet.deleteRule){
sheet.deleteRule(index);
} else if (sheet.removeRule){
sheet.removeRule(index);
}
}
```


##偏移量
某个元素在页面的偏移量:
```
function getElementLeft(element){
var actualLeft = element.offsetLeft;
var current = element.offsetParent;

while (current !== null){ 
actualLeft += current.offsetLeft;
current = current.offsetParent;
}

return actualLeft;
}

function getElementTop(element){
var actualTop = element.offsetTop;
var current = element.offsetParent;

while (current !== null){ 
actualTop += current.offsetTop;
current = current.offsetParent;
}

return actualTop;
}
```

##滚动大小

scrollHeight

scrollWidth

scrollLeft

scrollTop
