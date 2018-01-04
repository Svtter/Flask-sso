
#!/usr/bin/env python
# coding: utf-8

"""
验证token模块
"""

from flask import Blueprint, jsonify, abort, request
from model import Token

token_bp = Blueprint('token_bp', __name__)

@token_bp.route('/validate_token') # 需要填写method
def validate_token_route():
    """
    在此处填写验证token的相关代码

    浏览器中输入: localhost:5000/validate_token
    """

    if not request.json:
        abort(400)
    
    else:
        try:
            info = request.json
            token = Token.query.all(tokenid=info['token'])
            if token:
                return jsonify({'status': 'logined'})
            else:
                return jsonify({'status': 'unlogined'})
        except Exception as e:
            return jsonify({'status': 'failed'})
