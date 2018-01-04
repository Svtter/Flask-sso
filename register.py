#!/usr/bin/env python
from flask import Blueprint, render_template, request
from model import User, db

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register_endpoint():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if not request.json:
            username = request.form['username']
            password = request.form['password']
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return 'success'
            
        else:
            try:
                info = request.json
                user = User(info['username'], info['password'])
                db.session.add(user)
                db.session.commit()
                return jsonify({'status': 'success'})
            except Exception as e:
                return jsonify({'status': 'failed'})