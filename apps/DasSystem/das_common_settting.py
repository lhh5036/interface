# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: das_common_settting
@time:2021/10/26
@Author:quanliu 181324
@Desc:数据分析系统获取数据库配置
'''

from apps.Common_Config.db_config import ReadConfig

class Das_Common_Setting:
    # 测试环境MySQL数据库配置
    das_mysql = ReadConfig().getDbConfig("test", "das", "mysql")

    # 生产环境MySQL数据库配置
    # das_mysql = ReadConfig().getDbConfig("release", "das", "mysql")

    # 测试环境ES数据配置
    das_es = ReadConfig().getDbConfig("test", "das", "es")

    # 生产环境ES数据配置
    # das_es = ReadConfig().getDbConfig("release", "das", "es")


if __name__ == '__main__':
    print(Das_Common_Setting.das_es)
