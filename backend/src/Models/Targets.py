# coding: utf-8
from src.extension import db
from src.Utility import enumMachine
import json
targets_user=db.Table('user_target',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('target_id', db.Integer, db.ForeignKey('targets.id'))
                  )


class Targets(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    totalPriceRange = db.Column(db.String(64))
    unitPriceRange = db.Column(db.String(128))
    area=db.Column(db.String(128))
    district=db.Column(db.String(128))
    heating=db.Column(db.String(128))
    houseStructure=db.Column(db.String(128))
    direction=db.Column(db.String(128))
    decoration=db.Column(db.String(128))
    elevator=db.Column(db.String(128))

    target_users =    db.relationship('User', secondary=targets_user, backref=db.backref('targets', lazy='dynamic'),
                    lazy='dynamic')
    # area = data['area'], district = data['district'], houseStructure = data['houseStructure'], direction = data[
    #     'direction']
    # , decoration = data['decoration'], heating = data['heating'], elevator = data['elevator']

    def toDict(self):
       return {
        "totalPriceRange": self.totalPriceRange,
       "unitPriceRange": self.unitPriceRange,
       "area": self.area,
       "district": self.district,
       "houseStructure":self.houseStructure,
       "direction":self.direction,
       "decoration":self.decoration,
       "heating":self.heating,
       "elevator":self.elevator

       }

    def toEnum(self):
        price=[]
        for i in self.totalPriceRange.split(","):
            price.append(int(i))
        p2=[]
        for i in self.unitPriceRange.split(","):
            p2.append(int(i))
        a=[]
        for i in self.area.split(","):
            a.append(int(i))
        d=[]
        for i in self.district.split(","):
            d.append(enumMachine.District.field2enum(i))
        d1=[]
        for i in self.direction.split(","):
            d1.append(enumMachine.Direction.field2enum(i))
        d2=[]
        for i in self.decoration.split(","):
            d2.append(enumMachine.Ddecoration.field2enum(i))
        e1=[]
        for i in self.elevator.split(","):
            e1.append(enumMachine.Elevator.field2enum(i))
        h=[]
        for i in self.houseStructure.split(","):
            h.append(enumMachine.House_structrue.field2enum(i))
        h1=[]
        for i in self.heating.split(","):
            h1.append(enumMachine.Heating.field2enum(i))
        h2=[]
        for i in self.houseStructure.split(","):
            h2.append(enumMachine.House_structrue.field2enum(i))
        return{
        "totalPriceRange": price,
        "unitPriceRange": p2,
        "area": a,
        "district": d,
        "houseStructure": h ,
        "direction": d1,
        "decoration": d2,
        "heating": h1,
        "elevator": e1
        }

    def saveTarget(self,target):
        print(target)
        total=target['totalPriceRange']
        t=[]
        for i in total:
            q=str(i)
            t.append(q)
        self.totalPriceRange=",".join(t)
        unit=target['unitPriceRange']
        u=[]
        for i in unit:
            p=str(i)
            u.append(p)
        self.unitPriceRange=",".join(u)
        area=[]
        for i in target['area']:
            area.append(str(i))
        self.area=",".join(area)
        print(area)
        district=[]
        for i in target['district']:
            district.append(enumMachine.District.enum2field(i))
        self.district=",".join(district)
        heating=[]
        for i in target['heating']:
            heating.append(enumMachine.Heating.enum2field(i))
        self.heating=",".join(heating)
        houseStructure=[]
        for i in target['houseStructure']:
            houseStructure.append(enumMachine.House_structrue.enum2field(i))
        self.houseStructure=",".join(houseStructure)
        direction=[]
        for i in target['direction']:
            direction.append(enumMachine.Direction.enum2field(i))
        self.direction=",".join(direction)
        decoration=[]
        for i in target['decoration']:
            decoration.append(enumMachine.Ddecoration.enum2field(i))
        self.decoration=",".join(decoration)
        elevator=[]
        for i in target['elevator']:
            elevator.append(enumMachine.Elevator.enum2field(i))
        self.elevator=",".join(elevator)
        db.session.add(self)
        db.session.commit()
        return self

