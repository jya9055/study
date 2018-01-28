import requests



def getprice(coin):
    r = requests.get('https://api.coinnest.co.kr/api/pub/ticker')
    j = r.json()
	coin = j["coin"]
	last = j["last"]
	co_list = [btc, bch, btg, bcd, eth, etc, ada, qtum, xlm, neo, gas, rpx, hsr, knc, tsl, tron, omg, wtc, mco, storm, gto, pxs, ink, hlc, ent, 	qbt, spc, put 
		if coin not in co_list
		    return "false"
		else:
			return j["last"]

a = getprice(qtum)
print(a)

