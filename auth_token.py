
#!/usr/bin/env python
# coding: utf-8

"""
验证token模块
"""

from flask import Blueprint, jsonify, abort, request
from model import Token
from utils import auth_login

token_bp = Blueprint('token_bp', __name__)

@token_bp.route('/validate_token', methods=['POST', 'GET']) # 需要填写method
def validate_token_route():
    """
    在此处填写验证token的相关代码

    浏览器中输入: localhost:5000/validate_token
    """
    if request.method == 'GET':
        try:
            if auth_login():
                return '<h1>已登录</h1>'
            else:
                return '<h1>未登录</h1>'
        except Exception as e:
            print(e)
            return '<h1>未登录</h1>', 400

    else:
        if not request.json:
            abort(400)
        
        else:
            try:
                info = request.json
                token = Token.query.filter_by(tokenid=info['tokenid']).first()
                if token:
                    return jsonify({'status': 'logined'})
                else:
                    return jsonify({'status': 'unlogined'})
            except Exception as e:
                print(e)
                return jsonify({'status': 'failed'}), 400
