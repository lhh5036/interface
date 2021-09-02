'''
@File: queryCustomizeTaskListApi.py
@time:2021/9/2
@Author:quanliu
@Desc:任务中心-自定义采集日志查询接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl
from apps.Das.logger import MyLog
import json
import requests


# 实例化日志类
logger = MyLog("QueryCustomizeTaskListingApi").getlog() # 初始化
class QueryCustomizeTaskListingApi():
    def QueryCustomizeTaskListingFunction(self,idList):
        logger.info("customizeTaskRankListingFunction------------------->start")
        if len(idList) == 0:
            logger.error("customizeTaskRankListingFunction------>InputParam is null")
            return "请求参数为空!"
        # 获取请求地址
        url = DasApiUrl.queryCustomizeTask_url
        # 获取请求参数
        queryCustomizeTask02 = DasApiInputParam.queryCustomizeTask02
        queryCustomizeTask02["idList"] = idList
        queryCustomizeTask01 = DasApiInputParam.queryCustomizeTask01
        queryCustomizeTask01["args"] = json.dumps(queryCustomizeTask02)
        # 请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url
        self.formData = queryCustomizeTask01
        self.header = header
        resp = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
        if resp.json()["success"] == True:
            logger.info("customizeTaskRankListingFunction------------------->end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["result"])
        else:
            logger.error("customizeTaskRankListingFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,queryCustomizeTask01)

if __name__ == '__main__':
    print(QueryCustomizeTaskListingApi().QueryCustomizeTaskListingFunction(["31292385-0b53-4a1f-bd37-60773ded0c29"]))