'''
@File: models.py
@time:2022/5/31
@Author:quanliu 181324
@Desc:数据库建表模型类（必须要被引入）
'''
from dbExat import db


class User(db.Model):
    __bind_key__ = "test_db" # 绑定数据库
    __tablename__ = "user_info"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # 设置ID为主键并且自动增长
    username = db.Column(db.String(80), unique=True)

class Teacher(db.Model):
    __bind_key__ = "test_db" # 绑定数据库
    __tablename__ = "teacher_info"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # 设置ID为主键并且自动增长
    username = db.Column(db.String(80), unique=True)
