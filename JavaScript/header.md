# header

## [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition)

后端将要下载的文件直接写入响应头。

```golang
http.ResponseWriter.Header().Add("Content-Disposition", "attachment; filename="+fileName)
http.ResponseWriter.Header().Set("Content-Type", "application/octet-stream")
```

如果浏览器不自动弹窗保存，使用下面的代码手动处理。

```js
var data = JSON.stringify({});

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.responseType = "blob";
xhr.addEventListener("readystatechange", function() {
  if (this.readyState === 4) {
    var disposition_string = xhr.getResponseHeader("Content-Disposition");
    var file_name = disposition_string.split("=");
    var blob = xhr.response;
    var link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = file_name[1];
    link.click();
  }
});

xhr.open("POST", "http://127.0.0.1:8099/sale/inventory/download");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Accept", "*/*");
xhr.setRequestHeader("Cache-Control", "no-cache");
xhr.setRequestHeader("cache-control", "no-cache");

xhr.send(data);
```
