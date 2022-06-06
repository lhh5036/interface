'''
@File: crawlTaskApi.py
@time:2021/9/11
@Author:quanliu
@Desc:任务中心-分类监控页面/关键词监控页面-刷新任务接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def crawlTaskFunction(ids,saleChannelStr):
    app.logger.info("crawlTaskFunction------------------->start")
    if len(ids) == 0 or saleChannelStr == "":
        app.logger.error("crawlTaskFunction------------>Input Param is wrong")
        return "请求参数为空"
    url = DasApiUrl.crawlTask_url # 请求地址

    # 获取请求参数
    crawlTask_param02 = DasApiInputParam.crawlTask_param02
    crawlTask_param02["ids"] = ids
    crawlTask_param02["saleChannel"] = saleChannelStr
    crawlTask_param01 = DasApiInputParam.crawlTask_param01
    crawlTask_param01["args"] = json.dumps(crawlTask_param02)
    return url,crawlTask_param01