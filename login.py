#!/usr/bin/env python
# coding: utf-8
"""
登录注销模块
"""

from flask import Blueprint, abort, jsonify, request, make_response, render_template
from model import User, Token, db
from utils import generateToken

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST', 'GET']) # 需要填写method
def login_route():
    """
    在此处填写login的相关代码

    浏览器中输入: localhost:5000/login
    """
    if request.method == 'GET':
        return render_template('login.html')

    else:
        if not request.json:
            try:
                username = request.form['username']
                password = request.form['password']
                user = User.query.filter_by(username=username).first()
                if user.password == password:
                    resp = make_response('<h1>登录成功</h1>')

                    # save token
                    tokenid = generateToken()
                    token = Token(tokenid, username)
                    db.session.add(token)
                    db.session.commit()

                    resp.set_cookie('username', username)
                    resp.set_cookie('tokenid', tokenid)

                    return resp
                else:
                    return '<h1>凭证错误</h1>'
            except Exception as e:
                print(e)
                return '<h1>凭证错误</h1>'

        else:
            try:
                info = request.json
                user = User.query.filter_by(username=info['username']).fisrt()
                if user.password == info['password']:
                    tokenid = generateToken()
                    token = Token(tokenid, user.username)
                    db.session.add(token)
                    db.session.commit()
                    return jsonify({'status': 'success', 'token': token})
            except Exception as e:
                return jsonify({'status': 'failed'})
        

@login_bp.route('/logout', methods=['POST', 'GET'])
def logout_route():

    """
    在此处填写logout相关代码
    pass 可以删除
    """
    if request.method == 'GET':
        try:
            username = request.cookies.get('username')
            tokenid = request.cookies.get('tokenid')
            
            token = Token.query.filter_by(username=username).first()
            if token.tokenid == tokenid:
                db.session.delete(token)
                db.session.commit()
                return '<h1>登出成功</h1>'
            else:
                return '<h1>凭据错误</h1>'
        except Exception as e:
            return '<h1>未登录</h1>'
        
    else:
        if not request.json:
            abort(400)
        
        else:
            info = request.json
            try:
                token = Token.query.filter_by(info['username']).first()
                if token.tokenid == info['tokenid']:
                    db.session.delete(token)
                    return jsonify({'status': 'success', 'username': info['username']})
                else:
                    return jsonify({'status': 'failed'})
            except Exception as e:
                return jsonify({"status": "failed"})