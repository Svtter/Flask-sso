#!/usr/bin/env python

import requests
import json


url = 'http://127.0.0.1'
port = '5000'
url = url + ':' + port
tokenid = None
username = 'admin'
password = 'admin'
last_res = None

def login():
    endpoint = '/login'
    headers = {'content-type': 'application/json'}
    data = {
        'username': username,
        'password': password
    }

    content = json.dumps(data)

    r = requests.post(url+endpoint, headers=headers, data=content)
    
    print(r)
    global last_res
    last_res = json.loads(r.content)
    global tokenid
    tokenid = last_res['token']
    return r

def validate_token():
    endpoint = '/validate_token'
    headers = {'content-type': 'application/json'}
    global last_res, tokenid
    
    data = {
        'username': username,
        'tokenid': tokenid
    }
    
    content = json.dumps(data)
    r = requests.post(url+endpoint, headers=headers, data=content)

    print(r)
    last_res = json.loads(r.content)

    return r
    
    
def logout():
    endpoint = '/logout'
    headers = {'content-type': 'application/json'}
    global last_res, tokenid

    
    data = {
        'username': username,
        'tokenid': tokenid
    }
    
    content = json.dumps(data)
    r = requests.post(url+endpoint, headers=headers, data=content)

    print(r)
    last_res = json.loads(r.content)

    return r