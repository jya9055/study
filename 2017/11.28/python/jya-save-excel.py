```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 'yangahjo'

wb.save('../datas/jya-save.xlsx') 