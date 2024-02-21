from hello import hello

def test_argument():
    assert hello("Vien") == "hello, Vien"

def test_default():
    assert hello() == "hello, world"
