'''
@File: queryAliRankListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-1688查询接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests
from apps.Das.das_interface_service.publicCommonService import PublicCommonServiceClass

# 实例化日志类
logger = MyLog("AliRankListingQueryApi").getlog() # 初始化
class AliRankListingQueryApi():
    def aliRankListingFunction(self,platform,searchType,kwargs):
        logger.info("aliRankListingFunction------------------->start")
        # 获取请求参数
        aliRankListing03,aliRankListing02,aliRankListing01 = PublicCommonServiceClass().getApiInputParam(platform,searchType)
        url = PublicCommonServiceClass().getApiUrl(platform,searchType) # 获取请求地址
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                aliRankListing03[keyList[i]] = value
        # 替换中间层
        aliRankListing02["search"] = aliRankListing03
        # 替换最外层参数
        aliRankListing01["args"] = json.dumps(aliRankListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url # 请求地址
        self.header = header
        self.fromData = aliRankListing01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("aliRankListingFunction------------------->end")
            return "接口调用成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("aliRankListingFunction------------->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,aliRankListing01)


