#!/usr/bin/env python
# coding: utf-8

"""
启动文件
"""

from flask import Flask
from auth_token import token_bp
from login import login_bp

app = Flask(__name__)
app.register_blueprint(token_bp)
app.register_blueprint(login_bp)


@app.route('/')
def hello_world():
    return 'SSO系统运行中'

if __name__ == '__main__':
    app.run(debug=True)
