'''
@File: queryCustomizeTaskListApi.py
@time:2021/9/2
@Author:quanliu
@Desc:任务中心-自定义采集日志查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def queryCustomizeTaskListingFunction(idList):
    app.logger.info("queryCustomizeTaskListingFunction------------------->start")
    if len(idList) == 0:
        app.logger.error("queryCustomizeTaskListingFunction------>InputParam is null")
        return "请求参数为空!"
    # 获取请求地址
    url = DasApiUrl.queryCustomizeTask_url
    # 获取请求参数
    queryCustomizeTask02 = DasApiInputParam.queryCustomizeTask02
    queryCustomizeTask02["idList"] = idList
    queryCustomizeTask01 = DasApiInputParam.queryCustomizeTask01
    queryCustomizeTask01["args"] = json.dumps(queryCustomizeTask02)
    return url,queryCustomizeTask01

if __name__ == '__main__':
    print(queryCustomizeTaskListingFunction(["31292385-0b53-4a1f-bd37-60773ded0c29"]))
