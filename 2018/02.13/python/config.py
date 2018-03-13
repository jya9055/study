import configparser

config = configparser.ConfigParser()
config.read('../../config.ini')

def get_config(config):
    client_id = config.get('gAPI', 'client_id')
    client_secret = config.get('gAPI', 'client_secret')
    grant_type = config.get('gAPI', 'grant_type')
    return 'client_id={0}&client_secret={1}&grant_type={2}'.format(client_id, client_secret, grant_type)

# d = get_config(config)
# print(d)