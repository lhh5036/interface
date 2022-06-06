'''
@File: updateInterResult.py
@time:2022/6/6
@Author:
@Desc:
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