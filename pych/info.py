"""Help structures for library."""

from typing import Dict

import requests


def boards() -> Dict[str, str]:
    """Get list with all board names."""
    boards_list = {}

    api_url = 'https://2ch.hk/makaba/mobile.fcgi?task=get_boards'
    json_data = requests.get(api_url).json()

    for category in json_data:
        for board in json_data[category]:
            boards_list[board['id']] = board['name']

    return boards_list
