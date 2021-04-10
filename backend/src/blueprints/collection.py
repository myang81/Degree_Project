from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db

collection=Blueprint('collection',__name__)
#4. 用户中心页

#4.1 获取收藏列表

@collection.route("/center/collection/getCollectionList",methods=['GET','POST'])
def collectionList():
    collectionList=[]
    url=""
    title=""
    date=""
    date=""
    seller=""
    price=""
    collection={"imageURL":url,"title":title,"Date":date,"seller":seller,
                "price":price}
    return {
    "success": 1,
    "data": {
        "collectionList":[
            {
            "imgUrl":"",
            "title":"",
            "Date":"",
            "seller":"",
            "price":"",
            },
        ]
    },
        "error":"None"
    }

#4.2 获取发布列表（publish）

@collection.route("/center/published/getPublishedList",methods=['GET','POST'])
def publish():
    #db
    #
    return {
    "success": 1,
    "data": {
        "collectionList":[
            {
            "imgUrl":"",
            "title":"",
            "Date":"",
            "seller":"",
            "price":"",
            },
        ]
    },
        "error":"None"
    }

#4.3 获取兴趣信息

@collection.route("/center/target/getTargetInfo",methods=['GET','POST'])
def targetInfo():
    return {
        "success": 1,
    "data":{
        },
    "error":None
}


#4.4 更新兴趣信息（target）

@collection.route("/center/target/updateTargetInfo",methods=["POST"])
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
@collection.route("/center/collection/delCollection", methods=["POST"])
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

@collection.route("/center/published/delPublished", methods=["POST"])
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