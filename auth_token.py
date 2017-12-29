
#!/usr/bin/env python
# coding: utf-8

"""
验证token模块
"""

from flask import Blueprint

token_bp = Blueprint('token', __name__)

@token_bp.route('/validate_token') # 需要填写method
def validate_token_route():
    """
    在此处填写验证token的相关代码

    浏览器中输入: localhost:5000/validate_token
    """
    return 'token模块加载'

