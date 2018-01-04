#!/usr/bin/env python

import requests
import json


url = '127.0.0.1'

def login():
    endpoint = '/login'
    headers = {'content-type': 'application/json'}
    data = {
        'username': 'admin',
        'password': 'admin'
    }

    content = json.dumps(data)

    r = requests.post(url+endpoint, headers=headers, data=content)
    
    print(r)