# vim

- Insert 模式，请按下键 i
- Normal 模式，请按 ESC 键。
- x → 删当前光标所在的一个字符。
- :wq → 存盘 + 退出 (:w 存盘, :q 退出) （陈皓注：:w 后可以跟文件名）
- dd → 删除当前行，并把删除的行存到剪贴板里
- p → 粘贴剪贴板
- 在 normal 模式下按下/即可进入查找模式，输入要查找的字符串并按下回车。 Vim 会跳转到第一个匹配。按下 n 查找下一个，按下 N 查找上一个。

## 查找

在 normal 模式下按下/即可进入查找模式，输入要查找的字符串并按下回车。 Vim 会跳转到第一个匹配。按下 n 查找下一个，按下 N 查找上一个。

在 normal 模式下按下/即可进入查找模式，输入要查找的字符串并按下回车。 Vim 会跳转到第一个匹配。按下 n 查找下一个，按下 N 查找上一个。

Vim 查找支持正则表达式，例如/vim$匹配行尾的"vim"。 需要查找特殊字符需要转义，例如/vim\$匹配"vim$"。

注意查找回车应当用\n，而替换为回车应当用\r（相当于<CR>）。大小写敏感查找

在查找模式中加入\c 表示大小写不敏感查找，\C 表示大小写敏感查找。例如：

`/foo\c` 将会查找所有的"foo","FOO","Foo"等字符串。

大小写敏感配置

Vim 默认采用大小写敏感的查找，为了方便我们常常将其配置为大小写不敏感：

" 设置默认进行大小写不敏感查找
set ignorecase
" 如果有一个大写字母，则切换到大小写敏感查找
set smartcase
将上述设置粘贴到你的~/.vimrc，重新打开 Vim 即可生效。
查找当前单词

在 normal 模式下按下\*即可查找光标所在单词（word）， 要求每次出现的前后为空白字符或标点符号。例如当前为 foo， 可以匹配 foo bar 中的 foo，但不可匹配 foobar 中的 foo。 这在查找函数名、变量名时非常有用。

按下 g\*即可查找光标所在单词的字符序列，每次出现前后字符无要求。 即 foo bar 和 foobar 中的 foo 均可被匹配到。

查找与替换

`:s`（substitute）命令用来查找和替换字符串。语法如下：

:{作用范围}s/{目标}/{替换}/{替换标志}
例如:%s/foo/bar/g 会在全局范围(%)查找 foo 并替换为 bar，所有出现都会被替换（g）。

作用范围

作用范围分为当前行、全文、选区等等。

当前行：

`:s/foo/bar/g` 全文：

:%s/foo/bar/g
选区，在 Visual 模式下选择区域后输入:，Vim 即可自动补全为 :'<,'>。

:'<,'>s/foo/bar/g
2-11 行：

:5,12s/foo/bar/g 当前行.与接下来两行+2：

:.,+2s/foo/bar/g 替换标志

上文中命令结尾的 g 即是替换标志之一，表示全局 global 替换（即替换目标的所有出现）。 还有很多其他有用的替换标志：

空替换标志表示只替换从光标位置开始，目标的第一次出现：

:%s/foo/bar
i 表示大小写不敏感查找，I 表示大小写敏感：

:%s/foo/bar/i

# 等效于模式中的\c（不敏感）或\C（敏感）

:%s/foo\c/bar
c 表示需要确认，例如全局查找"foo"替换为"bar"并且需要确认：

:%s/foo/bar/gc
回车后 Vim 会将光标移动到每一次"foo"出现的位置，并提示

replace with bar (y/n/a/q/l/^E/^Y)?
按下 y 表示替换，n 表示不替换，a 表示替换所有，q 表示退出查找模式， l 表示替换当前位置并退出。^E 与^Y 是光标移动快捷键，参考： Vim 中如何快速进行光标移动。

高亮设置

高亮颜色设置

如果你像我一样觉得高亮的颜色不太舒服，也可以进行设置：

highlight Search ctermbg=grey ctermfg=black
将上述配置粘贴到~/.vimrc，重新打开 vim 即可生效。
上述配置指定 Search 结果的前景色（foreground）为黑色，背景色（background）为灰色。 更多的 CTERM 颜色可以查阅：http://vim.wikia.com/wiki/Xterm256_color_names_for_console_Vim

禁用/启用高亮

有木有觉得每次查找替换后 Vim 仍然高亮着搜索结果？ 可以手动让它停止高亮，在 normal 模式下输入：

:nohighlight
" 等效于
:nohl
其实上述命令禁用了所有高亮，正确的命令是:set nohlsearch。 下次搜索时需要:set hlsearch 再次启动搜索高亮。 怎么能够让 Vim 查找/替换后自动取消高亮，下次查找时再自动开启呢？

" 当光标一段时间保持不动了，就禁用高亮
autocmd cursorhold _ set nohlsearch
" 当输入查找命令时，再启用高亮
noremap n :set hlsearch<cr>n
noremap N :set hlsearch<cr>N
noremap / :set hlsearch<cr>/
noremap ? :set hlsearch<cr>?
noremap _ \*:set hlsearch<cr>
将上述配置粘贴到~/.vimrc，重新打开 vim 即可生效。

## 一般模式

- `vim hosts /etc/hosts`用一个 vim 打开两个文件
- `4yy`复制四列
- `:n`打开下一个文件 next
- `u`撤销编辑
- `:sp {filename}` 分区窗口
- `[ctrl]+w+↑`”及“`[ctrl]+w+↓`” 在两个窗口之间移动
- 大写的`G`经常使用，尤其是`1G, G` 移动到文章的头/尾功能

## vim 环境设置

可以通过配置文件来直接 vim 操作环境！ 整体 vim 的设置值一般是放置在 /etc/vimrc 这个文件，不过，不建议修改！ 你可以修改 ~/.vimrc 这个文件 （默认不存在，请你自行手动创建！），将你所希望的设置值写入！

```
[dmtsai@study ~]$ vim ~/.vimrc
"这个文件的双引号 （"） 是注解
set hlsearch            "高亮度反白
set backspace=2         "可随时用倒退键删除
set autoindent          "自动缩排
set ruler               "可显示最后一列的状态
set showmode            "左下角那一列的状态
set nu                  "可以在每一列的最前面显示行号啦！
set bg=dark             "显示不同的底色色调
syntax on               "进行语法检验，颜色显示。
```
