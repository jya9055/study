from openpyxl import Workbook
import sys
sys.path.append('C:/Users/조양아/Documents/GitHub/study/2018/04.10/python')
from jya_gAPIclass import GapiClass
# 이 파일과 동일한 경로에 config.py 추가 안하면 오류가 나는데, 모듈 불러올 때 config.py는 같이 안불러오나봐요??

wb = Workbook()
ws = wb.active

instance = GapiClass()
id_list = ['planning_d', 'test1gabia', 'jya9055']
number = 0

# 입력 받은 리스트의 수만큼 각 열에 번호 - 이름 입력

ws.cell(row=1, column=1).value = '번호'
ws.cell(row=1, column=2).value = '아이디'
ws.cell(row=1, column=3).value = '이름'

while number < len(id_list):
    id = id_list[number]
    number += 1
    ws.cell(row=number+1, column=1).value = number
    ws.cell(row=number+1, column=2).value = id
    ws.cell(row=number+1, column=3).value = instance.getMember(id)



wb.save('../datas/hanname-excel.xlsx')