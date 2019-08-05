"""Module for board catalog."""

from typing import List

import requests

from pych.thread import Thread


class Catalog(object):
    """Class for getting threads in specified board."""

    def __init__(self, board: str) -> None:
        """Prepare environment."""
        self.board: str = board

    @property
    def threads(self) -> List[Thread]:
        """Threads list."""
        api_url = 'https://2ch.hk/{0}/threads.json'.format(self.board)
        request_data = requests.get(api_url)
        json_data = request_data.json()

        threads_list = json_data['threads']

        return [
            Thread(thread_info, board=self.board)
            for thread_info in threads_list
        ]

    def __repr__(self) -> str:
        """Visual presentation of class object."""
        return '<Catalog board="{board}">'.format(
            board=self.board,
        )
