# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: usermgtSystem_interface_url
@time:2022/3/25
@Author:majiaqin 170479
@Desc:新用户系统接口地址
'''

from  apps.Common_Config.interface_common_info import InterfaceCommonInfo

class UsermgtApiUrl:
    # 查看账号在该页面下的数据权限
    getRDPEmployees_url = InterfaceCommonInfo.common_url + \
                          '/usermgt-n/sys/roledatapermission/getRDPEmployees'
    # 查看该组织架构id的下级员工
    listNextEmployeeByDeptId_url = InterfaceCommonInfo.common_url + \
                                   '/usermgt-n/hr/employee/listNextEmployeeByDeptId'
    # 根据职位查询员工
    getEmployeeList_url = InterfaceCommonInfo.common_url + \
                          '/usermgt-n/hr/employee/getEmployeeList'
    # 判断员工是否为负责人,返回相关员工信息
    listTeamLeaderByEmployeeNo_url = InterfaceCommonInfo.common_url + \
                                     '/usermgt-n/hr/employee/listTeamLeaderByEmployeeNo'
    # 根据平台和工号获取级联获取员工信息
    newlistOrgStructAndEmployeeVO_url = InterfaceCommonInfo.common_url + \
                                        '/usermgt-n/sys/orgstruct/newlistOrgStructAndEmployeeVO'
    # 获取页面数据权限
    employee_url = InterfaceCommonInfo.common_url + \
                   '/newpms/employee'
    # 根据平台和工号获取级联获取员工信息（树形返回）
    treeListOrgStructAndEmployeeVO_url = InterfaceCommonInfo.common_url + \
                                         '/usermgt-n/sys/orgstruct/treeListOrgStructAndEmployeeVO'
    # 返回新用户系统某个账号关联的角色名
    queryRoleByEmpNos_url = InterfaceCommonInfo.common_url + \
                            '/usermgt-n/api/das/queryRoleByEmpNos'
    # 根据账号获取该账号的上一级
    superByEmpNo_url = InterfaceCommonInfo.common_url + \
                       '/usermgt-n/api/das/superByEmpNo'
    # 根据账号获取该账号的菜单按钮code
    getMenuCodes_url = InterfaceCommonInfo.common_url + \
                       '/usermgt-n/sys/menu/getMenuCodes'
    # 菜单权限对接(通过传code返回code类型)
    getMenuPermissionTypes_url = InterfaceCommonInfo.common_url + \
                                 '/usermgt-n/sys/menupermission/getMenuPermissionTypes'
    # 根据角色名称获取关联该角色的所有账号
    getEmployeesByRoleName_url = InterfaceCommonInfo.common_url + \
                                 '/usermgt-n/sys/role/getEmployeesByRoleName/{0}'
    # 根据角色名称集合模糊查询角色集合中所有角色对应的员工工号及名称
    getEmployeesByRoleNamesroleNames_url = InterfaceCommonInfo.common_url + \
                                           '/usermgt-n/sys/role/getEmployeesByRoleNames?roleNames={0}'
    # 获取系统权限列表
    listSystem_url = InterfaceCommonInfo.common_url + \
                     '/usermgt-n/sys/system/listSystem?_t=1639446837284'
    # 获取所有员工信息
    getAllEmployeeInfo_url = InterfaceCommonInfo.common_url + \
                             '/usermgt-n/publish/employee/getAllEmployeeInfo'
    # 根据工号获取员工信息
    getUserByNo_url = InterfaceCommonInfo.common_url + \
                      '/usermgt-n/hr/employee/getUserByNo'
    # 根据所属平台和角色名称(模糊)获取所有员工指定信息
    getEmployeeByServicePlatformAndRoleName_url = InterfaceCommonInfo.common_url + \
                                                  '/usermgt-n/publish/employee/getEmployeeByServicePlatformAndRoleName'
    # 根据所属平台获取所有员工指定信息
    getEmployeeByServicePlatform_url = InterfaceCommonInfo.common_url + \
                                       '/usermgt-n/publish/employee/getEmployeeByServicePlatform?servicePlatform='
    # 根据组织架构id,获取当前级和下级用户
    listEmployeeByDeptId_url = InterfaceCommonInfo.common_url + \
                               '/usermgt-n/hr/employee/listEmployeeByDeptId'
    # 根据组织架构名称,获取当前级和下级用户
    listEmployeeByDeptName_url = InterfaceCommonInfo.common_url + \
                                 '/usermgt-n/hr/employee/listEmployeeByDeptName'
    # 根据角色id集合，查询角色对应员工工号、id及名称
    getEmployeesByRoleIds_url = InterfaceCommonInfo.common_url + \
                                '/usermgt-n/sys/role/getEmployeesByRoleIds?roleIds={0}'
    # 根据用户id获取该用户信息
    getEmplInfoById_url = InterfaceCommonInfo.common_url + \
                          '/usermgt-n/hr/employee/getEmplInfoById?ids={0}'
    # 根据工号获取该员工的菜单code和菜单权限code
    getMenuCodeAndMenuPermissionCodeByEmplNo_url = InterfaceCommonInfo.common_url + \
                                                   '/usermgt-n/sys/menu/getMenuCodeAndMenuPermissionCodeByEmplNo/{0}'
    # 角色管理-根据角色name集合查询角色对应员工工号、id及名称
    getEmpNoAndEmpNameDTOByRoleNames_url = InterfaceCommonInfo.common_url + \
                                           '/usermgt-n/sys/role/getEmpNoAndEmpNameDTOByRoleNames'

if __name__ == '__main__':
    pass