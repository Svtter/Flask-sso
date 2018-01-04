#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_session():
    return db.session

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Token(db.Model):
    __tablename__ = 'Token'
    id = db.Column(db.Integer, primary_key=True)
    tokenid = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    status = db.Column(db.Boolean, default=True)
    
    def __init__(self, tokenid, username):
        self.username = username
        self.tokenid = tokenid

    def __repr__(self):
        return '<Token %r>' % self.username
