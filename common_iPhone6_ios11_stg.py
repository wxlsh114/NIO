#coding=utf-8
import unittest
import time
import os
import sys
from time import sleep

import xlrd

from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

sys.path.append('../../')
from HTMLTestReportEN import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction

#*******************************************************
#Name:fun_getinfo
#Purpose:读取外部excel文件里的数据作为登录时的手机号和验证码的参数
#Parameters:入口参数无
#Outputs:返回手机号和验证码2个值
#Example:N/A
#Modified history:2018/08/13
#*******************************************************
def fun_getinfo(self):
    print('Common_从外部excel文件读取用户手机号、验证码信息')
    sleep(1)
    workbook = xlrd.open_workbook('../../test_data/UI_data/account.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[0]
    st1=workbook.sheet_by_name('Sheet1')
    mobile_no0=int(st1.cell(2,0).value)
    print('手机号：'+str(mobile_no0))
    code0=st1.cell(2,1).value
    print('验证码：'+code0)
    sleep(1)
    return (mobile_no0,code0)

#*******************************************************
#Name:bp_is_plusexist
#Purpose:判断发现首页右上角的+号是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/17
#*******************************************************
def bp_is_plusexist(self):
    driver=self.driver
    print('Common_检查手机号码登录APP，检查点:发现首页右上角的+号是否存在')
    sleep(2)
    #发现
    #driver.find_element_by_accessibility_id('发现').click()
    #sleep(2)
    plus=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="addPopMenu"]')
    if len(plus) == 0:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        driver.get_screenshot_as_file(sf)
        print('----发现首页右上角的+号不存在！请检查，谢谢！')
    else:
        print('----发现首页右上角的+号存在！检查通过！')
        return(True)
    sleep(1)

#*******************************************************
#Name:bp_is_publishnowexist
#Purpose:判断点击发现首页右上角的+号后是否存在发布此刻的按钮
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/17
#*******************************************************
def bp_is_publishnowexist(self):
    driver=self.driver
    print('Common_检查手机号码登录APP，检查点:点击发现首页右上角的+号后是否存在发布此刻的按钮')
    sleep(1)
    #发现
    #driver.find_element_by_accessibility_id('发现').click()
    #sleep(2)
    publish=driver.find_elements_by_accessibility_id('发此刻')
    if len(publish) == 0:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(1)
        print('----发现首页发此刻不存在！请检查，谢谢！')
    else:
        print('----发现首页发此刻存在！检查通过！')
        return(True)
    sleep(1)

#*******************************************************
#Name:bp_is_openmultichatexist
#Purpose:判断点击发现首页右上角的+号后是否存在发起群聊的按钮
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/17
#*******************************************************
def bp_is_openmultichatexist(self):
    driver=self.driver
    print('Common_检查手机号码登录APP，检查点:点击发现首页右上角的+号后是否存在发起群聊的按钮')
    sleep(1)
    #发现
    #driver.find_element_by_accessibility_id('发现').click()
    #sleep(2)
    publish=driver.find_elements_by_accessibility_id('建群聊')
    if len(publish) == 0:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        driver.get_screenshot_as_file(sf)
        sleep(1)
        print('----建群聊不存在！请检查，谢谢！')
    else:
        print('----建群聊存在！检查通过！')
        return(True)
    sleep(1)

#*******************************************************
#Name:bp_is_loggedin
#Purpose:判断用户是否已经登录了，如果已登录先退出目前账号
#Parameters:入口参数无
#Outputs:返回True值
#Example:N/A
#Modified history:2018/08/13
#*******************************************************
def bp_is_loggedin(self):
    driver=self.driver
    print('Common_检查手机号码登录APP，检查点:用户是否已经登录了，如果已登录先退出目前账号')
    sleep(2)
    #我的
    driver.find_element_by_accessibility_id('我的').click()
    sleep(2)
    login=driver.find_elements_by_accessibility_id('注册/登录')
    #print(len(login))
    if len(login) == 0:
        print('----用户已经登录')
        #self.driver.execute_script("mobile: scroll", {"direction": "down"})
        driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":550,"toX":50,"toY":250,"duration":1.0})
        sleep(2)
        #设置
        driver.find_element_by_accessibility_id('设置').click()
        sleep(1)
        driver.find_element_by_accessibility_id('退出登录').click()
        sleep(1)
        driver.find_element_by_accessibility_id('确认').click()
        sleep(2)
        #self.driver.execute_script("mobile: scroll", {"direction": "up"})
        driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":250,"toX":50,"toY":550,"duration":1.0})
        sleep(2)
    else:
        print('----用户没有登录')
        return(True)
    sleep(1)

#*******************************************************
#Name:bp_is_loginshow
#Purpose:判断用户登录界面是否正常弹出显示
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/13
#*******************************************************
def bp_is_loginshow(self):
    driver=self.driver
    print('Common_检查访客模式登录APP，检查点:用户登录界面是否正常弹出显示')
    sleep(2)
    login=driver.find_elements_by_accessibility_id('注册/登录')
    if len(login) == 0:
        print('----用户登录界面没有正常显示，请检查')
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorLoginUI_R.png'
        driver.get_screenshot_as_file(sf)
        #return(False)
    else:
        print('----用户登录界面正常显示')
        return(True)
    sleep(2)

#****************************************************************
#Name:fun_getmypublish
#Purpose:从外部excel文件读取我的发布页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回我的发布页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/10
#****************************************************************
def fun_getmypublish(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/myPublishUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,10):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM,listF)
    
#*******************************************************
#Name:fun_mypublishui_check
#Purpose:判断我的页面点击发布后页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/02
#*******************************************************
def fun_mypublishui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:我的页面点击发布后页面各个元素是否存在')
    sleep(2)
    f=fun_getmypublish(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(9):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----我的发布页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyPublishUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----我的发布页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)


#**************************************************************
#Name:fun_getmywatch
#Purpose:从外部excel文件读取我的关注页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回我的关注页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/10
#**************************************************************
def fun_getmywatch(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/myWatchUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,7):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM,listF)

#*******************************************************
#Name:fun_mywatchui_check
#Purpose:判断我的页面点击关注后显示页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/10
#*******************************************************
def fun_mywatchui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:我的页面点击关注后显示页面各个元素是否存在')
    sleep(2)
    f=fun_getmywatch(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(6):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----我的关注页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyWatchUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----我的关注页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

#***************************************************************
#Name:fun_getmyfans
#Purpose:从外部excel文件读取我的粉丝页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回我的粉丝页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/13
#***************************************************************
def fun_getmyfans(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/myFansUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,6):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************
#Name:fun_myfansui_check
#Purpose:判断我的页面点击粉丝后显示页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/02
#*******************************************************
def fun_myfansui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:我的页面点击粉丝后显示页面各个元素是否存在')
    sleep(2)
    f=fun_getmyfans(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(5):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----我的粉丝页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyFansUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----我的粉丝页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

"""
#*******************************************************************
#Name:fun_getmyes8order
#Purpose:从外部excel文件读取我的ES8订单页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回我的ES8订单页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/02
#*******************************************************************
def fun_getmyes8order(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/myES8OrderUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[0]
    st1=workbook.sheet_by_name('Sheet1')
    listM=[]
    listF=[]
    for i in range(1,6):
        id_checked=str(st1.cell(i,0).value)
        #print('ID'+str(i)+':'+id_checked)
        listM.append(id_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM,listF)

#*******************************************************
#Name:fun_myes8orderui_check
#Purpose:判断我的页面点击我的ES8订单后显示页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/02
#*******************************************************
def fun_myes8orderui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:我的页面点击我的ES8订单后显示页面各个元素是否存在')
    sleep(2)
    f=fun_getmyes8order(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(5):
        ids=driver.find_elements_by_id(f[0][j])
        if len(ids) == 0:
            print('我的ES8订单页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyES8OrderUI_R.png'
            driver.get_screenshot_as_file(sf)
            sleep(1)
            return(False)
        else:
            print('----我的ES8订单页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)
"""

#*******************************************************
#Name:bp_normalloginmp
#Purpose:用从外部excel文件里读取的参数手机号+验证码正常登录app
#Parameters:入口参数无
#Outputs:返回参数无
#Example:N/A
#Modified history:2018/08/13
#*******************************************************
def bp_normalloginmp(self):
    driver=self.driver
    print('Common_用手机号+验证码正常登录app')
    sleep(2)
    #f=fun_getinfo(self)
    #sleep(2)
    driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":250,"toX":50,"toY":550,"duration":1.0})
    sleep(2)
    #driver.find_element_by_accessibility_id('注册/登录').click()
    driver.execute_script("mobile: tap", {"touchCount":"1", "x":67, "y":100})
    sleep(2)
    #登录页面
    mobile_no=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
    mobile_no.click()
    sleep(1)
    mobile_no.send_keys('98762396871')
    sleep(1)
    code=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
    code.click()
    sleep(1)
    #code.send_keys(f[1])
    code.send_keys('867129')
    sleep(1)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="注册/登录"]').click()
    sleep(5)
    driver.find_element_by_accessibility_id('返回').click()
    sleep(2)
    driver.execute_script("mobile: dragFromToForDuration",{"fromX":150,"fromY":250,"toX":150,"toY":550,"duration":1.0})
    sleep(2)
    name=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"SamSTG")]')
    if len(name) != 0:
        print('登录成功！')
    else:
        print('登录失败！')
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errornormalLogin_R.png'
        driver.get_screenshot_as_file(sf)
    sleep(1)

#*******************************************************************
#Name:fun_getloginmenu
#Purpose:从外部excel文件读取访客模式下需要检查点击后是否弹出用户登录页面的菜单名称
#Parameters:入口参数无
#Outputs:返回访客模式下需要检查点击后是否弹出用户登录页面的菜单名称一个列表
#Example:N/A
#Modified history:2018/08/13
#*******************************************************************
def fun_getloginmenu(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/loginUI_menu.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    for i in range(0,10):
        name=str(st1.cell(i,0).value)
        #print('Menu'+str(i)+':'+name)
        listM.append(name)
    sleep(1)
    #print(listM)
    return (listM)

#***************************************************************
#Name:fun_getfind
#Purpose:从外部excel文件读取发现页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回发现页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/16
#***************************************************************
def fun_getfind(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/findUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,22):
        xpath_checked=str(st1.cell(i,0).value)
        #print('Xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************
#Name:fun_findui_check
#Purpose:判断发现页面tab上各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/16
#*******************************************************************************************
def fun_findui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:发现页面tab上各个元素和推荐、此刻子tab页上元素是否存在')
    sleep(1)
    f=fun_getfind(self)
    #print(f[0])
    #print(f[1])
    sleep(1)
    #check the element by its id in turn from the outside excel file
    for j in range(6):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----发现页面tab上元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindTabUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----发现页面tab上元素：'+f[1][j]+'--检查通过：正常显示')
    sleep(2)
    for k in range(6,13):
        xpaths=driver.find_elements_by_xpath(f[0][k])
        if len(xpaths) == 0:
            print('----推荐tab内元素：'+f[1][k]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindRecomUI_R.png'
            driver.get_screenshot_as_file(sf)
            sleep(1)
            #return(False)
        else:
            print('----推荐tab内元素：'+f[1][k]+'--检查通过：正常显示')
        sleep(2)
    #此刻
    driver.find_element_by_accessibility_id('此刻').click()
    sleep(2)
    for k in range(13,21):
        xpaths=driver.find_elements_by_xpath(f[0][k])
        if len(xpaths) == 0:
            print('----此刻tab内元素：'+f[1][k]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindNowUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----此刻tab内元素：'+f[1][k]+'--检查通过：正常显示')
        sleep(2)
    return(True)

#********************************************************************
#Name:fun_getpersonalinfo
#Purpose:从外部excel文件读取个人信息页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回个人信息页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/16
#********************************************************************
def fun_getpersonalinfo(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/personalInfoUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,10):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_personalinfoui_check
#Purpose:判断个人信息页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/16
#*******************************************************************************************************
def fun_personalinfoui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:我的页面点击头像后再点击编辑个人信息显示的个人信息页面上各个元素是否存在')
    sleep(2)
    f=fun_getpersonalinfo(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its xpath in turn from the outside excel file
    for j in range(9):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----个人信息页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorPersonalInfoUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----个人信息页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

#********************************************************************
#Name:fun_getscoredetail
#Purpose:从外部excel文件读取积分明细页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回积分明细页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/16
#********************************************************************
def fun_getscoredetail(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/scoredetailUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
    listM=[]
    listF=[]
    for i in range(1,8):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_scoredetailui_check
#Purpose:判断积分明细页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/16
#*******************************************************************************************************
def fun_scoredetailui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:积分明细页面点击头像后再点击编辑个人信息显示的个人信息页面上各个元素是否存在')
    sleep(2)
    f=fun_getscoredetail(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its xpath in turn from the outside excel file
    for j in range(7):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----积分明细页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorScoreDetailUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----积分明细页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

#********************************************************************
#Name:fun_getgift
#Purpose:从外部excel文件读取惊喜页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回惊喜页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/10
#********************************************************************
def fun_getgift(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/giftUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,5):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_giftui_check
#Purpose:判断惊喜页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/10
#*******************************************************************************************************
def fun_giftui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:惊喜页面上各个元素是否存在')
    sleep(2)
    f=fun_getgift(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(4):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----惊喜页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorGiftUI_R.png'
            driver.get_screenshot_as_file(sf)
            sleep(1)
            #return(False)
        else:
            print('----惊喜页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

#********************************************************************
#Name:fun_getarticle
#Purpose:从外部excel文件读取发现页面推荐tab里文章需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回发现页面推荐tab里文章需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/23
#********************************************************************
def fun_getarticle(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/articleUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,9):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_articleui_check
#Purpose:判断发现页面推荐tab里文章的各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/23
#*******************************************************************************************************
def fun_articleui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:发现页面推荐tab里文章的各个元素是否存在')
    sleep(1)
    f=fun_getarticle(self)
    #print(f[0])
    #print(f[1])
    sleep(1)
    #check the element by its xpath in turn from the outside excel file
    for j in range(8):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----发现页面推荐tab里文章元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorArticleUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----发现页面推荐tab里文章元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(1)
    return(True)

#********************************************************************
#Name:fun_getcart
#Purpose:从外部excel文件读取惊喜页面购物车页面需要检查的元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回惊喜页面购物车页面需要检查的元素名称和元素ID两个列表
#Example:N/A
#Modified history:2018/08/28
#********************************************************************

def fun_getcart(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/cartUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,10):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_cartui_check
#Purpose:判断惊喜页面购物车页面的各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/28
#*******************************************************************************************************
def fun_cartui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:惊喜页面购物车页面的各个元素是否存在')
    sleep(2)
    f=fun_getcart(self)
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(9):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----惊喜页面购物车页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorCartUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----惊喜页面购物车页面元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(2)
    return(True)

#********************************************************************
#Name:fun_getpgc
#Purpose:从外部excel文件读取发现页面资讯tab下的需要检查的pgc元素名称和元素ID
#Parameters:入口参数无
#Outputs:返回发现页面资讯tab下的需要检查的pgc元素名称和元素ID
#Example:N/A
#Modified history:2018/08/30
#********************************************************************
def fun_getpgc(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/pgcUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[2]
    st1=workbook.sheet_by_name('SheetiOSstg')
    listM=[]
    listF=[]
    for i in range(1,7):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************************************************************
#Name:fun_pgcui_check
#Purpose:判断发现页面资讯tab下的pgc的元素名称和元素ID的各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/30
#*******************************************************************************************************
def fun_pgcui_check(self):
    driver=self.driver
    print('Common_检查用户模式登录APP，检查点:发现页面资讯tab下的pgc的各个元素是否存在')
    sleep(2)
    f=fun_getpgc(self)
    sleep(2)
    #check the element by its xpath in turn from the outside excel file
    for j in range(6):
        xpaths=driver.find_elements_by_xpath(f[0][j])
        if len(xpaths) == 0:
            print('----发现页面资讯tab下的pgc的元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorPgcUI_R.png'
            driver.get_screenshot_as_file(sf)
            #return(False)
        else:
            print('----发现页面资讯tab下的pgc的元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(2)
    return(True)

#********************************************************************
#Name:fun_getjingxiloginmenu
#Purpose:从外部excel文件读取惊喜页面的商品详细页面需要检查的元素名称和元素xpath
#Parameters:入口参数无
#Outputs:返回惊喜页面的商品详细页面需要检查的元素名称和元素xpath两个列表
#Example:N/A
#Modified history:2018/09/17
#********************************************************************
def fun_getjingxiloginmenu(self):
    workbook = xlrd.open_workbook('../../test_data/UI_data/surpriseloginUI.xls')
    sheet_names= workbook.sheet_names()
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
    listM=[]
    listF=[]
    for i in range(1,5):
        xpath_checked=str(st1.cell(i,0).value)
        #print('xpath'+str(i)+':'+xpath_checked)
        listM.append(xpath_checked)
        func=str(st1.cell(i,1).value)
        listF.append(func)
    sleep(2)
    #print(listM)
    #print(listF)
    return (listM, listF)

#*******************************************************
#Name:bp_deleteaddress
#Purpose:删除个人信息里的所有地址
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/12/04
#*******************************************************
def bp_deleteaddress(self):
    driver=self.driver
    print('Common_检查手机号码登录APP，检查点:删除个人信息里的所有地址信息')
    sleep(1)
    #我的
    driver.find_element_by_accessibility_id('我的').click()
    sleep(3)
    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="SamSTG"]').click()
    sleep(2)
    #编辑个人信息
    driver.find_element_by_accessibility_id('编辑个人信息').click()
    sleep(15)
    #我的地址
    driver.find_element_by_accessibility_id('我的地址').click()
    sleep(2)
    default=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="默认地址"]')
    while len(default) != 0:
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="删除"]').click()
        sleep(1)
        driver.switch_to.alert.accept()
        sleep(1)
        default=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="默认地址"]')
    """
    else:
        print('----无任何地址信息！')
        return(True)
    """
    print('----此时无任何地址信息！')
    sleep(1)
    driver.find_element_by_accessibility_id('all page back black icon').click()
    sleep(1)
    driver.find_element_by_accessibility_id('all page back black icon').click()
    sleep(1)
    driver.find_element_by_accessibility_id('full screen back icon').click()
    sleep(1)
