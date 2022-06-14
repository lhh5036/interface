'''
@File: updateInterResult.py
@time:2022/6/6
@Author:quanliu 181324
@Desc:默认filter是且的关系，如果使用or需要导入from sqlalchemy import or_；用法：filter(or_(User.name=="lisi",User.password==123))
排序：User.query.order_by(User.id.asc()).all()   User.query.order_by(User.id.desc()).all()
分组:db.session.query(User.role_id,func.count(User.role_id)).group_by(User.role_id).all() ---导入：from sqlalchemy import func

查询第一行:
User.query.filter(User.name=="lili").first()
User.query.get(2) -->精确获取第二行的数据
模糊查询：
from sqlalchemy import or_
objs = User.query.filter(User.name.like('%{keyword}%'.format(keyword=keyword))).all()-->区分大小写
objs = User.query.filter(User.name.ilike('%{keyword}%'.format(keyword=keyword))).all() -->不区分大小写
'''
from models import InterfaceResultModel # 引入模板类
from dbExat import db
import datetime

def insterOrUpdateData(modelName,systemName,testCaseNum,successCaseNum,failCaseNum,reportUrl):
    # 1.先查询  2.后删除
    data_result = InterfaceResultModel.query.filter(InterfaceResultModel.modelName == modelName).all()
    if len(data_result) <= 0:
        try:
            inster_result = InterfaceResultModel(modelName=modelName,systemName=systemName,testCaseNum=testCaseNum,successCaseNum=successCaseNum,
                                                failCaseNum=failCaseNum,reportUrl=reportUrl,updateTime=datetime.datetime.now())
            db.session.add(inster_result)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        try:
            InterfaceResultModel.query.filter(InterfaceResultModel.modelName == modelName).update(
                {"testCaseNum": testCaseNum, "successCaseNum": successCaseNum,
                 "failCaseNum": failCaseNum, "reportUrl": reportUrl,"updateTime":datetime.datetime.now()})
            db.session.commit()
        except Exception as e:
            db.session.rollback()