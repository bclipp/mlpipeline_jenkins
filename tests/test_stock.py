import stock

import pytest

TESTDATA = [(2, 2, 4)]


@pytest.mark.parametrize("x,y,wanted", TESTDATA)
def test_hello_name(x, y, wanted):
    sum: str = adder.add(x, y)
    print(f"sum {sum} wanted {wanted}")
    assert sum == wanted