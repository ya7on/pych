"""Module for files."""

from typing import Optional


class File(object):
    """Class for files."""

    def __init__(self, file_info):
        """Parse file info data."""
        self.displayname: str = file_info['displayname']
        self.fullname: str = file_info['fullname']
        self.height: int = file_info['height']
        self.md5: str = file_info['md5']
        self.name: str = file_info['name']
        self.nsfw: int = file_info['nsfw']
        self.path: str = file_info['path']
        self.size: int = file_info['size']
        self.thumbnail: str = file_info['thumbnail']
        self.tn_height: int = file_info['tn_height']
        self.tn_width: int = file_info['tn_width']
        self.type: int = file_info['type']
        self.width: int = file_info['width']

        # For video only
        self.duration: Optional[int] = file_info.get('duration')
        self.duration_secs: Optional[int] = file_info.get('duration_secs')
