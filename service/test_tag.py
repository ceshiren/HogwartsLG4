import json

import pytest
import requests

# todo: 代码冗余
# todo: 与底层框架耦合太多
# todo: 封装层次不足，不利于管理
from service.tag import Tag


class TestTag:
    def setup_class(self):
        # todo：数据清理的过程，把测试数据清空或者还原
        self.tag = Tag()
        self.tag.get_token()

    def test_tag_list(self):
        # todo: 完善功能测试
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group_demo_1201", [{'name': 'tag_demo_1201'}]],
        ["group_demo_1202", [{'name': 'tag_demo_1202'}, {'name': 'tag_demo_1203'}]],
    ])
    def test_tag_add(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        # assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    def test_tag_add_fail(self):
        pass

#todo: 课后作业：丰富标签管理的测试用例，主要是list add delete接口，拔高点完善下数据清理的过程


