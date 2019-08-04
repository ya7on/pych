"""Post tests."""

from pych.file import File
from pych.post import Post


def test_post_success():
    """Test successful work of Post."""
    post_info = {
        'board': 'test',
        'banned': 0,
        'closed': 0,
        'comment': 'Test comment',
        'date': '01/04/19 Пон 04:20:00',
        'email': 'mail@example.com',
        'endless': 0,
        'files': [
            {
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
            },
        ],
        'lasthit': 1564941726,
        'name': 'Аноним',
        'num': 1488,
        'number': 1,
        'op': 0,
        'parent': '0',
        'sticky': 0,
        'subject': 'Test subject',
        'tags': '',
        'timestamp': 1564940566,
        'trip': '',
    }

    post = Post(**post_info)

    assert post.board == post_info['board']
    assert post.banned == post_info['banned']
    assert post.closed == post_info['closed']
    assert post.comment == post_info['comment']
    assert post.date == post_info['date']
    assert post.email == post_info['email']
    assert post.endless == post_info['endless']
    assert post.lasthit == post_info['lasthit']
    assert post.name == post_info['name']
    assert post.num == post_info['num']
    assert post.number == post_info['number']
    assert post.op == post_info['op']
    assert post.parent == post_info['parent']
    assert post.sticky == post_info['sticky']
    assert post.subject == post_info['subject']
    assert post.timestamp == post_info['timestamp']
    assert post.trip == post_info['trip']

    assert all(map(
        lambda post_file: isinstance(post_file, File),
        post.files,
    ))
