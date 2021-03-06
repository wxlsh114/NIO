#coding=utf-8
import wda
import unittest
import time
import os
import sys
from time import sleep

import xlrd

c=wda.Client('http://localhost:8100')

sys.path.append('../../')
from HTMLTestReportEN import HTMLTestRunner

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
    print('Common_检查手机号码登录APP，检查点:发现首页右上角的+号是否存在')
    sleep(1)
    s=c.session()
    #发现
    #s(id='发现').click()
    #sleep(2)
    plus=s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]')
    if not plus.exists:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        c.screenshot(sf)
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
    print('Common_检查手机号码登录APP，检查点:点击发现首页右上角的+号后是否存在发布此刻的按钮')
    sleep(1)
    s=c.session()
    #发现
    #s(id='发现').click()
    #sleep(2)
    p_now=s(id='发此刻')
    if not p_now.exists:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        c.screenshot(sf)
        sleep(1)
        print('----发现首页发布此刻不存在！请检查，谢谢！')
    else:
        print('----发现首页发布此刻存在！检查通过！')
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
    print('Common_检查手机号码登录APP，检查点:点击发现首页右上角的+号后是否存在发起群聊的按钮')
    sleep(1)
    s=c.session()
    #发现
    #s(id='发现').click()
    #sleep(2)
    m_chat=s(id='发起群聊')
    if not m_chat.exists:
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorPlus_R.png'
        c.screenshot(sf)
        sleep(1)
        print('----发起群聊不存在！请检查，谢谢！')
    else:
        print('----发起群聊存在！检查通过！')
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
    print('Common_检查手机号码登录APP，检查点:用户是否已经登录了，如果已登录先退出目前账号')
    sleep(1)
    s=c.session()
    #我的
    s(id='我的').click()
    sleep(2)
    login=s(id='注册/登录')
    #print(len(login))
    if not login.exists:
        print('----用户已经登录')
        s.swipe(150,550,150,250,0.5)
        sleep(2)
        #设置
        s(id='设置').click()
        sleep(1)
        s(id='退出登录').click()
        sleep(1)
        s(id='确认').click()
        sleep(2)
        s.swipe(150,250,150,550,0.5)
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
    print('Common_检查访客模式登录APP，检查点:用户登录界面是否正常弹出显示')
    sleep(1)
    s=c.session()
    login=s(id='注册/登录')
    if not login.exists:
        print('----用户登录界面没有正常显示，请检查')
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errorLoginUI_R.png'
        c.screenshot(sf)
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
    print('Common_检查用户模式登录APP，检查点:我的页面点击发布后页面各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getmypublish(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(9):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----我的发布页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyPublishUI_R.png'
            c.screenshot(sf)
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
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
    print('Common_检查用户模式登录APP，检查点:我的页面点击关注后显示页面各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getmywatch(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(6):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----我的关注页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyWatchUI_R.png'
            c.screenshot(sf)
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
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

#*******************************************************
#Name:fun_myfansui_check
#Purpose:判断我的页面点击粉丝后显示页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/02
#*******************************************************
def fun_myfansui_check(self):
    print('Common_检查用户模式登录APP，检查点:我的页面点击粉丝后显示页面各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getmyfans(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(6):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----我的粉丝页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyFansUI_R.png'
            c.screenshot(sf)
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
    print('Common_检查用户模式登录APP，检查点:我的页面点击我的ES8订单后显示页面各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getmyes8order(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(5):
        ids=s(id=f[0][j])
        if not ids.exists:
            print('我的ES8订单页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorMyES8OrderUI_R.png'
            c.screenshot(sf)
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
    print('Common_用手机号+验证码正常登录app')
    sleep(1)
    s=c.session()
    f=fun_getinfo(self)
    sleep(2)
    s.swipe(150,250,150,550,0.5)
    sleep(2)
    #s(id='注册/登录').click()
    s.tap(67,100)
    sleep(2)
    #登录页面
    mobile_no=s(className='XCUIElementTypeTextField')[0]
    mobile_no.click()
    sleep(1)
    mobile_no.set_text(str(f[0]))
    sleep(1)
    code=s(className='XCUIElementTypeTextField')[2]
    code.click()
    sleep(1)
    code.set_text(str(f[1]))
    #code.set_text('112233')
    sleep(1)
    s(xpath='//XCUIElementTypeButton[@name="注册/登录"]').click()
    sleep(6)
    s.swipe(150,250,150,550,0.5)
    sleep(2)
    name=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')
    if name.exists:
        print('登录成功！')
    else:
        print('登录失败！')
        now=time.strftime('%Y%m%d_%H%M%S')
        sf='../../test_report/ios/'+now+'_errornormalLogin_R.png'
        c.screenshot(sf)
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
    listM=[]
    for i in range(0,8):
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
    listM=[]
    listF=[]
    for i in range(1,19):
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
    print('Common_检查用户模式登录APP，检查点:发现页面tab上各个元素和推荐、此刻子tab页上元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getfind(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its id in turn from the outside excel file
    for j in range(5):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----发现页面tab上元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindTabUI_R.png'
            c.screenshot(sf)
            #return(False)
        else:
            print('----发现页面tab上元素：'+f[1][j]+'--检查通过：正常显示')
    sleep(2)
    for k in range(5,12):
        xpaths=s(xpath=f[0][k])
        if not xpaths.exists:
            print('----推荐tab内元素：'+f[1][k]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindRecomUI_R.png'
            c.screenshot(sf)
            sleep(1)
            #return(False)
        else:
            print('----推荐tab内元素：'+f[1][k]+'--检查通过：正常显示')
        sleep(2)
    #此刻
    s(id='此刻').click()
    sleep(2)
    for k in range(12,17):
        xpaths=s(xpath=f[0][k])
        if not xpaths.exists:
            print('----此刻tab内元素：'+f[1][k]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorFindNowUI_R.png'
            c.screenshot(sf)
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
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
#Name:fun_personalinfoui_check
#Purpose:判断个人信息页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/16
#*******************************************************************************************************
def fun_personalinfoui_check(self):
    print('Common_检查用户模式登录APP，检查点:我的页面点击头像后再点击编辑个人信息显示的个人信息页面上各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getpersonalinfo(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its xpath in turn from the outside excel file
    for j in range(8):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----个人信息页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorPersonalInfoUI_R.png'
            c.screenshot(sf)
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
    print('Common_检查用户模式登录APP，检查点:积分明细页面点击头像后再点击编辑个人信息显示的个人信息页面上各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getscoredetail(self)
    #print(f[0])
    #print(f[1])
    sleep(3)
    #check the element by its xpath in turn from the outside excel file
    for j in range(7):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----积分明细页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorScoreDetailUI_R.png'
            c.screenshot(sf)
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

#*******************************************************************************************************
#Name:fun_giftui_check
#Purpose:判断惊喜页面各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/10
#*******************************************************************************************************
def fun_giftui_check(self):
    print('Common_检查用户模式登录APP，检查点:惊喜页面上各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getgift(self)
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(4):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----惊喜页面元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorGiftUI_R.png'
            c.screenshot(sf)
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
#Name:fun_articleui_check
#Purpose:判断发现页面推荐tab里文章的各个元素是否存在
#Parameters:入口参数无
#Outputs:返回True/False值
#Example:N/A
#Modified history:2018/08/23
#*******************************************************************************************************
def fun_articleui_check(self):
    print('Common_检查用户模式登录APP，检查点:发现页面推荐tab里文章的各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getarticle(self)
    #print(f[0])
    #print(f[1])
    sleep(2)
    #check the element by its xpath in turn from the outside excel file
    for j in range(7):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----发现页面推荐tab里文章元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorArticleUI_R.png'
            c.screenshot(sf)
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
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
    print('Common_检查用户模式登录APP，检查点:惊喜页面购物车页面的各个元素是否存在')
    sleep(2)
    s=c.session()
    f=fun_getcart(self)
    sleep(2)
    #check the element by its id in turn from the outside excel file
    for j in range(9):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
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
    st1=workbook.sheet_names()[1]
    st1=workbook.sheet_by_name('SheetiOS')
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
    print('Common_检查用户模式登录APP，检查点:发现页面资讯tab下的pgc的各个元素是否存在')
    sleep(1)
    s=c.session()
    f=fun_getpgc(self)
    sleep(2)
    #check the element by its xpath in turn from the outside excel file
    for j in range(6):
        xpaths=s(xpath=f[0][j])
        if not xpaths.exists:
            print('----发现页面资讯tab下的pgc的元素：'+f[1][j]+'检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errorPgcUI_R.png'
            c.screenshot(sf)
            #return(False)
        else:
            print('----发现页面资讯tab下的pgc的元素：'+f[1][j]+'--检查通过：正常显示')
        sleep(2)
    return(True)

#*******************************************************
#Name:bp_is_initpicexist
#Purpose:判断发现首页闪屏是否存在,如果出现就点击button
#Parameters:入口参数无
#Outputs:无
#Example:N/A
#Modified history:2018/12/10
#*******************************************************
def bp_is_initpicexist(self):
    print('Common_检查手机号码登录APP，检查点:发现首页闪屏是否存在')
    sleep(1)
    s=c.session()
    init=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    if init.exists:
        print('闪屏存在')
        sleep(0.5)
        s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton').click()
    sleep(1)

