# 事件

JavaScript 与 HTML 之间的交互是通过事件实现。

事件:文档或浏览器窗口中发生的一些特定的交互瞬间。

触发 DOM 上的事件时会产生一个对象。

| DOM 事件对象           | IE 事件对象       | 作用               |
| ---------------------- | ----------------- | ------------------ |
| type 属性              | type 属性         | 用于获取事件类型   |
| target 属性            | srcElement 属性   | 用于获取事件目标   |
| stopPropagation()方法  | cancelBubble 属性 | 用于阻止事件冒泡   |
| preventDefault（）方法 | returnValue 属性  | 阻止事件的默认行为 |

只有在事件处理程序执行期间，event 对象才存在。

## 事件流

事件流描述从页面接收事件的顺序。

### 事件冒泡

IE 事件冒泡：事件由最具体的元素开始逐级向上传递。

### 事件捕获

### DOM 事件流

三个阶段：事件捕获阶段、处于目标阶段、事件冒泡阶段。

## 事件处理程序

响应某个事件的函数叫事件处理程序。

### HTML 事件处理程序

HTML 事件处理程序通常封装在一个 try-catch 块中。

### DOM0 级事件处理程序

### DOM2 级事件处理程序

定义两个方法：

- addEventListener()：按照添加顺序执行
- removeEventListener()

接受三个参数：要处理的事件名、作为事件处理程序的函数和一个布尔值。布尔值为 true，表示在捕获阶段调用事件处理程序；false，表示在冒泡阶段调用事件处理程序。

通过这种方法可以添加多个事件处理程序。

### IE 事件处理程序

- attachEvent()：按照添加相反顺序触发。

- detachEvent()

使用这两种方法时注意事件处理程序的作用域：全局作用域。

### 跨浏览器的事件处理程序

```js
var EventUtil = {
  addHandler: function(element, type, handler) {
    if (element.addEventListener) {
      element.addEventListener(type, handler, false);
    } else if (element.attachEvent) {
      element.attachEvent("on" + type, handler);
    } else {
      element["on" + type] = handler;
    }
  },

  removeHandler: function(element, type, handler) {
    if (element.removeEventListener) {
      element.removeEventListener(type, handler, false);
    } else if (element.detachEvent) {
      element.detachEvent("on" + type, handler);
    } else {
      element["on" + type] = null;
    }
  }
};
```
