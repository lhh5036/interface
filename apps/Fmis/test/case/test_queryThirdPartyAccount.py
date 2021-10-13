# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_queryThirdPartyAccount
@time:2021/10/6
@Author:majiaqin 170479
@Desc:第三方收款-Payoneer收款列表数据接口用例
'''

import unittest
import random
import pprint

from apps.Fmis.fmis_interface_service.financial_manage.queryThirdPartyAccount import QueryThirdPartyAccount
from apps.utils.date_operate_util import getMonthFirstDay, getMonthLastDay
from apps.Fmis.fmis_common_settting import Fmis_Common_Setting
from apps.Sale.sale_common_setting import Sale_Common_Setting
from apps.Fmis.fmis_interface_service.fmisSystem_interface_param import FmisApiInputParam
from apps.utils.mySql_database_util import Mysql_handleOperator


class Test_queryThirdPartyAccount(unittest.TestCase):

    def queryParams(self):
        # 获取请求参数中的key
        self.lis = []
        for k in FmisApiInputParam.thirdPartyAccount03.copy().keys():
            self.lis.append(k)
        return self.lis

    def queryThirdPartyAccount_noplatform(self):
        # 从财务数据库获取传参所需的值
        i = random.randint(1, 1000)
        sql_noplatform = "SELECT tpa.email, tpa.type, tpa.account_id, \
tpa.nick_Name, tpa.status, tpab.currency \
FROM third_party_account tpa \
LEFT JOIN third_party_account_balance tpab \
ON tpab.account_id = tpa.account_id \
LIMIT {0},10;".format(i)
        self.paramsList_noplatform = Mysql_handleOperator(Fmis_Common_Setting.fmis_mysql).data_sql("select", sql_noplatform)
        # pprint.pprint(paramsList_noplatform)
        return self.paramsList_noplatform

    def queryThirdPartyAccount_platform(self):
        # 从订单数据库获取传参所需的值
        sql_platform = "SELECT code FROM sale_channel;"
        self.paramsList_platform = Mysql_handleOperator(Sale_Common_Setting.sale_mysql).data_sql("select", sql_platform)
        # pprint.pprint(paramsList_platform)
        return self.paramsList_platform

    # 按单个邮箱查询
    def testCase01(self):
        self.paramsList = [i[0] for i in self.queryThirdPartyAccount_noplatform()]
        num = random.randint(0, len(self.paramsList)-1)
        l = []
        l.append(self.paramsList[num])
        self.paramDict = {self.queryParams()[0]: l}
        self.responseResult01 = QueryThirdPartyAccount().querythirdpartyaccount(self.paramDict)
        if self.responseResult01 == True:
            return "Api normal response!"
        else:
            return self.responseResult01

    # 按多个邮箱查询
    def testCase02(self):
        self.paramsList = [i[0] for i in self.queryThirdPartyAccount_noplatform()]
        self.paramDict = {self.queryParams()[0]: self.paramsList}
        self.responseResult02 = QueryThirdPartyAccount().querythirdpartyaccount(self.paramDict)
        if self.responseResult02 == True:
            return "Api normal response!"
        else:
            return self.responseResult02


if __name__ == '__main__':
    Test_queryThirdPartyAccount().testCase01()
    Test_queryThirdPartyAccount().testCase02()
    pass