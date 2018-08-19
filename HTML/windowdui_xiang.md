# window 对象

###全局作用域

BOM 核心对象是 window，其为 global 对象，所有在全局作用域中声明的变量、函数都是 window 对象的属性和方法。

定义全局变量与在 window 对象上直接定义属性的区别：全局变量不能通过 delete 删除，而直接在 window 对象上的定义属性可以。

###窗口位置
`screenLeft`：窗口相对屏幕左边；

`screenTop`：窗口相对屏幕上边。

###窗口大小

```
var pageWidth = window.innerWidth,
    pageHeight = window.innerHeight;

    if (typeof pageWidth != "number"){
        if (document.compatMode == "CSS1Compat"){
          //确定页面是否处于标准模式
            pageWidth = document.documentElement.clientWidth;
            pageHeight = document.documentElement.clientHeight;
        } else {
            pageWidth = document.body.clientWidth;
            pageHeight = document.body.clientHeight;
        }
    }
```

`resizeTo()`和`resizeBy()`调节窗口大小。

###打开窗口
`window.open()`

检测窗口是否被屏蔽：

```
var blocked = false;

try {
   var wroxWin = window.open("http://www.wrox.com", "_blank");
   if (wroxWin == null){
       blocked = true;//内置屏蔽程序
   }
} catch (ex){
   blocked = true;//浏览器扩展或者其他程序阻止弹出窗口。
}

if (blocked){
   alert("The popup was blocked!");
}
```

###间歇调用和超时调用

超时调用使用 window 对象的 setTimeout（）方法，两个参数：要执行的代码（字符串或者函数）和毫秒时间数。

```
//set the timeout
var timeoutId = setTimeout(function() {
      alert("Hello world!");
    }, 1000);

//nevermind  cancel it
clearTimeout(timeoutId);
```

间歇调用 setInterval()

```
var num = 0;
var max = 10;
var intervalId = null;

function incrementNumber() {
    num++;

    //if the max has been reached, cancel all pending executions
    if (num == max) {
        clearInterval(intervalId);
        alert("Done");
    }
}

intervalId = setInterval(incrementNumber, 500);
```

使用超时调用模拟间歇调用是一种最佳模式，因为一个间歇调用可能会在一个间歇调用结束前启动。

```
var num = 0;
var max = 100;

function incrementNumber() {
    num++;

    //if the max has not been reached, set another timeout
    if (num < max) {
        setTimeout(incrementNumber, 500);
    } else {
        alert("Done");
    }
}

setTimeout(incrementNumber, 500);
```

###系统对话框

alert()：常用于弹出警告；

confirm()：用于用户想要执行删除操作时；

prompt()：提示框。
