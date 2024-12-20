
from main import summ, razn


def test_summ():
    assert summ(2, 3) == 5
    assert summ(-1, 1) == 0
    assert summ(0, 0) == 0

def test_razn():
    assert razn(2,3) == -1
    assert razn(10,4) == 6
    assert razn(4,6) == -2