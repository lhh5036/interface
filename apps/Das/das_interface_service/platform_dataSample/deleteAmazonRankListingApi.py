'''
@File: deleteAmazonRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-删除接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.publicCommonService import PublicCommonServiceClass
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("AmazonDeleteRankListingApi").getlog() # 初始化
class AmazonDeleteRankListingApi():
    def deleteRankListingFunction(self,platform,searchType,paramList): # 请求参数为List
        logger.info("deleteRankListingFunction--------->start")
        if len(paramList) == 0:
            logger.error("deleteRankListingFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        deleteProduct02 = DasApiInputParam.deleteProduct02
        deleteProduct02["ids"] = paramList
        deleteProduct01 = DasApiInputParam.deleteProduct01
        deleteProduct01["args"] = json.dumps(deleteProduct02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonServiceClass().getApiUrl(platform,searchType)
        self.header = header
        self.formData = deleteProduct01
        self.url = url
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("deleteRankListingFunction-------->end")
            return "禁用接口响应成功"
        else:
            logger.error("deleteRankListingFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,deleteProduct01)

