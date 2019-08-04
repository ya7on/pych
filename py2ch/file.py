"""Module for files."""

from typing import Optional


class File(object):
    """Class for files."""

    def __init__(self, **kwargs):
        """Parse file info data."""
        self.displayname: str = kwargs['displayname']
        self.fullname: str = kwargs['fullname']
        self.height: int = kwargs['height']
        self.md5: str = kwargs['md5']
        self.name: str = kwargs['name']
        self.nsfw: int = kwargs['nsfw']
        self.path: str = kwargs['path']
        self.size: int = kwargs['size']
        self.thumbnail: str = kwargs['thumbnail']
        self.tn_height: int = kwargs['tn_height']
        self.tn_width: int = kwargs['tn_width']
        self.type: int = kwargs['type']
        self.width: int = kwargs['width']

        # For video only
        self.duration: Optional[int] = kwargs.get('duration')
        self.duration_secs: Optional[int] = kwargs.get('duration_secs')
