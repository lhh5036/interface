'''
@File: amazonSelectInterface.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:我的数据-Amazon查询接口
'''

import requests
import json
import logging
from apps.Das.das_config.das_common_header import DasCommonHeader
from apps.Das.das_config.myData_manage.myDataAmazon_inter_body import MyDataAmazonInterParam
from apps.Das.das_config.myData_manage.myDataAmazon_inter_url import MyDataAmazonInterUrl

# 数据管理-我的数据Amazon查询接口
class MyDataAmazonSelectInterface():
    # 我的数据-Amazon查询
    def myDataAmazonSelect(self,**kwargs): # 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        if kwargs == "" :
            logging.error("queryAmazonRankListing -->Into the parameter is wrong!")
        # 接口地址
        url = MyDataAmazonInterUrl.queryAmazonRankListing_url
        # 请求入参
        country = parseRequestDatas("country",kwargs) # 国家
        departmentName = parseRequestDatas("departmentName",kwargs)
        brand = parseRequestDatas("brand",kwargs)
        keywords = parseRequestDatas("keywords",kwargs) # 关键词
        asin = parseRequestDatas("asin",kwargs) # 产品asin
        mainSku = parseRequestDatas("mainSku",kwargs) # 主SKU
        associatedSystemSku = parseRequestDatas("associatedSystemSku",kwargs) # 关联系统SKU
        skuMapStr = parseRequestDatas("skuMapStr",kwargs) # 试卖SKU
        startPrice = parseRequestDatas("startPrice",kwargs)
        endPrice = parseRequestDatas("endPrice",kwargs)
        dataStatus = parseRequestDatas("dataStatus",kwargs)
        sellerName = parseRequestDatas("sellerName",kwargs)
        fba = parseRequestDatas("fba",kwargs)
        isBrand = parseRequestDatas("isBrand",kwargs)
        startFirstListOnTime = parseRequestDatas("startFirstListOnTime",kwargs)
        endFirstListOnTime = parseRequestDatas("endFirstListOnTime",kwargs)

        # 获取请求参数的基本格式
        repSelect = MyDataAmazonInterParam.accountProductInfo_select
        # 替换字符串里面的参数
        replaceRepSelect = repSelect.replace("{country}",country).replace("{departmentName}",departmentName).replace("{brand}",brand).replace("{keywords}",keywords).replace("{asin}",asin).\
            replace("{mainSku}",mainSku).replace("{associatedSystemSku}",associatedSystemSku).replace("{skuMapStr}",skuMapStr).replace("{startPrice}",startPrice).\
            replace("{endPrice}",endPrice).replace("{dataStatus}",dataStatus).replace("{sellerName}",sellerName).replace("{fba}",fba).replace("{isBrand}",isBrand).\
            replace("{startFirstListOnTime}",startFirstListOnTime).replace("{endFirstListOnTime}",endFirstListOnTime)
        # 替换最外层参数
        reqParam = MyDataAmazonInterParam.accountProductInfo_param
        reqParam["args"] = replaceRepSelect # 确保最后一层是dict格式

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()
        self.url = url
        self.formData = reqParam
        self.header = header

        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True :
            return resp.json()
        else:
            logging.error("queryAmazonRankListing -->response Data is wrong!")

# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName
