import allure
import pytest
import yaml

from test_pytest.core.calc import Calc


def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        keys = ",".join(data[0].keys())
        values = [list(d.values()) for d in data]
        data = {'keys': keys, 'values': values}
        return data


class TestCalc:
    #平时推荐使用这个方法
    def setup_class(self):
        print("setup_class")
        self.calc = Calc()

    data = load_data()

    # 优先执行，会override实例方法
    @classmethod
    def setup_class(cls):
        print("setup_class classmethod")

        cls.calc = Calc()

    def setup(self):
        pass

    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
        allure.attach.file(
            # 'https://ceshiren.com/uploads/default/original/2X/c/c49051f32076a3903e1a56a0bde6199bddd5f07b.jpeg',
            '/Users/seveniruby/Dropbox/sihanjishu/startup/霍格沃兹测试学院/banner/python自动化测试训练营.png',
            "测试访谈",
            attachment_type=allure.attachment_type.PNG
        )
        self.simple_step(f'{a} {b} {c}')
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

    # # 正常值例子
    # @pytest.mark.parametrize('a, b, c', [
    #     [2, 2, 1],
    #     [0.2, 0.1, 2],
    #     [0, 2, 0]
    # ])

    @pytest.mark.parametrize(
        data['keys'],
        data['values']
    )
    def test_div_data(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2
