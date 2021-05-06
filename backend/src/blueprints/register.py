from flask import Blueprint, render_template, session, flash, redirect,request,url_for

from src.Models.Target import Target
from src.Models.Targets import Targets
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
        username = request.json.get('name')
        password = request.json.get('password')
        email=request.json.get('email')
        prp=request.json.get('prp')
        print(username+" "+password+" "+prp+" "+email)
        if User.query.filter(User.username==username).first() == None:
            if prp==password:
                save = User(username=username)
                save.set_password(password)
                save.email=email
                token=generate_token(username)



                t = Targets.saveTarget(Targets(), Target.initDict())
                save.targets.append(t)
                db.session.add(save)

                # #add a empty target
                #
                # j = Target.initData()
                # save.saveTarget(target=j)
                # tars = save.targets.all()
                #
                # t = Targets.saveTarget(Targets(), target=target.toDict())
                # save.targets.append(t)
                # db.session.add(user)
                # #
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
                return
                {
                    "success": 0,
                    "data": {
                        "userId": None,
                        "token": None
                    },
                    "error": "The two passwords entered are inconsistent"
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





