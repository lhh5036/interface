'''
@File: amazonSelectInterface.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:我的数据-Amazon查询接口
'''

import requests
import json
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl
from apps.Das.logger import MyLog

# 实例化日志类
logger = MyLog("MyDataAmazonSelectInterface").getlog() # 初始化
# 数据管理-我的数据Amazon查询接口
class MyDataAmazonSelectInterface():
    # 我的数据-Amazon查询
    def myDataAmazonSelect(self,casename,kwargs): # 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("queryAmazonRankListing ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.amazon_queryListing_url
        # 请求入参
        country = parseRequestDatas("country",kwargs) # 国家
        if country == "":
            logger.error("queryAmazonRankListing --> ReqParam:country is null!")
            return "请求参数:country字段不能为空"
        # 最内层参数
        amazonProductInfoSelect = MyDataManageInterParam.amazon_ProductInfo03
        keyList =[]
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)

        if len(keyList) != 0:
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                amazonProductInfoSelect[keyList[i]] = value
        # 替换中间层
        amazon_ProductInfo02 = MyDataManageInterParam.amazon_ProductInfo02
        amazon_ProductInfo02["search"] = amazonProductInfoSelect

        # 替换外层
        amazonProductInfoParam = MyDataManageInterParam.amazon_ProductInfo01
        amazonProductInfoParam["args"] = json.dumps(amazon_ProductInfo02)

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader("new","181324")
        self.url = url
        self.formData = amazonProductInfoParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            return "{0}-->success".format(casename)
        else:
            logger.error("queryAmazonRankListing -->response Data is wrong!")
            return "{0}-->响应结果有误,接口地址:{1},接口入参:{2}".format(casename,url, kwargs)

        logger.info("queryAmazonRankListing ---->end!")
# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

if __name__ == '__main__':
    print(MyDataAmazonSelectInterface().myDataAmazonSelect("第一个用例",{"country":"US","asin":"B07SW7PVWW"}))