# Let do it!
from openpyxl import load_workbook

wb = load_workbook('../datas/daily_gabia_20171127.xlsx') # 엑셀 열기
ws = wb.active # 현재 워크시크 가져오기


E = ws['E4':'E10'] 

column_idx = 5

for t in E: # ( (), () )
    row_idx = t[0].row # 현재 행 index
    print('row_idx: {0}'.format(row_idx))
    for c in t: # t는 튜플 ( )
        print('now_value: {0}'.format(c.value))
        ws.cell(row=row_idx, column=column_idx).value = c.value + 2

wb.save('../datas/lsh-edit.xlsx') # 엑셀 파일 저장
wb.close()