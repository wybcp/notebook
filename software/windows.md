# win10 软件

## [系统优化 - Dism++](https://www.chuyu.me/zh-Hans/index.html)

Dism++是一款 ChuYu 团队开发的开源系统优化软件，帮助用户快速的管理各类启动项目、清理各类系统级别的缓存文件和临时文件、更快的管理电脑中的各种驱动。Dism++以一种更快捷的方式，大大的降低了用户进行系统清理和优化的门槛，可以说是装机必备之一。

## [RedisDesktopManager](https://masuit.com/125)

## [Windows 10 家庭版使用远程桌面](https://www.appinn.com/windows-10-home-remote-desktop/)

RDP Wrapper Library by Stas’M 是 Windows 7、8、10 家庭版中打开远程桌面的工具。

[Github 下载 RDP Wrapper Library by Stas’M](https://github.com/stascorp/rdpwrap)

## Terminal

微软为开发者打造的一款字体 [Cascadia](https://github.com/microsoft/cascadia-code/releases)

```json
 {
    "acrylicOpacity": 0.5,
    "background": "#272822",
    "closeOnExit": true,
    "colorScheme": "One Half Dark",
    "commandline": "powershell.exe",
    "cursorColor": "#FFFFFF",
    "cursorShape": "bar",
    "fontFace": "Cascadia",
    "fontSize": 16,
    "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    "historySize": 9001,
    "icon": "ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png",
    "name": "Windows PowerShell",
    "padding": "0, 0, 0, 0",
    "snapOnInput": true,
    "startingDirectory": "%USERPROFILE%",
    "useAcrylic": false
},
```

### 在terminal中添加git bash

```json
// git bash
{
    "guid": "{00000000-0000-0000-ba54-000000000002}",
    "acrylicOpacity" : 0.5,
    "background": "#272822",
    "closeOnExit" : true,
    "tabTitle": "Git",
    "colorScheme": "One Half Dark",
    "commandline" : "\"%PROGRAMFILES%\\git\\usr\\bin\\bash.exe\" -i -l",
    "cursorColor" : "#FFFFFF",
    "cursorShape" : "bar",
    "fontFace" : "Consolas",
    "fontSize" : 16,
    "historySize" : 9001,
        "icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
    "name" : "git Bash",
    "padding" : "0, 0, 0, 0",
    "snapOnInput" : true,
    "startingDirectory" : "%USERPROFILE%",
    "useAcrylic" : false
},
```

### [cmd运行时间](https://stackoverflow.com/questions/673523/how-do-i-measure-execution-time-of-a-command-on-the-windows-command-line/4801509#4801509)

Windows PowerShell has a built in command that is similar to Bash's "time" command, called "Measure-Command.

```cmd
Measure-Command {echo hi}
```

## [Fiddler](https://www.telerik.com/fiddler)

Fiddler运行在Windows平台，而Charles是基于Java实现的，Fiddler开源免费。

抓包、断点调试、请求替换、构造请求、代理功能

## 看图软件

- [MassiGra](https://www.vector.co.jp/download/file/win95/art/fh604583.html)，功能全面，读图快速，关键是占用内存极低
- [Honeyview](https://cn.bandisoft.com/honeyview/),实时显示照片的EXIF信息，并且非常全面，除了常规的信息之外，甚至可以显示GPS的位置
- [IrfanView](https://www.irfanview.com/)

## [Sumatra PDF](https://www.sumatrapdfreader.org/downloadafter.html)

使用Sumatra PDF打开文件后，无论是哪种文件格式都会自动记忆上次的阅读位置
