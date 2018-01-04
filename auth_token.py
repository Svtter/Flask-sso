
#!/usr/bin/env python
# coding: utf-8

"""
验证token模块
"""

from flask import Blueprint, jsonify, abort, request
from model import Token

token_bp = Blueprint('token_bp', __name__)

@token_bp.route('/validate_token', methods=['POST', 'GET']) # 需要填写method
def validate_token_route():
    """
    在此处填写验证token的相关代码

    浏览器中输入: localhost:5000/validate_token
    """
    if request.method == 'GET':
        try:
            username = request.cookies.get('username')
            tokenid = request.cookies.get('tokenid')
            
            token = Token.query.filter_by(tokenid=tokenid).first()
            # TODO: 对于过期的方法修正
            if token.username == username:
                return '<h1>已登录</h1>'
            else:
                return '<h1>凭证错误</h1>'
        except Exception as e:
            print(e)
            return '<h1>未登录</h1>'

    else:
        if not request.json:
            abort(400)
        
        else:
            try:
                info = request.json
                token = Token.query.filter_by(tokenid=info['token']).first()
                if token:
                    return jsonify({'status': 'logined'})
                else:
                    return jsonify({'status': 'unlogined'})
            except Exception as e:
                return jsonify({'status': 'failed'})
