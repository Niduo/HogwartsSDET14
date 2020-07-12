import pytest
import sys


# 加法
@pytest.mark.add
@pytest.mark.parametrize('a, b, result', [(1, 2, 3), (-1, 3, 2), (100, 0.44, 100.44)])
def test_addition(a, b, result):
    print(f"加法开始 {sys._getframe().f_code.co_name}")
    assert result == a + b
    print(f"加法结束,{a} + {b}  结果是 {result}")


# 减法
@pytest.mark.sub
@pytest.mark.parametrize('a, b, result', [(9, 2, 7), (10, 2.3, 7.7), (-4, -2, -2)])
def test_subtraction(a, b, result):
    print(f"减法开始 {sys._getframe().f_code.co_name}")
    assert result == a - b
    print(f"减法结束,{a} - {b}  结果是 {result}")


# 乘法
@pytest.mark.mul
@pytest.mark.parametrize('a, b, result', [(9, 2, 18), (10, 2.3, 23.0), (-4, -2, 8)])
def test_multiplication(a, b, result):
    print(f"乘法开始 {sys._getframe().f_code.co_name}")
    assert result == a * b
    print(f"乘法结束,{a} * {b}  结果是 {result}")


# 除法
@pytest.mark.div
@pytest.mark.parametrize('a, b, result', [(8, 2, 4), (10, 2.5, 4), (4, -2, -2)])
def test_division(a, b, result):
    try:
        print(f"除法开始 {sys._getframe().f_code.co_name}")
        assert result == a / b
        print(f"除法结束,{a} / {b}  结果是 {result}")
    except ZeroDivisionError as e:
        print(e, '被除数不能为0')
    assert result == a / b
