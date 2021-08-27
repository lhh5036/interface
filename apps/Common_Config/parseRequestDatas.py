# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: interface_common_info.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:解析每一个入参
'''

# 解析每一个入参
def parseRequestDatas(keyname,kwargs):
    if kwargs.get(keyname) is None:
        valueName = ""
    else:
        valueName = kwargs.get(keyname)
    return valueName

if __name__ == '__main__':
    pass