from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
import os
from src.setting import basedir
import datetime
import random



apiv2=Blueprint('api2',__name__)

# !/usr/bin/env python

import base64


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])
UPLOAD_FOLDER = 'upload'
#-*-coding:utf-8-*-

class Pic_str:
    def create_uuid(self): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
        randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum);
        uniqueNum = str(nowTime) + str(randomNum);
        return uniqueNum;


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@apiv2.route('/upload')
def upload_test():
    return render_template('up.html')


# 上传文件
@apiv2.route('/uploadimg', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, UPLOAD_FOLDER)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str().create_uuid() + '.' + ext
        f.save(os.path.join(file_dir, new_filename))
        url = "http://127.0.0.1:5000/show/" + new_filename

        return jsonify({
            "success": 1,
            "data":{
                "imgUrl":url
            },
            "error":"None"
            }
            )
    else:
        return jsonify(
            {
                "success": 0,
                "data": {
                },
                "error":"the fomat is not allowed"
        }
        )


@apiv2.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('upload', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        pass


# show photo
@apiv2.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, UPLOAD_FOLDER)
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass

