import jwt
from src.extension import db
from time import time
from flask import current_app
from datetime import datetime
from flask_avatars import Identicon


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=False)
    password = db.Column(db.String(128))



    def __init__(self,username,password):
        self.username = username
        self.password = password
