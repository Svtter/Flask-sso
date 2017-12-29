#!/usr/bin/env python
# coding: utf-8
"""
注册模块，需要提供用户的信息
"""

class User():
    def __init__(self):
        self.name = 'test'
        self.password = 'test'


if __name__ == '__main__':
    user = User()
    print(user.name)
    print(user.password)
