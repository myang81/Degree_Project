from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.extension import db
import json

list=Blueprint('list',__name__)

#3. 列表接口

#	3.1. 获取列表数据接口：
@list.route("/getHouseList", methods=['GET', 'POST'])
def houses():
    #connect to the database
    #db.session
    #HouseList = []
    #HouseList=db.session.query(...).all

    fd = [{'title': 'The corner gate of Majiabao has two bedrooms and double balcony, with convenient transportation',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 0,
      'describe': '2 room 1 halls | 75.43square meters | south west north | Banlou | high_floor ( total: 6 )',
      'unitPrice': 52897,
      'collected': 'true',
      'totalPrice': '3.99',
      'imgUrl': 'https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg'},
     {
         'title': 'The corner gate of Majiabao is close to the subway, with good north-south transparency, sufficient lighting and complete supporting facilities',
         'position': 'Fengtai-Corner_Gate',
         'houseId': 1,
         'describe': '2 room 1 halls | 69.1square meters | south north | Banlou | middle_floor ( total: 6 )',
         'unitPrice': 60203,
         'collected': 'true',
         'totalPrice': '4.16',
         'imgUrl': 'https://img1.baidu.com/it/u=1267115342,3426495198&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Jiaomen Dongli, full of five unique, sincere sale, easy to see',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 2,
      'describe': '2 room 1 halls | 73.63square meters | north southeast | tower | high_floor ( total: 19 )',
      'unitPrice': 51202,
      'collected': 'true',
      'totalPrice': '3.77',
      'imgUrl': 'https://img1.baidu.com/it/u=632875621,3849475090&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Jiaomen Majiabao Jiaomen Dongli two bedroom Jiaomen East Station',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 3,
      'describe': '2 room 1 halls | 64.8square meters | south | tower | low_floor ( total: 19 )',
      'unitPrice': 59723,
      'collected': 'true',
      'totalPrice': '3.87',
      'imgUrl': 'https://img2.baidu.com/it/u=428922356,2955791946&fm=26&fmt=auto&gp=0.jpg'},
     {
         'title': 'The corner gate of Majiabao is accessible from north to south, and the floor is full of five only two bedrooms',
         'position': 'Fengtai-Corner_Gate',
         'houseId': 4,
         'describe': '2 room 1 halls | 53.9square meters | south north | Banlou | low_floor ( total: 6 )',
         'unitPrice': 56587,
         'collected': 'true',
         'totalPrice': '3.05',
         'imgUrl': 'https://img1.baidu.com/it/u=1206287871,1293580609&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Jiaomen Majiabao Manwu subway line 10 Line 4 Jiaomen west station',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 5,
      'describe': '2 room 1 halls | 54.1square meters | south north | Banlou | low_floor ( total: 6 )',
      'unitPrice': 60999,
      'collected': 'true',
      'totalPrice': '3.3',
      'imgUrl': 'https://img0.baidu.com/it/u=3070448361,252388962&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Fine decoration of three bedroom low floor in dongsida community, Jiaomen, Majiabao',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 6,
      'describe': '3 room 1 halls | 76.12square meters | south north | Banlou | low_floor ( total: 6 )',
      'unitPrice': 52286,
      'collected': 'true',
      'totalPrice': '3.98',
      'imgUrl': 'https://img2.baidu.com/it/u=3614374747,1028706245&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Sunshine Garden Corner Gate East Majiabao dahongmen north south two houses',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 7,
      'describe': '2 room 1 halls | 89.99square meters | south north | Banlou | top_floor ( total: 19 )',
      'unitPrice': 75564,
      'collected': 'true',
      'totalPrice': '6.8',
      'imgUrl': 'https://img0.baidu.com/it/u=25061059,992130011&fm=26&fmt=auto&gp=0.jpg'},
     {'title': 'Jiaomen, Majiabao, Yangqiao, the only regular two bedroom in five years',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 8,
      'describe': '2 room 1 halls | 70.4square meters | south north | Banlou | high_floor ( total: 6 )',
      'unitPrice': 57245,
      'collected': 'true',
      'totalPrice': '4.03',
      'imgUrl': 'https://img2.baidu.com/it/u=1126845708,2463843041&fm=11&fmt=auto&gp=0.jpg'},
     {'title': 'Yangqiao, Majiabao, two bedrooms in Jiaomen Dongli community',
      'position': 'Fengtai-Corner_Gate',
      'houseId': 9,
      'describe': '2 room 1 halls | 54.11square meters | south north | Banlou | high_floor ( total: 6 )',
      'unitPrice': 60063,
      'collected': 'true',
      'totalPrice': '3.25',
      'imgUrl': 'https://img0.baidu.com/it/u=3774158723,4269643202&fm=11&fmt=auto&gp=0.jpg'}]
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



