from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
from src.Models.Houses import House

list=Blueprint('list',__name__)


#	3.1. 获取列表数据接口：

# 输入： timeRange	Array	发布时间区间	内部为字符串日历时间："yyyy-mm-dd"
# priceRange	Array	价格区间	内部为字符串格式价格："1000000"
# otherFeatures	Object	其他特征包装变量	对象内部特征根据配置静态文件中字典解析
# pageNum	String	当前页数	分页用数据
# pageSize	String	每页个数	分页用数据
# searchString	String	搜索字符串	bm25搜索

#输出： "success": 1,
# "data": {
#     "total": ""//数据总数，分页用       *****新增*****
#     "houseList":[//房源数据列表，注意数量与参数中每页信息数相同
#         {
#         "imgUrl":"",//房源图片url
#         "title":""//房源标题
#         "describe":""//房源描述
#         "position":""//房源地址（包含region和district，后端连接）
#         "coordinate":[]//房源经纬坐标（用于地图展示）
#         "houseId":""//房源Id
#         "totalPrice":""//房源总计 *****新增*****
#         "unitPrice":""//房源单价 *****新增*****
#         "collected": true//布尔值，是否已被收藏，仅是对这个用户自身       *****新增*****
#         }，
#     ]
# },
#

#变量解释: argDict： 请求用的参数字典

#相关的方法
def queryHouseList(timeRange,priceRange,otherFeatures,pageNum,pageSize,searchString):
    dict={}
    dict["timeRange"]=timeRange
    dict['priceRange']=priceRange
    dict['otherFeatrue']=otherFeatures
    dict['pageNum']=pageNum
    dict['pageSize']=pageSize
    dict['searchString']=searchString
    return dict

@list.route("/test",methods=['GET','POST'])
def test():
    timeRange=[]
    if request.method=='POST':
        timeRange=request.json.get('timeRange')
    i = 10
    if i in timeRange:
        return "true"
    else:
        return "false"


# @list.route("/getHouseList",methods=['GET','POST'])
# def getHouse():
#     argdict={}
#     if request.method=='POST':
#         #接收请求中的Post数据，储存到参数字典\
#         # print(request.json)
#         timeRange=request.json.get('timeRange')
#         priceRange=request.json.get('priceRange')
#         otherfeatrue=request.json.get('otherFeatrue')
#         pageNum=request.json.get('pageNum')
#         pageSize=request.json.get('pageSize')
#         searchString=request.json.get('searchString')
#         argdict=queryHouseList(timeRange,priceRange,otherfeatrue,pageNum,pageSize,searchString)
#         #
#         return 'argd' #可以post数据到后端了
#     return argdict


#3. 列表接口

#	3.1. 获取列表数据接口：
@list.route("/getHouseList",methods=['GET','POST'])
def getHouse():
    district = None
    houseStructrue =None
    direction = None
    decoration = None
    heating =None
    elevator = None
    pageNum = None
    pageSize = None
    searchString =None
    global argdict #get the parameter from the front
    if request.method == 'POST':
        timeRange = request.json.get('timeRange')
        if timeRange == [0,0]:
            timeRange=[0,999999]
        totalPriceRange = request.json.get('totalPriceRange')
        if totalPriceRange == [0,0]:
            totalPriceRange=[0,9999999]
        unitPriceRange=request.json.get('unitPriceRange')
        if unitPriceRange == [0,0]:
            unitPriceRange=[0,99999999]
        area=request.json.get('area')
        if area == [0,0]:
            area=[0,99999999]
        district=request.json.get('district')
        houseStructrue=request.json.get('houseStructrue')
        direction=request.json.get('direction')
        decoration=request.json.get('decoration')
        heating=request.json.get('heating')
        elevator=request.json.get('elevator')
        pageNum = request.json.get('pageNum')
        pageSize = request.json.get('pageSize')
        searchString = request.json.get('searchString')
        argdict={
        "timeRange": timeRange,
        "totalPriceRange":totalPriceRange,
        "unitPriceRange":unitPriceRange,
        "area":area,
        "district":district,
        "houseStructrue":houseStructrue,
        "direction":direction,
        "decoration":decoration,
        "heating":heating,
        "elevator":elevator,
        "pageNum":pageNum,
        "pageSize":pageSize,
        "searchString":searchString
        }
    direction={}
    # #process the drection
    # direction=argdict[direction]
    print(direction)
    direction={
        "west": "west" if "west" in direction else "no",
        "east": "east" if "east" in direction else "no",
        "south": "south" if "south" in direction else "no",
        "north": "north" if "north" in direction else "no",
        "southwest": "southwest" if "southwest" in direction else "no",
        "southeast": "southeast" if "southeast" in direction else "no",
        "northeast":"northeast" if "northeast" in direction else "no",
        "northwest":"northwest" if "northwest" in direction else "no"
    }
    print(direction)
    print(request.json)

    #从数据库查找数据 在价格区间内的数据
    Houses=House.query.filter(House.price >argdict['totalPriceRange'][0],House.price<argdict['totalPriceRange'][1],
                                House.floor_area >argdict['area'][0],House.floor_area<argdict['area'][1],
                              House._unit_price>argdict['unitPriceRange'][0],House._unit_price<argdict['unitPriceRange'][1],
                             House.District.in_(argdict["district"]),
                             House.House_structure.in_(argdict['houseStructrue']),

                             House.east==direction["east"],House.west==direction["west"],House.east_north==direction["northeast"],House.east_south==direction["southeast"]
                             ,House.north==direction["north"],House.south==direction["south"],House.west_south==direction["southwest"],House.east_south==direction["southwest"]
                             ,
                            House.Interior_design.in_(argdict["decoration"]),
                            House.heating.in_(argdict["heating"])
                              ,House.elevator.in_(argdict["elevator"])
                             ).all()

    total=House.query.filter(House.price >argdict['totalPriceRange'][0],House.price<argdict['totalPriceRange'][1],
                                House.floor_area >argdict['area'][0],House.floor_area<argdict['area'][1],
                              House._unit_price>argdict['unitPriceRange'][0],House._unit_price<argdict['unitPriceRange'][1],
                             House.District.in_(argdict["district"]),
                             House.House_structure.in_(argdict['houseStructrue']),

                             House.east==direction["east"],House.west==direction["west"],House.east_north==direction["northeast"],House.east_south==direction["southeast"]
                             ,House.north==direction["north"],House.south==direction["south"],House.west_south==direction["southwest"],House.east_south==direction["southwest"]
                             ,
                            House.Interior_design.in_(argdict["decoration"]),
                            House.heating.in_(argdict["heating"])
                              ,House.elevator.in_(argdict["elevator"])
                             ).count()
    #返回房子模型的数组
    print(Houses)
    print(total)
    houseList=[]

    for item in Houses:
        houseList.append(item.generateDetail())
    return {
            "success": 1,
            "data": {
                "total": total,
                "houseList":houseList

            },
            "error":None
        }




# @list.route("/getHouseList", methods=['GET', 'POST'])
# def houses():
#     #connect to the database
#     #db.session
#     #HouseList = []
#     #HouseList=db.session.query(...).all
#
#
#     return {
#     "success": 1,
#     "data": {
#         "total": 100,
#         "houseList":[
#         {
#         "imgUrl":"None",
#         "title":"Name",
#         "describe":"describe1",
#         "position":"term",
#         "coordinate":"none",
#         "houseId":"0",
#         "price":"1",
#         "Collected": "true"
#
#         }, {
#         "imgUrl":"None",
#         "title":"None",
#         "describe":"None",
#         "position":"None",
#         "coordinate":"None",
#         "houseId":"2",
#         "price":"1",
#         "Collected": "true"
#
#         },
#         ]
#     },
#     "error":None
# }
# =======
# @list.route("/getHouseList", methods=['GET', 'POST'])
# def houses():
#     #connect to the database
#     #db.session
#     #HouseList = []
#     #HouseList=db.session.query(...).all
#
#     fd = [{'title': 'The corner gate of Majiabao has two bedrooms and double balcony, with convenient transportation',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 0,
#       'describe': '2 room 1 halls | 75.43square meters | south west north | Banlou | high_floor ( total: 6 )',
#       'unitPrice': 52897,
#       'collected': 'true',
#       'totalPrice': '3.99',
#       'imgUrl': 'https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg'},
#      {
#          'title': 'The corner gate of Majiabao is close to the subway, with good north-south transparency, sufficient lighting and complete supporting facilities',
#          'position': 'Fengtai-Corner_Gate',
#          'houseId': 1,
#          'describe': '2 room 1 halls | 69.1square meters | south north | Banlou | middle_floor ( total: 6 )',
#          'unitPrice': 60203,
#          'collected': 'true',
#          'totalPrice': '4.16',
#          'imgUrl': 'https://img1.baidu.com/it/u=1267115342,3426495198&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Jiaomen Dongli, full of five unique, sincere sale, easy to see',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 2,
#       'describe': '2 room 1 halls | 73.63square meters | north southeast | tower | high_floor ( total: 19 )',
#       'unitPrice': 51202,
#       'collected': 'true',
#       'totalPrice': '3.77',
#       'imgUrl': 'https://img1.baidu.com/it/u=632875621,3849475090&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Jiaomen Majiabao Jiaomen Dongli two bedroom Jiaomen East Station',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 3,
#       'describe': '2 room 1 halls | 64.8square meters | south | tower | low_floor ( total: 19 )',
#       'unitPrice': 59723,
#       'collected': 'true',
#       'totalPrice': '3.87',
#       'imgUrl': 'https://img2.baidu.com/it/u=428922356,2955791946&fm=26&fmt=auto&gp=0.jpg'},
#      {
#          'title': 'The corner gate of Majiabao is accessible from north to south, and the floor is full of five only two bedrooms',
#          'position': 'Fengtai-Corner_Gate',
#          'houseId': 4,
#          'describe': '2 room 1 halls | 53.9square meters | south north | Banlou | low_floor ( total: 6 )',
#          'unitPrice': 56587,
#          'collected': 'true',
#          'totalPrice': '3.05',
#          'imgUrl': 'https://img1.baidu.com/it/u=1206287871,1293580609&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Jiaomen Majiabao Manwu subway line 10 Line 4 Jiaomen west station',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 5,
#       'describe': '2 room 1 halls | 54.1square meters | south north | Banlou | low_floor ( total: 6 )',
#       'unitPrice': 60999,
#       'collected': 'true',
#       'totalPrice': '3.3',
#       'imgUrl': 'https://img0.baidu.com/it/u=3070448361,252388962&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Fine decoration of three bedroom low floor in dongsida community, Jiaomen, Majiabao',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 6,
#       'describe': '3 room 1 halls | 76.12square meters | south north | Banlou | low_floor ( total: 6 )',
#       'unitPrice': 52286,
#       'collected': 'true',
#       'totalPrice': '3.98',
#       'imgUrl': 'https://img2.baidu.com/it/u=3614374747,1028706245&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Sunshine Garden Corner Gate East Majiabao dahongmen north south two houses',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 7,
#       'describe': '2 room 1 halls | 89.99square meters | south north | Banlou | top_floor ( total: 19 )',
#       'unitPrice': 75564,
#       'collected': 'true',
#       'totalPrice': '6.8',
#       'imgUrl': 'https://img0.baidu.com/it/u=25061059,992130011&fm=26&fmt=auto&gp=0.jpg'},
#      {'title': 'Jiaomen, Majiabao, Yangqiao, the only regular two bedroom in five years',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 8,
#       'describe': '2 room 1 halls | 70.4square meters | south north | Banlou | high_floor ( total: 6 )',
#       'unitPrice': 57245,
#       'collected': 'true',
#       'totalPrice': '4.03',
#       'imgUrl': 'https://img2.baidu.com/it/u=1126845708,2463843041&fm=11&fmt=auto&gp=0.jpg'},
#      {'title': 'Yangqiao, Majiabao, two bedrooms in Jiaomen Dongli community',
#       'position': 'Fengtai-Corner_Gate',
#       'houseId': 9,
#       'describe': '2 room 1 halls | 54.11square meters | south north | Banlou | high_floor ( total: 6 )',
#       'unitPrice': 60063,
#       'collected': 'true',
#       'totalPrice': '3.25',
#       'imgUrl': 'https://img0.baidu.com/it/u=3774158723,4269643202&fm=11&fmt=auto&gp=0.jpg'}]
#     nDict = {
#         "success": 1,
#         "data": {
#             "total": 100,
#             "houseList": fd
#         },
#         "error": None
#     }
#     str_json = json.dumps(nDict, indent=2, ensure_ascii=False)
#     return str_json
# >>>>>>> b5fa07ac013f7e2fd94a3e44313184f558901831
#
#
#
