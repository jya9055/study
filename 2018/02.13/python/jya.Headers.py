import requests, base64


def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': 'www_front', 'client_secret': 'eoqhfma', 'grant_type': 'client_credentials'})
    j = r.json()
    token = j['access_token']
    return token

print (getToken())

def makeHeadersAuth(token):
    encoded_text = {0}.encode('base64').format(token)
    # 'set' object has no attribute 'encode' 이런 오류가 계속 남 ㅜㅜ
    return 'Basic {0}'.format(encoded_text)


token = 'NDBhZmE5NTEzYzA3N2Q1ZWY2Yzc5ZGJjN2U2MmQ5'
k = makeHeadersAuth(token)
print(k)
# 프린트 실패

# 한 번에 처리하는 함수 만들기
def encoded_token():
    return makeHeadersAuth(getToken())

# 함수 실행하기?
encoded_token()