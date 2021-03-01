"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/1 9:04 下午'
"""
import pytest


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_mm(name):
    print(name)
