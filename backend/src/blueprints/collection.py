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
    collected=request.json.get('collected')
    if collected == "true":
        user=User.query.filter(User.id==userId).first()
        house=House.query.filter(House.id==houseId).first()
        user.collections.append(house)
        house.setCollected("true")
        db.session.add(user)
        db.session.add(house)
        db.session.commit()
        return {
        "success": 1,
        "data": {
        },
            "error":"None"
        }
    if collected == "false":
        user = User.query.filter(User.id == userId).first()
        house = House.query.filter(House.id == houseId).first()
        user.collections.remove(house)
        house.setCollected("false")
        db.session.add(user)
        db.session.add(house)
        db.session.commit()
        return {
            "success": 1,
            "data": {
            },
            "error": "None"
        }
    return {
            "success": 0,
            "data": {
            },
            "error": "Error"
        }

#4.1 获取收藏列表
@collection.route("/center/collection/getCollectionList",methods=["POST","GET"])
def get_collection():
    if request.method=="POST":
        userId = request.json.get('userId')
        current_user=User.query.filter(User.id==userId).first()

        houses=current_user.collections
        houseList=[]
        for item in houses:
            info={}
            info["houseId"]=item.id
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
    else:
        return {
            "success": 0,
            "data": {
            },
            "error": "error"
        }

#4.5 删除收藏列表
@collection.route("/center/collection/delCollection",methods=["GET","POST"])
def del_collection():
    if request.method=="POST":
        userId = request.json.get('userId')
        houseId = request.json.get('houseId')
        user = User.query.filter(User.id == userId).first()
        house = House.query.filter(House.id == houseId).first()
        user.collections.remove(house)
        house.setCollected("false")
        db.session.add(user)
        db.session.add(house)
        db.session.commit()
        return {
            "success": 1,
            "data": {
            },
            "error": "None"
        }
    else:
        return {
            "success": 0,
            "data": {
            },
            "error": "Error"
        }


#5.1 房源详情页
@collection.route("/detail/getHouseDetail",methods=["GET","POST"])
def detail():
    if request.method=="POST":
        houseId = request.json.get('houseId')
        house=House.query.filter(House.id==houseId).first()
        data={}
        houseDetial={}
        housePictrue=[]
        if(house is not None):
            data["collected"]=house.getCollected()
            data["sold"]=house.saled
            data["title"]=house.title
            data["totalPrice"]=house.price
            data["unitPrice"]=house._unit_price
            data["houseId"]=house.id
            houseDetial["describe"]=house.title
            houseDetial["area"]=house.floor_area
            houseDetial["position"]=house.Specific_area
            houseDetial["houseStructure"]=house.House_structure
            houseDetial["direction"]=house.generateDirection()
            houseDetial["decoration"]=house.Interior_design
            houseDetial["heating"]=house.heating
            houseDetial["elecator"]=house.elevator
            housePictrue.append(house.imgUrl)
            return {
                "success": 1,
                "data":{
                    "collected": data["collected"],
                    "sold":data["sold"],
                    "title":data["title"],
                    "totalPrice":data["totalPrice"],
                    "unitPrice":data["unitPrice"],
                    "houseId":data["houseId"],
                    "houseDetail":houseDetial,
                    "housePicture":housePictrue,
                },
                "error":None
            }

        else:
            return {
                "success": 1,
                "data": {
                },
                "error": "No such house"
            }
    else:
        return {
            "success": 0,
            "data": {
            },
            "error": "Error"
        }

#5.1 获取出售人详情
@collection.route("/detail/getSellerDetail",methods=["GET","POST"])
def sellerDetail():
    if request.method=="POST":
        houseId = request.json.get('houseId')
        house=House.query.filter(House.id==houseId).first()
        print(house)
        print(house.publishments_users.all())
        if (len(house.publishments_users.all())!=0):
            seller=house.publishments_users.all().pop(0)
            print(house)
            data={}
            houseDetial={}
            housePictrue=[]
            if(house is not None and seller is not None):
                return {
                    "success": 1,
                    "data":{
                       "userName":seller.username,
                       "userEmail":seller.email,
                        "createTime":house.PublishTime
                    },
                    "error":None
                }
            else:
                return {
                    "success": 0,
                    "data": {

                    },
                    "error": "No such house"
                }

        else:
            return {
                "success": 1,
                "data": {
                    "userName": "admin",
                    "userEmail": "admin@163.com",
                    "createTime": "00-00-00"
                },
                "error": "No such seller"
            }
    else:
        return {
            "success": 0,
            "data": {
            },
            "error": "Error"
        }

@collection.route("/detail/buyHouse",methods=["GET","POST"])
def buy():
    if request.method == "POST":
        houseId = request.json.get('houseId')
        userId=request.json.get('userId')
        if houseId is not None and userId is not None:
            house = House.query.filter(House.id == houseId).first()
            buyer = User.query.filter(User.id == userId).first()
            house.saled="TRUE"
            db.session.add(house)
            db.session.commit()
            return {
                "success": 1,
                "data":{
                     },
                "error":"Null"
                }
        else:

            return{
                "success": 0,
                "data": {
                },
                "error": "No such house or user"
            }
