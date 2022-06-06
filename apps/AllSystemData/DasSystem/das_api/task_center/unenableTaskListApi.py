'''
@File: unenableTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-禁用接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
import json

@api_assemble_new()
def unenableTaskListFunction(idsList):
    app.logger.info("unenableTaskListFunction------------------->start")
    if len(idsList) == 0:
        app.logger.error("unenableTaskListFunction------------>Input Param is wrong")
        return "请求参数为空"
    url = DasApiUrl.unenableTask_url # 请求地址

    # 获取请求参数
    unenableTask_param02 = DasApiInputParam.unenableTask_param02
    unenableTask_param02["ids"] = idsList
    unenableTask_param01 = DasApiInputParam.unenableTask_param01
    unenableTask_param01["args"] = json.dumps(unenableTask_param02)
    return url,unenableTask_param01

if __name__ == '__main__':
    print(unenableTaskListFunction(["21070911000231"]))
