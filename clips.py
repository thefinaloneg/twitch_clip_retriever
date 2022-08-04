import datetime
import api_access
import key
import requests

game_ids = {'League of Legends': 21779}


def get_clips(game_id, days_before=1):
    delta = datetime.timedelta(days=days_before)
    time = (datetime.datetime.now() - delta).isoformat('T') + 'Z'
    url = 'https://api.twitch.tv/helix/clips'
    headers = {'Client-id': key.client_id, 'Authorization': 'Bearer ' + api_access.get_access_token()}
    data = {'game_id': game_id, 'started_at': time}
    response = requests.get(url, headers=headers, params=data)
    return response.json()['data']


print(get_clips(game_ids['League of Legends'], 1))
