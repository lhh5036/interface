'''
@File: enableAmazonRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-启用接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AmazonEnableRankListingApi").getlog() # 初始化
class AmazonEnableRankListingApi():
    def enableRankListingFunction(self,url,paramList): # 请求参数为List
        logger.info("enableRankListingFunction--------->start")
        if len(paramList) == 0:
            logger.error("enableRankListingFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        enableProduct02 = DasApiInputParam.enableProduct02
        enableProduct02["ids"] = paramList
        enableProduct01 = DasApiInputParam.enableProduct01
        enableProduct01["args"] = json.dumps(enableProduct02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        self.header = header
        self.formData = enableProduct01
        self.url = url
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("enableRankListingFunction-------->end")
            return "启用接口响应成功"
        else:
            logger.error("enableRankListingFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, enableProduct01)
