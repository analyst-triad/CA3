from main import square, sub, div

def test_square():
    assert 4 == square(2)
def test_sub():
    assert 1 == sub(4)
def test_div():
    assert 2 == div(4,2)