import pytest

from test_pytest.core.calc import Calc


@pytest.fixture(scope='module')
def calc_init():
    print("setup_class")
    return Calc()