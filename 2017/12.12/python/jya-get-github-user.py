import requests

#params = {'name':'', 'blog':''}
r = requests.get('https://api.github.com/users/jya9055')
j = r.json()

def getUser(id):
    return j['name'] + "/" + j['blog']
    if j['name'] == '':
        return j['login']
    if j['blog'] == '':
        return j['html_url']

d = getUser(id)
print(d)

