'''
@File: checkAccountProductByRankApi.py
@time:2021/8/26
@Author:quanliu
@Desc:校验哪些产品已经被认领过接口类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json


# 校验哪些产品已经被认领过接口类
class CheckAccountProductByRankApi():
    def checkProductByRankFunction(self,platform,searchType,salechannelname,idsList):
        app.logger.info("checkProductByRankFunction------>start")
        if salechannelname == "" or len(idsList) == 0:
            app.logger.error("checkProductByRankFunction --> request parameters is wrong!")
            return "请求参数为空"

        # 拼接内层参数
        checkAccountProductByRank02 = DasApiInputParam.checkAccountProductByRank02
        checkAccountProductByRank02["saleChannel"] = salechannelname
        checkAccountProductByRank02["baseIdList"] = idsList
        # 拼接外层参数
        checkAccountProductByRank01 = DasApiInputParam.checkAccountProductByRank01
        checkAccountProductByRank01["args"] = json.dumps(checkAccountProductByRank02)
        # 获取请求头
        header = Common_TokenHeader().token_header("new","181324")
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType)
        # 拼接请求地址
        self.url = url
        self.fromData = checkAccountProductByRank01
        self.header = header
        responseResult = get_page_content_by_requests(self.url,self.header,self.fromData)
        if responseResult.json()["success"] == True:
            app.logger.info("checkProductByRankFunction------>end")
            return "接口响应成功,响应结果:{0}".format(responseResult.json()["result"])
        else:
            app.logger.error("checkProductByRankFunction -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(responseResult.json()["errorMsg"],url,checkAccountProductByRank01)



