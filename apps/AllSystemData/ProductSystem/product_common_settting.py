# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: product_common_settting
@time:2021/10/6
@Author:majiaqin 170479
@Desc:产品系统全局配置
'''

from apps.Common_Config.db_config import Mysql_Db_Config

class Fmis_Common_Setting:
    # 测试环境MySQL数据库配置
    product_mysql = Mysql_Db_Config("erp_product_test")

    # 生产环境MySQL数据库配置
    # product_mysql = Mysql_Db_Config("erp_product_release")