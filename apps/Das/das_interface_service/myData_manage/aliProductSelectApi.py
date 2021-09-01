'''
@File: aliProductSelectApi.py
@time:2021/8/24
@Author:quanliu
@Desc:我的数据-查询接口服务类（amazon/smt/1688/ebay/shopee共用）
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.das_interface_service.publicCommonService import PublicCommonServiceClass

from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("DataManageProductListingApi").getlog() # 初始化
class DataManageProductListingApi():
    def dataManageProductListingInfo(self,platform,searchType,kwargs):
        logger.info("dataManageProductListingInfo ---->start!")
        # 接口地址
        url = PublicCommonServiceClass().getApiUrl(platform,searchType) # 获取请求地址
        # 拼接接口入参
        productInfoSelect03,productInfoSelect02,productInfoSelect01 = PublicCommonServiceClass().getApiInputParam(platform,searchType)
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                productInfoSelect03[keyList[i]] = value
        # 替换中间层
        productInfoSelect02["search"] = productInfoSelect03
        # 替换外层
        productInfoSelect01["args"] = json.dumps(productInfoSelect02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.formData = productInfoSelect01
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("dataManageProductListingInfo---->end!")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("dataManageProductListingInfo -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,productInfoSelect01)


