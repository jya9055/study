import requests, base64
import config

id = config.GAPI_CONFIG['client_id']
secret = config.GAPI_CONFIG['client_secret']
type = config.GAPI_CONFIG['grant_type']

class GapiClass:
    def __init__(self, host='https://gapi.gabia.com'):
        self.host = host
        self.data = {'client_id': id, 'client_secret': secret, 'grant_type': type}
        self.headers = self.encoded_token()

    def Requests_get(self, url):
        r = requests.get('{0}{1}'.format(self.host, url), headers = self.headers)
        j = r.json()
        return j

    def Requests_post(self, url):
        r = requests.post('{0}{1}'.format(self.host, url), data = self.data)
        j = r.json()
        return j

    def getToken(self):
        j = self.Requests_post('/oauth/token')
        token_1 = j['access_token']
        token_2 = 'www_front:{0}'.format(token_1) 
        return token_2

    def makeHeadersAuth(self, token):
        encoded_text = token.encode()
        k = base64.b64encode(encoded_text)
        l = k.decode()
        return {'Authorization': 'Basic {0}'.format(l)}

    def encoded_token(self):
        return self.makeHeadersAuth(self.getToken())

    def getMember(self, id):
        j = self.Requests_get('/members?user_id={0}'.format(id))
        hanname = j['client_info']['hanadmin']
        return hanname

api1 = GapiClass()
a = api1.getMember('planning_d')
print(a)

