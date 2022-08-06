import string
import random
import requests
import key


def get_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    data = {'client_id': key.client_id, 'client_secret': key.client_secret, 'grant_type': 'client_credentials'}
    response = requests.post(url, data=data)
    return response.json()['access_token']

headers = {'Client-id': key.client_id, 'Authorization': 'Bearer ' + get_access_token()}


# def id_generator(size=32, chars=string.ascii_lowercase + string.digits):
# return ''.join(random.choice(chars) for _ in range(size))
