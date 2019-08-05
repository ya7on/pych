"""Module for files."""

from typing import Optional

from mypy_extensions import TypedDict

FileInfo = TypedDict(
    'FileInfo',
    {
        'displayname': str,
        'fullname': str,
        'height': int,
        'md5': str,
        'name': str,
        'nsfw': int,
        'path': str,
        'size': int,
        'thumbnail': str,
        'tn_height': int,
        'tn_width': int,
        'type': int,
        'width': int,
        'duration': Optional[int],
        'duration_secs': Optional[int],
    },
)


class File(object):
    """Class for files."""

    def __init__(self, file_info: FileInfo) -> None:
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
