'''
@File: queryAmazonCategoryListingApi.py
@time:2021/8/31
@Author:quanliu
@Desc:数据采集-Amazon关注分类数据查询页面接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("AmazonCategoryListingQueryApi").getlog() # 初始化
class AmazonCategoryListingQueryApi():
    def amazonCategoryListingFunction(self,kwargs):
        logger.info("amazonCategoryListingFunction------------------->start")
        # 校验必填项字段
        country = parseRequestDatas("country",kwargs)
        if country == "":
            logger.error("amazonCategoryListingFunction-------------->InputParam:country is null")
            return "请求入参country为空"
        # 获取最内层参数
        amazon_categoryListing03 = DasApiInputParam.amazon_categoryListing03
        keyList = []
        for key in kwargs.keys():
            keyList.append(key)
        for i in range(len(keyList)):
            value = parseRequestDatas(keyList[i],kwargs)
            amazon_categoryListing03[keyList[i]] = value
        # 替换中间层
        amazon_categoryListing02 = DasApiInputParam.amazon_categoryListing02
        amazon_categoryListing02["search"] = amazon_categoryListing03
        # 替换最外层
        amazon_categoryListing01 = DasApiInputParam.amazon_categoryListing01
        amazon_categoryListing01["args"] = json.dumps(amazon_categoryListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        # 请求地址
        url = DasApiUrl.amazon_attentStoreListing_url
        self.url = url
        self.header = header
        self.fromData = amazon_categoryListing01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("amazonAttentStoreListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("amazonAttentStoreListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazon_categoryListing01)