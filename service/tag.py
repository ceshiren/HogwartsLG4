import json

import requests

corpid = 'wwd6da61649bd66fea'
corpsecret = 'heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU'


class Tag:

    def __init__(self):
        self.token = ""

    def get_token(self):
        r = requests.get(
            ' https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        print(json.dumps(r.json(), indent=2))
        self.token = r.json()['access_token']

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def add(self, group_name, tags):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r
