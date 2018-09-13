# [循环语句 else 子句作为可选选项](https://bop.mol.uno/09.control_flow.html)

else 子句作为可选选项。while 和 for in

```python
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
```

else 部分是可选的。当循环中包含他时，它总会在 for 循环结束后开始执行，除非程序遇到了 break 语句。

break 语句用以中断（Break）循环语句，如果你的中断了一个 for 或 while 循环，任何相应循环中的 else 块都将不会被执行。
