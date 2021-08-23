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
logger = MyLog("AmazonReleaseProductInfoInterface").getlog() # 初始化
# 数据管理-我的数据Amazon查询接口
class MyDataAmazonSelectInterface():
    # 我的数据-Amazon查询
    def myDataAmazonSelect(self,casename,kwargs): # 设置动态入参，参数类型为字典{"name":"Jack","age":18}
        logger.info("queryAmazonRankListing ---->start!")
        # 接口地址
        url = MyDataManageInterUrl.queryAmazonRankListing_url
        # 请求入参
        country = parseRequestDatas("country",kwargs) # 国家
        if country == "":
            logger.error("queryAmazonRankListing --> ReqParam:country is null!")
            return "请求参数:country字段不能为空"
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
        repSelect = MyDataManageInterParam.accountProductInfo_select
        # 替换字符串里面的参数
        replaceRepSelect = repSelect.replace("{country}",country).replace("{departmentName}",departmentName).replace("{brand}",brand).replace("{keywords}",keywords).replace("{asin}",asin).\
            replace("{mainSku}",mainSku).replace("{associatedSystemSku}",associatedSystemSku).replace("{skuMapStr}",skuMapStr).replace("{startPrice}",startPrice).\
            replace("{endPrice}",endPrice).replace("{dataStatus}",dataStatus).replace("{sellerName}",sellerName).replace("{fba}",fba).replace("{isBrand}",isBrand).\
            replace("{startFirstListOnTime}",startFirstListOnTime).replace("{endFirstListOnTime}",endFirstListOnTime)
        # 替换最外层参数
        reqParam = MyDataManageInterParam.accountProductInfo_param
        reqParam["args"] = replaceRepSelect # 确保最后一层是dict格式

        # 接口请求头
        header = DasCommonHeader().getDasCommonHeader()
        self.url = url
        self.formData = reqParam
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

