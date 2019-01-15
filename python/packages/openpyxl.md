# openpyxl

excel 文件操作包

## [freeze entire header](https://stackoverflow.com/questions/25588918/how-to-freeze-entire-header-row-in-openpyxl#)

Make sure cell isn't on row one - freeze_panes will freeze rows above the given cell and columns to the left.

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
c = ws['B2']
ws.freeze_panes = c
wb.save('test.xlsx')
```

## [公式全部丢失的问题](https://hk.saowen.com/a/d41844a4c1fc53785ebc79fb6f637a54dd9aa4edceec08cbd93d78c5a26192a2)

通过调用系统安装的excel程序打开然后保存。

```python
import xlwings as xw
'''
https://docs.xlwings.org/en/stable/index.html
'''
if __name__ == '__main__':
    wb = xw.Book('xxx.xlsx')
    sht = wb.sheets['xxx']
    wb.save()
    wb.close()
```