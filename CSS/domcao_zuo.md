# DOM 操作

## 动态脚本

动态脚本：页面加载时不存在，在某一时刻通过修改 DOM 动态添加的脚本。

页面插入 JavaScript 代码的两种方式：

- 通过 src 特性包含外部文件

```js
function loadScript(url) {
  var script = document.createElement("script");
  script.type = "text/javasript";
  script.src = url;
  document.body.appendChild(script);
}
```

- 元素本身包含代码

```js
function loadScriptString(code) {
  var script = document.createElement("script");
  script.type = "text/javascript";
  try {
    script.appendChild(document.createTextNode(code)); //IE错误
  } catch (ex) {
    script.text = code;
  }
  document.body.appendChild(script);
}
function addScript() {
  loadScriptString("function sayHi(){alert('hi');}");
  sayHi();
}
```

## 动态样式

动态样式：页面加载时不存在，在页面加载完成时动态添加到页面中的样式。

- link 元素用于添加外部文件，且必须添加到 head 元素，这样能保证浏览器中行为一致

```js
function loadStyles(url) {
  var link = document.createElment("link");
  link.rel = "stylesheet";
  link.type = "text/css";
  link.href = url;
  var head = document.getElementsByTagName("head")[0];
  head.appendChild(link);
}
```

- `<style>`元素包含嵌套的 CSS

```js
function loadStyleString(css) {
  var style = document.createElememt("style");
  style.type = "text/css";
  try {
    style.appendChild(document.createTextNode(css));
  } catch (ex) {
    style.styleSheet.cssText = css;
  }
  var head = document.getElementsByTagName("head")[0];
  head.appendChild(link);
}
```

## 操作表格
