# vim

## 命令（normal）模式

`esc`键退出输入模式，进入命令模式。

|      命令       | 作用                                                         |
| :-------------: | :----------------------------------------------------------- |
|       dd        | 删除当前行，并把删除的行存到剪贴板里                         |
|       5dd       | 删除光标开始的5行，并把删除的行存到剪贴板里                  |
|       yy        | 复制光标所在行                                               |
|       5yy       | 复制5行                                                      |
|        u        | 撤销上一步操作                                               |
|        p        | 粘贴剪贴板                                                   |
|      `:w`       | 保存                                                         |
|      `:q`       | 退出                                                         |
|      `:q!`      | 强制退出（放弃修改）                                         |
|     `:wq!`      | 强制保存退出                                                 |
|    `:set nu`    | 显示行号                                                     |
|   `:set nonu`   | 不显示行号                                                   |
|     `:命令`     | 执行命令                                                     |
|     `:整数`     | 跳转到该行                                                   |
|  `:s/one/two`   | 将光标所在行的第一个one替换成two                             |
| `:s/one/two/g`  | 将光标所在行的所有one替换成two                               |
| `:%s/one/two/g` | 全文所有one替换成two                                         |
|     /字符串     | 进入查找（搜索）模式，从上向下，加入`\c` 表示大小写不敏感查找，`\C` 表示大小写敏感查找。 |
|     ?字符串     | 进入查找（搜索）模式，从下向上                               |
|        n        | 显示搜索命令定位的下一个                                     |
|        N        | 显示搜索命令定位的上一个                                     |

## 输入（insert）模式

命令模式按下`i`，进入输入模式。

## 末行模式

在命令模式下输入`:`进入末行模式。

主要用于保存或退出文件，以及设置vim编辑器的工作环境。

## `.vimrc`

可以通过配置文件来设置 vim 操作环境！  vim 的配置文件是 `/etc/vimrc` 。不建议修改该文件，可以修改 当前用户`~/.vimrc`这个文件 （默认不存在，手动创建！）！

Vim 默认采用大小写敏感的查找

```shell
#文件双引号 （"） 是注解
[dmtsai@study ~]$ vim ~/.vimrc
set hlsearch            "高亮度反白"
set backspace=2         "可随时用倒退键删除"
set autoindent          "自动缩排"
set ruler               "可显示最后一列的状态"
set showmode            "左下角那一列的状态"
set nu                  "可以在每一列的最前面显示行号啦！"
set bg=dark             "显示不同的底色色调"
syntax on               "进行语法检验，颜色显示。"
set ignorecase   "大小写不敏感查找"
set smartcase "大小写敏感查找"
```
