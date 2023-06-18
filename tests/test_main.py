from src import main


def test_main():
    assert main.main() != ''
    assert main.main() is not None
    assert type(main.main()) == list
    assert len(main.main()) == 5
