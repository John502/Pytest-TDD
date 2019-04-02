import pytest
from LineReader import read_from_file
from unittest.mock import MagicMock
from pytest import raises

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    # return for readline
    mock_file.readline = MagicMock(return_value="test_line")
    # return of open("/file/path")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returns_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = read_from_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test_line"

def test_throws_Exception_With_Bad_File(mock_open, monkeypatch):

    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = read_from_file("blah")