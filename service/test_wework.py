import json

import requests

corpid = 'wwd6da61649bd66fea'
corpsecret = 'heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU'


#todo: 代码冗余
#todo: 与底层框架耦合太多
#todo: 封装层次不足，不利于管理

def test_tag_get():
    r = requests.get(
        ' https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    print(json.dumps(r.json(), indent=2))
    token = r.json()['access_token']

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token': token},
        json={
            'tag_id': []
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        params={'access_token': token},
        json={
            'group_name': 'group_demo_1201',
            'tag': [
                {
                    'name': 'tag_demo_1201'
                }
            ]
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token': token},
        json={
            'tag_id': []
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
