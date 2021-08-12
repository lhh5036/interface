'''
@File: releaseProductInterface.py
@time:2021/8/7
@Author:quanliu 181324
@Desc:我的数据Amazon-释放产品接口
'''
from apps.Das.das_config.das_common_header import DasCommonHeader
from apps.Das.das_config.myData_manage.myDataAmazon_inter_body import MyDataAmazonInterParam
from apps.Das.das_config.myData_manage.myDataAmazon_inter_url import MyDataAmazonInterUrl
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("AmazonReleaseProductInfoInterface").getlog() # 初始化
# 我的数据Amazon-释放产品接口
class AmazonReleaseProductInfoInterface():
    def releaseProductInfo(self,paramStr): # 调用该接口使用入参为字符串类型,如果有多个可以用,拼接'"123","234"'
        logger.info("releaseProductInfo ---->start!")
        if paramStr == "" or len(paramStr) == 0:
            logger.error("releaseProductInfo --> request parameters is wrong!")

        # 接口地址
        url = MyDataAmazonInterUrl.releaseProductInfo_url

        # 拼接接口请求入参
        reqSelect = MyDataAmazonInterParam.releaseProductInfo_select
        reqSelectStr = reqSelect.replace("{ids}",paramStr) # 替换参数
        reqParam = MyDataAmazonInterParam.releaseProductInfo_param
        reqParam["args"] = reqSelectStr

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()

        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return resp.json()
        else:
            logger.error("releaseProductInfo -->response Data is wrong!")
        logger.info("releaseProductInfo ---->end!")

