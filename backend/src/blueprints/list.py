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
    if request.method == 'POST':
        timeRange = request.json.get('timeRange')
        priceRange = request.json.get('priceRange')
        otherfeatrue = request.json.get('otherFeatrue')
        pageNum = request.json.get('pageNum')
        pageSize = request.json.get('pageSize')
        searchString = request.json.get('searchString')
        argdict = queryHouseList(timeRange, priceRange, otherfeatrue, pageNum, pageSize, searchString)
        return argdict


    return 'success'


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



