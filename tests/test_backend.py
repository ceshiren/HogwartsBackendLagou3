from unittest import TestCase

import requests


class TestUserApi(TestCase):
    def test_post(self):
        r=requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby'
        })
        print(r.text)
        assert r.status_code == 200
        assert r.json()['msg'] == 'login success'

        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby2'
        })

        print(r.text)
        assert r.status_code == 200
        assert r.json()['msg'] == 'login fail'



