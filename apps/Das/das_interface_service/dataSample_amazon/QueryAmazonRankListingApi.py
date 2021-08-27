'''
@File: QueryAmazonRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-Amazon查询页面
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import MyDataManageInterParam
from apps.Das.das_interface_service.dasSystem_interface_url import MyDataManageInterUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("AmazonRankListingQueryApi").getlog() # 初始化
class AmazonRankListingQueryApi():
    def amazonRankListingFunction(self,kwargs):
        logger.info("amazonRankListingFunction ---->start!")
        # 拼接接口最内层入参
        amazon_dataSampleListing03 = MyDataManageInterParam.amazon_dataSampleListing03
        # 校验入参必填项
        baseListingType = parseRequestDatas("baseListingType",kwargs)
        menuCode = parseRequestDatas("menuCode",kwargs)
        if baseListingType=="" or menuCode=="":
            logger.error("amazonRankListingFunction--->InputParam:baseListingType、menuCode is null")
            return "请求参数baseListingType,menuCode为空!"
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                amazon_dataSampleListing03[keyList[i]] = value
        # 替换中间层
        amazon_dataSampleListing02 = MyDataManageInterParam.amazon_dataSampleListing02
        amazon_dataSampleListing02["search"] = amazon_dataSampleListing03
        # 替换外层
        amazon_dataSampleListing03 = MyDataManageInterParam.amazon_dataSampleListing03
        amazon_dataSampleListing03["args"] = json.dumps(amazon_dataSampleListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        # 请求地址
        url = MyDataManageInterUrl.amazon_dataSampleListing_url
        self.url = url
        self.formData = amazon_dataSampleListing03
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("amazonRankListingFunction---->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("amazonRankListingFunction--->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazon_dataSampleListing03)

