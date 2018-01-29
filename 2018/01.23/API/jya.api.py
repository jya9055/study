import requests

def getPrice(A): 
    # coin 파라미터  사용!
    # https://api.coinnest.co.kr/api/pub/ticker?coin=eth
    # https://api.coinnest.co.kr/api/pub/ticker?coin={변수}
    # .format()

	#. 문자형 .format() 인자값
	#. () 안에 들어오는 코인은 정해져 있고, 정해진 코인이 아닐 경우 false 리턴
	#. 정해진 코인을 입력한 경우, 해당 코인의 마지막 가격을 리턴
	
	r = requests.get('https://api.coinnest.co.kr/api/pub/ticker?coin={coin}'.format(A))
	j = r.json()
	A = j['coin']
	if A not in coin:
		return "false"
	else:
		return j["last"]

a = getPrice(qtum)
print(a)

