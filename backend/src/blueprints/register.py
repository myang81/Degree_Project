from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db

register=Blueprint('register',__name__)

#2. 注册页接口

# 2.1.注册接口：

@register.route("/register", methods=['GET', 'POST'])
def registerPage():
    return {
    "success": 1,
    "data":{
    "userId":"",
    "token":"",
    },
    "error":None
    }




