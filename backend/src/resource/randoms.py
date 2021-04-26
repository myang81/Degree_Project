
import numpy as np
import random
import xlwt

#
# 市界的地理坐标为：北纬39”26’至41”03’,东经115”25’至 117”30’

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("My Workbook")
print(worksheet)

a=[]
for i in range(0,5107):
    x=random.uniform(115,117)
    y=random.uniform(39,41)
    a.append(str(
        ( str(y))))

print(a[0])
j=0
for i in a:
    worksheet.write(j,0,i)
    j=j+1

workbook.save("test.xls")