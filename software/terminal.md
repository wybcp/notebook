# Terminal

## [Eternal Terminal](https://github.com/MisterTea/EternalTerminal)

Eternal Terminal is a remote shell that automatically reconnects without interrupting the session.

使用终端 ssh 连接时自动重连。

## []

## 主题

[10 个 Terminal 主题，让你的 macOS 终端更好看](https://sspai.com/post/53008)

## windows Terminal

[新生代 Windows 终端：Windows Terminal 的全面自定义](https://sspai.com/post/59380)

```json

// To view the default settings, hold "alt" while clicking on the "Settings" button.
// For documentation on these settings, see: https://aka.ms/terminal-documentation

{
    "$schema": "https://aka.ms/terminal-profiles-schema",

    "defaultProfile": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",

    "profiles":
    [
        // {
        //     // Make changes here to the powershell.exe profile
        //     "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
        //     "name": "Windows PowerShell",
        //     "commandline": "powershell.exe",
        //     "hidden": false,
        //     "acrylicOpacity": 0.5,
        //     "background": "#272822",
        //     "closeOnExit": true,
        //     "colorScheme": "One Half Dark",
        //     "cursorColor": "#FFFFFF",
        //     "cursorShape": "bar",
        //     "fontFace": "Cascadia",
        //     "fontSize": 16,
        //     "historySize": 9001,
        //     "icon": "ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png",
        //     "padding": "0, 0, 0, 0",
        //     "snapOnInput": true,
        //     "startingDirectory": "%USERPROFILE%",
        //     "useAcrylic": false
        // },
        // powershell 7
        {
            "guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
            "hidden": false,
            "name": "PowerShell",
            "source": "Windows.Terminal.PowershellCore",
            "acrylicOpacity": 0.5,
            "background": "#272822",
            "closeOnExit": true,
            "colorScheme": "Dark+",
            "cursorColor": "#FFFFFF",
            "cursorShape": "bar",
            "fontFace": "Cascadia",
            "fontSize": 16,
            "historySize": 9001
        },

        // git bash
        {
            "guid": "{00000000-0000-0000-ba54-000000000002}",
            "acrylicOpacity" : 0.5,
            "background": "#272822",
            "closeOnExit" : true,
            "tabTitle": "Git",
            // "colorScheme": "One Half Dark",
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
        {
            // Make changes here to the cmd.exe profile
            "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
            "name": "cmd",
            "commandline": "cmd.exe",
            "hidden": true
        },
        {
            "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
            "hidden": true,
            "name": "Azure Cloud Shell",
            "source": "Windows.Terminal.Azure"
        },
        {
            "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
            "hidden": false,
            "name": "Ubuntu-18.04",
            "source": "Windows.Terminal.Wsl"
        }

    ],

    // Add custom color schemes to this array
    "schemes": [
        {
            "name": "Dark+",
            "black": "#000000",
            "red": "#cd3131",
            "green": "#0dbc79",
            "yellow": "#e5e510",
            "blue": "#2472c8",
            "purple": "#bc3fbc",
            "cyan": "#11a8cd",
            "white": "#e5e5e5",
            "brightBlack": "#666666",
            "brightRed": "#f14c4c",
            "brightGreen": "#23d18b",
            "brightYellow": "#f5f543",
            "brightBlue": "#3b8eea",
            "brightPurple": "#d670d6",
            "brightCyan": "#29b8db",
            "brightWhite": "#e5e5e5",
            "background": "#0e0e0e",
            "foreground": "#cccccc"
          },
          {
            "name": "Builtin Solarized Light",
            "black": "#073642",
            "red": "#dc322f",
            "green": "#859900",
            "yellow": "#b58900",
            "blue": "#268bd2",
            "purple": "#d33682",
            "cyan": "#2aa198",
            "white": "#eee8d5",
            "brightBlack": "#002b36",
            "brightRed": "#cb4b16",
            "brightGreen": "#586e75",
            "brightYellow": "#657b83",
            "brightBlue": "#839496",
            "brightPurple": "#6c71c4",
            "brightCyan": "#93a1a1",
            "brightWhite": "#fdf6e3",
            "background": "#fdf6e3",
            "foreground": "#657b83"
          },
          {
            "name": "Builtin Solarized Dark",
            "black": "#073642",
            "red": "#dc322f",
            "green": "#859900",
            "yellow": "#b58900",
            "blue": "#268bd2",
            "purple": "#d33682",
            "cyan": "#2aa198",
            "white": "#eee8d5",
            "brightBlack": "#002b36",
            "brightRed": "#cb4b16",
            "brightGreen": "#586e75",
            "brightYellow": "#657b83",
            "brightBlue": "#839496",
            "brightPurple": "#6c71c4",
            "brightCyan": "#93a1a1",
            "brightWhite": "#fdf6e3",
            "background": "#002b36",
            "foreground": "#839496"
          },
          {
            "name": "Dracula",
            "black": "#000000",
            "red": "#ff5555",
            "green": "#50fa7b",
            "yellow": "#f1fa8c",
            "blue": "#bd93f9",
            "purple": "#ff79c6",
            "cyan": "#8be9fd",
            "white": "#bbbbbb",
            "brightBlack": "#555555",
            "brightRed": "#ff5555",
            "brightGreen": "#50fa7b",
            "brightYellow": "#f1fa8c",
            "brightBlue": "#bd93f9",
            "brightPurple": "#ff79c6",
            "brightCyan": "#8be9fd",
            "brightWhite": "#ffffff",
            "background": "#1e1f29",
            "foreground": "#f8f8f2"
          }
    ],

    // Add any keybinding overrides to this array.
    // To unbind a default keybinding, set the command to "unbound"
    "keybindings": []
}

```

### 字体

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
