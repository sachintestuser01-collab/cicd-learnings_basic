from src.main import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(3, 2) == 5
    assert add(5, 5) == 10

def test_sub():
    assert sub(5, 2) == 3
    assert sub(4, 2) == 2
    assert sub(4, 3) == 1

def test_mul():
    assert mul(5, 2) == 10
    assert mul(4, 2) == 8
    assert mul(4, 3) == 12


def test_div():
    assert div(10, 2) == 5
    assert div(4, 2) == 2
    assert div(9, 3) == 3