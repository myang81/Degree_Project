from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Users import User
from src.Models.Houses import House

center=Blueprint('center',__name__)

# #4.1 获取收藏列表
# @center.route("/center/collection/getCollectionList",methods=["POST"])
# def get_collection():
#     userId = request.json.get('userId')
#     current_user=User.query.filter(User.id==userId).first()
#
#     houses=current_user.houses
#     houseList=[]
#     for item in houses:
#         info={}
#         info["sold"]=True
#         info["imgUrl"]=item.imgUrl
#         info["title"]=item.title
#         info["date"]=item.PublishTime
#         info["seller"]=current_user.username
#         info["price"]=item.price
#         info["collectDate"]='collectDate'
#         houseList.append(info)
#     return {
#         "success": 1,
#         "data": {
#             "collectionList":houseList
#             },
#             "error":None
#             }

#4.4 更新兴趣信息（target）

@center.route("/center/target/updateTargetInfo",methods=["POST"])
def get_profile():
    #db
    if request.method=="POST":
        print(request.form)
        print(request.json)
        print(request.data)
        priceRange=request.json.get('priceRange')
        layout=request.json.get('layout')
        measure=request.json.get('measure')
        orientation=request.json.get('orientation')
        floor=request.json.get('floor')
        decoration=request.json.get('decoration')

        return {
            "success":1,
            "data":{
                "priceRange":priceRange,
                "layout":layout,
                "measure":measure,
                "orientation":orientation,
                "floor":floor,
                "decoration":decoration
            },
            "error":None
        }

#4.5 删除收藏（不支持批量删除）
@center.route("/center/collection/delCollection", methods=["POST"])
def update_profile():
    # db
    if request.method == "POST":
        print(request.form)
        print(request.json)
        print(request.data)
        priceRange = request.json.get('priceRange')
        layout = request.json.get('layout')
        measure = request.json.get('measure')
        orientation = request.json.get('orientation')
        floor = request.json.get('floor')
        decoration = request.json.get('decoration')

        return {
            "success": 1,
            "data": {
                "priceRange": priceRange,
                "layout": layout,
                "measure": measure,
                "orientation": orientation,
                "floor": floor,
                "decoration": decoration
            },
            "error":None
        }

#4.6 删除已发布（不支持批量删除）

@center.route("/center/published/delPublished", methods=["POST"])
def delete_profile():
    # # db
    # if request.method == "POST":
    #     print(request.form)
    #     print(request.json)
    #     print(request.data)
    #     priceRange = request.json.get('priceRange')
    #     layout = request.json.get('layout')
    #     measure = request.json.get('measure')
    #     orientation = request.json.get('orientation')
    #     floor = request.json.get('floor')
    #     decoration = request.json.get('decoration')

        return {
            # "success": 1.
            # "data": {
            #     "priceRange": priceRange,
            #     "layout": layout,
            #     "measure": measure,
            #     "orientation": orientation,
            #     "floor": floor,
            #     "decoration": decoration
            # },
            # "error":None
        }