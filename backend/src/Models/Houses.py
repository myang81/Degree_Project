# coding: utf-8
from src.extension import db




collections=db.Table('user_houses_collection',
            db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
            db.Column('house_id',db.Integer,db.ForeignKey('houses.id'))
                     )

publishments=db.Table('user_houses_publish',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('house_id', db.Integer, db.ForeignKey('houses.id'))
                  )


class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
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
    south = db.Column(db.String(120), index=True, unique=False)
    west = db.Column(db.String(120), index=True, unique=False)
    north = db.Column(db.String(120), index=True, unique=False)
    east_south = db.Column(db.String(120), index=True, unique=False)
    east_north = db.Column(db.String(120), index=True, unique=False)
    west_south = db.Column(db.String(120), index=True, unique=False)
    west_north = db.Column(db.String(120), index=True, unique=False)
    room = db.Column(db.Integer)
    Longitude = db.Column(db.String(120), index=True, unique=False)
    Latitude = db.Column(db.String(120), index=True, unique=False)
    PublishTime = db.Column(db.String(120), index=True, unique=False)
    imgUrl = db.Column(db.String(120), index=True, unique=False)
    collected = db.Column(db.String(120), index=True, unique=False)
    saled=db.Column(db.String(120),index=True,unique=False)


    collection_users=db.relationship('User',secondary=collections,backref=db.backref('collections',lazy='dynamic'),lazy='dynamic')
    publishments_users = db.relationship('User', secondary=publishments, backref=db.backref('publishments', lazy='dynamic'),
                                       lazy='dynamic')

    def generateDirection(self):
        direction_str = ""
        if self.east == 'no':
            direction_str += ""
        else:
            direction_str += self.east + " "
        if self.west == 'no':
            direction_str += ""
        else:
            direction_str += self.west + " "
        if self.south == 'no':
            direction_str += ""
        else:
            direction_str += self.south + " "
        if self.north == 'no':
            direction_str += ""
        else:
            direction_str += self.north + " "
        if self.east_south == 'no':
            direction_str += ""
        else:
            direction_str += self.east_south + " "
        if self.west_south == 'no':
            direction_str += ""
        else:
            direction_str += self.west_south + " "
        if self.east_north == 'no':
            direction_str += ""
        else:
            direction_str += self.east_north + " "
        if self.west_north == 'no':
            direction_str += ""
        else:
            direction_str += self.west_north + " "
        return direction_str

    def isSold(self):
        if self.saled=="TRUE":
            return "TRUE"
        else:
            return "FALSE"

    def getCollected(self):
        if self.collected=="FALSE":
            return "false"
        else:
            return "true"

    def setCollected(self,value):
        if value=="false":
            self.collected="FALSE"
        if value=="true":
            self.collected="TRUE"
        db.session.add(self)
        db.session.commit()

    def generateDetail(self):
        direction_str = ""
        if self.east == 'no':
            direction_str += ""
        else:
            direction_str += self.east + " "
        if self.west == 'no':
            direction_str += ""
        else:
            direction_str += self.west + " "
        if self.south == 'no':
            direction_str += ""
        else:
            direction_str += self.south + " "
        if self.north == 'no':
            direction_str += ""
        else:
            direction_str += self.north + " "
        if self.east_south == 'no':
            direction_str += ""
        else:
            direction_str += self.east_south + " "
        if self.west_south == 'no':
            direction_str += ""
        else:
            direction_str += self.west_south + " "
        if self.east_north == 'no':
            direction_str += ""
        else:
            direction_str += self.east_north + " "
        if self.west_north == 'no':
            direction_str += ""
        else:
            direction_str += self.west_north + " "

        first='https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg'
        if self.imgUrl !="None":
            firstPics = self.imgUrl.split(',')
            first = firstPics[0]


        return {'title': self.title,
                'position': self.Specific_area,
                'district': self.District,
                'houseId': self.id,
                'describe': str(self.room) + ' room' + str(self.hall) + ' halls' + ' |' + str(
                    self.floor_area) + ' square meters ' + '| ' + str(direction_str) + '| '
                            + str(self.Building_Type) + ' | ' +
                            str(self.House_structure) + ' ( total: ' +
                            str(self.total_floors) + ' )',
                'sold':self.saled,
                'unitPrice': str(self._unit_price),
                'collected': self.getCollected(),
                'totalPrice': self.price,
                'otherInfo': str(self.Interior_design + '|' + self.heating + '|' + self.elevator),
                'imgUrl': first,
                # 'imgUrl': 'https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg',
                "latitude": self.Latitude,
                "longitude": self.Longitude
                }
