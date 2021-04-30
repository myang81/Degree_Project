from flask import Blueprint, render_template, session, flash, redirect, request, url_for
from src.extension import db
from src.Models.Houses import House
from src.Utility import enumMachine
import math
import re
from time import time
import os
import json
from backend.src.Models.Targets import Targets

c_id = 1
c_target = Targets.query.filter(id=c_id).first()
tP = c_target.totalPriceRange
up = c_target.unitPriceRange
ar = c_target.area
ds = c_target.district
he = c_target.heating
hs = c_target.houseStructure
dr = c_target.direction
de = c_target.decoration
el = c_target.elevator

searchString = ar + ',' + ds + ',' + he + ',' + hs + ',' + de

######### indexing finish
document = {}
houseList = []
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
    if r[1] > 0 or searchString == '':
        houseList.append(document[int(r[0])])
    rank += 1
print(len(houseList))