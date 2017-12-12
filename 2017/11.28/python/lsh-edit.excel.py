# Let do it!
from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string

wb = load_workbook('../datas/daily_gabia_20171127.xlsx') # 엑셀 열기
ws = wb.active # 현재 워크시크 가져오기

def edit(cell, append):
    for t in cell: # ( (), () )
        row_idx = t[0].row # 현재 행 index
        column_idx = column_index_from_string(t[0].column)
        row_value = t[0].value
        ws.cell(row=row_idx, column=column_idx).value = row_value + append

E = ws['E4':'E10'] 

edit(E, 3)

wb.save('../datas/lsh-edit.xlsx') # 엑셀 파일 저장
wb.close()