'''
@File: cancelDevelopmentApi.py
@time:2021/8/23
@Author:quanliu
@Desc:取消开发接口服务
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("CancelDevelopmentApi").getlog() # 初始化
# 我的数据-取消开发接口服务类
class CancelDevelopmentApi():
    def cancelDevelopmentFunction(self,platform,searchType,paramList,cancelNotesInfoStr):
        logger.info("cancelDevelopmentFunction ---->start!")
        if len(paramList) == 0 or cancelNotesInfoStr == "" or searchType == "" or platform == "":
            logger.error("cancelDevelopmentFunction --> request parameters is wrong!")
            return "请求参数为空"
        # 将入参list转为string类型
        paramStr = ""
        for i in range(len(paramList)):
            paramStr += "'" + paramList[i] + "',"
        # 拼接接口请求入参
        reqSelect = DasApiInputParam.cancelDevelop_select
        reqSelectStr = reqSelect.replace("{ids}", paramStr).replace("{cancelNotesInfo}", cancelNotesInfoStr)  # 替换接口入参
        reqParam = DasApiInputParam.cancelDevelop_param
        reqParam["args"] = reqSelectStr
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("cancelDevelopmentFunction ---->end!")
            return "取消开发---接口响应成功"
        else:
            logger.error("cancelDevelopmentFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, reqParam)

