import pytest
import yaml
from pytestHomework.lesson1_homework.test_calcu import addition, subtraction, multiplication, division


# 加法
@pytest.fixture(scope="function")
@pytest.mark.parametrize("a, b, expected_result", [(1, 2, 3),
                                                   (-1, 3, 2),
                                                   (100, 0.44, 100.44)])
def test_addition(a, b, expected_result):
    actual_result = addition(a, b)
    assert expected_result == actual_result


# 减法
@pytest.fixture()
@pytest.mark.parametrize('a, b, expected_result', [(9, 2, 7),
                                                   (10, 2.3, 7.7),
                                                   (-4, -2, -6)])
def test_subtraction(a, b, expected_result):
    actual_result = subtraction(a, b)
    assert expected_result == actual_result


# 乘法
@pytest.fixture()
@pytest.mark.parametrize('a, b, expected_result', [(9, 2, 18),
                                                   (10, 2.3, 23.0),
                                                   (-4, -2, 8)])
def test_multiplication(a, b, expected_result):
    actual_result = multiplication(a, b)
    assert expected_result == actual_result


# 除法
@pytest.fixture()
@pytest.mark.parametrize('a, b, expected_result', [(8, 2, 4),
                                                   (10, 2.5, 4),
                                                   (4, -2, -2)])
def test_division(a, b, expected_result):
    try:
        actual_result = division(a, b)
    except ZeroDivisionError as e:
        print(e, '被除数不能为0')
    assert expected_result == actual_result
