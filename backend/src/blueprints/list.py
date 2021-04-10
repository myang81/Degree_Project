from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db

list=Blueprint('list',__name__)

#3. 列表接口

#	3.1. 获取列表数据接口：
@list.route("/getHouseList", methods=['GET', 'POST'])
def houses():
    #connect to the database
    #db.session
    #HouseList = []
    #HouseList=db.session.query(...).all

    return {
    "success": 1,
    "data": {
        "total": 100,
        "houseList":[
        {
        "imgUrl":"None",
        "title":"Name",
        "describe":"describe1",
        "position":"term",
        "coordinate":"none",
        "houseId":"0",
        "price":"1",
        "Collected": "true"

        }, {
        "imgUrl":"None",
        "title":"None",
        "describe":"None",
        "position":"None",
        "coordinate":"None",
        "houseId":"2",
        "price":"1",
        "Collected": "true"

        },
        ]
    },
    "error":None
}



