import pytest
import yaml
from testing.test_calcu import addition, subtraction, multiplication, division


# 加法
@pytest.mark.usefixtures("print_method")
@pytest.mark.parametrize("a, b, expected_result", yaml.safe_load(open("./testParam/add.yaml")))
def test_addition(a, b, expected_result):
    actual_result = addition(a, b)
    assert expected_result == actual_result


# 减法
@pytest.mark.usefixtures("print_method")
@pytest.mark.parametrize('a, b, expected_result', yaml.safe_load(open("./testParam/sub.yaml")))
def test_subtraction(a, b, expected_result):
    actual_result = subtraction(a, b)
    assert expected_result == actual_result


# 乘法
@pytest.mark.usefixtures("print_method")
@pytest.mark.parametrize('a, b, expected_result', yaml.safe_load(open("./testParam/multi.yaml")))
def test_multiplication(a, b, expected_result):
    actual_result = multiplication(a, b)
    assert expected_result == actual_result


# 除法
@pytest.mark.usefixtures("print_method")
@pytest.mark.parametrize('a, b, expected_result', yaml.safe_load(open("./testParam/div.yaml")))
def test_division(a, b, expected_result):
    try:
        actual_result = division(a, b)
    except ZeroDivisionError as e:
        print(e, '被除数不能为0')
    assert expected_result == actual_result


if __name__ == '__main__':
    pytest.main()
