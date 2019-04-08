# navigation 对象

## 检测插件

对于非 IE 浏览器，使用 plugins 数组。

```js
//plugin detection - doesn't work in IE
function hasPlugin(name) {
  name = name.toLowerCase();
  for (var i = 0; i < navigator.mimeTypes.length; i++) {
    if (navigator.mimeTypes[i].name.toLowerCase().indexOf(name) > -1) {
      return true;
    }
  }

  return false;
}

//detect flash
alert(hasPlugin("Flash"));

//detect quicktime
alert(hasPlugin("QuickTime"));

//detect Java
alert(hasPlugin("Java"));
```

IE 插件，使用专有的 ActiveXObject 类型，以 COM 对象实现插件，有专有的 COM 标识符。

```js
//plugin detection for IE
function hasIEPlugin(name) {
  try {
    new ActiveXObject(name);
    return true;
  } catch (ex) {
    return false;
  }
}

//detect flash
alert(hasIEPlugin("ShockwaveFlash.ShockwaveFlash"));

//detect quicktime
alert(hasIEPlugin("QuickTime.QuickTime"));
```

由于两种插件检测方法差别巨大，因此经典的做法是针对每个插件分别创建检测函数。

```js
//plugin detection - doesn't work in IE
function hasPlugin(name) {
  name = name.toLowerCase();
  for (var i = 0; i < navigator.plugins.length; i++) {
    if (navigator.plugins[i].name.toLowerCase().indexOf(name) > -1) {
      return true;
    }
  }

  return false;
}

//plugin detection for IE
function hasIEPlugin(name) {
  try {
    new ActiveXObject(name);
    return true;
  } catch (ex) {
    return false;
  }
}

//detect flash for all browsers
function hasFlash() {
  var result = hasPlugin("Flash");
  if (!result) {
    result = hasIEPlugin("ShockwaveFlash.ShockwaveFlash");
  }
  return result;
}

//detect quicktime for all browsers
function hasQuickTime() {
  var result = hasPlugin("QuickTime");
  if (!result) {
    result = hasIEPlugin("QuickTime.QuickTime");
  }
  return result;
}

//detect flash
alert(hasFlash());

//detect quicktime
alert(hasQuickTime());
```
