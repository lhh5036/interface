# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: pmsSystem_interface_param.py
@time:2021/9/22
@Author:majiaqin 170479
@Desc:财务管理接口请求入参
'''

class FmisApiInputParam:
    """python无法处理true，因此需要先给false赋值并设置为全局变量"""
    global true
    true = ''

    # 财务报表-资金收入日报表查询入参
    capital_income01 = {"method":"capitalIncomeList", "args":"{0}"}
    capital_income02 = {"search":"{0}","pageReqired":true,"limit":10,
                        "offset":0,"order":"desc"}
    capital_income03 = {"startDate":"{0}","endDate":"{1}",
                        "incomeTypes":"{2}"}

    # 财务报表-资金支出日报表查询入参
    capital_cost01 = {"method":"capitalCostList","args":"{0}"}
    capital_cost02 = {"search":0,"pageReqired":true,"limit":10,
                      "offset":0,"order":"desc"}
    capital_cost03 = {"startDate":"{0}","endDate":"{1}",
                      "costTypes":"{2}"}

    # 财务报表-资金余额日报表查询入参
    fund_balance01 = {"method":"fundBalanceList","args":"{0}"}
    fund_balance02 = {"search": 0,"pageReqired":true,"limit":10,
                      "offset":0,"order":"desc"}
    fund_balance03 = {"startDate":"","endDate":"","startModifyTime":"",
                      "endModifyTime":""}

    # 财务报表-资金对比日报表查询入参
    capital_contrast01 = {"method":"selectCapitalContrastList","args":"{0}"}
    capital_contrast02 = {"search":0,"sort":"recordDate","order":"DESC",
                          "pageReqired":true,"limit":10,"offset":0}
    capital_contrast03 = {"startDate":"","endDate":""}

    # 第三方收款-Payoneer收款查询入参
    thirdPartyAccount01 = {"method":"searchThirdPartyAccount","args":"{0}"}
    thirdPartyAccount02 = {"search": 0,"pageReqired":true,"limit":10,
                           "offset":0,"order":"desc"}
    thirdPartyAccount03 = {"emailList":[],"accountTypeList":[],
                           "platformList":[],"platformAccountList":[],
                           "nickNameList":[],"statusList":[],
                           "curTypeList":[],"exportType":"EXPORT_PLATFORM"}
    pass