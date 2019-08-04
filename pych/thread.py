"""Module for threads."""

from typing import List

import requests

from pych.post import Post


class Thread(object):
    """Thread object."""

    def __init__(self, **kwargs) -> None:
        """Parse kwargs arguments."""
        self.board: str = kwargs['board']
        self.comment: str = kwargs['comment']
        self.lasthit: int = kwargs['lasthit']
        self.num: str = kwargs['num']
        self.posts_count: int = kwargs['posts_count']
        self.score: float = kwargs['score']
        self.subject: str = kwargs['subject']
        self.timestamp: int = kwargs['timestamp']
        self.views: int = kwargs['views']

        self.url = '/{board}/{num}.html'.format(
            board=self.board,
            num=self.num,
        )

    @property
    def posts(self) -> List[Post]:
        """Thread posts list."""
        api_url = 'https://2ch.hk/{board}/res/{num}.json'.format(
            board=self.board,
            num=self.num,
        )

        request_data = requests.get(api_url)
        json_data = request_data.json()

        posts_list = json_data['threads'].pop()['posts']

        return [
            Post(board=self.board, **post_info)
            for post_info in posts_list
        ]

    def __repr__(self) -> str:
        """Visual presentation of class object."""
        max_subject_length = 32

        return '<Thread board="{board}" #{num} "{subject}">'.format(
            board=self.board,
            num=self.num,
            subject=self.subject[:max_subject_length],
        )
