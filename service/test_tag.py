import json
from datetime import datetime

import pytest
import requests

# todo: 代码冗余
# todo: 与底层框架耦合太多
# todo: 封装层次不足，不利于管理
from jsonpath import jsonpath

from service.tag import Tag


class TestTag:
    update_index_class=0

    def setup_class(self):
        # todo：数据清理的过程，把测试数据清空或者还原

        # 还原数据库，如果可以还原数据库，那么测试用例中是可以使用一些变化的tagid。否则不要硬编码这些tagid，一旦数据被清空，tagid就会失效。
        # 使用接口去清理数据
        # 使用接口去构建测试数据

        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear_all()
        self.update_index = 0
        print("update_index")
        print(self.update_index)

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

    @pytest.mark.parametrize("group_name, tag_names, need_group_id", [
        # 删除有效的单个标签
        ['group_delete_demo', [{'name': "tag_delete_demo_1"}], False],
        # 删除多个标签
        ['group_delete_demo', [{'name': "tag_delete_demo_2", 'name': "tag_delete_demo_3"}], False],
        # 删除整个组
        ['group_delete_demo', [{'name': 'tag_delete_demo_4'}], True],
        # 删除标签组，名字或者id
    ])
    def test_tag_delete(self, group_name, tag_names, need_group_id):
        self.tag.add(group_name, tag_names)
        r = self.tag.list()
        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tag_ids = [tag['id'] for tag in group['tag']]
        if need_group_id:
            group_id = group['group_id']
            tag_ids = None
        else:
            group_id = None

        self.tag.delete(group_id, tag_ids)
        r = self.tag.list()
        groups = [group for group in r.json()['tag_group'] if group['group_name'] == group_name]
        assert groups == []

    @pytest.mark.parametrize("name", [
        # 普通改名 加长
        'tag_test_update_name_1',
        # 缩短
        'tag_1',
        # 不变
        'tag_test_update_name',
        # 重名
        # 组名重名
        # 特殊字符

    ])
    def test_update_name(self, name):
        self.update_index += 1
        # doine: id一样 不要用实例变量就可以
        print(f"update_index={self.update_index}")
        tag_name = 'tag_test_update_name_' + str(datetime.now())[-5:]
        tag = [{'name': tag_name}]
        self.tag.add("group_test_update_name", tag)
        r = self.tag.list()
        tag_id = jsonpath(r.json(), f'$..[?(@.name=="{tag_name}")].id')[0]
        r = self.tag.update(tag_id, name)
        assert r.json()['errcode'] == 0
        r = self.tag.list()
        assert len(jsonpath(r.json(), f'$..[?(@.name=="{name}")].id')) == 1

    @pytest.mark.parametrize("order_id", [
        # [5,4,3,2,1]  标签/标签组的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)

    ])
    def test_update_order(self, order_id):
        pass

    def test_clear_all(self):
        r = self.tag.clear_all()
        assert len(r.json()['tag_group']) == 0

    def setup(self):
        self.update_index += 1

    @pytest.mark.parametrize('a', [1, 2, 3, 4, 5])
    def test_demo(self, a):
        self.update_index += 1
        TestTag.update_index_class+=1
        print(f"update_index={self.update_index}")
        print(f"update_index_class={self.update_index_class}")

# todo: 课后作业：丰富标签管理的测试用例，主要是list add delete接口，拔高点完善下数据清理的过程
