'''
@File: claimAmazonRankListingApi.py
@time:2021/8/26
@Author:quanliu
@Desc:数据采集-认领产品接口类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AmazonClaimRankLinstingApi").getlog() # 初始化
class AmazonClaimRankLinstingApi():
    def claimAmazonRankListingFun(self,url,paramList):
        logger.info("claimAmazonRankListingFun -------->start")
        if len(paramList) == 0:
            logger.error("claimAmazonRankListingFun----->Input Parameter is null")
            return "请求参数为空"
        # 参数化接口入参
        claimProduct02 = DasApiInputParam.claimProduct02
        claimProduct02["ids"] = paramList
        claimProduct01 = DasApiInputParam.claimProduct01
        claimProduct01["args"] = json.dumps(claimProduct02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.header = header
        self.formData = claimProduct01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("claimAmazonRankListingFun -------->end")
            return "认领产品接口调用成功"
        else:
            logger.error("claimAmazonRankListingFun -->response Data is wrong!")
            return "接口调用失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,claimProduct01)



