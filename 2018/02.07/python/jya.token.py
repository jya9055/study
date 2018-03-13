import requests, configparser

config = configparser.ConfigParser()
config.read('../../config.ini')

id = config['gAPI']['client_id']
secret = config['gAPI']['client_secret']
type = config['gAPI']['grant_type']

data = {'client_id': '{0}', 'client_secret': '{1}', 'grant_type': '{2}'.format(id, secret, type)}

r = requests.post('https://gapi.gabia.com/oauth/token', data=data)
# print(r)

j = r.json()
# print(j)

token = j['access_token']
# print(token)
