import datetime
import api_access
import requests

def get_clips(game_id, days_before=1, num_top_clips=1):
    """Returns the top clips for a given game_id.

    Keyword arguments:
    game_id -- the game_id of the game to get clips for
    days_before -- the number of days before the current date to get clips for
    num_top_clips -- the number of top clips to get
    """
    delta = datetime.timedelta(days=days_before)
    time = (datetime.datetime.now() - delta).isoformat('T') + 'Z'
    url = 'https://api.twitch.tv/helix/clips'
    data = {'game_id': game_id, 'started_at': time}
    response = requests.get(url, headers=api_access.headers, params=data)
    clips_list = []
    for i in range(num_top_clips):
        clips_list.append(response.json()['data'][i]['url'])
    return clips_list

