'''
@File: queryCategoryListApi.py
@time:2021/9/11
@Author:quanliu
@Desc:分类监控页面-查询各个平台的分类信息
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonJudgeEmptySevice import PublicCommonJudgeEmptySevice
from apps.AllSystemData.DasSystem.das_api.publicCommonParamService import PublicCommonParamServiceClass
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.get_page_content_by_requests import get_page_content_by_requests
from logger import MyLog
import json



# 实例化日志类
logger = MyLog("QueryCategoryListApi").getlog() # 初始化
class QueryCategoryListApi():
    def queryCategoryListFunction(self,platform,searchType,kwargs):# 字典格式
        logger.info("queryCategoryListFunction------------------->start")
        # 是否校验入参
        needJudge = PublicCommonJudgeEmptySevice().needJudgeEmpty(platform, searchType, kwargs)
        if needJudge == True:
            logger.error("queryCategoryListFunction-------->InputParam is null")
            return "请求参数为空!"
        # 获取请求参数
        categoryListing03, categoryListing02, categoryListing01 = PublicCommonParamServiceClass().getApiInputParam(platform, searchType)
        url = PublicCommonUrlServiceClass().getApiUrl(platform, searchType)  # 获取请求地址
        keyList = []
        if kwargs != "":
            for key in kwargs.keys():
                keyList.append(key)
            for i in range(len(keyList)):
                value = parseRequestDatas(keyList[i], kwargs)
                categoryListing02[keyList[i]] = value
        # 替换最外层
        categoryListing01["args"] = json.dumps(categoryListing02)
        # 接口请求头
        header = Common_TokenHeader().token_header("new", "181324")
        self.url = url  # 请求地址
        self.header = header
        self.fromData = categoryListing01
        resp = get_page_content_by_requests(self.url, self.header, self.fromData)
        if resp.json()["success"] == True:
            logger.info("queryCategoryListFunction------------------->end")
            return "接口响应成功,响应结果:{0}".format(resp.json()["result"])
        else:
            logger.error("queryCategoryListFunction------------->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},接口类型:{2},请求参数:{3}".format(resp.json()["errorMsg"], url, searchType,categoryListing01)

if __name__ == '__main__':
    print(QueryCategoryListApi().queryCategoryListFunction("SMT","smt_listCategoryMonitor",{}))
