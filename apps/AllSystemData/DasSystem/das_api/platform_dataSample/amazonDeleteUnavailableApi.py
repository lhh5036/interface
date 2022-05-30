'''
@File: amazonDeleteUnavailableApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-Amazon死贴数据删除接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog
import json

# 实例化日志类
logger = MyLog("AmazonDeleteUnavilableApi").getlog() # 初始化
class AmazonDeleteUnavilableApi():
    def amazonDeleteUnavilableFunction(self,platform,searchType,idsList):
        logger.info("amazonDeleteUnavilableFunction -------->start")
        if len(idsList) == 0 or searchType == "":
            logger.error("amazonDeleteUnavilableFunction----->Input Parameter is null")
            return "请求参数searchType或ids或分配人字段为空!"
        # 拼接请求参数
        amazon_deleteUnavailable02 = DasApiInputParam.amazon_deleteUnavailable02
        amazon_deleteUnavailable02["ids"] = idsList
        amazon_deleteUnavailable01 = DasApiInputParam.amazon_deleteUnavailable01
        amazon_deleteUnavailable01["args"] = json.dumps(amazon_deleteUnavailable02)
        # 获取接口请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        url = DasApiUrl.amazon_deleteUnavailable_url
        self.url = url # 接口地址
        self.header = header
        self.formData = amazon_deleteUnavailable01
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.status_code == 200:
            logger.info("amazonDeleteUnavilableFunction -------->end")
            return "死贴数据删除接口响应成功"
        else:
            logger.error("amazonDeleteUnavilableFunction------>response Data is wrong!")
            return "死贴数据删除接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,amazon_deleteUnavailable01)
