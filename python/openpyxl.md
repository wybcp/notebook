## freeze entire header
https://stackoverflow.com/questions/25588918/how-to-freeze-entire-header-row-in-openpyxl#

Make sure cell isn't on row one - freeze_panes will freeze rows above the given cell and columns to the left.
```
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
c = ws['B2']
ws.freeze_panes = c
wb.save('test.xlsx')
```
