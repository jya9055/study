import requests

data = {'client_id': 'www_front', 'client_secret': 'eoqhfma', 'grant_type': 'client_credentials'}

r = requests.post('https://gapi.gabia.com/oauth/token', data=data)
# print(r)

j = r.json()
token = j['access_token']

print(token)