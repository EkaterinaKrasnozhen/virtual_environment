import pytest
from utils import divider
# запуск теста
# pytest -v test_division.py::test_division_good - один из
# pytest test_division.py
# python -m pytest test_division.py
# python -m pytest -v test_division.py

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         divider(10,0)

        
# def test_type_error():
#     with pytest.raises(TypeError):
#         divider(10,'b')
        

@pytest.mark.parametrize('expected_exeption, division_n, devider', [(ZeroDivisionError, 100, 0),
                                                                 (TypeError, 100, 'b')])
def test_division_with_error(expected_exeption, division_n, devider):
    with pytest.raises(expected_exeption):
        divider(division_n, devider)