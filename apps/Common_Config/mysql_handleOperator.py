'''
@File: mysql_handleOperator.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:mysql数据库操作类
'''


from apps.Common_Config.db_config import ReadConfig
import pymysql

# mysql数据库具体操作实现类
class Mysql_handleOperator():
    def __init__(self,projectname,env,dbtype="mysql"):
        self.projectname = projectname # 系统名称
        self.env = env # 当前环境
        self.dbtype = dbtype # 数据库类型
        _database,_host,_user,_password = ReadConfig().getDbConfig(self.env,self.projectname,self.dbtype) # 根据条件得到对应的数据库信息
        self.host = _host
        self.user = _user
        self.password = _password
        self.database = _database
        self.port = 3306
        self.charset = "utf-8"

        # # 连接数据库
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            charset=self.charset)

    def data_sql(self, methods, sql):
        self.methods = methods      # 声明增删改查哪种操作(insert/delete/update/select)
        self.sql = sql              # sql语句

        # 查询数据库数据
        if self.methods == 'select':
            cursor = self.con.cursor() # 创建一个游标
            cursor.execute(self.sql)
            cursor.close()
            results = cursor.fetchall() # 返回全部结果
            self.con.close() # 关闭数据库连接
            return results

        # 新增修改删除数据库数据
        elif self.methods == 'insert' or self.methods == 'update' or self.methods == 'delete':
            cursor = self.con.cursor()
            try:
                cursor.execute(self.sql)
                self.con.commit()
            except:
                self.con.rollback() # 出现异常回滚
            self.con.close() # 关闭数据库连接


