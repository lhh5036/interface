'''
@File: models.py
@time:2022/5/31
@Author:quanliu 181324
@Desc:数据库建表模型类（必须要被引入）
primary_key(主键)、unique(唯一)、index(索引)、default(默认值)
'''
from dbExat import db
import datetime


class InterfaceResultModel(db.Model):
    __bind_key__ = "test_db" # 绑定数据库
    __tablename__ = "interface_result_info" # 接口自动化结果表
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    modelName = db.Column(db.String(20),comment="模块名")
    systemName = db.Column(db.String(80), unique=True,comment="系统名称")
    testCaseNum = db.Column(db.Integer,comment="总的用例数")
    successCaseNum = db.Column(db.Integer,comment="执行成功数")
    failCaseNum = db.Column(db.Integer,comment="失败数")
    reportUrl = db.Column(db.String(500),comment="报告地址")
    updateTime = db.Column(db.DateTime,default=datetime.datetime.now(),onupdate=datetime.datetime.now())


# 一对一
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32), unique=True)
#     userdata = db.relationship('UserData', uselist=False, back_populates='user')
#
# class UserData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(200))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user = db.relationship('User', back_populates=('userdata'))
#
# 1.上述代码中的relationship，是关联属性的意思，是SQLAlchemy提供给开发者快速引用外键模型的一个对象属性，本身并不存在于MySQL中；
# 2.relationship的参数backref表示反向引用，通过外键模型查询主模型数据时的关联属性，通俗的讲就是在查DeviceDetail数据时，可以通过backref引用到Devices。
# 3.useList表示关联模型是否为List，如果为False，则不使用列表，而使用标量值。一对一关系中，需要设置relationship中的uselist=Flase
