'''
@File: associateSystemSkuInterface.py
@time:2021/8/20
@Author:quanliu 181324
@Desc:我的数据-Amazon关联系统SKU接口
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myData_manage.myDataAmazon_inter_body import MyDataAmazonInterParam
from apps.Das.das_interface_service.myData_manage.myDataAmazon_inter_url import MyDataAmazonInterUrl
from apps.Das.logger import MyLog
import requests
import json


# 实例化日志类
logger = MyLog("AmazonAssociateSystemSkuInterface").getlog() # 初始化

# 我的数据Amazon-关联系统SKU接口
class AmazonAssociateSystemSkuInterface():
    def associateSystemSku(self,paramList,systemSkuStr): # 调用该接口使用入参为list和字符串类型
        logger.info("associateSystemSku ---->start!")
        if len(paramList) == 0 or systemSkuStr == "":
            logger.error("associateSystemSku --> request parameters is wrong!")
            return "请求参数为空"
        # 接口地址
        url = MyDataAmazonInterUrl.associateSySku_url
        # 将入参list转为string类型
        paramStr = ""
        for i in range(len(paramList)):
            paramStr += "'"+paramList[i]+"',"

        # 拼接接口请求入参
        reqSelect = MyDataAmazonInterParam.associateSySku_select
        reqSelectStr = reqSelect.replace("{ids}",paramStr).replace("{systemSku}",systemSkuStr) # 替换接口入参
        reqParam = MyDataAmazonInterParam.associateSySku_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()

        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))

        if resp.json()["success"] == True:
            return "响应结果:success,接口入参:{0}".format(reqParam)
        else:
            logger.error("associateSystemSku -->response Data is wrong!")
            return "响应结果有误,接口地址:{0},接口入参:{1}".format(url, reqParam)


        logger.info("associateSystemSku ---->end!")

