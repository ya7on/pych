"""Module for post info."""

from typing import List

from pych.file import File


class Post(object):
    """Class for thread post."""

    def __init__(self, **kwargs) -> None:
        """Parse post info data."""
        self.board: str = kwargs['board']
        self.banned: int = kwargs['banned']
        self.closed: int = kwargs['closed']
        self.comment: str = kwargs['comment']
        self.date: str = kwargs['date']
        self.email: str = kwargs['email']
        self.endless: int = kwargs['endless']
        self.files: List[File] = [
            File(**file_info)
            for file_info in kwargs['files']
        ]
        self.lasthit: int = kwargs['lasthit']
        self.name: str = kwargs['name']
        self.num: int = kwargs['num']
        self.number: int = kwargs['number']
        self.op: int = kwargs['op']
        self.parent: str = kwargs['parent']
        self.sticky: int = kwargs['sticky']
        self.subject: str = kwargs['subject']
        self.timestamp: int = kwargs['timestamp']
        self.trip: str = kwargs['trip']

    def __repr__(self) -> str:
        """Visual presentation of class object."""
        return '<Post #{num}>'.format(
            num=self.num,
        )
