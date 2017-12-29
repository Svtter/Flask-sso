#!/usr/bin/env python
# coding: utf-8
"""
登录注销模块
"""

from flask import Blueprint

login_bp = Blueprint('login', __name__)

@login_bp.route('/login') # 需要填写method
def login_route():
    """
    在此处填写login的相关代码

    浏览器中输入: localhost:5000/login
    """
    return 'login模块加载'


@login_bp.route('/logout', methods=['POST'])
def logout_route():

    """
    在此处填写logout相关代码
    pass 可以删除
    """

    pass
