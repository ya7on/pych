"""Module for files."""


class File(object):
    """Class for files."""

    def __init__(self, **kwargs):
        """Parse file info data."""
        self.displayname = kwargs['displayname']
        self.duration = kwargs['duration']
        self.duration_secs = kwargs['duration_secs']
        self.fullname = kwargs['fullname']
        self.height = kwargs['height']
        self.md5 = kwargs['md5']
        self.name = kwargs['name']
        self.nsfw = kwargs['nsfw']
        self.path = kwargs['path']
        self.size = kwargs['size']
        self.thumbnail = kwargs['thumbnail']
        self.tn_height = kwargs['tn_height']
        self.tn_width = kwargs['tn_width']
        self.type = kwargs['type']
        self.width = kwargs['width']
