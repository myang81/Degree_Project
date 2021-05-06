from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Users import User
from src.Models.Houses import House
from src.Utility import enumMachine
from src.Models.Target import Target
import datetime
from src.Models.Targets import Targets
from datetime import datetime

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

#添加已经发布
# @collection.route("/addCollection",methods=['GET','POST'])
# def addCollection():
#     #db
#     userId=request.json.get('userId')
#     houseId=request.json.get('houseId')
#     collected=request.json.get('collected')
#     if collected == "true":
#         user=User.query.filter(User.id==userId).first()
#         house=House.query.filter(House.id==houseId).first()
#         user.collections.append(house)
#         house.setCollected("true")
#         db.session.add(user)
#         db.session.add(house)
#         db.session.commit()
#         return {
#         "success": 1,
#         "data": {
#         },
#             "error":"None"
#         }
#     if collected == "false":
#         user = User.query.filter(User.id == userId).first()
#         house = House.query.filter(House.id == houseId).first()
#         user.collections.remove(house)
#         house.setCollected("false")
#         db.session.add(user)
#         db.session.add(house)
#         db.session.commit()
#         return {
#             "success": 1,
#             "data": {
#             },
#             "error": "None"
#         }
#     return {
#             "success": 0,
#             "data": {
#             },
#             "error": "Error"
#         }

#添加已经发布
@center.route("/addPublishlist",methods=["POST"])
def publish():
    arg={}
    arg['userId'] = request.json.get('userId')
    arg['bathroom'] = request.json.get('bathroom')
    arg['hall'] = request.json.get('hall')
    arg['kitchen'] = request.json.get('kitchen')
    arg['room'] = request.json.get('room')
    arg['area'] = request.json.get('area')
    arg['floors'] = request.json.get('floors')
    arg['buildingStructure'] = request.json.get('buildingStructure')
    arg['buildingType'] = request.json.get('buildingType')
    arg['elevator'] = request.json.get('elevator')
    arg['floorType'] = request.json.get('floorType')
    arg['heating'] = request.json.get('heating')
    arg['houseStructure'] = request.json.get('houseStructure')
    arg['property'] = request.json.get('property')
    arg['region'] = request.json.get('region')
    arg['decoration'] = request.json.get('decoration')
    arg['district'] = request.json.get('district')
    arg['coordinate'] = request.json.get('coordinate')
    arg['direction'] = request.json.get('direction')
    arg['elevatorNum'] = int(request.json.get('elevatorNum'))
    arg['houseNum'] = int(request.json.get('houseNum'))
    arg['community'] = request.json.get('community')
    arg['title'] = request.json.get('title')
    arg['describe'] = request.json.get('describe')
    arg['unitPrice'] = int(request.json.get('unitPrice'))
    arg['totalPrice'] = int(request.json.get('totalPrice'))

    print(arg)
    house=House()
    user=User.query.filter(User.id == arg['userId']).first()
    print(user)



    house.toilet=arg['bathroom']
    house.hall=arg['hall']
    house.kitchen=arg['kitchen']
    house.room=arg['room']
    house.floor_area=arg['area']
    house.total_floors=arg['floors']
    house.Architectural_structure=enumMachine.Building_structrue.enum2field(arg['buildingStructure'])
    house.Building_Type=enumMachine.Building_type.enum2field(arg['buildingType'])
    house.elevator=enumMachine.Elevator.enum2field(arg['elevator'])
    house.Floor_type=enumMachine.Floor_type.enum2field(arg['floorType'])
    house.heating=enumMachine.Heating.enum2field(arg['heating'])
    house.House_structure=enumMachine.House_structrue.enum2field(arg['houseStructure'])
    house.Property_information=enumMachine.PropertyInfo.enum2field(arg['property'])
    house.Specific_area=enumMachine.Region.enum2field(arg['region'])
    house.Interior_design=enumMachine.Ddecoration.enum2field(arg['decoration'])
    house.District=enumMachine.District.enum2field(arg['district'])
    house.Longitude=int(arg['coordinate'][0])
    house.Latitude=int(arg['coordinate'][1])
    house.title=arg['title']
    house._unit_price=arg['unitPrice']
    house.price=arg['totalPrice']/10000
    house.saled="FALSE"
    utc_time = datetime.utcnow()
    house.PublishTime=utc_time
    house.imgUrl=None
    house.collected="FALSE"


    direction_list=[]
    for i in arg['direction']:
        direction_list.append(enumMachine.Direction.enum2field(i))

    direction = {
        "west": "west" if "west" in direction_list else "no",
        "east": "east" if "east" in direction_list else "no",
        "south": "south" if "south" in direction_list else "no",
        "north": "north" if "north" in direction_list else "no",
        "southwest": "southwest" if "southwest" in direction_list else "no",
        "southeast": "southeast" if "southeast" in direction_list else "no",
        "northeast": "northeast" if "northeast" in direction_list else "no",
        "northwest": "northwest" if "northwest" in direction_list else "no"
    }
    house.west=direction['west']
    house.east=direction['east']
    house.north=direction["north"]
    house.south=direction["south"]
    house.east_north=direction['northeast']
    house.east_south=direction['southeast']
    house.west_north=direction['northwest']
    house.west_south=direction['southwest']

    elvatorNum=arg['elevatorNum']
    houseNum=arg['houseNum']
    ratio=elvatorNum/houseNum
    house.ladder_ratio=ratio
    user.publishments.append(house)
    db.session.add(house)
    db.session.add(user)
    db.session.commit()


    return {
        "success": 1,
        "data":{
            "houseId":house.id
        },
        "error":"None"
        }



#4.2 获取发布列表
@center.route("/center/published/getPublishedList",methods=["POST"])
def getPublish():
    userId = request.json.get('userId')
    current_user = User.query.filter(User.id == userId).first()

    houses = current_user.publishments
    houseList = []
    for item in houses:
        info = {}
        info["sold"] = True
        info["imgUrl"] = item.imgUrl
        info["Title"] = item.title
        info["Date"] = item.PublishTime
        info["seller"] = current_user.username
        info["price"] = item.price
        houseList.append(info)
    return {
        "success": 1,
        "data": {
            "publishList": houseList
        },
        "error": None
    }


#4.6 删除已发布
@center.route("/center/published/delPublished",methods=["GET","POST"])
def del_publish():
    if request.method=="POST":
        userId = request.json.get('userId')
        houseId = request.json.get('houseId')
        if houseId is not None and userId is not  None:
            user = User.query.filter(User.id == userId).first()
            house = House.query.filter(House.id == houseId).first()
            if house in user.publishments:
                user.publishments.remove(house)
                db.session.add(user)
                db.session.commit()
            else:
                return {
                    "success": 0,
                    "data": {
                    },
                    "error": "The house is not in publish list"
                }

            return {
                "success": 1,
                "data": {
                },
                "error": "No such house or user"
            }
        else:
            return {
                "success": 1,
                "data": {
                },
                "error": "No such user or house"
            }
    else:
        return {
            "success": 0,
            "data": {
            },
            "error": "Error"
        }


# #4.4 更新兴趣信息（target）
#
# @center.route("/center/target/updateTargetInfo",methods=["POST"])
# def get_profile():
#     #db
#     if request.method=="POST":
#         print(request.form)
#         print(request.json)
#         print(request.data)
#         priceRange=request.json.get('priceRange')
#         layout=request.json.get('layout')
#         measure=request.json.get('measure')
#         orientation=request.json.get('orientation')
#         floor=request.json.get('floor')
#         decoration=request.json.get('decoration')
#
#         return {
#             "success":1,
#             "data":{
#                 "priceRange":priceRange,
#                 "layout":layout,
#                 "measure":measure,
#                 "orientation":orientation,
#                 "floor":floor,
#                 "decoration":decoration
#             },
#             "error":None
#         }

# #4.5 删除收藏（不支持批量删除）
# @center.route("/center/collection/delCollection", methods=["POST"])
# def update_profile():
#     # db
#     if request.method == "POST":
#         print(request.form)
#         print(request.json)
#         print(request.data)
#         priceRange = request.json.get('priceRange')
#         layout = request.json.get('layout')
#         measure = request.json.get('measure')
#         orientation = request.json.get('orientation')
#         floor = request.json.get('floor')
#         decoration = request.json.get('decoration')
#
#         return {
#             "success": 1,
#             "data": {
#                 "priceRange": priceRange,
#                 "layout": layout,
#                 "measure": measure,
#                 "orientation": orientation,
#                 "floor": floor,
#                 "decoration": decoration
#             },
#             "error":None
#         }


#4.3 获取兴趣信息
@center.route("/center/target/getTargetInfo",methods=["POST"])
def getTartgetInfo():
    if request.method == "POST":
        user = User.query.filter(User.id == request.json.get("userId")).first()
        if user is None:
            return {
            "success": 0,
            "data":{
            },
            "error":"User not found"
            }
        else:

            t_str=user.target

            ts=user.targets.all()
            list=[]
            for i in ts:
                list.append(i.toEnum())
            return {
                "success":1,
                "data":list,
                "error":None
            }
    return "0"


#4.4 更新兴趣信息
@center.route("/center/target/updateTargetInfo",methods=["POST"])
def updateTartget():
    if request.method=="POST":
        user = User.query.filter(User.id == request.json.get("userId")).first()
        print(user)
        if not user:
            return {
            "success": 0,
            "data":{
            },
            "error":"User not found"
            }
        else:
            print(request.data)
            print(type(request.json))
            target=Target.loadJson(d=request.data)
            print(type(target))
            j=Target.convertJson(target=target)
            user.saveTarget(target=j)
            tars=user.targets.all()
            if len(tars) != 0:
                tar = user.targets.all()[0]
                print(tar)
                t=Targets.saveTarget(tar,target=target.toDict())
            else:
                t = Targets.saveTarget(Targets(), target=target.toDict())
                user.targets.append(t)
            db.session.add(user)
            db.session.commit()


            return {
                "success": 1,
                "data":{
                },
                "error":None
                }

    return {
            "success": 0,
            "data":{
            },
            "error":"No this method"
            }
