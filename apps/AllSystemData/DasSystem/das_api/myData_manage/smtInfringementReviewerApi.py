'''
@File: smtInfringementReviewerApi.py
@time:2021/8/30
@Author:quanliu
@Desc:我的数据-SMT分配侵权审核人接口服务类
'''
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_url import DasApiUrl
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.DasSystem.das_api.dasSystem_interface_param import DasApiInputParam
from apps.get_page_content_by_requests import get_page_content_by_requests
from flask import current_app as app
import json


class SmtInfringementReviewerApi():
    def smtInfringementReviewerFun(self,paramList,paramStr):# paramList--id集合,paramStr---侵权审核人字段
        app.logger.info("smtInfringementReviewerFun--------------->start")
        if paramStr == "" or len(paramList) == 0:
            app.logger.error("smtInfringementReviewerFun---->Input Parameters is null")
            return "请求参数为空"
        # 替换参数
        smt_infringementReviewer02 = DasApiInputParam.smt_infringementReviewer02
        smt_infringementReviewer02["ids"] = paramList
        smt_infringementReviewer02["infringementReviewer"] = paramStr
        smt_infringementReviewer01 = DasApiInputParam.smt_infringementReviewer01
        smt_infringementReviewer01["args"] = json.dumps(smt_infringementReviewer02)
        # 获取请求地址
        url = DasApiUrl.smt_infringementReviewer_url
        # 获取请求头信息
        header = Common_TokenHeader().token_header("new","181324")
        self.url = url
        self.header = header
        self.data = smt_infringementReviewer01
        resp = get_page_content_by_requests(self.url,self.header,self.data)
        if resp.status_code == 200:
            app.logger.info("smtInfringementReviewerFun--------------->end")
            return "分配侵权审核人---接口响应成功"
        else:
            app.logger.error("smtInfringementReviewerFun -->response Data is wrong!")
            return "接口响应失败,失败原因:{0},接口地址:{1},请求参数:{2}".format(resp.json()["errorMsg"],url,smt_infringementReviewer01)

if __name__ == '__main__':
    print(SmtInfringementReviewerApi().smtInfringementReviewerFun(["08183185-2023-41d1-b3e4-db56d24f6aff"],"172-肖群"))


