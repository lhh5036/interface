'''
ES数据库操作工具类
'''

from elasticsearch6 import Elasticsearch
from apps.config import db_config


#ES数据库操作工具
class Es_database_util():
    def __init__(self):
        esCofig = db_config.getEsConfig("testCase_mydata_manage")
        self.hosts = esCofig[0]
        self.port = esCofig[1]
        self.timeout = int(esCofig[2])
    #查询
    def data_es(self,index, querys):
        self.index = index  # es表(索引)
        self.query = querys  # 查询语句

        es = Elasticsearch(hosts=self.hosts, port=self.port, timeout=self.timeout)
        query = self.query
        allDoc = es.search(index=self.index, body=query)
        if allDoc['hits']['total'] == 0:
            return 0
        else:
            return allDoc['hits']

    # 按游标获取数据(解决获取一百万以上数据导致数据库报错的问题)
    def data_es_new(self, method, index, querys, scroll='20m', nsize=1000):
        self.method = method    # total获取表数据数量 data获取表全部数据
        self.index = index      # es表(索引)
        self.query = querys     # 查询语句
        self.scroll = scroll    # 通过此参数可以获取es表中的scroll_id
        self.nsize = nsize      # 设置游标查询条目数

        es = Elasticsearch(hosts=self.hosts, port=self.port, timeout=self.timeout)
        query = self.query
        allDoc = es.search(index=self.index, body=query, scroll=self.scroll, size=self.nsize)
        if self.method == 'total':
            return allDoc['hits']['total']
        elif self.method == 'data':
            # 游标用于输出es查询出的所有结果
            scroll_id = allDoc['_scroll_id']
            results = []
            results.append(allDoc['hits']['hits'])
            for j in range(0, int(allDoc['hits']['total']/self.nsize)+1):
                result = es.scroll(scroll_id=scroll_id, scroll=self.scroll)
                if len(result['hits']['hits']) == 0:
                    pass
                else:
                    results.append(result['hits']['hits'])
            return results[0]

