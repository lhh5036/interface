# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: das_common_settting
@time:2021/10/26
@Author:quanliu 181324
@Desc:数据分析系统获取数据库配置
'''

from apps.Common_Config.db_config import Es_Db_Config

class Das_Common_Setting:
    # 测试环境ES数据配置
    das_es = Es_Db_Config("es_test")

    # 生产环境ES数据配置
    # das_es = Es_Db_Config("es_release")


if __name__ == '__main__':
    print(Das_Common_Setting.das_es)
