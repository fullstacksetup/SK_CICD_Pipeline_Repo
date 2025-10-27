from src.main import add, subtract

def test_add():
    assert add(1,2) == 3
    assert add(3,4) == 7
    assert add(0,0) == 0

def test_subtract():
    assert subtract(2,2) == 0
    assert subtract(5,4) == 1
    assert subtract(1,0) == 1