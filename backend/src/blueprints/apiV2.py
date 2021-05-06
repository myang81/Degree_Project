from flask import Blueprint, render_template, session, flash, redirect,request,url_for

apiv2=Blueprint('api2',__name__)

@apiv2.route("/apiV2/photos", methods=['GET', 'POST'])
def uploadPhoto():
    return




