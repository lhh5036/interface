'''
@File: productGetTongkuanInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:产品同款接口服务
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl

from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("ProductGetTongkuanInterface").getlog() # 初始化

# 数据管理-同款接口服务
class ProductGetTongkuanInterface():
    def productGetTongkuan(self,casename,paramStr):
        logger.info("productGetTongkuan ---->start!")
        if paramStr == "" or casename == "":
            logger.error("productGetTongkuan --> ReqParam:paramStr and casename is null!")
            return "请求入参不能为空!"

        # 接口请求地址
        url = MyDataManageInterUrl.productGenTongkuan_url

        # 拼接接口请求入参
        paramSelect = MyDataManageInterParam.productGenTongkuan_select
        replaceRepSelect = paramSelect.replace("{asinUrlStr}", paramStr)  # 替换接口里面的参数
        reqParam = MyDataManageInterParam.productGenTongkuan_param
        reqParam["args"] = replaceRepSelect  # 替换最外层参数

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")

        self.header = header
        self.formData = reqParam
        self.url = url

        respResult = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if respResult.json()["success"] == True:
            return "{0}-->success".format(casename)
        else:
            logger.error("productGetTongkuan -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename, url, json.dumps(self.formData))

        logger.info("productGetTongkuan ---->end!")
