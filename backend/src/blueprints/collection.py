from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Users import User
from src.Models.Houses import House

collection=Blueprint('collection',__name__)

#3.2 获取发布列表（publish）

@collection.route("/addCollection",methods=['GET','POST'])
def addCollection():
    #db
    userId=request.json.get('userId')
    houseId=request.json.get('houseId')
    user=User.query.filter(User.id==userId).first()
    house=House.query.filter(House.id==houseId).first()
    user.collections.append(house)
    db.session.add(user)
    db.session.commit()
    return {
    "success": 1,
    "data": {
    },
        "error":"None"
    }

#4.1 获取收藏列表
@collection.route("/center/collection/getCollectionList",methods=["POST"])
def get_collection():
    userId = request.json.get('userId')
    current_user=User.query.filter(User.id==userId).first()

    houses=current_user.collections
    houseList=[]
    for item in houses:
        info={}
        info["sold"]=True
        info["imgUrl"]=item.imgUrl
        info["title"]=item.title
        info["date"]=item.PublishTime
        info["seller"]=current_user.username
        info["price"]=item.price
        info["collectDate"]='collectDate'
        houseList.append(info)
    return {
        "success": 1,
        "data": {
            "collectionList":houseList
            },
            "error":None
            }

