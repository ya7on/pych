"""Module for post info."""

from typing import List

from pych.file import File


class Post(object):
    """Class for thread post."""

    def __init__(self, post_info, board) -> None:
        """Parse post info data."""
        self.board: str = board
        self.banned: int = post_info['banned']
        self.closed: int = post_info['closed']
        self.comment: str = post_info['comment']
        self.date: str = post_info['date']
        self.email: str = post_info['email']
        self.endless: int = post_info['endless']
        self.files: List[File] = [
            File(file_info)
            for file_info in post_info['files']
        ]
        self.lasthit: int = post_info['lasthit']
        self.name: str = post_info['name']
        self.num: int = post_info['num']
        self.number: int = post_info['number']
        self.op: int = post_info['op']
        self.parent: str = post_info['parent']
        self.sticky: int = post_info['sticky']
        self.subject: str = post_info['subject']
        self.timestamp: int = post_info['timestamp']
        self.trip: str = post_info['trip']

    def __repr__(self) -> str:
        """Visual presentation of class object."""
        return '<Post #{num}>'.format(
            num=self.num,
        )
