# 控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
# 减法依赖加法， 除法依赖乘法

import pytest


class TestOrdering:
    # 第1顺位跑且被"test_subtraction" 减法依赖 -- 执行成功，正常输出 --dependency不加name验证
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    @pytest.mark.parametrize('a, b, expected_result', [(1, 2, 3),
                                                       (-1, 3, 2),
                                                       (100, 0.44, 100.44)],
                             ids=[i for i in range(3)])
    def test_addition(self, a, b, expected_result):
        assert expected_result == a + b

    # 第3顺位跑且被"test_division"依赖 ，该方法case fail return false -- 执行失败， 正常输出，--dependency 加name验证
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="test_m")
    @pytest.mark.parametrize('a, b, expected_result', [(9, 2, 18),
                                                       (10, 2.3, 23.0),
                                                       (-4, -2, 6)],
                             ids=[i for i in range(3)])
    def test_multiplication(self, a, b, expected_result):
        assert expected_result == a * b

    # 第2顺位跑且依赖"test_addition" --执行成功，正常输出
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expected_result', [(9, 2, 7),
                                                       (10, 2.3, 7.7),
                                                       (-4, -2, -2)],
                             ids=[i for i in range(3)])
    @pytest.mark.dependency(depends=["test_addition"])
    def test_subtraction(self, a, b, expected_result):
        assert expected_result == a - b

    # 第4顺位跑且依赖"test_multiplication" --不执行成功，不输出
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expected_result', [(8, 2, 4),
                                                       (10, 2.5, 4),
                                                       (4, -2, -2)],
                             ids=[i for i in range(3)])
    @pytest.mark.dependency(depends=["test_m"])
    def test_division(self, a, b, expected_result):
        try:
            assert expected_result == a / b
        except ZeroDivisionError as e:
            print(e, '被除数不能为0')


if __name__ == 'main':
    pytest.main()
