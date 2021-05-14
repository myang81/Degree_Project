import requests
import re
import time
import html
import os

"""请求网页"""
#此处设置headers为了防止反扒，因为服务器可以看到request.headers显示的'User-Agent'是'python-requests/.....'此时，服务器会意识到爬虫。
#我们可以到网页中的network中的header中找到官方的user-agent
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}

i = 0
for t in range(11,21):


    #这里的url网址要使用文件中对应网址文件中的url，因为网页的url对其内容进行了伪装，使部分页面内容无法拿到
    response = requests.get('http://bj.fang.ke.com/loupan/pg'+str(t)+'/', headers = headers)
    #自己的身份
    #print(response.request.headers)
    # print(response.text)
    html = response.text
    # print(html)
    """解析网页"""

    #网易云歌曲爬取
    #音乐外链：
    #https://music.liuzhijin.cn/
    #当播放歌曲时，在XHR中（Ajax接口）会多出来许多文件，getseeds文件中会获取到这个文件的网址


    #xpath库
    # 主要方法：
    # //  ：根目录
    # [] : 选择属性
    # / ：单个元素
    # @ ：提取这个元素



    #此处用的正则！！！！！！！！！！！！！！！
    #(.*?)表示最小匹配，即满足条件的情况只匹配一次
    #(.*)表示贪婪匹配
    #例如<H1>Chapter 1 - 介绍正则表达式</H1>
    #(.*?)结果为H1
    #(.*)结果为H1>Chapter 1 - 介绍正则表达式</H1









    urls = re.findall('<img alt=".*?" class="lj-lazy" data-original="(.*?)" src=".*?">',html)
    print(urls)
    
    dir = r'A:\Scrapy'
    # #os库用来操作系统，判断是否有此文件夹，如果没有用os.mkdir创建文件夹
    # if not os.path.exists(dir):
    #     os.mkdir(dir)
    # urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    # print(urls)
    # """保存图片"""



    for url in urls:
        #图片名字
        file_name = str(i)+'.jpg'
        response = requests.get(url,headers = headers)
        with open(dir+'/'+file_name,'wb') as f:
            f.write(response.content)
        i += 1


    # """保存图片"""
    # for url in urls:
    #
    #     #图片名字
    #     file_name = url.split('/')[-1]
    #     response = requests.get(url,headers = headers)
    #     with open(dir+ '/' +file_name,'wb') as f:
    #         f.write(response.content)
    #     i+=1

print("finish "+str(i)+"pics")