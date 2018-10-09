# Ajax

Asynchronous JavaScript XML

一种无需刷新页面即可从服务器取得数据，核心是 XMLHttpRequest。

同源策略：相同的域、相同的端口、相同的协议。

## 使用方法

### 同步请求

```js
var xhr = new XMLHttpRequest(); //创建XML对象
xhr.open("get", "example.txt", false);
/*三个参数：发送的请求类型；请求的URL，要处于同一个域中，具有相同的端口和协议；表示是否异步发送请求的布尔值。
注意这个只是启动一个请求以备发送*/

xhr.send(null); //接受一个参数，即请求发送的数据。

if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {
  //HTTP响应状态，200表示成功，304表示资源没有修改，直接使用缓存。
  alert(xhr.statusText); //状态说明
  alert(xhr.responseText); //作为响应主体返回的文本
} else {
  alert("Request was unsuccessful: " + xhr.status);
}
```

### 异步请求

XHR 对象的 readyState 属性，表示请求/响应过程的当前活动对象。

- 0：未初始化，尚未调用 open();
- 1：启动，已调用 open()，未调用 send();
- 2：发送，已调动 send()，尚未收到响应；
- 3：接收，已接收到部分相应数据；
- 4：完成。

只要 readyState 属性的值变动，就会触发一次 readystatechange 事件。

```js
var xhr = new XMLHttpRequest(); //创建XML对象
xhr.onreadystatechange = function(event) {
  if (xhr.readyState == 4) {
    if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {
      alert(xhr.responseText);
    } else {
      alert("Request was unsuccessful: " + xhr.status);
    }
  }
};
xhr.open("get", "example.txt", true);
xhr.setRequestHeader("MyHeader", "MyValue"); //设置自定义的请求头部信息，需位于open和send之间。
xhr.send(null);
```

在接收到响应之前还可以调用 abort()取消异步请求。

`xhr.getResponseHeader("xxx")`取得 xxx 头部信息的字符串

`xhr.getAllResponseHeaders`取得所有头部信息的字符串

### get 请求

常用于向服务器查询某些信息。

下面函数向现有的 URL 的末尾添加查询字符串参数：

```js
function addURLParam(url, name, value) {
  url = +(url.indexOf("?") == -1 ? "?" : "&"); //check ?:if not, add a ?;else, add a &
  url = +encodeURIComponent(name) + "=" + encodeURIComponent("value"); //encode name and value
  return url;
}
```

### post 请求

通常用于向服务器发送应该被保存的数据。

## 跨域资源共享

cross-origin resources sharing

基本思想：使用自定义的 HTTP 头部让浏览器与服务器进行沟通，决定是否响应。

### IE 对 CORS 的实现

XDR：XDomainRequest。

### 其他浏览器对 CORS 的实现

XMLHttpRequest 原生支持，open()方法传入绝对 URL。

### Prefighted Requests

### 跨浏览器的 CORS

```js
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    xhr = null;
  }
  return xhr;
}

var request = createCORSRequest("get", "http://www.somewhere-else.com/xdr.php");
if (request) {
  request.onload = function() {
    //do something with request.responseText
  };
  request.send();
}
```
