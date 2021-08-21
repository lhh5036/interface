'''
@File: das_interface_entry.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据分析系统接口调用入口
'''

from flask import Flask,render_template

from apps.Das.test.case.test_amazon_associateSystemSkuInterface import test_amazonAssociateSySkuInterface
from apps.Das.test.case.test_amazon_releaseProductInterface import test_amazonReleaseRroductInterface
from apps.Das.test.case.test_amazon_selectInterface import test_amazonSelectInterface

app = Flask(__name__)


# 接口调用入口
@app.route("/dasInterfaceEntry")
def dasInterfaceEntry():
    return render_template('das_entry.html')



# 数据管理-我的数据Amazon查询用例执行入口
@app.route('/dataManage/amazon/selectInterface')
def amazonSelectInterface():
    selectResultlist = test_amazonSelectInterface() # 调用查询接口用例返回list
    return render_template("das_error.html",selectResult=selectResultlist)


# 数据管理-我的数据Amazon释放产品用例执行入口
@app.route('/dataManage/amazon/releaseRroductInterface')
def run_amazonReleaseRroductInterface():
    releaseProResultlist = test_amazonReleaseRroductInterface() # 调用释放产品接口用例
    return render_template('das_error.html', releaseProResult=releaseProResultlist)



# 数据管理-我的数据Amazon关联系统SKU用例执行入口
@app.route('/dataManage/amazon/associateSystemSkuInterface')
def test_amazonAssociateSystemSkuInterface():
    assSySkuResultlist = test_amazonAssociateSySkuInterface() # 调用关联系统SKU接口
    return render_template('das_error.html',assSySkuResult=assSySkuResultlist)

if __name__ == '__main__':
    app.run(debug=True)