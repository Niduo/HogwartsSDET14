import pytest


# 控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
class TestOrdering:
    @pytest.mark.run(order=1)
    def test_add(self):
        pytest.assume(2 == 1 + 1)
        pytest.assume(3 == 1.3 + 1.7)

    @pytest.mark.run(order=3)
    def test_mul(self):
        pytest.assume(2 == 1 * 2)
        pytest.assume(4 == 2 * 2)

    @pytest.mark.run(order=2)
    def test_sub(self):
        pytest.assume(2 == 4 - 2)
        pytest.assume(-3 == 0 - 3)

    @pytest.mark.run(order=4)
    def test_div(self):
        pytest.assume(2 == 4 / 2)
        pytest.assume(3 == 9 / 3)


# 减法依赖加法， 除法依赖乘法
class TestDepends:
    @pytest.mark.dependency()
    def test_add(self):
        pytest.assume(4 == 1 + 1)
        pytest.assume(3 == 1.3 + 1.7)

    @pytest.mark.dependency()
    def test_mul(self):
        pytest.assume(2 == 1 * 2)
        pytest.assume(4 == 2 * 2)

    @pytest.mark.dependency(denpends="test_add")
    def test_sub(self):
        pytest.assume(2 == 4 - 2)
        pytest.assume(-3 == 0 - 3)

    @pytest.mark.dependency(depends="test_mul")
    def test_div(self):
        pytest.assume(2 == 4 / 2)
        pytest.assume(3 == 9 / 3)


if __name__ == 'main':
    pytest.main()
