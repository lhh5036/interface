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
                statucode = Assert_Api().assert_statucode(func(*args))
                connect = Assert_Api().assert_connect(func(*args))
                l.append(statucode)
                l.append(connect)
                if "False" in l:
                    return "False"
                else:
                    return "True"
            else:
                statucode = Assert_Api().assert_statucode(func(*args))
                connect = Assert_Api().assert_connect(func(*args))
                total = Assert_Api().assert_total(func(*args), sql)
                l.append(statucode)
                l.append(connect)
                l.append(total)
                if "False" in l:
                    return "False"
                else:
                    return "True"
        return demo
    return wragger

if __name__ == '__main__':
    pass