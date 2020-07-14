# 1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
# 2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
import pytest
from testing.pytestHomework.lesson2_homework1.target_func import addition, subtraction, multiplication, division


class TestTargetFunc:
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize("a, b, result", [(1, 2, 3),
                                              (-1, 0, -1),
                                              (9.1, 1, 10.1)],
                             ids=[f"第{i}组测试" for i in range(3)])
    def check_add(self, a, b, result):
        assert result == addition(a, b)
        pytest.assume(result == addition(2, 1))

    @pytest.mark.parametrize("a, b, result", [(1, 2, -1),
                                              (-1, 0, -1),
                                              (9.1, 1, 8.1)],
                             ids=[f"第{i}组测试" for i in range(3)])
    def check_sub(self, a, b, result):
        assert result == subtraction(a, b)

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize("a, b, result", [(1, 2, 2),
                                              (-1, 0, 0),
                                              (9.1, 1, 9.1)],
                             ids=[i for i in range(3)])
    def test_mul(self, a, b, result):
        assert result == multiplication(a, b)

    @pytest.mark.parametrize("a, b, result", [(1, 2, 0.5),
                                              (-1, 0, 0),
                                              (9.1, 1, 9.1)],
                             ids=[f"第{i}组测试" for i in range(3)])
    def test_div(self, a, b, result):
        try:
            assert result == division(a, b)
        except ZeroDivisionError as e:
            print(e, "can't be zero")
            return False


if __name__ == "__main__":
    pytest.main()
