# ESLint
原文: http://www.gyzhao.me/2016/05/12/VsCodeESLint/　　作者: gyzhao

##前言

在团队协作开发中，为了统一代码风格，避免一些低级错误，应该设有团队成员统一遵守的编码规范。很多语言都提供了Lint工具来实现这样的功能，JavaScript也有类似的工具：ESLint。除了可以集成到构建工具中(如：Gulp)在构建过程中检查代码风格以外；还可以通过将ESLint和代码编辑器相结合以提供代码风格的实时校验。这里将介绍如何在Visual Studio Code使用ESLint来提供代码风格的实时校验。
##安装 Visual Studio Code ESLint 插件

打开 Visual Studio Code ，首先使用快捷键 Ctrl + Shift + P 调出VsCode的控制台，然后输入下面的命令安装ESLint插件：`ext install ESLint`

###使用 NPM 安装 ESLint

为了方便我们通过ESLint命令行工具来帮助我们生成ESLint相关的配置，我们需要进行全局安装：`npm install eslint -g`

安装完成后我们使用命令行工具进入到需要引入ESLint的项目的目录中，然后输入下面的命令进行ESLint的初始化操作：
`
eslint --init`

执行命令后，我们选择相应的代码风格，也可以自定义，在这里我使用standard风格的规则，如下所示：

![standard](http://7xrkzy.com1.z0.glb.clouddn.com/install-eslint-package.gif)

配置ESLint的项目中需要设置好该项目的 package.json 文件，如果没有的话可以使用 npm init来设置。

安装完成后我们可以看到除了ESLint命令行工具为我们生成的ESLint依赖包，还有一个特殊的.eslintrc.json文件，该文件是ESLint的配置文件，如下所示：
```
{
    "extends": "standard",
    "installedESLint": true,
    "plugins": [
        "standard"
    ]
}```

配置文件中除了声明我们所使用的代码风格以外，我们还可以定制自己的规则，比如：声明全局变量或者规定字符串引号的风格，以及其他任何ESLint支持的规则都是可以配置的，下面是一个简单的示例：
```
{
    "extends": "standard",
    "installedESLint": true,
    "plugins": [
        "standard"
    ],
    "rules": {
        //关闭额外的分号检查
        //0:关闭，1:警告，2:异常
        "semi": 0,
        //字符串必须使用单引号
        "quotes": [
            "error",
            "single"
        ]
    }
}```

更多配置相关可以参考官方文档：http://eslint.org/docs/user-guide/configuring

##使用ESLint校验代码风格

安装完成后我们使用 Visual Studio Code 打开项目，可以看到ESLint插件在运行了，不过给了我们一个错误提示：
![cannot find eslint plugin promise](http://7xrkzy.com1.z0.glb.clouddn.com/cannot-find-eslint-plugin-promise.PNG)

这时候我们需要在当面目录下输入下面的命令安装相应的开发依赖包：
`
npm install eslint-plugin-promise --save-dev`

下面我们来测试一些看ESLint是否配置成功了，如下所示，我们编写一段不符合我们设定代码风格的典型的IIFE代码，可以看到ESLint插件为我们提供了准确方便且实时的提示信息：
![eslint test](http://7xrkzy.com1.z0.glb.clouddn.com/eslint-test.gif)

可以看到通过ESLint为我们提供的代码风格检查，能够帮助我们可以写出更规范，更优雅的Javascript代码~

参考资料&进一步阅读

http://eslint.org/
http://eslint.org/docs/user-guide/configuring
https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
https://csspod.com/getting-started-with-eslint/