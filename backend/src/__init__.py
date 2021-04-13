from flask_cors import CORS
import os
from src.blueprints.collection import collection
from src.blueprints.apiV1 import apiv1
from src.blueprints.apiV2 import apiv2
from src.blueprints.login import login
from src.blueprints.register import register
from src.blueprints.list import list
from src.setting import config
from flask import Flask,render_template,Blueprint
from src.Models.Users import User
from src.Models.Houses import House
from src.extension import avatars
from src.extension import mail,db,moment,bootstrap,migrate,dropzone
from src.extension import socketio
import click


# 构建FLask APP 导入设置，允许跨域
def create_app(config_name=None):
    if config_name is None:
        config_name=os.getenv('FLASK_CONFIG','development')

    app=Flask(__name__)
    app.config.from_object(config[config_name])


    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    register_blueprint(app)
    register_error(app)
    register_externsion(app)
    register_shell_context(app)
    register_logging(app)
    register_commands(app)
    return app


# 绑定蓝图
def register_blueprint(app):
    app.register_blueprint(blueprint=register)
    app.register_blueprint(blueprint=collection)
    app.register_blueprint(blueprint=list)
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
    migrate.init_app(app,db)
    dropzone.init_app(app)
    avatars.init_app(app)
    socketio.init_app(app)



def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db,User=User,House=House)

#Customized Commands
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




app=create_app(None)





