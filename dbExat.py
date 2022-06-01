'''
@File: dbExat.py
@time:2022/5/31
@Author:quanliu 181324
@Desc:创建数据库对象
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # 实例化一个SQLAlchemy对象，用于操作数据库