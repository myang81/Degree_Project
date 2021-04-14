# coding: utf-8
from src.extension import db

class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=False)
    price = db.Column(db.Integer)
    _unit_price = db.Column(' unit price', db.Integer)
    Property_information = db.Column(db.String(120), index=True, unique=False)
    floor_area = db.Column('floor area', db.Float)
    House_structure = db.Column(db.String(120), index=True, unique=False)
    Building_Type = db.Column(db.String(120), index=True, unique=False)
    Architectural_structure = db.Column(db.String(120), index=True, unique=False)
    Interior_design = db.Column(db.String(120), index=True, unique=False)
    ladder_ratio = db.Column('ladder ratio', db.Float)
    heating = db.Column(db.String(120), index=True, unique=False)
    elevator = db.Column(db.String(120), index=True, unique=False)
    District = db.Column(db.String(120), index=True, unique=False)
    Specific_area = db.Column(db.String(120), index=True, unique=False)
    hall = db.Column(db.Integer)
    kitchen = db.Column(db.Integer)
    toilet = db.Column(db.Integer)
    Floor_type = db.Column(db.String(120), index=True, unique=False)
    total_floors = db.Column('total floors', db.Integer)
    east = db.Column(db.String(120), index=True, unique=False)
    south =db.Column(db.String(120), index=True, unique=False)
    west = db.Column(db.String(120), index=True, unique=False)
    north = db.Column(db.String(120), index=True, unique=False)
    east_south = db.Column(db.String(120), index=True, unique=False)
    east_north = db.Column(db.String(120), index=True, unique=False)
    west_south = db.Column(db.String(120), index=True, unique=False)
    west_north = db.Column(db.String(120), index=True, unique=False)
    room = db.Column(db.Integer)
    Latitude_and_longitude = db.Column(db.String(120), index=True, unique=False)
    PublishTime = db.Column(db.String(120), index=True, unique=False)
    imgUrl = db.Column(db.String(120), index=True, unique=False)
    None2 = db.Column(db.String(120), index=True, unique=False)
    _None = db.Column(db.String(120), index=True, unique=False)


    def generateDetail(self):
        direction_str=""
        if self.east=='no':
            direction_str+=""
        else:
            direction_str+=self.east
        if self.west == 'no':
            direction_str += ""
        else:
            direction_str += self.west+" "
        if self.south == 'no':
            direction_str += ""
        else:
            direction_str += self.south+" "
        if self.north == 'no':
            direction_str += ""
        else:
            direction_str += self.north+" "
        if self.east_south == 'no':
            direction_str += ""
        else:
            direction_str += self.east_south+" "
        if self.west_south == 'no':
            direction_str += ""
        else:
            direction_str += self.west_south+" "
        if self.east_north == 'no':
            direction_str += ""
        else:
            direction_str += self.east_north+" "
        if self.west_north == 'no':
            direction_str += ""
        else:
            direction_str += self.west_north+" "

        return     {'title': self.title,
     'position': self.Specific_area,
     'houseId': self.id,
     'describe': str(self.room) +' room'+ str(self.hall) +' halls' + ' |'+ str(self.floor_area)+' square meters '+'| '+str(direction_str) +'| '
                 +str(self.Building_Type)+  ' | '+
                 str(self.House_structure)+' ( total: '+
                 str(self.total_floors)+' )',
     'unitPrice':str(self._unit_price),
     'collected': 'true',
     'totalPrice': self.price,
     'imgUrl': 'https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg'}