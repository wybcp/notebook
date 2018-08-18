#事件

JavaScript与HTML之间的交互是通过事件实现。

事件:文档或浏览器窗口中发生的一些特定的交互瞬间。

##事件流
事件流描述从页面接收事件的顺序。
###事件冒泡
IE事件冒泡：事件由最具体的元素开始逐级向上传递。
###事件捕获
###DOM事件流
三个阶段：事件捕获阶段、处于目标阶段、事件冒泡阶段。

## 事件处理程序

响应某个事件的函数叫事件处理程序。

###HTML事件处理程序
HTML事件处理程序通常封装在一个try-catch块中。

###DOM0级事件处理程序
###DOM2级事件处理程序
定义两个方法：
+ addEventListener()：按照添加顺序执行
+ removeEventListener()

接受三个参数：要处理的事件名、作为事件处理程序的函数和一个布尔值。布尔值为true，表示在捕获阶段调用事件处理程序；false，表示在冒泡阶段调用事件处理程序。

通过这种方法可以添加多个事件处理程序。

###IE事件处理程序
+ attachEvent()：按照添加相反顺序触发。

+ detachEvent()

使用这两种方法时注意事件处理程序的作用域：全局作用域。

###跨浏览器的事件处理程序

```
var EventUtil = {

    addHandler: function(element, type, handler){
        if (element.addEventListener){
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent){
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;
        }
    },
      
    removeHandler: function(element, type, handler){
        if (element.removeEventListener){
            element.removeEventListener(type, handler, false);
        } else if (element.detachEvent){
            element.detachEvent("on" + type, handler);
        } else {
            element["on" + type] = null;
        }
    },
 
};
```
