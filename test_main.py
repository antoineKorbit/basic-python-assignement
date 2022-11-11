
import main;

def test_main_return_correct():
    assert main.main() == "Hello World!"

def test_main_not_return_0():
    assert main.main() != 0
