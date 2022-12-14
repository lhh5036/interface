'''
@File: smtInfringementAuditsApi.py
@time:2021/8/23
@Author:quanliu
@Desc:侵权审核接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.publicCommonUrlSevice import PublicCommonUrlServiceClass
import json
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new
from flask import current_app as app
from apps.Common_Config.parseRequestDatas import parseRequestDatas

@api_assemble_new()
def infringementAuditFunction(platform,searchType,idsList,auditStatus,salesProhibitionList,infringementInfoMap):
    # 入参地址:url,idsList--id集合  auditStatus--审核状态（通过，不通过）salesProhibitionList--禁售平台和站点list infringementInfoMap--禁售信息dict
    # salesProhibitionList 格式[{"plat":"Amazon","sites":"US,UK,IT"},{"plat":"Ebay","sites":"US,UK,AU"}]
    # infringementInfoMap 格式 {"infringementTypeName":"cjz测试的禁售类型","infringementObj":"cjz测试的禁售原因","auditNotesInfo":"禁售备注"}
    app.logger.info("infringementAuditFunction-------->start")
    if searchType == "" or auditStatus == "" or len(idsList) == 0:
        app.logger.error("infringementAuditFunction---->Input Parameters is NULL!")
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

        url = PublicCommonUrlServiceClass().getApiUrl(platform,searchType) # 请求地址
        return url,resultReplace
