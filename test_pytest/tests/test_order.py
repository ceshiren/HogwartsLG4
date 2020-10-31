import pytest


class TestPytest(object):

    @pytest.mark.run(order=-1)
    def test_two(self, session_init):
        print("test_two")

    @pytest.mark.run(order=-3)
    def test_one(self):
        print("test_one")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("test_three")