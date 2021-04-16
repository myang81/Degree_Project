from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Users import User
register=Blueprint('register',__name__)

#2. 注册页接口

# 2.1.注册接口：

@register.route("/register", methods=['GET', 'POST'])
def registerPage():
    print("hello")
    if request.method=='POST':
        username = request.json.get('username')
        password = request.json.get('password')
        save = User(username=username)
        save.set_password(password)  # 调用密码加密方法
        db.session.add(save)
        db.session.commit()
        return 'success'
    else:
        return 'error'





