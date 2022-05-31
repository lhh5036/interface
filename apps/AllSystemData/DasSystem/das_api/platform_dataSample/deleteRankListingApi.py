'''
@File: deleteRankListingApi.py
@time:2021/8/27
@Author:quanliu
@Desc:数据采集-删除接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json

class DeleteRankListingApi():
    def deleteRankListingFunction(self,platform,searchType,paramList): # 请求参数为List
        app.logger.info("deleteRankListingFunction--------->start")
        if len(paramList) == 0:
            app.logger.error("deleteRankListingFunction----->InputParameter is null")
            return "请求参数为空!"
        # 对入参进行参数化
        deleteProduct02 = DasApiInputParam.deleteProduct02
        deleteProduct02["ids"] = paramList
        deleteProduct01 = DasApiInputParam.deleteProduct01
        deleteProduct01["args"] = json.dumps(deleteProduct02)
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        self.header = header
        self.formData = deleteProduct01
        self.url = url
        resp = get_page_content_by_requests(self.url,self.header,self.formData)
        if resp.status_code == 200:
            app.logger.info("deleteRankListingFunction-------->end")
            return "禁用接口响应成功"
        else:
            app.logger.error("deleteRankListingFunction--------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,deleteProduct01)

