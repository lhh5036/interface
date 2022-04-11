# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: pms_common_setting
@time:2021/10/6
@Author:quanliu 181324
@Desc:采购系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Pms_Common_Setting:
    # 测试环境MySQL数据库配置
    pms_mysql = Mysql_Db_Config("erp_pms_test")

    # 生产环境MySQL数据库配置
    # pms_mysql = Mysql_Db_Config("erp_pms_release")
