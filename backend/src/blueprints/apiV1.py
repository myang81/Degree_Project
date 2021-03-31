from flask import Blueprint, render_template, session, flash, redirect,request,url_for

apiv1=Blueprint('api',__name__)

@apiv1.route("/apiV1/home", methods=['GET', 'POST'])
def hello():
    return "hello"



@apiv1.route("/", methods=['GET', 'POST'])
def time():
    return "hi"