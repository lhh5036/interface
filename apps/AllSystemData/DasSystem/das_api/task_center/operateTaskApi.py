'''
@File: operateTaskApi.py
@time:2021/9/11
@Author:quanliu
@Desc:任务中心-分类监控页面/关键词监控页面-关注/删除/取消关注接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def operateTaskFunction(operateType,ids):
    app.logger.info("operateTaskFunction------------------->start")
    if len(ids) == 0 or operateType == "":
        app.logger.error("operateTaskFunction------------>Input Param is wrong")
        return "请求参数为空"
    if operateType == "attentionTask":
        url = DasApiUrl.attentionTask_url # 请求地址
    elif operateType == "deleteTask":
        url = DasApiUrl.deleteTask_url
    elif operateType == "cancelAttentionTask":
        url = DasApiUrl.cancelAttentionTask_url
    # 获取请求参数
    categoryTask_param02 = DasApiInputParam.categoryTask_param02
    categoryTask_param02["ids"] = ids
    categoryTask_param01 = DasApiInputParam.categoryTask_param01
    categoryTask_param01["args"] = json.dumps(categoryTask_param02)
    return url,categoryTask_param01