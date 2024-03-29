# vscode

## 在 Mac 中打开隐藏文件

在 Open 界面中，使用 Mac 快捷键`Command+Shift+.`

增加code命令: vscode->view->command palette->输入path，选择install code command in path

- `code 文件夹`：打开指定文件夹
- `code .`：打开当前目录
- `code -h`

## 插件

- filesize
- Chinese(Simplified) Language Pack for Visual Studio Code
- vscode-icons
- Image preview
- gitlens
- Live Server：静态、动态页面的实时预览
- Code Spell Checker
- Path Intellisense
- code run
- vscode-fileheader：顶部注释模板，可定义作者、时间等信息，并会自动更新最后修改时间
- npm Intellisense：NPM 依赖补全，在你引入任何 node_modules 里面的依赖包时提供智能提示和自动完成
- JavaScript (ES6) code snippets：常用的类声明、ES 模块声明、CMD 模块导入等
- ESLint：代码语法检查
- Beautify：格式化代码的工具

## config

```json
{
  "workbench.iconTheme": "vscode-icons",
  "typescript.locale": "zh-CN",
  "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
  "explorer.confirmDelete": false,
  "go.useLanguageServer": true,
  "[markdown]": {},
  "editor.codeActionsOnSave": {
    "source.fixAll.markdownlint": true
  },
  "go.lintTool": "golangci-lint",
  "go.lintFlags": ["--fast"]
}
```
