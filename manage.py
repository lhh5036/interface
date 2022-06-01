'''
@File: manage.py
@time:2021/8/19
@Author:quanliu 181324
@Desc: 总入口
'''
from apps import create_app
from flask import render_template,request,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
import os
# 必须要在引入db前先引入db.Model类
from models import User,Teacher
from dbExat import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # 实例化APP 进入开发环境

db.drop_all(bind=["test_db"],app=app) # 删除表
db.create_all(bind=["test_db"],app=app) # 创建表

class RegisterForm(FlaskForm):
    username = StringField(label='username',validators=[DataRequired()], render_kw={'placeholder': 'username', 'class': 'input_text'})
    password = PasswordField(label='password',validators=[DataRequired(),Length(3, 8, '密码长度必须在3-8之间')])
    cpassword = PasswordField(label='cpassword',validators=[DataRequired(),EqualTo('password', '两次密码不一致')])
    submit = SubmitField('提交')



# 接口调用入口
@app.route("/projectEntry")
def estoneInterfaceEntry():
    if 'username' in session:
        username = session['username']
        return render_template("system_entry.html",name=username)
    return redirect(url_for('login'))

@app.route('/login',methods=['POST','GET'])
def login():
    print(db)
    print(db.Model.__name__)
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        if user == "admin" and password == "123456":
            session['username'] = user
            session['password'] = password
            flash('You were successfully logged in')
            return redirect('projectEntry') # redirect直接是url，就是app.route的路径参数；url_for()是对函数进行操作
        elif user == "" or password == "":
            error = "请输入用户名和密码!"
            return render_template('login.html', error=error)
        else:
            error = "用户名或密码错误，请重新输入!"
            flash('You were failed logged in')
            return render_template('login.html',error=error)
    else:
        # user = request.args.get("name")
        # password = request.args.get("password")
        # if user == "admin" and password == "123456":
        #     session['username'] = user
        #     session['password'] = password
        #     flash('You were successfully logged in')
        #     return redirect(url_for('estoneInterfaceEntry'))
        # elif user == "" or password == "":
        #     error = "请输入用户名和密码!"
        #     return render_template('login.html',error=error)
        # else:
        #     error = "用户名或密码错误，请重新输入!"
        #     flash('You were failed logged in')
        #     return render_template('login.html',error=error)
        return render_template('login.html')


@app.route('/logout',endpoint='logout',methods=['POST'])
def logout():
    session.clear()
    return '666'

if __name__ == '__main__':
    app.run()