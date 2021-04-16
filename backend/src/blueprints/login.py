from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from flask_login import login_user

from src.extension import db
from src.Models.Users import User
import werkzeug.security
login=Blueprint('login',__name__)
#1. 登录页接口
#使用flask-login
#reference https://www.pianshen.com/article/5244187696/
#https://www.cnblogs.com/-wenli/p/14016905.html
#https://www.jianshu.com/p/7bff6e3d869b

#login in
@login.route("/login", methods=['GET', 'POST'])
def loginPage():
    if request.method=='POST':
        username=request.json.get('username') #add database then
        password=request.json.get('password') #add database then
        user=User.query.filter(User.name == username).first()
        if user:
            if werkzeug.check_password_hash(user.password_hash,password):
                login_user(user)
                return {
                    "success": 1,
                    "data":{
                        "userId":user.id,
                        "token":"babbaba"
                    },
                    "error":None
                    }
            else:
                return {
                    "success":404
                }


    return {
        "success":1,
        "data":{
            "userId":username,
            "token":password
        },
        "error":None
    }

