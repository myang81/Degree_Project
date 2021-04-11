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
  'price': 52897.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 75.43square meters | south west north | Banlou | high_floor ( total: 6 )'},
 {'title': 'The corner gate of Majiabao is close to the subway, with good north-south transparency, sufficient lighting and complete supporting facilities',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 1,
  'price': 60203.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 69.1square meters | south north | Banlou | middle_floor ( total: 6 )'},
 {'title': 'Jiaomen Dongli, full of five unique, sincere sale, easy to see',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 2,
  'price': 51202.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 73.63square meters | north southeast | tower | high_floor ( total: 19 )'},
 {'title': 'Jiaomen Majiabao Jiaomen Dongli two bedroom Jiaomen East Station',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 3,
  'price': 59723.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 64.8square meters | south | tower | low_floor ( total: 19 )'},
 {'title': 'The corner gate of Majiabao is accessible from north to south, and the floor is full of five only two bedrooms',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 4,
  'price': 56587.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 53.9square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': 'Jiaomen Majiabao Manwu subway line 10 Line 4 Jiaomen west station',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 5,
  'price': 60999.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 54.1square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': 'Fine decoration of three bedroom low floor in dongsida community, Jiaomen, Majiabao',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 6,
  'price': 52286.0,
  'Collected': 'true',
  'describe': '3 room 1 halls | 76.12square meters | south north | Banlou | low_floor ( total: 6 )'},
 {'title': 'Sunshine Garden Corner Gate East Majiabao dahongmen north south two houses',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 7,
  'price': 75564.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 89.99square meters | south north | Banlou | top_floor ( total: 19 )'},
 {'title': 'Jiaomen, Majiabao, Yangqiao, the only regular two bedroom in five years',
  'position': 'Fengtai-Corner_Gate',
  'houseId': 8,
  'price': 57245.0,
  'Collected': 'true',
  'describe': '2 room 1 halls | 70.4square meters | south north | Banlou | high_floor ( total: 6 )'},
 {'title': 'Yangqiao, Majiabao, two bedrooms in Jiaomen Dongli community',
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



