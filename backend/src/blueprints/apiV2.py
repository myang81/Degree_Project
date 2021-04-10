from flask import Blueprint, render_template, session, flash, redirect,request,url_for

apiv2=Blueprint('api2',__name__)

@apiv2.route("/apiV2/home", methods=['GET', 'POST'])
def hello():
    return "hello"


#login in
@apiv2.route("/login", methods=['GET', 'POST'])
def login():
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


