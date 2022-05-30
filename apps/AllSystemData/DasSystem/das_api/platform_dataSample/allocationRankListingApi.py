'''
@File: allocationRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集--分配接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog
import json


# 实例化日志类
logger = MyLog("AllocationRankLinstingApi").getlog() # 初始化
class AllocationRankLinstingApi():
    def allocationRankListingFunction(self,platform,searchType,idsList,claimantStr):
        logger.info("allocationRankListingFunction -------->start")
        if len(idsList) == 0 or searchType == "" or claimantStr == "":
            logger.error("allocationRankListingFunction----->Input Parameter is null")
            return "请求参数searchType或ids或分配人字段为空!"
        # 拼接请求参数
        allocationProduct02 = DasApiInputParam.allocationProduct02
        allocationProduct02["ids"] = idsList
        allocationProduct02["claimant"] = claimantStr
        allocationProduct01 = DasApiInputParam.allocationProduct01
        allocationProduct01["args"] = json.dumps(allocationProduct02)
        # 获取接口请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 请求地址
        self.url = url # 接口地址
        self.header = header
        self.formData = allocationProduct01
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.status_code == 200:
            logger.info("allocationRankListingFunction -------->end")
            return "分配接口响应成功"
        else:
            logger.error("allocationRankListingFunction------>response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,allocationProduct01)
