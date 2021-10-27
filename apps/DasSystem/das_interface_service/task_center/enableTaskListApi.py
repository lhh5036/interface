'''
@File: enableTaskListApi.py
@time:2021/9/15
@Author:quanliu 181324
@Desc:任务中心-启用接口服务类
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.DasSystem.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.DasSystem.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.logger import MyLog
import json
import requests

# 实例化日志类
logger = MyLog("EnableTaskListApi").getlog() # 初始化
class EnableTaskListApi():
    def enableTaskListFunction(self,idsList):
        logger.info("enableTaskListFunction------------------->start")
        if len(idsList) == 0:
            logger.error("enableTaskListFunction------------>Input Param is wrong")
            return "请求参数为空"
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        url = DasApiUrl.enableTask_url # 请求地址

        # 获取请求参数
        unenableTask_param02 = DasApiInputParam.unenableTask_param02
        unenableTask_param02["ids"] = idsList
        unenableTask_param01 = DasApiInputParam.unenableTask_param01
        unenableTask_param01["args"] = json.dumps(unenableTask_param02)
        self.url = url  # 请求地址
        self.header = header
        self.fromData = unenableTask_param01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("enableTaskListFunction------------------->end")
            return "任务启用成功"
        else:
            logger.error("enableTaskListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"], url, unenableTask_param01)

if __name__ == '__main__':
    print(EnableTaskListApi().enableTaskListFunction(["21070911000231"]))