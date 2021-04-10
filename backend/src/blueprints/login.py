from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db

login=Blueprint('login',__name__)
#1. 登录页接口


#login in
@login.route("/login", methods=['GET', 'POST'])
def loginPage():
    #connect to the database
    #db.session
    username="username" #add database then
    password="password" #add database then
    return {
        "success":1,
        "data":{
            "userId":username,
            "token":password
        },
        "error":None
    }

