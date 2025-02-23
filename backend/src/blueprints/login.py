
from flask import Blueprint
from flask import request


from src.Models.Users import User

login=Blueprint('login',__name__)
#1. 登录页接口
#使用flask-login
#reference https://www.pianshen.com/article/5244187696/
#https://www.cnblogs.com/-wenli/p/14016905.html
#https://www.jianshu.com/p/7bff6e3d869b

#https://www.ucloud.cn/yun/42706.html
import time
import base64
import hmac
#生成token 入参：用户id

def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")

#验证token 入参：用户id 和 token
def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True

def res_json(successCode,data,error):
    res={
        "success": successCode,
        "data":data,
        "error":error
        }
    return res

#login in
@login.route("/login", methods=['GET', 'POST'])
def loginFunction():
    username = request.json.get('userName')
    password = request.json.get('password')
    obj = User.query.filter_by(username=username).first()
    if not obj:
        return res_json(0, '', 'The user is not found')
    if obj.check_password(password):
        token = generate_token(username)
        return res_json(1, {'userId':obj.id,'token': token}, 'Login Successfully')
    else:
        return res_json(0, '', 'Wrong Password')
