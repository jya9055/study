from openpyxl import Workbook
import sys
sys.path.append('C:/Users/조양아/Documents/GitHub/study/2018/04.10/python')
from jya_gAPI_class import GapiClass
# 이 파일과 동일한 경로에 config.py 추가 안하면 오류가 나는데, 모듈 불러올 때 config.py는 같이 안불러오나봐요??

wb = Workbook()
ws = wb.active

wb.save('../datas/hanname-excel.xlsx')

instance = GapiClass()
a = instance.getMember('planning_d')
print(a)

# 아직 다 안함