# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Home(Base):
    __tablename__ = 'home'

    名称 = Column(Text)
    总价 = Column(Integer)
    单价 = Column(Integer)
    产权信息 = Column(Text)
    户型 = Column(Text)
    楼层 = Column(Text)
    建筑面积 = Column(Text)
    户型结构 = Column(Text)
    套内面积 = Column(Text)
    建筑类型 = Column(Text)
    朝向 = Column(Text)
    建筑结构 = Column(Text)
    装修 = Column(Text)
    梯户比 = Column(Text)
    供暖 = Column(Text)
    电梯 = Column(Text)
    区域 = Column(Text)
    具体区域 = Column(Text)
    id = Column(Integer, primary_key=True)
