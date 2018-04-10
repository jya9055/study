class GapiClass:
    def __init__(self, host='https://gapi.gabia.com'):
        self.host = host
    
    def getToken(self):
        r = requests.post('{0}/oauth/token'.format(self.host), data={'client_id': id, 'client_secret': secret, 'grant_type': type})
        j = r.json()
        token_1 = j['access_token']
        token_2 = 'www_front:{0}'.format(token_1) 
        return token_2

    def makeHeadersAuth(self, token):
        encoded_text = token.encode()
        k = base64.b64encode(encoded_text)
        l = k.decode()
        return 'Basic {0}'.format(l)

    def getMember(self, id):
        r = requests.get('{0}/members?user_id={1}'.format(self.host, id), headers=headers)
        j = r.json()
        hanname = j['client_info']['hanadmin']
        return hanname

api1 = GapiClass()
k = api1.getMember('planning_d')

