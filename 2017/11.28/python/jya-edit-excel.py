# 환불 필드 E4부터 E10까지 +2

from openpyxl import load_workbook

wb = load_workbook('../datas/daily_gabia_20171127.xlsx')
ws = wb.active

def edit(a):
    return  a + 2


c1 = ws['E4']
d = c1.value
k = edit(d)
ws['E4'] = k

c2 = ws['E5']
d = c2.value
k = edit(d)
ws['E5'] = k

c3 = ws['E6']
d = c3.value
k = edit(d)
ws['E6'] = k

c4 = ws['E7']
d = c4.value
k = edit(d)
ws['E7'] = k

c5 = ws['E8']
d = c5.value
k = edit(d)
ws['E8'] = k

c6 = ws['E9']
d = c6.value
k = edit(d)
ws['E9'] = k

c7 = ws['E10']
d = c7.value
k = edit(d)
ws['E10'] = k

##A = ws['E4':'E10']
#for t in A:
#    for c in t:
#        d = c.value
#        t = edit(d)
#        for i in range (0, 7):
#            A[i] = t

wb.save('../datas/daily_gabia_20171127_edit.xlsx')