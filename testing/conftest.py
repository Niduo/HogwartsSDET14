import pytest


@pytest.fixture()
def print_method():
    print("【开始计算】")
    yield
    print("【计算结束】")
