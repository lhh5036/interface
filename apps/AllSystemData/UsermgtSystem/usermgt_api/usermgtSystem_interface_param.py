# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: usermgtSystem_interface_param
@time:2022/4/20
@Author:majiaqin 170479
@Desc:新用户接口入参汇总
'''

class UsermgtApiInputParam:
    # 查看账号在该页面下的数据权限接口入参
    getRDPEmployees_param01 = {"args": ""}
    getRDPEmployees_param02 = {'employeeNo': '',
                               'menuCode': ''}

    # 查看该组织架构id的下级员工接口入参
    listNextEmployeeByDeptId_param01 = {"args": ""}

    # 根据职位查询员工入参
    getEmployeeList_param01 = {"positionName": ""}

    # 判断员工是否为负责人,返回相关员工信息接口入参
    listTeamLeaderByEmployeeNo_param01 = {"args": ""}
    listTeamLeaderByEmployeeNo_param02 = {"employeeNo": "3381",
                                          "servicePlatform": "SMT平台"}

    # 根据平台和工号获取级联获取员工信息接口入参
    newListOrgStructAndEmployeeVO_param01 = {"orgName": "",
                                             "employeeNo": ""}

    # 根据平台和工号获取级联获取员工信息（树形返回）接口入参
    treeListOrgStructAndEmployeeVO_param01 = {"orgName": "",
                                              "employeeNo": ""}

    # 获取页面数据权限
    employee_params01 = {"args": "",
                         "method": ""}
    employee_params02 = {"employeeNo": "",
                         "menuCode": ""}

    # 返回新用户系统某个账号关联的角色名接口入参
    queryRoleByEmpNos_param01 = [""]

    # 根据账号获取该账号的上一级接口入参
    superByEmpNo_param01 = {"empNo": ""}

    # 根据账号获取该账号的菜单按钮code接口入参
    getMenuCodes_param01 = {"args": ""}

    # 菜单权限对接(通过传code返回code类型)接口入参
    getMenuPermissionTypes_param01 = {"args": ""}
    getMenuPermissionTypes_param02 = {'employeeNo': '',
                                      'codes': []}

    # 获取系统权限列表接口入参
    listSystem_param01 = {"time": "",
                          "signature": ""}

    # 获取所有员工信息接口入参
    listAllEmployee_param01 = {"method": "getEmployeeNames",
                               "args": "{}"}

    # 根据工号获取员工信息接口入参
    getUserByNo_param01 = {"args": ""}
    getUserByNo_param02 = {"employeeNo": ""}

    # 根据所属平台和角色名称（模糊）获取所有员工指定信息
    getEmployeeByServicePlatformAndRoleName_param01 = {"servicePlatform": "",
                                                       "roleName": ""}

    # 根据组织架构id,获取当前级和下级用户接口入参
    listEmployeeByDeptId_param01 = {"args": ""}
    listEmployeeByDeptId_param02 = {"deptIds": []}

    # 根据组织架构名称,获取当前级和下级用户接口入参
    listEmployeeByDeptName_param01 = {"method": "getEmplayeeByFunNames",
                                      "args": ""}

    # 修改员工信息接口入参
    saveOrUpdate_param01 = [{
            "id": 3395,
            "employeeNo": "10001",
            "deptId": 50495088,
            "positionId": 48,
            "positionName": "产品开发"
          }]