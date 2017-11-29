# 환불 필드 E4부터 E10까지 +2

from openpyxl import load_workbook

wb = load_workbook('../datas/daily_gabia_20171127.xlsx')
ws = wb.active

ws['E4:E10'] =+ 2

wb.save('../datas/jya-edit.xlsx')