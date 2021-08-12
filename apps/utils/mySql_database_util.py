'''
@File: mySql_database_util.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:mySql数据库操作工具类
'''

import pymysql
from apps.Common_Config.db_config import ReadConfig

# MYSQL数据操作工具类
class Mysql_database_util():
    def __init__(self,env,projectname,dbtype='mysql',port=3306,charset='utf8'):
        mySqlConfig = ReadConfig.getDbConfig(env,projectname,dbtype)
        self.database = mySqlConfig[0] #数据库名
        self.host = mySqlConfig[1] #数据库ip
        self.user = mySqlConfig[2] #数据库用户名
        self.password = mySqlConfig[3] #数据库密码
        self.port = port #数据库端口号
        self.charset = charset

        # 连接数据库
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            charset=self.charset)

    def data_sql(self, methods, sql):
        self.methods = methods  # 声明增删改查哪种操作(insert/delete/update/select)
        self.sql = sql  # sql语句

        # 查询数据库数据
        if self.methods == 'select':
            # 得到一个可以执行SQL语句的光标对象
            cursor = self.con.cursor()
            cursor.execute(self.sql)
            results = cursor.fetchall()
            # 关闭光标对象
            cursor.close()
            # 关闭数据库连接
            self.con.close()
            return results
        # 新增修改删除数据库数据
        elif self.methods == 'insert' or self.methods == 'update' or self.methods == 'delete':
            cursor = self.con.cursor()
            cursor.execute(self.sql)
            cursor.close()
            self.con.commit()
            self.con.close()



