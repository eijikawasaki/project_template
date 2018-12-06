import src


def test_hello_word():
    """
    hello_word method unitary test
    :return:
    """
    template = src.ClassTemplate()
    assert template.hello_world() == "Hello world"
