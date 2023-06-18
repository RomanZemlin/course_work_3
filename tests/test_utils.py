from src import utils


def test_open_file():
    assert utils.open_file() != ''
    assert utils.open_file() is not None
    assert type(utils.open_file()) == list


def test_get_executed():
    assert utils.get_executed() != ''
    assert utils.get_executed() is not None
    assert type(utils.get_executed()) == list
    assert  len(utils.get_executed()) != len(utils.open_file())


def test_output():
    assert utils.output() != ''
    assert utils.output() is not None
    assert type(utils.output()) == list
    assert len(utils.output()) == 5
