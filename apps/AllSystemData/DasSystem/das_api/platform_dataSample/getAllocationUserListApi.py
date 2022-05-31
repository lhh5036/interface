'''
@File: getAllocationUserListApi.py
@time:2021/9/1
@Author:quanliu
@Desc:数据采集-获取分配人员信息接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json


class GetAllocationUserListApi():
    def getAllocationUserListFunction(self,platform,searchType,jobNumber): # 请求参数为用户工号
        app.logger.info("getAllocationUserListFunction--------->start")
        if jobNumber == "":
            app.logger.error("getAllocationUserListFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        allocationPerson02 = DasApiInputParam.allocationPerson02
        allocationPerson02["jobNumber"] = jobNumber
        allocationPerson01 = DasApiInputParam.allocationPerson01
        allocationPerson01["args"] = json.dumps(allocationPerson02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        self.header = header
        self.formData = allocationPerson01
        self.url = url
        resp = get_page_content_by_requests(self.url,self.header, self.formData)
        if resp.json()["success"] == True:
            app.logger.info("getAllocationUserListFunction-------->end")
            return "接口响应成功,返回结果:{0}".format(resp.json()["result"])
        else:
            app.logger.error("getAllocationUserListFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, allocationPerson01)
