from main import square, sub, div, add

def test_square():
    assert 4 == square(2)
def test_sub():
    assert "1" == sub(4)
def test_div():
    assert 2 == div(4,2)
def test_add():
    assert "5" == add(3,2)