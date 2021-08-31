'''
@File: queryAmazonKeywordsListingApi.py
@time:2021/8/31
@Author:quanliu
@Desc:数据采集-Amazon关注关键词数据页面接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("AmazonKeywordsListingQueryApi").getlog() # 初始化
class AmazonKeywordsListingQueryApi():
    def amazonKeywordsListingFunction(self,kwargs):
        logger.info("amazonKeywordsListingFunction------------------->start")
        country = parseRequestDatas("country",kwargs)
        if country == "":
            logger.error("amazonKeywordsListingFunction--------->InputParam:country is null")
            return "请求参数country为空"
        # 获取最内层参数
        amazon_keywordsListing03 = DasApiInputParam.amazon_keywordsListing03
        keyList = []
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            amazon_keywordsListing03[keyList[i]] = value
        # 替换中间层
        amazon_keywordsListing02 = DasApiInputParam.amazon_keywordsListing02
        amazon_keywordsListing02["search"] = amazon_keywordsListing03
        # 替换最外层参数
        amazon_keywordsListing01 = DasApiInputParam.amazon_keywordsListing01
        amazon_keywordsListing01["args"] = json.dumps(amazon_keywordsListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        # 请求地址
        url = DasApiUrl.amazon_attentStoreListing_url
        self.url = url
        self.header = header
        self.fromData = amazon_keywordsListing01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("amazonAttentStoreListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("amazonAttentStoreListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, amazon_keywordsListing01)