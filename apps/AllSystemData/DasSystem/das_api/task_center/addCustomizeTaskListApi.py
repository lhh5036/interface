'''
@File: addCustomizeTaskListApi.py
@time:2021/9/2
@Author:quanliu
@Desc:任务中心-自定义采集-新增采集接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json


@api_assemble_new()
def addCustomizeTaskListingFunction(itemUrlList,saleChannel,country):
    app.logger.info("addCustomizeTaskListingFunction------------------->start")
    if len(itemUrlList) == 0 or saleChannel == "" or country == "":
        app.logger.error("addCustomizeTaskListingFunction------>InputParam is null")
        return "请求参数为空!"
    # 获取请求地址
    url = DasApiUrl.addCustomizeTask_url
    # 获取请求参数
    addCustomizeTask02 = DasApiInputParam.addCustomizeTask02
    addCustomizeTask02["itemUrlList"] = itemUrlList
    addCustomizeTask02["saleChannel"] = saleChannel
    addCustomizeTask02["country"] = country
    addCustomizeTask01 = DasApiInputParam.addCustomizeTask01
    addCustomizeTask01["args"] = json.dumps(addCustomizeTask02)
    return url,addCustomizeTask01


if __name__ == '__main__':
    print(addCustomizeTaskListingFunction(["https://www.aliexpress.com/item/1005002065663912.html?spm=a2g0o.store_pc_groupList.8148356.3.17136ae1hUFRSF"],"SMT","US"))
