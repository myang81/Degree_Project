from flask import Blueprint, render_template, session, flash, redirect, request, url_for
from src.extension import db
from src.Models.Houses import House
from src.Utility import enumMachine
import math
import re
from time import time
import os
import json

list = Blueprint('list', __name__)


###################################################
# 3. 列表接口
############################################
@list.route("/test", methods=['GET', 'POST'])
def test():
    return 0


def calculateLength(dict):  # calculate the length of a document
    length = 0
    for values in dict.values():
        length += values
    return length


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


####################################
#	3.1. 获取列表数据接口：        ###
####################################

# 输入： timeRange	Array	发布时间区间	内部为字符串日历时间："yyyy-mm-dd"
# priceRange	Array	价格区间	内部为字符串格式价格："1000000"
# otherFeatures	Object	其他特征包装变量	对象内部特征根据配置静态文件中字典解析
# pageNum	String	当前页数	分页用数据
# pageSize	String	每页个数	分页用数据
# searchString	String	搜索字符串	bm25搜索

# 输出： "success": 1,
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

# 变量解释: argDict： 请求用的参数字典
@list.route("/getHouseList", methods=['GET', 'POST'])
def getHouse():
    global argdict  # get the parameter from the front
    if request.method == 'POST':
        timeRange = None
        totalPriceRange = None
        unitPriceRange = None
        area = None
        district = None
        houseStructrue = None
        decoration = None
        direction = None
        heating = None
        elevator = None
        pageNum = None
        pageSize = None
        searchString = None

        timeRange = request.json.get('timeRange')
        if timeRange == [0, 0]:
            timeRange = [0, 9999990]

        totalPriceRange = request.json.get('totalPriceRange')
        if totalPriceRange == [0, 0]:
            totalPriceRange = [0, 9999999]

        unitPriceRange = request.json.get('unitPriceRange')
        if unitPriceRange == [0, 0]:
            unitPriceRange = [0, 99999999]

        area = request.json.get('area')
        if area == [0, 0]:
            area = [0, 99999999]

        districtEnum = request.json.get('district')
        if districtEnum == []:
            districtEnum = enumMachine.District.values

        district = []
        for item in districtEnum:
            district.append(enumMachine.District.enum2field(item))


        houseStructrueEnum=request.json.get('houseStructure')
        if houseStructrueEnum==[]:
            houseStructrueEnum=enumMachine.House_structrue.values
        print(houseStructrueEnum)
        houseStructrue=[]


        for item in houseStructrueEnum:
            houseStructrue.append(enumMachine.House_structrue.enum2field(item))

        direction_listEnum = request.json.get('direction')
        if direction_listEnum == []:
            direction_listEnum = enumMachine.Direction.values
        direction_list = []
        for item in direction_listEnum:
            direction_list.append(enumMachine.Direction.enum2field(item))

        decorationEnum = request.json.get('decoration')
        if decorationEnum == []:
            decorationEnum = enumMachine.Ddecoration.values
        decoration = []
        for item in decorationEnum:
            decoration.append(enumMachine.Ddecoration.enum2field(item))

        heatingEnum = request.json.get('heating')
        if heatingEnum == []:
            heatingEnum = enumMachine.Heating.values
        heating = []
        for item in heatingEnum:
            heating.append(enumMachine.Heating.enum2field(item))

        elevatorEnum = request.json.get('elevator')
        if elevatorEnum == []:
            elevatorEnum = enumMachine.Elevator.values
        elevator = []
        for item in elevatorEnum:
            elevator.append(enumMachine.Elevator.enum2field(item))

        pageNum = request.json.get('pageNum')
        pageSize = request.json.get('pageSize')
        searchString = request.json.get('searchString')

        argdict = {
            "timeRange": timeRange,
            "totalPriceRange": totalPriceRange,
            "unitPriceRange": unitPriceRange,
            "area": area,
            "district": district,
            "houseStructrue": houseStructrue,
            "direction": direction_list,
            "decoration": decoration,
            "heating": heating,
            "elevator": elevator,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "searchString": searchString
        }

        # 返回房子模型的数组

        houseList = []
        direction = {}
        # #process the drection
        # direction=argdict[direction]

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

        def filterDirection(l1, l2):
            l1.append('no')
            for element in l2:
                if element not in l1:
                    return False
            return True

        def convertListToEnum(li):
            for e in li:
                e['position'] = enumMachine.Region.field2enum(e['position'])
                e['district'] = enumMachine.District.field2enum(e['district'])
            return li
        # print(direction)
        # print(request.json)
        print("The filter requirement is:")
        print(argdict)
        print('searchString: ', searchString)
        houses = []
        total = 0

        document = {}
        document_id = 0
        houses = House.query.filter().all()
        for h in houses:
            temp_h = h.generateDetail()
            document[document_id] = temp_h
            document_id += 1
        #####Search Engine
        stopwords = set()  # A set to store the stopwords
        with open("stopwords.txt") as f:
            for line in f:
                line = line[:-1]  # Remove the /n in the back of the line
                stopwords.add(line)

        if not os.path.exists(
                "home_search.txt"):  # The following code are for indexing, will only run on the first run.
            print("This is the first time to run. The program needs document processing. Please wait a moment")
            N = 0  # Calculate the number of documents in the collection
            avg_doclen = 0  # The average length of a document in the collection, will be used later
            comp = re.compile('[^a-z^0-9^ ]')  # A compiler to remove the punctuation
            Ni = {}  # Number of documents contains term i, key is the term, value is Ni
            Fij = {}  # Frequency of term i in document j, key is the document number, value is a dict
            k = 1  # k for BM25
            b = 0.75  # b for BM25
            t1 = time()
            for docs in document.values():
                temp_l = []
                for v in docs.values():
                    if get_keys(docs, v)[0] != 'collected' and get_keys(docs, v)[0] != 'imgUrl' and get_keys(docs, v)[
                        0] != 'houseId':
                        temp_l.append(str(v))
                N += 1
                line = ' '.join(temp_l)
                # line = comp.sub(' ', line.lower())
                line = line.lower()
                line = line.replace("-", ",")
                line = line.replace("_", ",")
                line = line.replace(" ", ",")
                line = line.replace("|", ",")
                line_split = line.split(",")
                print(line_split)
                newDict = {}  # Store the frequency of terms in this document, key is the term, value is the frequency
                for elements in line_split:
                    avg_doclen += 1  # Calculate the number of terms in the document collection
                    if elements in newDict:  # Calculate the frequency of this term in this document
                        newDict[elements] += 1
                    else:
                        newDict[elements] = 1
                for terms in newDict:  # Calculate the number of documents contains this term
                    if terms not in Ni:
                        Ni[terms] = 1
                    else:
                        Ni[terms] += 1
                Fij[get_keys(document, docs)[0]] = newDict
            t2 = time()
            for terms in Ni.keys():
                Ni[terms] = math.log2(
                    (N - Ni[terms] + 0.5) / (Ni[terms] + 0.5))  # Calculate the value for future calculations
            avg_doclen = avg_doclen / N  # Calculate the average doc length
            index = {}  # Store the BM25 value of every term in every document, key is the document name, value is the BM25_dict
            for keys in Fij.keys():
                BM25_dict = {}  # Store the BM25 value of each term, key is the term, value is BM25 value
                lenDj = calculateLength(Fij[keys])
                for elements in Fij[keys].keys():
                    BM25 = (((Fij[keys])[elements] * (1 + k)) / (
                            (Fij[keys])[elements] + k * ((1 - b) + (b * lenDj) / avg_doclen))) * Ni[elements]
                    BM25_dict[elements] = BM25
                index[keys] = BM25_dict
            js = json.dumps(index)  # use json to store the dict in the txt file
            with open("home_search.txt", "w") as f:
                f.write(js)
            t3 = time()
            print("Document processing completed")
        ######### indexing finish
        file = open('home_search.txt', 'r')  # open the index file and store to a dictionary
        print("Please wait for the system to load the file")
        t4 = time()
        js = file.read()
        index = json.loads(js)
        t5 = time()
        print("done")
        print(t5 - t4)
        query = searchString
        print("Enter query: ", query)
        query = query.lower()
        similarity = {}  # A dict store the similarity, the  key is the document id, the value is the score
        query_term = []  # A list store the stemmed terms in the query
        print("Result for query: ")
        for elements in query.split(" "):
            if elements not in stopwords:  # remove stopwords
                query_term.append(elements)
        for documents in index:  # calculate similarity score for every document
            score = 0
            for terms in query_term:
                if terms in index[documents]:
                    score += (index[documents])[terms]
                similarity[documents] = score
        result = sorted(similarity.items(), key=lambda x: x[1], reverse=True)  # Sort by similarity
        rank = 1
        for r in result:  # Print top 15 results
            # print("rank: ", rank, "document: ", document[int(r[0])], "score: ", r[1])
            if r[1] > 0:
                houseList.append(document[int(r[0])])
            rank += 1
            # if rank == 16:
            #     break
        p_max = len(houseList)
        total = p_max
        print(p_max)
        # p_start = (int(pageNum) - 1) * int(pageSize)
        # p_end = p_start + 10
        # if p_end > p_max:
        #     p_end = p_max
        # houseList = houseList[p_start:p_end]
        filter_List = []
        if direction_listEnum == enumMachine.Direction.values:
            for h in houseList:
                if (argdict['totalPriceRange'][0] <= int(h['totalPrice']) <= argdict['totalPriceRange'][1] and
                        argdict['area'][0] <= float((h['describe'].split('|')[1]).split(' ')[0]) <= argdict['area'][1] and
                        argdict['unitPriceRange'][0] <= int(h['unitPrice']) <= argdict['unitPriceRange'][1] and
                        h['district'] in (argdict["district"]) and
                        (h['describe'].split('|')[4]).split(' ')[1] in (argdict['houseStructrue']) and
                        h['otherInfo'].split('|')[0] in (argdict["decoration"]) and
                        h['otherInfo'].split('|')[1] in (argdict["heating"]) and
                        h['otherInfo'].split('|')[2] in (argdict["elevator"])
                ):
                    filter_List.append(h)
            total = len(filter_List)
            print(total, '111')
        #     total=House.query.filter(House.price >argdict['totalPriceRange'][0],House.price<argdict['totalPriceRange'][1],
        #                             House.floor_area >argdict['area'][0],House.floor_area<argdict['area'][1],
        #                           House._unit_price>argdict['unitPriceRange'][0],House._unit_price<argdict['unitPriceRange'][1],
        #                          House.District.in_(argdict["district"]),
        #                          House.House_structure.in_(argdict['houseStructrue']),
        #
        #                          # House.east==direction["east"],House.west==direction["west"],House.east_north==direction["northeast"],House.east_south==direction["southeast"]
        #                          # ,House.north==direction["north"],House.south==direction["south"],House.west_south==direction["southwest"],House.east_south==direction["southwest"]
        #                          # ,
        #                         House.Interior_design.in_(argdict["decoration"]),
        #                         House.heating.in_(argdict["heating"])
        #                           ,House.elevator.in_(argdict["elevator"])
        #                          ).count()
        # 从数据库查找数据 在价格区间内的数据
        else:
            for h in houseList:
                if (argdict['totalPriceRange'][0] <= int(h['totalPrice']) <= argdict['totalPriceRange'][1] and
                        argdict['area'][0] <= float((h['describe'].split('|')[1]).split(' ')[0]) <= argdict['area'][
                            1] and
                        argdict['unitPriceRange'][0] <= int(h['unitPrice']) <= argdict['unitPriceRange'][1] and
                        h['district'] in (argdict["district"]) and
                        filterDirection((h['describe'].split('|')[2]).split(' '), argdict['direction']) and
                        (h['describe'].split('|')[4]).split(' ')[1] in (argdict['houseStructrue']) and
                        h['otherInfo'].split('|')[0] in (argdict["decoration"]) and
                        h['otherInfo'].split('|')[1] in (argdict["heating"]) and
                        h['otherInfo'].split('|')[2] in (argdict["elevator"])
                ):
                    filter_List.append(h)
            total = len(filter_List)
            print(total, '222')
        p_start = (int(pageNum) - 1) * int(pageSize)
        p_end = p_start + 10
        if p_end > total:
            p_end = total
        filter_List = filter_List[p_start:p_end]
        convertListToEnum(filter_List)
        print(filter_List)
            # houses=House.query.filter(House.price >argdict['totalPriceRange'][0],House.price<argdict['totalPriceRange'][1],
            #                                 House.floor_area >argdict['area'][0],House.floor_area<argdict['area'][1],
            #                               House._unit_price>argdict['unitPriceRange'][0],House._unit_price<argdict['unitPriceRange'][1],
            #                              House.District.in_(argdict["district"]),
            #                              House.House_structure.in_(argdict['houseStructrue']),
            #                              #
            #                              House.east==direction["east"],House.west==direction["west"],House.east_north==direction["northeast"],House.east_south==direction["southeast"]
            #                              ,House.north==direction["north"],House.south==direction["south"],House.west_south==direction["southwest"],House.east_south==direction["southwest"]
            #                              ,
            #                             House.Interior_design.in_(argdict["decoration"]),
            #                             House.heating.in_(argdict["heating"])
            #                               ,House.elevator.in_(argdict["elevator"])
            #                              ).all()
            # total=House.query.filter(House.price >argdict['totalPriceRange'][0],House.price<argdict['totalPriceRange'][1],
            #                         House.floor_area >argdict['area'][0],House.floor_area<argdict['area'][1],
            #                       House._unit_price>argdict['unitPriceRange'][0],House._unit_price<argdict['unitPriceRange'][1],
            #                      House.District.in_(argdict["district"]),
            #                      House.House_structure.in_(argdict['houseStructrue']),
            #
            #                      House.east==direction["east"],House.west==direction["west"],House.east_north==direction["northeast"],House.east_south==direction["southeast"]
            #                      ,House.north==direction["north"],House.south==direction["south"],House.west_south==direction["southwest"],House.east_south==direction["southwest"]
            #                      ,
            #                     House.Interior_design.in_(argdict["decoration"]),
            #                     House.heating.in_(argdict["heating"])
            #                       ,House.elevator.in_(argdict["elevator"])
            #                      ).count()
        #
        # for item in houses:
        #     houseList.append(item.generateDetail())
        #
        # print(houses)
        # print(total)

        return {
            "success": 1,
            "data": {
                "total": total,
                "houseList": filter_List

            },
            "error": None
        }
    else:
        return {
            "success": 1,
            "data": {
                "total": 'total',
                "houseList": 'houseList'

            },
            "error": None
        }

####################################
#	3.2. 添加收藏接口：        ###
####################################
# 输入

# @list.route("/addCollection",methods=['GET','POST'])
# def addCollection():
#

# 注释区域
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
#
#
#
