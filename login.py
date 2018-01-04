#!/usr/bin/env python
# coding: utf-8
"""
登录注销模块
"""

from flask import Blueprint, abort, jsonify, request
from model import User, Token, db
from utils import generateToken

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST', 'GET']) # 需要填写method
def login_route():
    """
    在此处填写login的相关代码

    浏览器中输入: localhost:5000/login
    """
    if not request.json:
        abort(400)
    else:
        try:
            info = request.json
            user = User.query.all(username=info['username'])
            if user.password == info['password']:
                tokenid = generateToken()
                token = Token(tokenid, user.username)
                db.session.add(Token)
                db.session.commit()
                return jsonify({'status': 'success', 'token': token})
        except Exception as e:
            return jsonify({'status': 'failed'})
        

@login_bp.route('/logout', methods=['POST'])
def logout_route():

    """
    在此处填写logout相关代码
    pass 可以删除
    """

    if not request.json:
        abort(400)
    
    else:
        info = request.json
        try:
            token = Token.query.all(info['username'])
            if token.tokenid == info['tokenid']:
                db.session.delete(token)
                return jsonify({'status': 'success', 'username': info['username']})
            else:
                return jsonify({'status': 'failed'})
        except Exception as e:
            return jsonify({"status": "failed"})