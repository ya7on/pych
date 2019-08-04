"""Thread tests."""

from py2ch.thread import Thread


def test_thread_success():
    """Test successful work of Thread."""
    thread_data = {
        'board': 'test',
        'comment': 'Test comment',
        'lasthit': 1564943807,
        'num': '1488',
        'posts_count': 228,
        'score': 0.4815162342,
        'subject': 'Test subject',
        'timestamp': 1498755907,
        'views': 420,
    }

    thread = Thread(**thread_data)

    assert thread.board == thread_data['board']
    assert thread.comment == thread_data['comment']
    assert thread.lasthit == thread_data['lasthit']
    assert thread.num == thread_data['num']
    assert thread.posts_count == thread_data['posts_count']
    assert thread.score == thread_data['score']
    assert thread.subject == thread_data['subject']
    assert thread.timestamp == thread_data['timestamp']
    assert thread.views == thread_data['views']

    assert thread.url == '/{board}/{num}.html'.format(
        board=thread_data['board'],
        num=thread_data['num'],
    )
