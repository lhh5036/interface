# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_selectSmtSellers_data
@time:2022/7/13
@Author:majiaqin 170479
@Desc:selectSmtSellers用例实际出参和期望出参拼接
'''

from loggerUtils import MyLog
from apps.Common_Config.interface_common_info import InterfaceCommonInfo
from apps.Common_Config.operate_api_data import Splicing_Params
from apps.Common_Config.operate_api_data import api_assemble_new

# 实例化日志类
logger = MyLog("Test_SelectSmtSellers_Data").getlog()
class Test_SelectSmtSellers_Data():
    def __init__(self, resp_list):
        self.resp_list = resp_list
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'saleaccount': []}
        json_list = [i.split("-")[0] for i in self.resp_json['result']]
        json_dict['saleaccount'] = list(set(json_list))
        return json_dict

    '''获取期望数据'''
    @api_assemble_new()
    def expect_json(self):
        self.url = InterfaceCommonInfo.common_url + '/sale-extra/saleaccount/listSaleAccount'
        self.paramsMap = {"saleChannel": "SMT",
                          "accountStatus": "1"}
        self.params_list = [{"saleChannel": "",
                            "accountStatus": ""}]
        self.api_params = Splicing_Params(self.params_list, self.paramsMap).splicing_params()
        return self.url, self.api_params

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_dict = {'saleaccount': list(set([i['id'] for i in self.expect_json()[1]['result']]))}
        return [self.resp_list[0], self.get_json(), expect_dict]

if __name__ == '__main__':
    pass