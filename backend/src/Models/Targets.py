# coding: utf-8
from src.extension import db
import json


class Targets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalPriceRange = db.Column(db.String(64), index=True, unique=True)
    unitPriceRange = db.Column(db.String(128))
    area=db.Column(db.String(128))
    district=db.Column(db.String(128))
    heating=db.Column(db.String(128))
    houseStructure=db.Column(db.String(128))
    direction=db.Column(db.String(128))
    decoration=db.Column(db.String(128))
    elevator=db.Column(db.String(128))

    @classmethod
    def loadJson(self, d):
        data = json.loads(d)
        a = Target(totalPriceRange=data['totalPriceRange'], unitPriceRange=data['unitPriceRange'],
                   area=data['area'], district=data['district'], houseStructure=data['houseStructure'],
                   direction=data['direction']
                   , decoration=data['decoration'], heating=data['heating'], elevator=data['elevator'])
        return a

