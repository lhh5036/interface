'''
@File: productGetDijiaApi.py
@time:2021/8/23
@Author:quanliu
@Desc:低价接口服务
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app


# 数据管理-低价接口
@api_assemble_new()
def productDetDiJia(paramStr): # 请求入参为用例名称，string类型的参数
    app.logger.info("productGenDijia ---->start!")
    if paramStr == "":
        app.logger.error("productGenDijia --> ReqParam:paramStr is null!")
        return "请求入参不能为空!"
    # 接口请求地址
    url = DasApiUrl.productGenDijia_url
    # 拼接接口请求入参
    paramSelect = DasApiInputParam.productGenDijia_select
    paramSelect["asinUrlStr"] = paramStr
    reqParam = DasApiInputParam.productGenDijia_param
    reqParam["args"] = str(paramSelect) # 替换最外层参数
    return url,reqParam
    # self.header = header
    # self.formData = reqParam
    # self.url = url
    # respResult = get_page_content_by_requests(self.url, self.header,self.formData)
    # if respResult.json()["success"] == True:
    #     app.logger.info("productGenDijia ---->end!")
    #     return "接口响应成功,响应结果:{0}".format(respResult.json()["result"])
    # else:
    #     app.logger.error("productGenDijia -->response Data is wrong!")
    #     return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(respResult.json()["errorMsg"], url,reqParam)
