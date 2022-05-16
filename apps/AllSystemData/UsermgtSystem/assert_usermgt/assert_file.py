# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: assert_file
@time:2022/3/25
@Author:majiaqin 170479
@Desc:断言文件
'''

import requests
import json
import pprint

from apps.utils.assert_utils import Assert_Api

def usermgt_unit_assert(sql=None):
    def wragger(func):
        def demo(*args):
            l = []
            if sql == None:
                statucode = Assert_Api().assert_statucode(func(*args)[0])
                connect = Assert_Api().assert_connect(func(*args)[0], func(*args)[1])
                l.append(statucode)
                l.append(connect)
                if "False" in l:
                    print("False")
                    return "False"
                else:
                    print("True")
                    return "True"
            else:
                statucode = Assert_Api().assert_statucode(func(*args)[0])
                connect = Assert_Api().assert_connect(func(*args)[0], func(*args)[1])
                total = Assert_Api().assert_total(func(*args)[1], sql)
                l.append(statucode)
                l.append(connect)
                l.append(total)
                if "False" in l:
                    print("False")
                    return "False"
                else:
                    print("True")
                    return "True"
        return demo
    return wragger

@usermgt_unit_assert()
def test():
    l = [200, {'success': True, 'result': None, 'errorMsg': None, 'connectionRefused': False}]
    return l

if __name__ == '__main__':
    test()
    pass