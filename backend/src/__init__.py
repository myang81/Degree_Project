import _thread
import threading
import time

from flask_cors import CORS
import os
from src.blueprints.collection import collection
from src.blueprints.apiV1 import apiv1
from src.blueprints.apiV2 import apiv2
from src.blueprints.login import login
from src.blueprints.register import register
from src.blueprints.houseList import houseList
from src.blueprints.center import center
from src.setting import config
from flask import Flask, render_template, Blueprint
from src.Models.Users import User
from src.Models.Houses import House
from src.extension import avatars
from src.extension import loginManager
from src.extension import mail, db, moment, bootstrap, migrate, dropzone
from src.extension import socketio
import click

# 构建FLask APP 导入设置，允许跨域
from src.blueprints.houseList import preProcessing





def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    #photo setting
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    register_blueprint(app)
    register_error(app)
    register_externsion(app)
    register_shell_context(app)
    register_logging(app)
    register_commands(app)
    return app


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 绑定蓝图
def register_blueprint(app):
    app.register_blueprint(blueprint=register)
    app.register_blueprint(blueprint=center)
    app.register_blueprint(blueprint=collection)
    app.register_blueprint(blueprint=houseList)
    app.register_blueprint(blueprint=login)
    app.register_blueprint(blueprint=apiv2)
    app.register_blueprint(blueprint=apiv1)


def register_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error/400.html'), 400


def register_logging(app):
    pass


# 注册flask拓展
def register_externsion(app):
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    dropzone.init_app(app)
    avatars.init_app(app)
    socketio.init_app(app)
    loginManager.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, House=House)


# Customized Commands
def register_commands(app):
    @app.cli.command()
    def initdb():
        db.create_all()
        click.echo('Initialized database')

    @app.cli.command()
    def dbdrop():
        db.metadata.clear()
        db.drop_all()
        click.echo('Initialized database')


# def func_timer():
#     print('开始线程')
#     global timer  # 定义全局变量
#     # 定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
#     timer = threading.Timer(10, func_timer)  # 10秒调用一次函数
#
#     print("线程名称={},\n正在执行的线程列表:{},\n正在执行的线程数量={},\n当前激活线程={}\n".format(
#         timer.getName(), threading.enumerate(), threading.active_count(), timer.isAlive)
#     )
#     timer.start()  # 启用定时器
#
#
# func_timer()
# print('定时器启动成功-----')

def update_bm25():
    while True:
        time.sleep(3600)
        document = {}
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
        preProcessing(document)


app = create_app(None)


# try:
#     print('3213213')
#     thread1 = threading.Thread(target=start())
#     thread1.start()
#     thread = threading.Thread(target=update_bm25())
#     thread.start()
# except:
#     print("Error: 无法启动线程")
