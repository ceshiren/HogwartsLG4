"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/1 8:17 下午'
"""
from typing import List

import pytest
import yaml


# def pytest_collection_modifyitems(session, config, items:List):
#     for item in items:
#         # item.name 用例的名字
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         # item.nodeid 用例的路径
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#
#         if 'login' in item.nodeid:
#             item.add_marker(pytest.mark.login)
#
#     items.reverse()

# 添加一个命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env", default='test')
    if env == 'test':
        print("test 环境")
        datapath = "datas/test/datas.yml"
    elif env == 'dev':
        print("开发 环境")
        datapath = "datas/dev/datas.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return env, datas
