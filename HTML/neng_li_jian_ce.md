# 能力检测

在浏览器环境测试任何对象的某个特性是否存在，使用下面的函数：
```
function isHostMethod(object,property){
    var t = typeof object[property];
    return t == 'function'||(!!(t=='object'&&object[property]))||t=='unknown';
}
```

```
//determine if the browser has Netscape-style plugins
var hasNSPlugins = !!(navigator.plugins && navigator.plugins.length);

//determine if the browser has basic DOM Level 1 capabilities
var hasDOM1 = !!(document.getElementById && document.createElement && 
               document.getElementsByTagName);
               ```
               
