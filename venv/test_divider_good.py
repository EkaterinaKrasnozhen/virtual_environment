import pytest
from utils import divider

@pytest.mark.parametrize('x, b, expected_result',[(10,2,5),
                                                  (10,5,2),
                                                  (10,10,1),
                                                  10,-5,-2])


def test_divider_good(x,b,expected_result):
    assert divider(x,b) == expected_result
    
    

try:
    print(divider(10,0))

except ZeroDivisionError:
    print('на ноль делить нельзя')
    
except TypeError:
    print('введите число')