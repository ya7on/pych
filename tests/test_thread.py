"""Thread tests."""

from pych.catalog import Catalog
from pych.post import Post
from pych.thread import Thread


def test_thread_success():
    """Test successful work of Thread."""
    thread_data = {
        'comment': 'Test comment',
        'lasthit': 1564943807,
        'num': '1488',
        'posts_count': 228,
        'score': 0.4815162342,
        'subject': 'Test subject',
        'timestamp': 1498755907,
        'views': 420,
    }

    thread = Thread(thread_data, board='test')

    assert thread.board == 'test'
    assert thread.comment == thread_data['comment']
    assert thread.lasthit == thread_data['lasthit']
    assert thread.num == thread_data['num']
    assert thread.posts_count == thread_data['posts_count']
    assert thread.score == thread_data['score']
    assert thread.subject == thread_data['subject']
    assert thread.timestamp == thread_data['timestamp']
    assert thread.views == thread_data['views']

    assert thread.url == '/{board}/{num}.html'.format(
        board='test',
        num=thread_data['num'],
    )

    assert str(thread) == '<Thread board="test" #1488 "Test subject">'


def test_thread_with_connection():
    """Test Thread with connection to 2ch."""
    catalog = Catalog('test')
    thread = catalog.threads[0]

    assert isinstance(thread, Thread)

    posts_list = thread.posts
    assert isinstance(posts_list, list)
    for post in posts_list:
        assert isinstance(post, Post)
