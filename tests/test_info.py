"""Info functions test."""

from pych.info import boards


def test_boards():
    """Test `boards` function."""
    boards_list = boards()

    for board_id in boards_list:
        assert board_id
        assert isinstance(board_id, str)

        board_name = boards_list[board_id]
        assert board_name
        assert isinstance(board_name, str)
