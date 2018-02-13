import requests

def makeHeadersAuth():
    
    

    return {'Authorization': 'Basic {key}'}

    def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': 'www_front', 'client_secret': 'eoqhfma', 'grant_type': 'client_credentials'})
    j = r.json()
    token = j['access_token']
    return token
    

