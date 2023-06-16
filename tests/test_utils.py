from src import utils


def test_open_file():
    assert utils.open_file() != ''
    assert utils.open_file() != 'None'


def test_get_executed():
    assert utils.get_executed() != ''
    assert utils.get_executed() != 'None'


def test_output():
    assert utils.output() != ''
    assert utils.output() != 'None'