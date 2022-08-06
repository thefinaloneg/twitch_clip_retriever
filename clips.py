import datetime
import api_access
import key
import requests
import constants


def get_clips(game_id, days_before=1, num_top_clips=1):
    delta = datetime.timedelta(days=days_before)
    time = (datetime.datetime.now() - delta).isoformat('T') + 'Z'
    url = 'https://api.twitch.tv/helix/clips'
    data = {'game_id': game_id, 'started_at': time}
    response = requests.get(url, headers=api_access.headers, params=data)
    clips_list = []
    for i in range(num_top_clips):
        clips_list.append(response.json()['data'][i]['url'])
    return clips_list


#print(get_clips(constants.game_ids['League of Legends'], 1, 5))
