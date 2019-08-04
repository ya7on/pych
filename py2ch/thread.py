"""Module for threads."""


class Thread(object):
    """Thread object."""

    def __init__(self, **kwargs):
        """Parse kwargs arguments."""
        self.board: str = kwargs.get('board')
        self.comment: str = kwargs.get('comment')
        self.lasthit: int = kwargs.get('lasthit')
        self.num: int = kwargs.get('num')
        self.posts_count: int = kwargs.get('posts_count')
        self.score: float = kwargs.get('score')
        self.subject: str = kwargs.get('subject')
        self.timestamp: int = kwargs.get('timestamp')
        self.views: int = kwargs.get('views')

    def __repr__(self) -> str:
        """Visual presentation of class object."""
        max_subject_length = 32

        return '<Thread board="{board}" #{num} "{subject}">'.format(
            board=self.board,
            num=self.num,
            subject=self.subject[:max_subject_length],
        )
