import json

import requests

corpid='wwd6da61649bd66fea'
corpsecret='heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU'

def test_tag_get():
    r=requests.get(
        ' https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret }
    )
    print(json.dumps(r.json(), indent=2))
    token=r.json()['access_token']

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
