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
