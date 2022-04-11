'''
@File: queryTaskCenterListingApi.py
@time:2021/9/1
@Author:quanliu
@Desc:任务中心-查询接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader

from apps.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
import json
import requests

# 实例化日志类
logger = MyLog("TaskCenterRankListingApi").getlog() # 初始化
class TaskCenterRankListingApi():
    def taskCenterRankListingFunction(self,platform,searchType,kwargs):
        logger.info("taskCenterRankListingFunction------------------->start")
        # 是否校验入参
        needJudge = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform,searchType,kwargs)
        if needJudge == True :
            logger.error("taskCenterRankListingFunction-------->InputParam is null")
            return "请求参数为空!"
        # 获取请求参数
        rankListing03,rankListing02,rankListing01 = PublicCommonParamServiceClass().getApiInputParam(platform,searchType)
        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 获取请求地址
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i],kwargs)
                rankListing03[keyList[i]] = value
        # 替换中间层
        rankListing02["search"] = rankListing03
        # 替换最外层参数
        rankListing01["args"] = json.dumps(rankListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url # 请求地址
        self.header = header
        self.fromData = rankListing01
        resp = requests.post(url=self.url, headers=self.header, data=json.dumps(self.fromData))
        if resp.json()["success"] == True:
            logger.info("taskCenterRankListingFunction------------------->end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["rows"])
        else:
            logger.error("taskCenterRankListingFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url,searchType,rankListing01)


if __name__ == '__main__':
    # Amazon/SMT/Alibaba1688/Shopee
    print(TaskCenterRankListingApi().taskCenterRankListingFunction("Amazon","amazon_customizeMarkListing",{"saleChannel":"Amazon","country":"US"}))