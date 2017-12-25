#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 xiuhao <xiuhao@xiuhaodeMacBook-Pro.local>
#

"""

用于API操作树莓派机器的蓝图

"""

from flask import Blueprint, abort, request, jsonify
import os

message = Blueprint('message', __name__, template_folder='templates')

@message.route('/message', methods=['POST'])
def messageHandle():
    """
    关闭机器的指令
    """
    if not request.json or 'method' not in request.json:
        abort(400)

    methods = request.json['method']
    if methods == 'poweroff':
        os.system('poweroff')
    elif methods == 'reboot':
        os.system('reboot')
    else:
        return jsonify({"result": "Not recognise method."}), 400
