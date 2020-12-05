import json

import requests

corpid = 'wwd6da61649bd66fea'
corpsecret = 'heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU'

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}


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
            },
            proxies=proxies,
            verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, group_ids, tag_ids):
        if tag_ids is None:
            json_data = {
                'group_id': group_ids
            }
        else:
            json_data = {
                'tag_id': tag_ids,
                'group_id': group_ids
            }

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json=json_data,
            proxies=proxies,
            verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, tag_id, name, order_id=None):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.token},
            json={
                "id": tag_id,
                "name": name,
                "order": order_id
            },
            proxies=proxies,
            verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def clear_all(self):
        r = self.list()
        group_ids = [group['group_id'] for group in r.json()['tag_group']]
        if len(group_ids) > 0:
            self.delete(group_ids, None)
            return self.list()
        else:
            return r
