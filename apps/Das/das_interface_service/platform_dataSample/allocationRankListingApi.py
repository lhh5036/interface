'''
@File: allocationRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集--分配接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("AllocationRankLinstingApi").getlog() # 初始化
class AllocationRankLinstingApi():
    def allocationRankListingFunction(self,url,idsList,claimantStr):
        logger.info("allocationRankListingFunction -------->start")
        if len(idsList) == 0 or url == "" or claimantStr == "":
            logger.error("allocationRankListingFunction----->Input Parameter is null")
            return "请求参数url或ids或分配人字段为空!"
        # 拼接请求参数
        allocationProduct02 = DasApiInputParam.allocationProduct02
        allocationProduct02["ids"] = idsList
        allocationProduct02["claimant"] = claimantStr
        allocationProduct01 = DasApiInputParam.allocationProduct01
        allocationProduct01["args"] = json.dumps(allocationProduct02)
        # 获取接口请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url # 接口地址
        self.header = header
        self.formData = allocationProduct01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.status_code == 200:
            logger.info("allocationRankListingFunction -------->end")
            return "分配接口响应成功"
        else:
            logger.error("allocationRankListingFunction------>response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,allocationProduct01)
