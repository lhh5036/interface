'''
@File: amazonSelectApi.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:我的数据-Amazon查询接口
'''

import requests
import json
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas

# 实例化日志类
logger = MyLog("MyDataAmazonSelectApi").getlog() # 初始化
# 数据管理-我的数据Amazon查询接口
class MyDataAmazonSelectApi():
    # 我的数据-Amazon查询
    def myDataAmazonSelect(self,kwargs): # 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("queryAmazonRankListing ---->start!")
        # 接口地址
        url = DasApiUrl.amazon_queryListing_url
        # 请求入参
        country = parseRequestDatas("country",kwargs) # 国家
        if country == "":
            logger.error("queryAmazonRankListing --> ReqParam:country is null!")
            return "请求参数:country字段不能为空"
        # 最内层参数
        amazonProductInfoSelect = DasApiInputParam.amazon_ProductInfo03
        keyList =[]
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                amazonProductInfoSelect[keyList[i]] = value
        # 替换中间层
        amazon_ProductInfo02 = DasApiInputParam.amazon_ProductInfo02
        amazon_ProductInfo02["search"] = amazonProductInfoSelect

        # 替换外层
        amazonProductInfoParam = DasApiInputParam.amazon_ProductInfo01
        amazonProductInfoParam["args"] = json.dumps(amazon_ProductInfo02)

        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = amazonProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("queryAmazonRankListing ---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("queryAmazonRankListing -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazonProductInfoParam)

