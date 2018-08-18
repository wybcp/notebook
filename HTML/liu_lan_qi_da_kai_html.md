# 浏览器打开html

通过配置tasks.json文件来解决这个问题。

按Ctrl+P打开命令面板，输入tasks.json然后回车打开这个文件，可以看到默认配置，然后修改如下：

```
{
    // See http://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "0.1.0",
    "command": "Chrome",    //使用chrome浏览器
    "windows": {
        "command": "C:/Users/wang/AppData/Local/Google/Chrome/Application/chrome.exe" //chrome浏览器的路径
    },
    "isShellCommand": true,
    "args": ["${file}"],    //表示对当前文件进行操作
    "showOutput": "always"
}
```
保存后打开一个html文件，按组合键Ctrl+Shift+B就可以使用指定的浏览器打开html文件了。