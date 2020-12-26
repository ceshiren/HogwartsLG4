from datetime import datetime

import requests


def test_testcase_get():
    testcase_url = 'http://127.0.0.1:5000/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f'case1 {datetime.now().isoformat()}',
            'description': 'description 1',
            'steps': ['1', '2', '3']
        }
    )

    assert r.status_code == 200

    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_task():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'testcases': [1, 2, 3]
        }
    )
    assert r.status_code == 200
    assert r.json()['msg'] == 'ok'


def test_task_run():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.put(
        task_url,
        json={
            'id': 1
        }
    )
    assert r.status_code == 200
    print(r.json())
    assert r.json()['msg'] == 'ok'
