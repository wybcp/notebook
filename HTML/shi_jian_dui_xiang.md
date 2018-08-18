# 事件对象

触发DOM上的事件时会产生一个对象。


| DOM事件对象 | IE事件对象 | 作用|
| -- | -- | -- |
| type属性 | type属性 | 用于获取事件类型 |
| target属性 | srcElement属性 | 用于获取事件目标 |
| stopPropagation()方法| cancelBubble属性 |用于阻止事件冒泡 |
| preventDefault（）方法|  returnValue属性 | 阻止事件的默认行为 |

只有在事件处理程序执行期间，event对象才存在。 

##DOM中的事件对象

只有cancelable属性设置为true时，才可以使用preventDefault()方法阻止特定事件的默认行为。

stopPropagation()方法用于立即停止事件在DOM中的传播。


##IE中的事件对象

##跨浏览器的事件对象
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

    getEvent: function(event){
        return event ? event : window.event;
    },

    
    getTarget: function(event){
        return event.target || event.srcElement;
    },
    
    preventDefault: function(event){
        if (event.preventDefault){
            event.preventDefault();
        } else {
            event.returnValue = false;
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
    
    stopPropagation: function(event){
        if (event.stopPropagation){
            event.stopPropagation();
        } else {
            event.cancelBubble = true;
        }
    }

};
```