'''
@File: crawlTaskApi.py
@time:2021/9/11
@Author:quanliu
@Desc:任务中心-分类监控页面/关键词监控页面-刷新任务接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("CrawlTaskApi").getlog() # 初始化
class CrawlTaskApi():
    def crawlTaskFunction(self,ids,saleChannelStr):
        logger.info("crawlTaskFunction------------------->start")
        if len(ids) == 0 or saleChannelStr == "":
            logger.error("crawlTaskFunction------------>Input Param is wrong")
            return "请求参数为空"
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        url = DasApiUrl.crawlTask_url # 请求地址

        # 获取请求参数
        crawlTask_param02 = DasApiInputParam.crawlTask_param02
        crawlTask_param02["ids"] = ids
        crawlTask_param02["saleChannel"] = saleChannelStr
        crawlTask_param01 = DasApiInputParam.crawlTask_param01
        crawlTask_param01["args"] = json.dumps(crawlTask_param02)
        self.url = url # 请求地址
        self.header = header
        self.fromData = crawlTask_param01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("crawlTaskFunction------------------->end")
            return "接口响应成功"
        else:
            logger.error("crawlTaskFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,crawlTask_param01)