'''
@File: unenableTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-禁用接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json

class UnenableTaskListApi():
    def unenableTaskListFunction(self,idsList):
        app.logger.info("unenableTaskListFunction------------------->start")
        if len(idsList) == 0:
            app.logger.error("unenableTaskListFunction------------>Input Param is wrong")
            return "请求参数为空"
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        url = DasApiUrl.unenableTask_url # 请求地址

        # 获取请求参数
        unenableTask_param02 = DasApiInputParam.unenableTask_param02
        unenableTask_param02["ids"] = idsList
        unenableTask_param01 = DasApiInputParam.unenableTask_param01
        unenableTask_param01["args"] = json.dumps(unenableTask_param02)
        self.url = url  # 请求地址
        self.header = header
        self.fromData = unenableTask_param01
        resp = get_page_content_by_requests(self.url, self.header, self.fromData)
        if resp.json()["success"] == True:
            app.logger.info("unenableTaskListFunction------------------->end")
            return "任务禁用成功"
        else:
            app.logger.error("unenableTaskListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, unenableTask_param01)

if __name__ == '__main__':
    print(UnenableTaskListApi().unenableTaskListFunction(["21070911000231"]))
