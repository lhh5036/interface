'''
@File: operateTaskApi.py
@time:2021/9/11
@Author:quanliu
@Desc:任务中心-分类监控页面/关键词监控页面-关注/删除/取消关注接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam

from apps.logger import MyLog
import json
import requests


# 实例化日志类
logger = MyLog("OperateTaskApi").getlog() # 初始化
class OperateTaskApi():
    def operateTaskFunction(self,operateType,ids):
        logger.info("operateTaskFunction------------------->start")
        if len(ids) == 0 or operateType == "":
            logger.error("operateTaskFunction------------>Input Param is wrong")
            return "请求参数为空"
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
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
        self.url = url # 请求地址
        self.header = header
        self.fromData = categoryTask_param01
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("operateTaskFunction------------------->end")
            return "接口响应成功"
        else:
            logger.error("operateTaskFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,categoryTask_param01)