money = 100000

while money:
    print("퀀텀 구매합니다")
    money = money - getPrice(qtum)
    if money < getPrice(qtum):
        break



def tradingBot():
    import threading

    end = False

    def execute_func(second=60.0):
        global end
        if end:
            return
        elif :
            return '풀매도'
        elif:
            if money > getPrice(qtum):
                return '풀매수'
        else:
            return '존버'
        threading.Timer(second, execute_func, [second]).start()

    execute_func(60.0)
        
        if (1):
            return '소고기'
        else:
            return '한강'