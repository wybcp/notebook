# DOM操作

##动态脚本

动态脚本：页面加载时不存在，在某一时刻通过修改DOM动态添加的脚本。

页面插入JavaScript代码的两种方式：
+ 通过src特性包含外部文件

```
 function loadScript(url){
 var script = document.createElement("script");
 script.type="text/javasript";
 script.src=url;
 document.body.appendChild(script);
}
```
+ 元素本身包含代码
```
function loadScriptString(code){
    var script = document.createElement("script");
    script.type = "text/javascript";
    try {
        script.appendChild(document.createTextNode(code));//IE错误
    } catch (ex){
        script.text = code;
    }
    document.body.appendChild(script);
}
function addScript(){
    loadScriptString("function sayHi(){alert('hi');}");
    sayHi();
}
```
##动态样式
动态样式：页面加载时不存在，在页面加载完成时动态添加到页面中的样式。

+ link元素用于添加外部文件，且必须添加到head元素，这样能保证浏览器中行为一致

```
function loadStyles(url){
  var link = document.createElment("link");
  link.rel="stylesheet";
  link.type="text/css";
  link.href=url;
  var head=document.getElementsByTagName("head")[0];
  head.appendChild(link);
}
```
+ `<style>`元素包含嵌套的CSS

```
function loadStyleString(css){
  var style=document.createElememt("style");
  style.type="text/css";
  try{
    style.appendChild(document.createTextNode(css));
  }catch(ex){
    style.styleSheet.cssText=css;
  }
  var head=document.getElementsByTagName("head")[0];
  head.appendChild(link);
}

```
##操作表格