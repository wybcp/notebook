# [babel](https://babeljs.io/)

参考http://es6.ruanyifeng.com/#docs/intro

Babel 是一个广泛使用的 ES6 转码器，可以将 ES6 代码转为 ES5 代码

##配置文件.babelrc
Babel 的配置文件是.babelrc，存放在项目的根目录下。使用 Babel 的第一步，就是配置这个文件。

该文件用来设置转码规则和插件，基本格式如下。

````
{
  "presets": [],
  "plugins": []
}```
presets字段设定转码规则，官方提供以下的规则集，你可以根据需要安装。
````

# ES2015 转码规则

$ npm install --save-dev babel-preset-es2015

# react 转码规则

$ npm install --save-dev babel-preset-react

# ES7 不同阶段语法提案的转码规则（共有 4 个阶段），选装一个

$ npm install --save-dev babel-preset-stage-0
$ npm install --save-dev babel-preset-stage-1
$ npm install --save-dev babel-preset-stage-2
$ npm install --save-dev babel-preset-stage-3

```
然后，将这些规则加入.babelrc。
```

{
"presets": [
"es2015",
"react",
"stage-2"
],
"plugins": []
}```

注意，以下所有 Babel 工具和模块的使用，都必须先写好.babelrc。

可以使用 package.json 代替.babelrc。

```
{
  "name": "my-package",
  "version": "1.0.0",
  "babel": {
    "presets": [
      "es2015",
      "react"
    ],
    "plugins": []
  },
 }
```

##命令行转码 babel-cli

Babel 提供 babel-cli 工具，用于命令行转码:`npm install --global babel-cli`
基本用法如下。

````
# 转码结果输出到标准输出
$ babel example.js

# 转码结果写入一个文件
# --out-file 或 -o 参数指定输出文件
$ babel example.js --out-file compiled.js
# 或者
$ babel example.js -o compiled.js

# 整个目录转码
# --out-dir 或 -d 参数指定输出目录
$ babel src --out-dir lib
# 或者
$ babel src -d lib

# -s 参数生成source map文件
$ babel src -d lib -s```
上面代码是在全局环境下，进行Babel转码。这意味着，如果项目要运行，全局环境必须有Babel，也就是说项目产生了对环境的依赖。另一方面，这样做也无法支持不同项目使用不同版本的Babel。

一个解决办法是将babel-cli安装在项目之中。
````

npm install --save-dev babel-cli```

然后，改写 package.json。

````
{
  // ...
  "devDependencies": {
    "babel-cli": "^6.0.0"
  },
  "scripts": {
    "build": "babel src -d lib"
  },
}```
转码的时候，就执行下面的命令。

```npm run build```
##babel-register
babel-register模块改写require命令，为它加上一个钩子。此后，每当使用require加载.js、.jsx、.es和.es6后缀名的文件，就会先用Babel进行转码。

```npm install --save-dev babel-register```

使用时，必须首先加载babel-register。
````

require("babel-register");
require("./index.js");

````
然后，就不需要手动对index.js转码了。

需要注意的是，babel-register只会对require命令加载的文件转码，而不会对当前文件转码。另外，由于它是实时转码，所以只适合在开发环境使用。

##babel-polyfill
Babel默认只转换新的JavaScript句法（syntax），而不转换新的API，比如Iterator、Generator、Set、Maps、Proxy、Reflect、Symbol、Promise等全局对象，以及一些定义在全局对象上的方法（比如Object.assign）都不会转码。

举例来说，ES6在Array对象上新增了Array.from方法。Babel就不会转码这个方法。如果想让这个方法运行，必须使用babel-polyfill，为当前环境提供一个垫片。

安装命令如下。

```npm install --save babel-polyfill```

然后，在脚本头部，加入如下一行代码。
````

import 'babel-polyfill';
// 或者
require('babel-polyfill');

```
Babel默认不转码的API非常多，详细清单可以查看babel-plugin-transform-runtime模块的definitions.js文件。
```
