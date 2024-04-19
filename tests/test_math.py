import pytest

def test_one_plus_one():
    assert 1 + 1 == 2

def test_one_plus_two():
    a = 2
    b = 1
    c = 3
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

#Test multiplication

products = [
    (2,3,6),
    (3,-4,-12),
    (-5,-5,25),
    (1,99,99),
    (0,99,0),
    (2.5,6.7,17.75)
]


@pytest.mark.parametrize('a, b, product', products)
def test_product(a,b,product):
    assert a*b == product