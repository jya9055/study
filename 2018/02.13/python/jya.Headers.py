import requests


def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': 'www_front', 'client_secret': 'eoqhfma', 'grant_type': 'client_credentials'})
    j = r.json()
    token = j['access_token']
    return token

print (getToken())

def makeHeadersAuth(token):   
    auth = btoa('www_front:{0}'.format(token))
    print(auth)
    return {'Authorization': 'Basic {0}'.format(auth)}

