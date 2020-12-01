import json

import requests



#todo: 代码冗余
#todo: 与底层框架耦合太多
#todo: 封装层次不足，不利于管理
from service.tag import Tag

def test_tag_get():
    tag=Tag()
    tag.get_token()

    r = tag.list()
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    group_name = "group_demo_1201"
    tag_names = [{'name': 'tag_demo_1201'}]
    r=tag.add(group_name, tag_names)
    assert r.status_code == 200
    # assert r.json()['errcode'] == 0

    r = tag.list()
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    group=[group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
    tags=[{'name': tag['name']} for tag in group['tag']]
    print(group)
    print(tags)
    assert group['group_name'] == group_name
    assert tags == tag_names
