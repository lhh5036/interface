'''
@File: cancelDevelopmentApi.py
@time:2021/8/23
@Author:quanliu
@Desc:取消开发接口服务
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app


# 我的数据-取消开发接口服务类
class CancelDevelopmentApi():
    def cancelDevelopmentFunction(self,platform,searchType,paramList,cancelNotesInfoStr):
        app.logger.info("cancelDevelopmentFunction ---->start!")
        if len(paramList) == 0 or cancelNotesInfoStr == "" or searchType == "" or platform == "":
            app.logger.error("cancelDevelopmentFunction --> request parameters is wrong!")
            return "请求参数为空"
        # 将入参list转为string类型
        paramStr = ""
        for i in range(len(paramList)):
            paramStr += "'" + paramList[i] + "',"
        # 拼接接口请求入参
        reqSelect = DasApiInputParam.cancelDevelop_select
        reqSelect["ids"] = paramList
        reqSelect["cancelNotesInfo"] = cancelNotesInfoStr
        reqParam = DasApiInputParam.cancelDevelop_param
        reqParam["args"] = str(reqSelect)
        # 接口请求头
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        # 组装接口所需要的参数
        self.url = url
        self.formData = reqParam
        self.header = header
        resp = get_page_content_by_requests(self.url, self.header, self.formData)
        if resp.json()["success"] == True:
            app.logger.info("cancelDevelopmentFunction ---->end!")
            return "取消开发---接口响应成功"
        else:
            app.logger.error("cancelDevelopmentFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, reqParam)

