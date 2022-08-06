from collections import defaultdict
import requests
import api_access


class DefaultDict(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)


def get_game_ids(game_name):
    url = "https://api.twitch.tv/helix/games"
    data = {'name': game_name}
    response = requests.get(url, headers=api_access.headers, params=data)
    return response.json()['data'][0]['id']

game_ids = DefaultDict(lambda key: get_game_ids(key))