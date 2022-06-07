'''
@File: test_purchaseSuggestionApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:需求管理-采购建议用例
'''

import unittest
from apps.AllSystemData.PmsSystem.pms_api.menuManager.purchaseSuggestionApi import purchaseSuggestionApi


class Test_purchaseSuggestionApi(unittest.TestCase):

    def testCase01(self):
        '''需求管理-采购建议查询(有参数)'''
        responseResult01 = purchaseSuggestionApi({"articleNumber":"5AC304821-A03"})
        print(responseResult01)

    def testCase02(self):
        '''需求管理-采购建议查询(无参数)'''
        responseResult02 = purchaseSuggestionApi({"warehouseAttr":"美景仓"})
        print(responseResult02)

if __name__ == '__main__':
    unittest.main(verbosity=2)