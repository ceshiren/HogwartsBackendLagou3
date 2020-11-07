import datetime
from time import time
from unittest import TestCase

import requests


class TestTestCaseApi:
    url = 'http://127.0.0.1:5000/testcase'

    def setup_class(self):
        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby'
        })
        print(r.text)
        assert r.status_code == 200
        assert r.json()['msg'] == 'login success'

        self.token = r.json()['access_token']

    def test_testcase_get(self):
        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )

        print(r.json())
        assert r.status_code == 200
        assert len(r.json()) >= 0

    def test_testcase_post(self):
        r = requests.post(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            },
            json={
                'name': 'testcase demo name' + str(datetime.datetime.now()),
                'data': 'click a; click b;'
            }
        )
        print(r.text)
        assert r.status_code == 200

        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )

        print(r.text)
        assert r.status_code == 200
        assert len(r.json()) >= 1

    def test_testcase_put(self):
        r = requests.post(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            },
            params={
                'id': 1
            },
            json={
                'data': 'click a1; click b2;'
            }
        )
        print(r.text)
        assert r.status_code == 200

        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )

        print(r.text)
        assert r.status_code == 200
        data=[testcase['data'] for testcase in r.json() if testcase['id'] == 1][0]
        # for testcase in r.json():
        #     if testcase.id == 1:
        #         data=testcase.data

        assert 'b2' in data



