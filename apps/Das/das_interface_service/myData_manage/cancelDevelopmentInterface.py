'''
@File: cancelDevelopmentInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:取消开发接口服务
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("CancelDevelopmentInterface").getlog() # 初始化
# 我的数据-取消开发接口服务类
class CancelDevelopmentInterface():
    def cancelDevelopmentFunction(self,casename,url,paramList,cancelNotesInfoStr):
        logger.info("cancelDevelopmentFunction ---->start!")
        if len(paramList) == 0 or cancelNotesInfoStr == "" or url == "":
            logger.error("cancelDevelopmentFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 将入参list转为string类型
        paramStr = ""
        for i in range(len(paramList)):
            paramStr += "'" + paramList[i] + "',"

        # 拼接接口请求入参
        reqSelect = MyDataManageInterParam.cancelDevelop_select
        reqSelectStr = reqSelect.replace("{ids}", paramStr).replace("{cancelNotesInfo}", cancelNotesInfoStr)  # 替换接口入参
        reqParam = MyDataManageInterParam.cancelDevelop_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()

        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))

        if resp.json()["success"] == True:
            return "{0}-->success".format(casename)
        else:
            logger.error("cancelDevelopmentFunction -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, json.dumps(reqParam))

        logger.info("cancelDevelopmentFunction ---->end!")