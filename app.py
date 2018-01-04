#!/usr/bin/env python
# coding: utf-8

"""
启动文件
"""

import os
from flask import Flask, redirect, render_template
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from auth_token import token_bp
from login import login_bp
from register import register_bp
from model import db, User, Token

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# 初始化数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data/data.sqlite')
app.config['secret_key'] = 'dsfdsfasdac12!!ewfdsa23fdssfa21#@'

db.init_app(app)

app.register_blueprint(token_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
admin = Admin(app, name='sso', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Token, db.session))

manager = Manager(app)


@app.route('/')
def hello_world():
    """
    直接跳转管理系统
    """
    return render_template('home.html')

if __name__ == '__main__':
    manager.run()