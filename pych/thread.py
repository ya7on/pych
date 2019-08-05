"""Module for threads."""

from typing import List

import requests

from pych.post import Post


class Thread(object):
    """Thread object."""

    def __init__(self, thread_info, board) -> None:
        """Parse kwargs arguments."""
        self.board: str = board
        self.comment: str = thread_info['comment']
        self.lasthit: int = thread_info['lasthit']
        self.num: str = thread_info['num']
        self.posts_count: int = thread_info['posts_count']
        self.score: float = thread_info['score']
        self.subject: str = thread_info['subject']
        self.timestamp: int = thread_info['timestamp']
        self.views: int = thread_info['views']

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
            Post(post_info, board=self.board)
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
