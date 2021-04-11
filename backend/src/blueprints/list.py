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

    fd = [{'title': '马家堡角门南北通透两居室  双阳台 交通便利',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 0,
  'price': 52897.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 75.43square meters | south west north | Banlou | high_floor ( total: 6 )'},
 {'title': '马家堡角门近地铁 南北通透 格局好 采光充足 配套齐全',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 1,
  'price': 60203.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 69.1square meters | south north | Banlou | middle_floor ( total: 6 )'},
 {'title': '角门东里，满五唯一，诚心出售，看房方便',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 2,
  'price': 51202.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 73.63square meters | north southeast | tower | high_floor ( total: 19 )'},
 {'title': '角门 马家堡  角门东里  南向两居室角门东站',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 3,
  'price': 59723.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 64.8square meters | south | tower | low_floor ( total: 19 )'},
 {'title': '马家堡角门 南北通透 低楼层满五唯一 两居室',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 4,
  'price': 56587.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 53.9square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': '角门马家堡 满五唯一 地铁10号线4号线角门西站',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 5,
  'price': 60999.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 54.1square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': '马家堡角门东司达小区三居室低楼层精装修',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 6,
  'price': 52286.0,
  'Collected': 'true',
  'describe': '3 room 1 halls | 76.12square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': '阳光花园角门东马家堡大红门南北两居',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 7,
  'price': 75564.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 89.99square meters | south north | Banlou | top_floor ( total: 19 )'},
 {'title': '角门，马家堡，洋桥，满五年唯一正规二居室',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 8,
  'price': 57245.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 70.4square meters | south north | Banlou | high_floor ( total: 6 )'},
 {'title': '洋桥，马家堡，角门东里小区二居室',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 9,
  'price': 60063.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 54.11square meters | south north | Banlou | high_floor ( total: 6 )'}]
    nDict = {
        "success": 1,
        "data": {
            "total": 100,
            "houseList": fd
        },
        "error": None
    }
    str_json = json.dumps(nDict, indent=2, ensure_ascii=False)
    return str_json



