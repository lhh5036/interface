'''
@File: test_purchaseSuggestionApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:需求管理-采购建议用例
'''

import unittest
from apps.AllSystemData.PmsSystem.pms_api.menuManager.purchaseSuggestionApi import purchaseSuggestionApi
from apps.utils.assert_new_utils import concat_assert_data, new_assert_utils


class Test_purchaseSuggestionApi(unittest.TestCase):
    @new_assert_utils
    @concat_assert_data
    def testCase01(self):
        '''需求管理-采购建议查询(有参数)'''
        responseResult01 = purchaseSuggestionApi({"articleNumber":"5AC304821-A03"})
        tCode1 = responseResult01[0]
        tJson1 = {"articleNumber":"5AC304821-A03","status":1}
        tkey = ["articleNumber","status"]
        tCode2 = 500
        tJson2 = (("5AC304821-A03",1),)
        t1 = [tCode1,tJson1]
        t2 = [tCode2,tJson2]
        return tkey,t1,t2

    def testCase02(self):
        '''需求管理-采购建议查询(无参数)'''
        responseResult02 = purchaseSuggestionApi({"warehouseAttr":"美景仓"})
        return responseResult02

if __name__ == '__main__':
    unittest.main(verbosity=2)