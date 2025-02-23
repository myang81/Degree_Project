from src.extension import db
from src.Utility import enumMachine
import json
#https://blog.csdn.net/mingyuli/article/details/104546321/

class Target(object):
    json={}

    def __init__(self,totalPriceRange,unitPriceRange,area,district,houseStructure,direction,decoration,heating,elevator):
        self.totalPriceRange=totalPriceRange
        self.unitPriceRange=unitPriceRange
        self.area=area
        self.distrcit=district
        self.heating=heating
        self.houseStructure=houseStructure
        self.direction=direction
        self.decoration=decoration
        self.elevator=elevator


    def toEnum(self):
        dict={}
        dict["totalPriceRange"] = self.totalPriceRange
        dict["unitPriceRange"] = self.unitPriceRange
        dict["area"] = self.area
        dict["district"] = self.distrcit
        dict["houseStructure"] = self.houseStructure
        dict["decoration"] = self.decoration
        dict["direction"] = self.direction
        dict["heating"] = self.heating
        dict["elevator"] = self.elevator


    @classmethod
    def loadJson(self,d):
        data = json.loads(d)
        a=Target(totalPriceRange=data['totalPriceRange'],unitPriceRange=data['unitPriceRange'],
                 area=data['area'],district=data['district'],houseStructure=data['houseStructure'],direction=data['direction']
                 ,decoration=data['decoration'],heating=data['heating'],elevator=data['elevator'])
        print(type(a))
        return a

    @classmethod
    def convertJson(self,target):
        data={}
        data['totalPriceRange']=target.totalPriceRange
        data['unitPriceRange']=target.unitPriceRange
        data['area']=target.area
        data['district']=target.distrcit
        data['houseStructure']=target.houseStructure
        data['direction']=target.direction
        data['decoration']=target.decoration
        data['heating']=target.heating
        data['elevator']=target.elevator
        j=json.dumps(data,ensure_ascii=False)
        return j

    @classmethod
    def initDict(self):
        data={}
        data['totalPriceRange'] = [0,100]
        data['unitPriceRange'] = [0,999]
        data['area'] = [1,2]
        data['district'] = [1]
        data['houseStructure'] = [1]
        data['direction'] = [1]
        data['decoration'] = [0]
        data['heating'] = [1]
        data['elevator'] = [0]
        return data

    def getJson(self):
        str=Target.convertJson(self)
        return str

    def toDict(self):
        dict={}
        dict["totalPriceRange"]=self.totalPriceRange
        dict["unitPriceRange"]=self.unitPriceRange
        dict["area"]=self.area
        dict["district"]=self.distrcit
        dict["houseStructure"]=self.houseStructure
        dict["decoration"]=self.decoration
        dict["direction"]=self.direction
        dict["heating"]=self.heating
        dict["elevator"]=self.elevator
        return dict

    def __repr__(self):
        return self.getJson()
