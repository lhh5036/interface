'''
@File: productGetDijiaInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:低价接口服务
'''
import requests
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myData_manage.myDataAmazon_inter_body import MyDataAmazonInterParam
from apps.Das.das_interface_service.myData_manage.myDataAmazon_inter_url import MyDataAmazonInterUrl
from apps.Das.logger import MyLog
import json

# 实例化日志类
logger = MyLog("ProductGetDijiaInterface").getlog() # 初始化

# 数据管理-低价接口
class ProductGetDijiaInterface():
    def productDetDiJia(self,casename,paramStr): # 请求入参为用例名称，string类型的参数
        logger.info("productGenDijia ---->start!")
        if paramStr == "" or casename == "":
            logger.error("productGenDijia --> ReqParam:paramStr and casename is null!")
            return "请求入参不能为空!"

        # 接口请求地址
        url = MyDataAmazonInterUrl.productGenDijia_url

        # 拼接接口请求入参
        paramSelect = MyDataAmazonInterParam.productGenDijia_select
        replaceRepSelect = paramSelect.replace("{asinUrlStr}",paramStr) #替换接口里面的参数
        reqParam = MyDataAmazonInterParam.productGenDijia_param
        reqParam["args"] = replaceRepSelect # 替换最外层参数

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()

        self.header = header
        self.formData = reqParam
        self.url = url

        respResult = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if respResult.json()["success"] == True:
            return "{0}-->success".format(casename)
        else:
            logger.error("productGenDijia -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, json.dumps(self.formData))

        logger.info("productGenDijia ---->end!")


