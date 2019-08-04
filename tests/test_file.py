"""File tests."""

from py2ch.file import File


def test_file_success():
    """Test successful work of File."""
    file_info = {
        'displayname': 'video.mp4',
        'duration': '00:00:19',
        'duration_secs': 19,
        'fullname': 'video.mp4',
        'height': 640,
        'md5': 'md5hash',
        'name': 'video.mp4',
        'nsfw': 0,
        'path': '/b/src/1/2.mp4',
        'size': 1488,
        'thumbnail': '/b/thumb/1/2.jpg',
        'tn_height': 320,
        'tn_width': 240,
        'type': 10,
        'width': 480,
    }

    file_instance = File(**file_info)

    assert file_instance.displayname == file_info['displayname']
    assert file_instance.duration == file_info['duration']
    assert file_instance.duration_secs == file_info['duration_secs']
    assert file_instance.fullname == file_info['fullname']
    assert file_instance.height == file_info['height']
    assert file_instance.md5 == file_info['md5']
    assert file_instance.name == file_info['name']
    assert file_instance.nsfw == file_info['nsfw']
    assert file_instance.path == file_info['path']
    assert file_instance.size == file_info['size']
    assert file_instance.thumbnail == file_info['thumbnail']
    assert file_instance.tn_height == file_info['tn_height']
    assert file_instance.tn_width == file_info['tn_width']
    assert file_instance.type == file_info['type']
    assert file_instance.width == file_info['width']
