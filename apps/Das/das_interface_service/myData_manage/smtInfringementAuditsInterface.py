'''
@File: smtInfringementAuditsInterface.py
@time:2021/8/23
@Author:quanliu
@Desc:侵权审核接口服务类
'''
from apps.Das.das_interface_service.das_common_header import DasCommonHeader
from apps.Das.das_interface_service.myDataManage_inter_body import MyDataManageInterParam
import requests
import json

from apps.Das.das_interface_service.myDataManage_inter_url import MyDataManageInterUrl


class InfringementAuditsInterface():
    def infringementAuditFunction(self,casename,url,idsList,auditStatus,salesProhibitionList,infringementInfoMap):
        # 入参地址:url,idsList--id集合  auditStatus--审核状态（通过，不通过）salesProhibitionList--禁售平台和站点list infringementInfoMap--禁售信息dict
        # salesProhibitionList 格式[{"plat":"Amazon","sites":"US,UK,IT"},{"plat":"Ebay","sites":"US,UK,AU"}]
        # infringementInfoMap 格式 {"infringementTypeName":"cjz测试的禁售类型","infringementObj":"cjz测试的禁售原因","auditNotesInfo":"禁售备注"}
        if casename == "" or url == "" or auditStatus == "" or len(idsList) == 0:
            return "接口入参为空!"

        if infringementInfoMap != "":
            infringementTypeName = parseRequestDatas("infringementTypeName",infringementInfoMap) # 禁售类型
            infringementObj = parseRequestDatas("infringementObj",infringementInfoMap) # 禁售原因
            auditNotesInfo = parseRequestDatas("auditNotesInfo",infringementInfoMap) # 禁售备注信息
        idStr = ""
        # 处理入参idList
        for i in range(len(idsList)):
            idStr += "'"+idsList[i] +"',"

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
                        siteReplace = MyDataManageInterParam.infringmentReview_site
                        siteReplace["site"] = itemSite
                        siteReplaceList.append(siteReplace)

                platSiteReplace = MyDataManageInterParam.infringementReview_plat
                platSiteReplace["plat"] = plat
                platSiteReplace["sites"] = siteReplaceList

                platSiteReplaceList.append(platSiteReplace)

            infringementReviewReplace = MyDataManageInterParam.infringementReview_select
            infringementReviewReplace["ids"] = idsList
            infringementReviewReplace["infringementObj"] = infringementObj
            infringementReviewReplace["auditNotesInfo"] = auditNotesInfo
            infringementReviewReplace["infringementTypeName"] = infringementTypeName
            infringementReviewReplace["salesProhibition"] = platSiteReplaceList
            infringementReviewReplace["auditStatus"] = auditStatus

            infringementReviewReplace0 = json.dumps(infringementReviewReplace,ensure_ascii=False)

            resultReplace = MyDataManageInterParam.infringementReview_param
            resultReplace["args"] = infringementReviewReplace0

            # 接口请求头
            header = DasCommonHeader().getDasCommonHeader("new", "181324")

            self.url = url
            self.header = header
            self.formData = resultReplace

            response = requests.post(url=self.url,headers=self.header,data=json.dumps(self.formData))






# 解析每一个入参
def parseRequestDatas(keyname, kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName


if __name__ == '__main__':
    casename = "第一个用例"
    url = MyDataManageInterUrl.smt_infringementAudit_url
    idsList = ["9b1d40a0-9f3f-4658-ab86-9dc82f5761ea"]
    auditStatus = "2"
    salesProhibitionList = [{"plat":"Amazon","sites":"US,UK,IT"},{"plat":"Ebay","sites":"US,UK,AU"}]
    infringementInfoMap = {"infringementTypeName":"cjz测试的禁售类型","infringementObj":"cjz测试的禁售原因","auditNotesInfo":"禁售备注"}
    print(InfringementAuditsInterface().infringementAuditFunction(casename,url,idsList,auditStatus,salesProhibitionList,infringementInfoMap))