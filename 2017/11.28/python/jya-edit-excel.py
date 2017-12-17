# 환불 필드 E4부터 E10까지 +2

from openpyxl import load_workbook

wb = load_workbook('../datas/daily_gabia_20171127.xlsx')
ws = wb.active


# 환불 데이터 가져오기
for r in ws.rows:
    row_idx = r[4].row
    k = r[4].value
    if k in [2, 0, 12, 21, 8, 18]: 
        # 위 조건이 없을 경우, E1, E2, E3이 숫자가 아니어서 오류가 남
        # if k in int 처럼 정수면 더하라는 조건을 추가하고 싶었으나, 못 찾아서 위처럼 처리
        p = k + 2

        # 2 더한 값 넣기
        ws.cell(row = row_idx, column=5).value = p
        # 근데 r[4]랑 column=5는 같은 의미 아닌가요???

    else: #else일 때 그냥 넘어가는 걸 어떻게 쓰나요??? return만 쓰면 빠져나온다고 했는데 outside function 오류남
        print("ddd")


wb.save('../datas/daily_gabia_20171127_edit.xlsx')