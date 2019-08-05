"""Catalog tests."""

from pych.catalog import Catalog
from pych.thread import Thread


def test_catalog_success():
    """Test successful work of Catalog."""
    catalog_instance = Catalog('test')

    assert str(catalog_instance) == '<Catalog board="test">'

    assert catalog_instance.board == 'test'

    threads_list = catalog_instance.threads
    mapped_threads = map(
        lambda thread: isinstance(thread, Thread),
        threads_list,
    )
    assert all(mapped_threads)
