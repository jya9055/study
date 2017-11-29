```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 'jya9055'

wb.save('../datas/jya-save.xlsx') 