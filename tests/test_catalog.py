"""Catalog tests."""

from py2ch.catalog import Catalog
from py2ch.thread import Thread


def test_catalog_success():
    """Test successful work of Catalog."""
    catalog_instance = Catalog('test')

    assert catalog_instance.board == 'test'

    threads_list = catalog_instance.threads
    mapped_threads = map(
        lambda thread: isinstance(thread, Thread),
        threads_list,
    )
    assert all(mapped_threads)
