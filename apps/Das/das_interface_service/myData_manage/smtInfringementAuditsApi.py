'''
@File: smtInfringementAuditsApi.py
@time:2021/8/23
@Author:quanliu
@Desc:侵权审核接口服务类
'''
from apps.Common_Config.interface_common_info import Common_TokenHeader
import requests
import json

from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.logger import MyLog
from apps.Common_Config.parseRequestDatas import parseRequestDatas
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl


# 实例化日志类
logger = MyLog("InfringementAuditsApi").getlog() # 初始化
class InfringementAuditsApi():
    
    def infringementAuditFunction(self,url,idsList,auditStatus,salesProhibitionList,infringementInfoMap):
        # 入参地址:url,idsList--id集合  auditStatus--审核状态（通过，不通过）salesProhibitionList--禁售平台和站点list infringementInfoMap--禁售信息dict
        # salesProhibitionList 格式[{"plat":"Amazon","sites":"US,UK,IT"},{"plat":"Ebay","sites":"US,UK,AU"}]
        # infringementInfoMap 格式 {"infringementTypeName":"cjz测试的禁售类型","infringementObj":"cjz测试的禁售原因","auditNotesInfo":"禁售备注"}
        logger.info("infringementAuditFunction-------->start")
        if url == "" or auditStatus == "" or len(idsList) == 0:
            logger.error("infringementAuditFunction---->Input Parameters is NULL!")
            return "接口入参为空!"
        if infringementInfoMap != "":
            infringementTypeName = parseRequestDatas("infringementTypeName",infringementInfoMap) # 禁售类型
            infringementObj = parseRequestDatas("infringementObj",infringementInfoMap) # 禁售原因
            auditNotesInfo = parseRequestDatas("auditNotesInfo",infringementInfoMap) # 禁售备注信息
        siteReplaceList = []
        platSiteReplaceList = []
        if len(salesProhibitionList) > 0:
            for i in range(len(salesProhibitionList)):
                plat = salesProhibitionList[i].get("plat")
                sitesList = salesProhibitionList[i].get("sites").split(",")
                if len(sitesList) == 0:
                    platSiteReplaceList = []
                else:
                    for siteNum in range(len(sitesList)):
                        itemSite = sitesList[siteNum]
                        siteReplace = DasApiInputParam.infringmentReview_site
                        siteReplace["site"] = itemSite
                        siteReplaceList.append(siteReplace)
                platSiteReplace = DasApiInputParam.infringementReview_plat
                platSiteReplace["plat"] = plat
                platSiteReplace["sites"] = siteReplaceList
                platSiteReplaceList.append(platSiteReplace)
            infringementReviewReplace = DasApiInputParam.infringementReview_select
            infringementReviewReplace["ids"] = idsList
            infringementReviewReplace["infringementObj"] = infringementObj
            infringementReviewReplace["auditNotesInfo"] = auditNotesInfo
            infringementReviewReplace["infringementTypeName"] = infringementTypeName
            infringementReviewReplace["salesProhibition"] = platSiteReplaceList
            infringementReviewReplace["auditStatus"] = auditStatus
            infringementReviewReplace0 = json.dumps(infringementReviewReplace,ensure_ascii=False) # 转为string类型
            resultReplace = DasApiInputParam.infringementReview_param
            resultReplace["args"] = infringementReviewReplace0
            # 接口请求头
            header = Common_TokenHeader().token_header("new","181324")
            self.url = url
            self.header = header
            self.formData = resultReplace
            response = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))
            if response.json()["success"] == True:
                logger.info("infringementAuditFunction-------->end")
                return "侵权审核---接口响应成功"
            else:
                logger.error("cancelDevelopmentFunction -->response Data is wrong!")
                return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(response.json()["errorMsg"],url,resultReplace)




if __name__ == '__main__':
    url = DasApiUrl.smt_infringementAudit_url
    idsList = ["fc4764f3-aaaa-46bd-b932-14750c685078"]
    auditStatus = "2"
    salesProhibitionList = [{"plat":"Amazon","sites":"US,UK,IT"},{"plat":"Ebay","sites":"US,UK,AU"}]
    infringementInfoMap = {"infringementTypeName":"cjz测试的禁售类型","infringementObj":"cjz测试的禁售原因","auditNotesInfo":"禁售备注"}
    print(InfringementAuditsApi().infringementAuditFunction(url,idsList,auditStatus,salesProhibitionList,infringementInfoMap))