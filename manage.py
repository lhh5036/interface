'''
@File: manage.py
@time:2021/8/19
@Author:quanliu 181324
@Desc: 总入口
'''
from functools import wraps
from apps import create_app
from flask import render_template,request,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
import os,time,json
from dbExat import db
from hashlib import md5
from flask_migrate import Migrate,MigrateCommand # 使用版本2.7.0;flask_migrate版本过高（3.1.0）会没有MigrateCommand这个函数
from flask_script import Manager # (使用版本2.0.5;版本2.0.6中没有flask._compat)
# python3 manage.py db init  ---初始化环境(#该命令会在当前目录下生成一个migrations文件夹，用于记录变更的版本信息)
# python3 manage.py db migrate  ---将模型生成一个迁移文件(#该命令会在此命令会在migrations下生成一个version文件夹，下面包含了对应版本的数据库操作py脚本以及创建数据库中版本表alembic_version。)
# python3 managepy db upgrade   ---将模型真正的映射到数据库中(#执行了version文件夹下的相应py版本，对数据库进行变更操作。 #以后的model变化，只要重复migrate和upgrade即可。)

# 模型 -->  迁移文件 --> 表
app = create_app(os.getenv('FLASK_CONFIG') or 'default') # 实例化APP 进入开发环境
# manager = Manager(app)
# # 1.要使用flask-migrate必须绑定app和db
# migrate = Migrate(app,db)
# # 2.把MigrateCommand(数据库迁移)命令添加到manager
# manager.add_command('db',MigrateCommand)

# 判断数据库是否存在表
with app.app_context():
    has_table = db.engine.dialect.has_table(db.engine.connect(), f"interface_result_info")
    if not has_table:
        # db.drop_all(bind=["test_db"],app=app) # 删除表
        db.create_all(bind=["test_db"],app=app) # 创建表

# 存放账号的json文件
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")
print(ACCOUNTS_FILE)
global SESSION_IDS
SESSION_IDS = {}
LOGIN_TIMEOUT = 60 * 60 * 24 # 登录超时时间设置

# 登录装饰器
def admin_login_req(func):
    @wraps(func)
    def demo(*args):
        if not session.get("username"):
            return redirect(url_for("login"))
        return func(*args)
    return demo


# 接口调用入口
@app.route("/projectEntry")
@admin_login_req
def estoneInterfaceEntry():
    return render_template("system_entry.html")

# 注册
@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    """注册用户信息"""
    username = request.form.get("username")
    password = request.form.get("password")
    newDict = {"username":username,"password":md5(password.encode()).hexdigest()} # 密码加密
    if not username or not password:  # 判断用户输入的参数
        return {"data": None, "status_code": "InvalidParams", "message": "must have username and password"}
    if not os.path.exists(ACCOUNTS_FILE):  # 判断是否存在指定文件
        return {"data": None, "status_code": "NotFound", "message": "not found accounts file"}
    # 先读取文件
    with open("accounts.json", "r+") as f:
        accounts = json.load(f)
    for account in accounts:
        if account["username"] == username:  # 判断是否用户已存在
            message = {"data": None, "status_code": "Duplicated", "message": "username is already exists"}
            return render_template("login.html", message=message)
        else:
            # 找回密码
            pass
    # 先注册
    accounts.append(newDict)
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)
    message = {"data": username, "status_code": "OK", "message": "register username successfully"}
    return redirect(url_for("login")) # redirect直接是url，就是app.route的路径参数；url_for()是对函数进行操作

# GET request.args.get("name")
# POST request.form['name']
# 登录
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    """用户登录"""
    username = request.form.get("username")
    password = request.form.get("password")
    if not os.path.exists(ACCOUNTS_FILE):  # 是否存在用户信息文件
        return {"data": None, "status_code": "NotFound", "message": "not found accounts file"}
    with open("accounts.json", "r+") as f:
        accounts = json.load(f)
    usernames = [account["username"] for account in accounts]
    if username not in usernames:  # 是否用户已注册
        # error = {"data": None, "status_code": "NotFound", "message": "username is not exists"}
        error = "用户名不存在，请点击注册按钮"
        return render_template("login.html",error=error)
    current_user = None
    for account in accounts:
        if account["username"] == username:
            current_user = account
            if md5(password.encode()).hexdigest() != account["password"]:  # 是否用户名密码正确
                # error = {"data": None, "status_code": "Unauthorized", "message": "password is not correct"}
                error = "密码错误,请重新输入"
                return render_template('login.html', error=error)
            session['username'] = username
            session['password'] = password
            return redirect('projectEntry')



@app.route('/logout',endpoint='logout',methods=['POST'])
def logout():
    session.clear()
    return '666'

if __name__ == '__main__':
    app.run()