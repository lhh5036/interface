# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: sale_common_setting
@time:2021/10/6
@Author:majiaqin 170479
@Desc:订单系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Tms_Common_Setting:
    # 测试环境MySQL数据库配置
    tms_mysql = Mysql_Db_Config("erp_tms_test")

    # 生产环境MySQL数据库配置
    # tms_mysql = Mysql_Db_Config("erp_tms_release")
