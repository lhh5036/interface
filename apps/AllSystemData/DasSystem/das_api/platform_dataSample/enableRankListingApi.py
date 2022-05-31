'''
@File: enableRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-启用接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json

class EnableRankListingApi():
    def enableRankListingFunction(self,platform,searchType,paramList): # 请求参数为List
        app.logger.info("enableRankListingFunction--------->start")
        if len(paramList) == 0:
            app.logger.error("enableRankListingFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        enableProduct02 = DasApiInputParam.enableProduct02
        enableProduct02["ids"] = paramList
        enableProduct01 = DasApiInputParam.enableProduct01
        enableProduct01["args"] = json.dumps(enableProduct02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new", "181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        self.header = header
        self.formData = enableProduct01
        self.url = url
        resp = get_page_content_by_requests(self.url, self.header, self.formData)
        if resp.status_code == 200:
            app.logger.info("enableRankListingFunction-------->end")
            return "启用接口响应成功"
        else:
            app.logger.error("enableRankListingFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, enableProduct01)
