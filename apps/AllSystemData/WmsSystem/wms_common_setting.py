# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: wms_common_setting
@time:2021/10/6
@Author:majiaqin 170479
@Desc:仓库系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Wms_Common_Setting:
    # 测试环境MySQL数据库配置
    wms_mysql = Mysql_Db_Config("erp_wms_test")

    # 生产环境MySQL数据库配置
    # wms_mysql = Mysql_Db_Config("erp_wms_release")
