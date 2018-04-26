from openpyxl import Workbook
import sys
sys.path.append('C:/Users/조양아/Documents/GitHub/study/2018/04.10/python')
from jya_gAPIclass import GapiClass
# 이 파일과 동일한 경로에 config.py 추가 안하면 오류가 나는데, 모듈 불러올 때 config.py는 같이 안불러오나봐요??

wb = Workbook()
ws = wb.active

instance = GapiClass()
id_list = ['planning_d', 'test1gabia', 'jya9055']

# for id in id_list:
#     number = 0
#     for k in (1, 2, 3):
#         number = number + 1
#         ws.cell(row=k, column=1).value = number
#         ws.cell(row=k, column=2).value = instance.getMember(id)

number = 0
for k in (1, 2, 3):
    number = number + 1
    ws.cell(row=k, column=1).value = number
    for id in id_list:
        ws.cell(row=k, column=2).value = instance.getMember(id)
        
wb.save('../datas/hanname-excel.xlsx')


# 내일 다시!!!