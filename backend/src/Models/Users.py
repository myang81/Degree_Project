
#https://bbs.csdn.net/topics/395304418
#Python中怎么将一个类实例化出来的对象以二进制的方式保存到文件里
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import pickle
from src.extension import db






class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email=db.Column(db.String(128))
    target=db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def saveTarget(self,target):
        self.target=target
        db.session.add(self)
        db.session.commit()

    def getTarget(self):
        target=self.target
        return target


    def __repr__(self):
        return '<User {}>'.format(self.username)