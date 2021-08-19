'''
@File: das_interface_entry.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据分析系统接口调用入口
'''

from flask import Flask,render_template
from apps.Das.das_interface_service.myData_manage.testCase_mydata_manage.testCase_amazon_releaseProductInterface import testCase_amazonReleaseRroductInterface
from apps.Das.das_interface_service.myData_manage.testCase_mydata_manage.testCase_amazon_selectInterface import testCase_amazonSelectInterface

app = Flask(__name__)

# 接口调用入口
@app.route("/dasInterfaceEntry")
def dasInterfaceEntry():
    return render_template('das_entry.html')

# 数据管理-我的数据Amazon查询用例执行入口
@app.route('/dataManage/amazon/selectInterface')
def test_amazonSelectInterface():
    selectResult = testCase_amazonSelectInterface() # 调用查询用例接口
    return render_template('dasManage_selectInterface.html',selectResult=selectResult)


# 数据管理-我的数据Amazon释放产品用例执行入口
@app.route('/dataManage/amazon/releaseRroductInterface')
def test_amazonReleaseRroductInterface():
    releaseProResult = testCase_amazonReleaseRroductInterface() #调用释放产品接口
    return render_template('dasManage_releaseProductInterface.html', releaseProResult=releaseProResult)



if __name__ == '__main__':
    app.run(debug=True)