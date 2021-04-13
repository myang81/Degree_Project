# coding=utf-8
import pymysql
import pandas as pd
import math
import re
from time import time
import os
import json

# # 连接数据库
# config = {'host': 'localhost',
#           'port': 3306,
#           'user': 'root',
#           'passwd': 'Chen0902',
#           'charset': 'utf8mb4',
#           'local_infile': 1
#           }
# conn = pymysql.connect(**config)
# cur = conn.cursor()

def calculateLength(dict):  # calculate the length of a document
    length = 0
    for values in dict.values():
        length += values
    return length


# load_csv函数，参数分别为csv文件路径，表名称，数据库名称
def load_csv(csv_file_path, table_name, database='test'):
    # 打开csv文件
    file = open(csv_file_path, 'r', encoding='utf-8')
    # 读取csv文件第一行字段名，创建表
    reader = file.readline()
    b = reader.split(',')
    colum = ''
    for a in b:
        colum = colum + a + ' varchar(255),'
    colum = colum[:-1]
    # 编写sql，create_sql负责创建表，data_sql负责导入数据
    create_sql = 'create table if not exists ' + table_name + ' ' + '(id' + colum + ')' + ' DEFAULT CHARSET=utf8'
    data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES" % (
    csv_file_path, table_name)

    # 使用数据库
    cur.execute('use %s' % database)
    # 设置编码格式
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    # 执行create_sql，创建表
    print(create_sql)
    cur.execute(create_sql)
    # 执行data_sql，导入数据
    print(data_sql)
    cur.execute(data_sql)
    conn.commit()
    # 关闭连接
    conn.close()
    cur.close()

# load_csv("final_home.csv", 'tab1')
df = pd.read_csv("20210408.csv", error_bad_lines=False)
document = {}
for d in range(len(df)):
    document[d] = (','.join([str(i) for i in df.loc[d,:].to_list()]))
print(document[1])

#####Search Engine
stopwords = set()  # A set to store the stopwords
with open("stopwords.txt") as f:
    for line in f:
        line = line[:-1]  # Remove the /n in the back of the line
        stopwords.add(line)

if not os.path.exists("home_search.txt"):  # The following code are for indexing, will only run on the first run.
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
        N += 1
        line = docs
        #line = comp.sub(' ', line.lower())
        line = line.lower()
        line = line.replace("-", ",")
        line = line.replace("_", ",")
        line = line.replace(" ", ",")
        line_split = line.split(",")
        print(line_split)
        # for i in range(len(line_split)):
        #     if i != 1:
        #         tempL = (comp.sub(' ',line_split[i])).split(' ')
        #         line_split.remove(line_split[i])
        #         for e in tempL:
        #             line_split.append(e)
        # print (line_split)
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
        Fij[docs] = newDict
        print(newDict)
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
# indexing finish
file = open('home_search.txt', 'r') # open the index file and store to a dictionary
print("Please wait for the system to load the file")
t4 = time()
js = file.read()
index = json.loads(js)
t5 = time()
print("done")
print(t5 - t4)
query = input("Enter a query for search, or enter QUIT to quit")
print("Enter query: ", query)
while query != "QUIT":  # Repeat this process until the user input QUIT
    query = query.lower()
    similarity = {}  # A dict store the similarity, the  key is the document id, the value is the score
    query_term = []  # A list store the stemmed terms in the query
    print("Result for query: ")
    for elements in query.split(" "):
        if elements not in stopwords:  # remove stopwords
            query_term.append(elements)
    print(query_term)
    for documents in index:  # calculate similarity score for every document
        score = 0
        for terms in query_term:
            if terms in index[documents]:
                score += (index[documents])[terms]
            similarity[documents] = score
    result = sorted(similarity.items(), key=lambda x: x[1], reverse=True)  # Sort by similarity
    rank = 1
    for r in result:  # Print top 15 results
        print("rank: ", rank, "document: ", r[0], "score: ", r[1])
        rank += 1
        if rank == 16:
            break
    query = input("Enter a query")