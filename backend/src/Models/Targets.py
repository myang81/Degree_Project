# coding: utf-8
from src.extension import db

self.totalPriceRange = totalPriceRange
self.unitPriceRange = unitPriceRange
self.area = area
self.distrcit = district
self.heating = heating
self.houseStructure = houseStructure
self.direction = direction
self.decoration = decoration
self.elevator = elevator

class Targets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalPriceRange = db.Column(db.String(64), index=True, unique=True)
    unitPriceRange = db.Column(db.String(128))
    email=db.Column(db.String(128))
    target=db.Column(db.String(128))

