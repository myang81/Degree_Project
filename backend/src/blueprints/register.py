from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Users import User
from datetime import time
register=Blueprint('register',__name__)

import time
import base64
import hmac
#2. 注册页接口

# 2.1.注册接口：
def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


@register.route("/register", methods=['GET', 'POST'])
def registerPage():
    if request.method=='POST':
        username = request.json.get('username')
        password = request.json.get('password')
        email=request.json.get('email')
        if User.query.filter(username==username).first() == None:
            save = User(username=username)
            save.set_password(password)
            save.email=email
            token=generate_token(username)
            db.session.add(save)
            db.session.commit()
            return {
                "success": 1,
                "data":{
                    "userId":save.id,
                    "token":token
                },
                "error":None
            }
        else:
            return {
                "success": 0,
                "data": {
                    "userId": None,
                    "token": None
                },
                "error": "User already exist"
            }
    else:
        return 'error'





