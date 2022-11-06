from utils import sum_float
from utils import multi_N
import pytest

#pytest -v tests.py::


#тестрируем sum_float
@pytest.mark.parametrize('x, expected_result',[('123',6),
                                                  ('234',9),
                                                  ('65',11),
                                                  ('55',10)])
def test_sum_float(x, expected_result):
    assert sum_float(x) == expected_result
    

#тестируем sum_float на ошибку 'int' object is not iterable    
@pytest.mark.parametrize('expected_exeption, sum', [(TypeError, 123)])
def test_sum_float_with_error(expected_exeption, sum):
    with pytest.raises(expected_exeption):
        sum_float(sum)
        

#тестируем multi_N        
@pytest.mark.parametrize('x, expected_result',[(3, [1, 2, 6]),
                                                  (5, [1, 2, 6, 24, 120])])
def test_multi_N(x, expected_result):
    assert multi_N(x) == expected_result
    

#тестриуем multi_N с TypeError 'str'   
@pytest.mark.parametrize('expected_exeption, num', [(TypeError, 'b')])
def test_multi_N_with_error(expected_exeption, num):
    with pytest.raises(expected_exeption):
        multi_N(num)