#https://www.cnblogs.com/sanghai/p/6243529.html

class District():
    district={"Dongcheng":0,"Fengtai":1,"Yizhuang":2,"Daxing":3,"Miyun":4,"Pinggu":5,"Yanqing":6,"Huairou":7,"Fangshan":8,"Changping":9,"Chaoyang":10,"Haidian":11,"Shijingshan":12,"Xicheng":13,"Tongzhou":14,"Mentougou":15,"Shunyi":16}
    @staticmethod
    def field2enum(field):
        enum=District.district[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field=list(District.district.keys())[list(District.district.values()).index(enum)]
        return field

class PropertyInfo():
    propertyInfo={"non_co_ownership": 0, "co_ownership": 1}

    @staticmethod
    def field2enum(field):
        enum = PropertyInfo.propertyInfo[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(PropertyInfo.propertyInfo.keys())[list(PropertyInfo.propertyInfo.values()).index(enum)]
        return field

class House_structrue():
    house_structure = {"flat_floor": 0, "duplex": 1, "skip_floor": 2, "staggered_floor": 3}
    @staticmethod
    def field2enum(field):
        enum = House_structrue.house_structure[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(House_structrue.house_structure.keys())[list(House_structrue.house_structure.values()).index(enum)]
        return field

class Building_type():
    building_type = {"Banlou": 0, "tower": 1, "banta_combination": 2, "bungalow": 3}

    @staticmethod
    def field2enum(field):
        enum = Building_type.building_type[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Building_type.building_type.keys())[list(Building_type.building_type.values()).index(enum)]
        return field

class Ddecoration():
    decortaion={"hardcover": 0, "simple_decoration": 1, "others": 2, "rough": 3}

    @staticmethod
    def field2enum(field):
        enum = Ddecoration.decortaion[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Ddecoration.decortaion.keys())[list(Ddecoration.decortaion.values()).index(enum)]
        return field

class Heating():
    heating = {"central_heating": 0, "self_heating": 1}
    @staticmethod
    def field2enum(field):
        enum = Heating.heating[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Heating.heating.keys())[list(Heating.heating.values()).index(enum)]
        return field

class Elevator():
    elevator = {"elevator": 0, "no": 1,"no_data_yet":3}
    @staticmethod
    def field2enum(field):
        enum = Elevator.elevator[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Elevator.elevator.keys())[list(Elevator.elevator.values()).index(enum)]
        return field


class Floor_type():
    floor_type = {
        "middle_floor": 0,
        "low_floor": 1,
        "high_floor": 2,
        "top_floor": 3,
        "bottom_floor": 4,
        "basement": 5,
    }
    @staticmethod
    def field2enum(field):
        enum = Floor_type.floor_type[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Floor_type.floor_type.keys())[list(Floor_type.floor_type.values()).index(enum)]
        return field


class Direction():
    direction = {
        "east": 0,
        "south": 1,
        "west": 2,
        "north": 3,
        "southeast": 4,
        "northeast": 5,
        "southwest": 6,
        "northwest": 7,
    }

    @staticmethod
    def field2enum(field):
        enum = Direction.direction[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Direction.direction.keys())[list(Direction.direction.values()).index(enum)]
        return field


class Building_structrue():
    building_structrue={"steel_concrete_structure":0,"mixed_structure":1,"brick_concrete_structure":2,"steel_structure":4,"brick_wood_structure":5,"frame_structure":6}

    @staticmethod
    def field2enum(field):
        enum = Building_structrue.building_structrue[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field = list(Building_structrue.building_structrue.keys())[list(Building_structrue.building_structrue.values()).index(enum)]
        return field

class Region():
    region={"CBD": 0, "Qilizhuang": 1, "Wanshou_Road": 2, "Wanliu": 3, "Wanda": 4, "Sanyuanqiao": 5, "Sanlitun": 6,
     "Shangdi": 7, "Century_City": 8, "Dongguan": 9, "Dongdan": 10, "Dongsi": 11, "Dongba": 12, "East_Bridge": 13,
     "Dongzhimen": 14, "Donghua_Market": 15, "Zhongguancun": 16, "Central_Villa": 17, "Fengtai_others": 18,
     "Linheli": 19, "Lizer": 20, "Yihezhuang": 21, "Qiaozhuang": 22, "jiukeshuCarrefour": 23, "Erlizhuang": 24,
     "Wukesong": 25, "Wudaokou": 26, "Wulidian": 27, "Asian_Games_Village": 28, "Asian_Games_Village_Camp": 29,
     "crossing": 30, "Yizhuang": 31, "Others_in_Yizhuang_Development_Zone": 32, "Liangmaqiao": 33, "Jianxiangqiao": 34,
     "Anise": 35, "princess_grave": 36, "Liuli_bridge": 37, "Liupu_Kang": 38, "Junbo": 39,
     "Agricultural_Exhibition_Hall": 40, "Feng_Village": 41, "Liu_Jia_Yao": 42, "front_door": 43, "Jinsong": 44,
     "Beiqijia": 45, "Beijing_South_Railway_Station": 46, "Beiguan": 47, "Beidadi": 48, "Beitaipingzhuang": 49,
     "Beijing_University_of_Technology": 50, "Beiyuan": 51, "Shibalidian": 52, "Shilibao": 53, "Shilibao_Town": 54,
     "Shilihe": 55, "Huawei_bridge": 56, "south_central_axis_airport_business_district": 57, "Nankou": 58,
     "south_Beach": 59, "Nanshao": 60, "Lugou_Bridge": 61, "Changwa": 62, "shuangjing": 63, "double_bridge": 64,
     "shuangyushu": 65, "Gubeikou_Town": 66, "Ancient_city": 67, "Youanmennei": 68, "youanmenwai": 69, "Houshayu": 70,
     "Heyi": 71, "Peace_Lane": 72, "sijiqing": 73, "Sihui": 74, "Huiguan": 75, "Tuanjie_Lake": 76,
     "National_Exhibition": 77, "Yuanmingyuan": 78, "Dianmen": 79, "kuatou": 80, "Chengguan": 81, "Chengzi": 82,
     "Daxing_others": 83, "Daxing_new_airport": 84, "daxing_new_airport_villa_area": 85, "Dashanzi": 86, "Dayu": 87,
     "Dawang_road": 88, "Dahongmen": 89, "The_temple_of_heaven": 90, "Tianning_Temple": 91, "Tiangongyuan": 92,
     "Tiangongyuan_South": 93, "tiantongyuan": 94, "Taiping_Bridge": 95, "Sun_Palace": 96, "Olympic_Park": 97,
     "Xueyuan_Road": 98, "Anning_Village": 99, "Andingmen": 100, "Anzhen": 101, "songjiazhuang": 102, "Guanyuan": 103,
     "Dinghui_Temple": 104, "Dingfu_Village": 105, "Xuanwumen": 106, "Miyun_others": 107, "Miyun_Town": 108,
     "Xiaotangshan": 109, "Xiaoxitian": 110, "Yuegezhuang": 111, "Chongwenmen": 112, "Gongti": 113, "Zuoanmen": 114,
     "Changying": 115, "Pinggu_others": 116, "Guanganmen": 117, "Guangqumen": 118, "Yanqing_others": 119,
     "Jianguo_men_Nei": 120, "Outside_Jianguo": 121, "Deshengmen": 122, "Huairou": 123, "Huixin_West_Street": 124,
     "Chengshou_Temple": 125, "Fangshan_others": 126, "New_palace": 127, "Xinjiekou": 128, "Fangzhuang": 129,
     "Old_palace": 130, "Changping_others": 131, "Yuetan": 132, "Wangjing": 133, "Chaoyang_Park": 134,
     "Chaoyang_others": 135, "Inside_Chaoyang_Gate": 136, "Outside_Chaoyang_Gate": 137, "Chaoqing": 138,
     "Muxiyuan": 139, "muxidi": 140, "Li_Qiao": 141, "Yangzhuang": 142, "Orchard": 143, "Orchard_Street": 144,
     "Jujube_Garden": 145, "pear_garden": 146, "Happy_Valley": 147, "Wuyi_Garden": 148, "Yongdingmen": 149,
     "Shahe": 150, "Foreign_bridge": 151, "Haidian_others": 152, "Haidian_North_New_District": 153, "Qinghe": 154,
     "Xiwengzhuang_Town": 155, "riverside_West": 156, "Pan_Jiayuan": 157, "Lu_Yuan": 158, "Yinghai": 159,
     "dengshikou": 160, "Yanshan": 161, "Yansha": 162, "Niujie": 163, "Peony_Garden": 164, "Jade_bridge": 165,
     "Yuquanying": 166, "Yuquan_Road": 167, "Liuli_River": 168, "Ganjiakou": 169, "Manna_garden": 170,
     "Sweet_water_garden": 171, "Tiancun": 172, "Baishiqiao": 173, "White_paper_shop": 174, "Baiziwan": 175,
     "Zaojun_Temple": 176, "See_Dan_bridge": 177, "Zhichun_Road": 178, "shifoying": 179, "shijingshan_others": 180,
     "Shimen_camp": 181, "science_and_Technology_Park": 182, "Doudian": 183, "Lishui_bridge": 184, "Guanzhuang": 185,
     "Zizhuqiao": 186, "Red_temple": 187, "Laoshan": 188, "Good_country": 189, "shaoyaoju": 190,
     "Hometown_of_flowers": 191, "Suzhou_bridge": 192, "Apple_Orchard": 193, "Caoqiao": 194, "Caihuying": 195,
     "Puhuangyu": 196, "Xisanqi": 197, "Xierqi": 198, "Xiguan_Huandao": 199, "Xibeiwang": 200, "Xidan": 201,
     "Xisi": 202, "Xiba_River": 203, "Xishan": 204, "Xizhimen": 205, "Xihongmen": 206, "Xiluoyuan": 207,
     "Guanyin_Temple": 208, "Corner_Gate": 209, "dougezhuang": 210, "Zhao_Gongkou": 211, "Chegongzhuang": 212,
     "Tongzhou_others": 213, "Tongzhou_Beiyuan": 214, "Jiuxianqiao": 215, "Jinbao_Street": 216, "Financial_Street": 217,
     "Changchun_Street": 218, "Changyang": 219, "Mentougou_others": 220, "Yan_Village": 221, "fumen": 222,
     "Taoran_Pavilion": 223, "Huoying": 224, "green_pagoda": 225, "Hancun_River": 226, "Shunyi_others": 227,
     "Shunyi_City": 228, "Summer_Palace": 229, "Capital_Airport": 230, "Ma_Po": 231, "Majiabao": 232, "Madian": 233,
     "malianwa": 234, "malian_road": 235, "majuqiao": 236, "Gaobeidian": 237, "Gaomi_shop": 238, "Weigong_Village": 239,
     "Lugu": 240, "Huangcunzhong": 241, "Huangcun_railway_station": 242, "Gulou_Street": 243, "Gulou_Streets": 244}


    @staticmethod
    def field2enum(field):
        enum=Region.region[field]
        return enum

    @staticmethod
    def enum2field(enum):
        field=list(Region.region.keys())[list(Region.region.values()).index(enum)]
        return field




if __name__ == '__main__':
    enum=Region.field2enum(field="Huangcunzhong")
    print(enum)
    field = Region.enum2field(enum=241)
    print(field)
    enum = District.field2enum(field="Yizhuang")
    print(enum)
