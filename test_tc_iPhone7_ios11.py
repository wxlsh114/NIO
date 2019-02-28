#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhone7
#version:iOS11.3.1
#author: Sam Wang
#update date: created by Sam [2018-11-21]

import unittest
import time
import os
import random
from time import sleep

from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction

from HTMLTestReportEN import HTMLTestRunner

from common_iPhone7_ios11 import fun_myfansui_check
from common_iPhone7_ios11 import fun_mywatchui_check
from common_iPhone7_ios11 import fun_mypublishui_check
from common_iPhone7_ios11 import bp_is_loggedin
from common_iPhone7_ios11 import fun_getinfo
from common_iPhone7_ios11 import bp_normalloginmp
from common_iPhone7_ios11 import bp_is_loginshow
from common_iPhone7_ios11 import fun_getloginmenu
from common_iPhone7_ios11 import bp_is_plusexist
from common_iPhone7_ios11 import bp_is_publishnowexist
from common_iPhone7_ios11 import bp_is_openmultichatexist
from common_iPhone7_ios11 import fun_findui_check
from common_iPhone7_ios11 import fun_personalinfoui_check
from common_iPhone7_ios11 import fun_scoredetailui_check
from common_iPhone7_ios11 import fun_giftui_check
from common_iPhone7_ios11 import fun_articleui_check
from common_iPhone7_ios11 import fun_cartui_check
from common_iPhone7_ios11 import fun_pgcui_check
#from common_iPhone7_ios11 import fun_articledetailui_check
#from common_iPhone7_ios11 import fun_giftorderui_check
#from common_iPhone7_ios11 import fun_giftorderdetailui_check
from common_iPhone7_ios11 import fun_getjingxiloginmenu

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Weilai_test(unittest.TestCase):


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['browserName']=''
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '11.3'
        desired_caps['deviceName'] = 'iPhone7B'
        desired_caps['app'] = os.path.abspath('../../test_data/app/ios_package/NextevCarInhouseQA.ipa')
        desired_caps['udid'] = '538a602ef0730186afc7c89cd6b38120409114f2'
        desired_caps['noReset'] = True
        #desired_caps['clearSystemFiles'] = True
        desired_caps['xcodeOrgId'] = 'L8MRL9B64V'
        #desired_caps['xcodeSigning'] = 'iPhone Developer'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()

#*******************************************************
#TC Name:test_wode_fans_tc001
#Purpose:检查我的页面点击粉丝后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/13]
#*******************************************************
    def test_wode_fans_tc001(self):
        driver=self.driver
        print('TC_检查用户模式打开APP，检查点:我的_粉丝功能----step1检查我的页面点击粉丝后页面各个元素是否存在')
        print('step2取消互相关注/关注；step3检查被取消互相关注/关注的粉丝关系是否变成+关注/互相关注')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        #粉丝
        #driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[5]').click()
        driver.find_element_by_accessibility_id('粉丝').click()
        sleep(3)
        #检查粉丝面的各个元素是否存在
        c1=fun_myfansui_check(self)
        sleep(2)
        if c1 == True:
            print('粉丝页面上各个被检查元素都检查完毕')
            sleep(1)
            #取消互相关注
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            #...
            driver.find_element_by_accessibility_id('icon more white').click()
            sleep(1)
            driver.find_element_by_accessibility_id('取消关注').click()
            sleep(1)
            #check the message of toast
            n1=driver.find_elements_by_accessibility_id('取消成功')
            if len(n1) != 0:
                print('取消关注的功能检查通过--聊天-->关注')
                sleep(1)
            else:
                print('取消关注的功能检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorCancelWatch_R_tc001.png'
                driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('full screen back icon').click()
            sleep(2)
            #+关注
            driver.find_element_by_accessibility_id('关注').click()
            sleep(1)
            #check the message of toast
            n2=driver.find_elements_by_accessibility_id('关注成功')
            if len(n2) != 0:
                print('+关注的功能检查通过--关注-->聊天')
                sleep(1)
            else:
                print('+关注的功能检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorPlusWatch_R_tc001.png'
                driver.get_screenshot_as_file(sf2)
            sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_watch_tc002
#Purpose:检查我的页面点击关注后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/10]
#*******************************************************
    def test_wode_watch_tc002(self):
        driver=self.driver
        print('TC_检查用户模式打开APP，检查点:我的_关注功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2检查取消关注是否成功；step3检查加关注是否成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        #关注
        driver.find_element_by_accessibility_id('关注').click()
        #driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[4]').click()
        sleep(3)
        #检查发布关注面的各个元素是否存在
        c1=fun_mywatchui_check(self)
        sleep(2)
        if c1==True:
            print('关注页面上各个被检查元素都正常显示.')
            sleep(2)
            #取消关注
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            #...
            driver.find_element_by_accessibility_id('icon more white').click()
            sleep(1)
            driver.find_element_by_accessibility_id('取消关注').click()
            sleep(1)
            #check the toast
            n=driver.find_elements_by_accessibility_id('取消成功')
            if len(n) != 0:
                print('取消互相关注的功能检查通过--聊天-->关注')
                sleep(1)
            else:
                print('取消互相关注的功能检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorCancelMuCare_R_tc002.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            driver.find_element_by_accessibility_id('full screen back icon').click()
            sleep(2)
            #+关注
            driver.find_element_by_accessibility_id('关注').click()
            sleep(1)
            m=driver.find_elements_by_accessibility_id('关注成功')
            if len(m) != 0:
                print('+关注的功能检查通过--关注-->聊天')
                sleep(1)
            else:
                print('+关注的功能检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorAddCare_R_tc002.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            """
            #-关注
            driver.find_element_by_accessibility_id('已关注').click()
            sleep(1)
            m2=driver.find_elements_by_accessibility_id('取消成功')
            if len(m2) != 0:
                print('取消关注的功能检查通过--已关注-->关注')
                sleep(1)
            else:
                print('取消关注的功能检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorCancelCare_R_tc002.png'
                driver.get_screenshot_as_file(sf1)
            sleep(1)
            """
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_publish_tc003
#Purpose:检查我的页面点击发布后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/10]
#*******************************************************
    def test_wode_publish_tc003(self):
        driver=self.driver
        print('TC_检查用户模式打开APP，检查点:我的_发布功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2发布功能是否正常；step3检查发布内容里是否可以一次最大上传9张图片；step4检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(2)
        #发布
        #driver.find_element_by_accessibility_id('发布').click()
        driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[3]').click()
        sleep(2)
        #检查发布页面的各个元素是否存在
        c1=fun_mypublishui_check(self)
        sleep(2)
        if c1==True:
            print('发布页面上各个被检查元素都正常显示.')
            sleep(1)
            #发布
            #driver.find_element_by_ios_predicate('type==XCUIElementTypeButton AND name=="icon camera"').click()
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon camera"]').click()
            sleep(3)
            #+
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":55, "y":264})
            sleep(2)
            #好
            allow=driver.find_elements_by_accessibility_id('好')
            if len(allow) != 0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(2)
            sleep(1)
            try:
                for i in range(9):
                    #driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="compose guide check box defaul"]')[i].click()
                    driver.find_elements_by_ios_predicate('name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                driver.find_element_by_accessibility_id('完成(9/9)').click()
                sleep(2)
                word=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('I love Shanghai_评论_'+now0)
                t0='I love Shanghai_评论_'+now0
                sleep(1)
                driver.find_element_by_accessibility_id('发布').click()
                sleep(9)
                #ios doesn't need to refresh
                #check numbers of pictures and published text here
                title=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,t0)]')
                sleep(2)
                #print(t0)
                if len(title) != 0 :
                    print('发布内容的文字检查通过')
                    sleep(1)
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPublishText_R_tc003.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)
                number=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="9"]')
                #print(number.text)
                if len(number) != 0:
                    print('发布内容的上传9张图片检查通过')
                    sleep(1)
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R_tc003.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(1)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(1)
            except Exception as e:
                print('发生异常：'+str(e))
                sleep(1)
                pass
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginmp_tc004
#Purpose:检查用户用手机号+验证码重新登录app的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/13]
#*******************************************************
    def test_wode_loginmp_tc004(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的页面里用手机号码重新登录，如果已登录先退出账号----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择用手机号+验证码登录；step4检查登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('客户重新登录账号----开始:'+now)
        f=fun_getinfo(self)
        sleep(2)
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":67, "y":100})
        sleep(1)
        mobile_no=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        mobile_no.click()
        sleep(1)
        mobile_no.send_keys(f[0])
        sleep(1)
        code=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
        code.click()
        sleep(1)
        code.send_keys(f[1])
        #code.send_keys('112233')
        #完成
        #driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        sleep(1)
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="注册/登录"]').click()
        sleep(7)
        #driver.swipe(50,300,50,700,1000)
        #sleep(2)
        name=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="Sam8202"]')
        if len(name) != 0:
            print('登录成功！')
            sleep(1)
        else:
            print('登录失败！')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf='../../test_report/ios/'+now+'_errornormalLogin_R_tc004.png'
            driver.get_screenshot_as_file(sf)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_客户重新登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_visitor_tc005
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/13]
#*******************************************************
    def test_wode_visitor_tc005(self):
        driver=self.driver
        print('TC_访客模式点击我的页面各个菜单，检查点:点击我的页面各个菜单是否跳转到用户登录页面----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3点击我的页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面;step5点击加入蔚来跳转页面是否正常显示;step6点击设置弹出页面是否正常显示;')
        print('step7用原来账号和验证码重新登录app')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_访客模式点击我的页面各个菜单跳转页面----开始:'+now)
        sleep(4)
        bp_is_loggedin(self)
        sleep(2)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(2)
        menu_name=fun_getloginmenu(self)
        sleep(1)
        #check the menu by turn
        for j in range(1,9):
            menu=driver.find_element_by_accessibility_id(menu_name[j])
            menu.click()
            sleep(2)
            print('检查的菜单名称：'+menu_name[j])
            bp_is_loginshow(self)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
        driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":550,"toX":50,"toY":250,"duration":1.0})
        sleep(2)
        #加入蔚来
        driver.find_element_by_accessibility_id('加入蔚来').click()
        sleep(9)
        #所有职位
        tl=driver.find_elements_by_xpath('//XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[4]')
        if len(tl) == 0:
            print('访客模式点击加入蔚来跳转页面不正常，请检查')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='../../test_report/ios/'+now+'_errorJoinNIO_R_tc005.png'
            driver.get_screenshot_as_file(sf0)
        else:
            print('访客模式点击加入蔚来跳转页面正常显示')
        sleep(2)
        driver.find_element_by_accessibility_id('返回“蔚来Test”').click()
        sleep(2)
        #设置
        driver.find_element_by_accessibility_id('设置').click()
        sleep(2)
        out=driver.find_elements_by_accessibility_id('退出登录')
        if len(out) != 0:
            print('访客模式点击设置跳转页面不正常，请检查')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorSettings_R_tc005.png'
            driver.get_screenshot_as_file(sf1)
        else:
            print('访客模式点击设置跳转页面正常显示')
        sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_访客模式点击我的页面各个菜单跳转页面----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnow_tc006
#Purpose:检查发现页面的发布功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/17]
#*******************************************************
    def test_faxian_publishnow_tc006(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻功能----step1检查发现首页右上角+号是否存在')
        print('step2检查发布此刻按钮是否存在；step3发布功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片')
        print('step5检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻----开始:'+now)
        sleep(4)
        #发现
        #driver.find_element_by_accessibility_id('发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #发此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                driver.find_element_by_accessibility_id('发此刻').click()
                sleep(2)
                #driver.find_element_by_xpath('//xxxx').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':55, 'y':264})
                sleep(3)
                #好
                allow=driver.find_elements_by_accessibility_id('好')
                if len(allow) != 0:
                    driver.find_element_by_accessibility_id('好').click()
                    sleep(2)
                try:
                    for i in range(9):
                        driver.find_elements_by_ios_predicate('name=="compose guide check box defaul"')[i].click()
                        sleep(1)
                    sleep(1)
                    driver.find_element_by_accessibility_id('完成(9/9)').click()
                    sleep(3)
                    words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                    sleep(2)
                    if len(words) != 0:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].send_keys('I love Shanghai:'+now0)
                        t0='I love Shanghai:'+now0
                        sleep(1)
                        print(t0)
                        driver.find_element_by_accessibility_id('发布').click()
                        sleep(8)
                        #check numbers of pictures and published text here
                        title=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,t0)]')
                        sleep(2)
                        if len(title) != 0:
                            print('发布内容的文字检查通过')
                            sleep(1)
                        else:
                            print('发布内容的文字检查失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf1='../../test_report/ios/'+now+'_errorText_R_tc006.png'
                            driver.get_screenshot_as_file(sf1)
                        sleep(2)
                        number=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="9"]')
                        if len(number) != 0:
                            print('发布内容的上传9张图片检查通过')
                            sleep(1)
                        else:
                            print('发布内容的上传9张图片检查失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf2='../../test_report/ios/'+now+'_errorPic9_R_tc006.png'
                            driver.get_screenshot_as_file(sf2)
                        sleep(2)
                    else:
                        print('发布文字框没有获取，请重新尝试')
                        sleep(2)
                except Exception as e:
                    print('发生异常：'+str(e))
                    sleep(1)
                    pass
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            print('TC_发现_发布此刻----结束:'+now)

#*******************************************************
#TC Name:test_wode_deletepublished_tc007
#Purpose:检查我的页面的删除已发布内容的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/17]
#*******************************************************
    def test_wode_deletepublished_tc007(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的——删除已发布的内容---step1点击我的页面发布;step2检查是否有已发布的内容,')
        print('有的话点击它进入详细页面再点击右上角按钮，执行删除动作;step3检查被删除的发布内容是否删除成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_删除已发布的内容----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(2)
        driver.find_element_by_accessibility_id('发布').click()
        #driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[3]').click()
        sleep(3)
        p=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if len(p) != 0:
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="Sam8202"]')[0].click()
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(1)
            #删除
            driver.find_element_by_accessibility_id('删除').click()
            sleep(1)
            #确认
            driver.find_element_by_accessibility_id('确认').click()
            sleep(1)
            ch=driver.find_elements_by_accessibility_id('删除成功')
            if len(ch) == 0:
                print('发布的内容删除失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorDeleted_R_tc007.png'
                driver.get_screenshot_as_file(sf1)
            else:
                print('发布的内容删除成功')
            sleep(1)
        else:
            print('没有已发布的内容可以删除！')
        sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_删除已发布的内容----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwechat_tc008
#Purpose:检查用户能否用微信账号登录app
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/17]
#*******************************************************
    def test_wode_loginwechat_tc008(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的页面里用微信登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微信登录；step4检查微信登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(1)
        #登录页面
        driver.find_element_by_accessibility_id('注册/登录').click()
        sleep(1)
        #微信登录
        btn=driver.find_elements_by_accessibility_id('log in wechat icon')
        if len(btn) != 0:
            print('微信登录按钮存在')
            driver.find_element_by_accessibility_id('log in wechat icon').click()
            sleep(7)
            #driver.find_element_by_accessibility_id('确认登录').click()
            #sleep(5)
            name=driver.find_elements_by_accessibility_id('王若妍')
            if len(name) != 0:
                print('微信登录成功！')
                sleep(1)
            else:
                print('微信登录失败！')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWechat_R_tc008.png'
                driver.get_screenshot_as_file(sf0)
            sleep(1)
        else:
            print('微信登录按钮不存在，请检查原因')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R_tc008.png'
            driver.get_screenshot_as_file(sf1)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwebo_tc009
#Purpose:检查用户能否用微博账号登录app
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/17]
#*******************************************************
    def test_wode_loginwebo_tc009(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的页面里用微博登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微博登录；step4检查微博登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        driver.find_element_by_accessibility_id('注册/登录').click()
        sleep(1)
        #微博登录
        btn=driver.find_elements_by_accessibility_id('log in microblog icon')
        if len(btn) != 0:
            print('微博登录按钮存在')
            driver.find_element_by_accessibility_id('log in microblog icon').click()
            sleep(4)
            driver.find_element_by_accessibility_id('确认').click()
            sleep(6)
            name=driver.find_elements_by_accessibility_id('Sam8202')
            if len(name) != 0:
                print('微博登录成功！')
                sleep(1)
            else:
                print('微博登录失败！')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWebo_R_tc009.png'
                driver.get_screenshot_as_file(sf0)
        else:
            print('微博登录按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R_tc009.png'
            driver.get_screenshot_as_file(sf1)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tabcheck_tc010
#Purpose:检查发现页面tab上元素和推荐、此刻子tab页上元素是否存在
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/16]
#*******************************************************
    def test_faxian_tabcheck_tc010(self):
        driver=self.driver
        print('TC_检查用户模式打开APP，检查点:发现_tabUI检查功能----step1检查发现页面tab上各子tab元素是否存在;')
        print('step2检查推荐子tab页上各元素是否存在;step3检查此刻子tab页上各元素是否存在')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----开始:'+now)
        sleep(4)
        for i in range(7):
            driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":550,"toX":50,"toY":50,"duration":1.0})
            sleep(2)
        driver.execute_script("mobile: dragFromToForDuration",{"fromX":350,"fromY":450,"toX":350,"toY":50,"duration":1.0})
        #driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        #检查发现页面的各个元素是否存在
        c1=fun_findui_check(self)
        if c1 == True:
            print('发现页面tab上各子tab元素检查通过')
        else:
            print('发现页面tab上各子tab元素检查失败，请检查原因')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_personalinfo_tc011
#Purpose:我的个人信息页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/16]
#*******************************************************
    def test_wode_personalinfo_tc011(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:个人信息页面上元素UI检查和相关元素的功能检查----step1进入个人信息页面；')
        print('step2个人信息页面上元素UI检查;step3检查点击头像的功能;step4检查昵称和简称是否可以编辑;step5检查性别是否')
        print('可以改变;step6检查常驻地区页面是否可以进入;step7检查地址管理页面是否可以进入;step8检查用户隐私条款页面')
        print('是否可以进入;step9检查修改的个人信息是否可以保存成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        driver.find_element_by_accessibility_id('Sam8202').click()
        sleep(2)
        #编辑个人信息
        driver.find_element_by_accessibility_id('编辑个人信息').click()
        sleep(2)
        #检查发布页面的各个元素是否存在
        c1=fun_personalinfoui_check(self)
        sleep(2)
        if c1 == True:
            print('个人信息页面上各个被检查元素都正常显示.')
            sleep(1)
            #点击头像
            head=driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton')
            head.click()
            sleep(2)
            #拍照
            ph=driver.find_elements_by_accessibility_id('拍照')
            if len(ph) != 0:
                print('拍照按钮存在')
                driver.find_element_by_accessibility_id('拍照').click()
                sleep(1)
                #好
                allow=driver.find_elements_by_accessibility_id('好')
                if len(allow) != 0:
                    driver.find_element_by_accessibility_id('好').click()
                    sleep(2)
                phbtn=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="PhotoCapture"]')
                if len(phbtn) != 0:
                    print('手机相机已正常弹出')
                    sleep(1)
                else:
                    print('手机相机没有正常弹出，请检查原因')
                sleep(1)
                driver.find_element_by_accessibility_id('取消').click()
                sleep(1)
            else:
                print('拍照按钮不存在，请检查')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(2)
            #从手机相册选择
            pic=driver.find_elements_by_accessibility_id('从手机相册选择')
            if len(pic) != 0:
                print('从手机相册选择按钮存在')
                driver.find_element_by_accessibility_id('从手机相册选择').click()
                sleep(1)
                #好
                allow=driver.find_elements_by_accessibility_id('好')
                if len(allow) != 0:
                    driver.find_element_by_accessibility_id('好').click()
                    sleep(2)
                picbtn=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="照片"]')
                if len(picbtn) != 0:
                    print('手机相册可以正常调用')
                    sleep(1)
                else:
                    print('手机相册不可以正常调用，请检查原因')
                sleep(1)
                driver.find_element_by_accessibility_id('取消').click()
                sleep(1)
            else:
                print('从手机相册选择按钮不存在，请检查')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(2)
            #取消
            can=driver.find_elements_by_accessibility_id('取消')
            if len(can) != 0:
                print('取消按钮存在')
                driver.find_element_by_accessibility_id('取消').click()
                sleep(2)
            else:
                print('取消按钮不存在，请检查')
            sleep(2)
            #昵称
            nick=driver.find_element_by_xpath('//XCUIElementTypeTextField[@value="Sam8202"]')
            nick.click()
            sleep(1)
            #focused=true;
            c1=driver.find_elements_by_accessibility_id('清除文本')
            if len(c1) != 0:
                print('昵称可以被编辑')
            else:
                print('昵称不可以被编辑，请检查原因')
            sleep(2)
            driver.find_element_by_accessibility_id('清除文本').click()
            sleep(1)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(1)
            driver.find_element_by_accessibility_id('确定').click()
            sleep(2)
            #编辑个人信息
            driver.find_element_by_accessibility_id('编辑个人信息').click()
            sleep(2)
            #简介
            """
            intro=driver.find_element_by_xpath('//XCUIElementTypeTextField[@value="测试D"]')
            intro.click()
            sleep(1)
            c2=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="清除文本"]')
            if len(c2) != 0:
                print('简介可以被编辑')
            else:
                print('简介不可以被编辑，请检查原因')
            sleep(1)
            #完成
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":331, "y":382})
            sleep(1)
            """
            #性别
            man=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="default address not choose"]')[0]
            woman=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="default address not choose"]')[1]
            #checked=true
            c_man=man.get_attribute('value')
            c_woman=woman.get_attribute('value')
            if c_man == '1':
                woman.click()
                sleep(1)
                print('用户性别可以从男改变成女')
                sleep(1)
            else:
                man.click()
                sleep(1)
                print('用户性别可以从女改变成男')
            sleep(2)
            #地区
            driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="地区"]').click()
            sleep(3)
            ct=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="天津市"]')
            if len(ct) != 0:
                print('常驻地区页面可以进入')
            else:
                print('常驻地区页面不可以进入，请检查原因')
            sleep(1)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
            #我的地址
            driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="我的地址"]').click()
            sleep(3)
            addr=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="默认地址"]')
            if len(addr) != 0:
                print('地址管理页面可以进入')
            else:
                print('地址管理页面没有默认地址，请添加新地址')
            sleep(1)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
            #保存
            #driver.find_element_by_xpath('//XCUIElementTypeButton[@name="保存"]').click()
            driver.find_element_by_accessibility_id('保存').click()
            sleep(1)
            save=driver.find_elements_by_accessibility_id('保存成功')
            if len(save) != 0:
                print('----修改的个人信息可以保存成功')
                sleep(1)
            else:
                print('----修改的个人信息没有保存成功，请检查')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf='../../test_report/ios/'+now+'_errorSaveInfo_R_tc011.png'
                driver.get_screenshot_as_file(sf)
            sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_products_tc013
#Purpose:惊喜页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*******************************************************
    def test_jingxi_products_tc013(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:惊喜页面上元素UI检查----step1惊喜页面上任意礼品的元素UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----开始:'+now)
        sleep(4)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        #惊喜页面的各个元素是否存在
        c1=fun_giftui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素都检查完毕')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_instuninstversioncheck_tc015
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/16]
#*******************************************************
    def test_wode_instuninstversioncheck_tc015(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:兼容性测试：安装和卸载app功能----step1卸载app')
        print('step2检查app是否存在；step3重新安装app；step4检查app是不是最新/所需版本')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app功能----开始:'+now)
        sleep(4)
        #home
        #driver.find_element_by_accessibility_id('我的').click()
        #sleep(2)
        #卸载app
        driver.remove_app('com.do1.WeiLaiApp.inhouse')
        sleep(3)
        #check if app is uninstalled
        c=driver.is_app_installed('com.do1.WeiLaiApp.inhouse')
        sleep(1)
        if c == True:
            print('卸载蔚来app失败，请检查原因')
        else:
            print('卸载蔚来app成功')
            sleep(2)
            #install app
            d=os.path.abspath(os.path.join(os.getcwd(), "../.."))
            driver.install_app(d+'/test_data/app/ios_package/NextevCarInhouseQA.ipa')
            sleep(3)
            driver.launch_app()
            sleep(5)
            #允许
            allow=driver.find_elements_by_accessibility_id('允许')
            if len(allow) != 0:
                driver.find_element_by_accessibility_id('允许').click()
                sleep(2)
            allow=driver.find_elements_by_accessibility_id('允许')
            if len(allow) != 0:
                driver.find_element_by_accessibility_id('允许').click()
                sleep(2)
            #我的
            driver.find_element_by_accessibility_id('我的').click()
            sleep(2)
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
            sleep(2)
            #设置
            driver.find_element_by_accessibility_id('设置').click()
            sleep(2)
            n=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="3.0.5 build:2077"]')
            if len(n) != 0:
                print('重新安装app后版本检查通过')
                sleep(1)
            else:
                print('重新安装app后版本检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf='../../test_report/ios/'+now+'_errorVersonCheck_R_tc015.png'
                driver.get_screenshot_as_file(sf)
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_scores_tc016
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/16]
#*******************************************************
    def test_wode_scores_tc016(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:积分明细页面上元素UI检查和相关元素的功能检查----step1进入积分明细页面；')
        print('step2页面上元素UI检查;step3检查点击积分规则按钮的功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[2]').click()
        sleep(3)
        #检查积分明细页面的各个元素是否存在
        c1=fun_scoredetailui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素都检查完毕')
            sleep(1)
            #点击？号
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="integration rule"]').click()
            sleep(3)
            #拍照
            t=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="积分规则"]')
            if len(t) != 0:
                print('积分规则页面存在')
                sleep(1)
            else:
                print('积分规则页面不存在，请检查')
            sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_remarkfriend_tc018
#Purpose:朋友页面对好友设置备注并检查备注是否生效
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_pengyou_remarkfriend_tc018(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:对好友设置备注并检查备注是否生效----step1从朋友页面进入朋友列表页面')
        print('step2选择一个朋友进入朋友详细信息页面；step3检查点击设置备注按钮的功能;step4检查备注是否生效')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----开始:'+now)
        sleep(4)
        #朋友
        driver.find_element_by_accessibility_id('朋友').click()
        sleep(5)
        driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        f=driver.find_elements_by_class_name('XCUIElementTypeCell')
        sleep(2)
        if len(f) >= 2:
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            old=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            sleep(1)
            driver.find_element_by_accessibility_id('icon more white').click()
            sleep(2)
            combtn=driver.find_elements_by_accessibility_id('设置备注')
            sleep(1)
            if len(combtn) != 0:
                driver.find_element_by_accessibility_id('设置备注').click()
                sleep(2)
                edit=driver.find_element_by_class_name('XCUIElementTypeTextField')
                edit.click()
                sleep(1)
                edit.clear()
                sleep(1)
                edit.send_keys(old+'的备注')
                sleep(1)
                driver.find_element_by_accessibility_id('保存').click()
                sleep(3)
                #print(old)
                #print(old+'的备注')
                cc=driver.find_elements_by_accessibility_id(old+'的备注')
                sleep(2)
                if len(cc) != 0:
                    print('好友的备注设置已经生效')
                    sleep(1)
                else:
                    print('好友的备注设置没有生效，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorRemark_R_tc018.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)   
            else:
                print('设置备注的按钮不存在，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorNoRemark_R_tc018.png'
                driver.get_screenshot_as_file(sf2)
                sleep(1)
                driver.find_element_by_accessibility_id('取消').click()
                sleep(2)
            driver.find_element_by_accessibility_id('full screen back icon').click()
            sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
        else:
            print('没有好友可以设置备注，请先添加好友')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/ios/'+now+'_errorNoFriend_R_tc018.png'
            driver.get_screenshot_as_file(sf3)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_article_tc019
#Purpose:发现页面推荐tab里文章元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/23]
#*******************************************************
    def test_faxian_article_tc019(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现页面推荐tab里文章元素UI检查和评论的功能检查----step1从发现页面推荐tab页找到一个文章')
        print('step2文章详情页面上元素UI检查;step3检查点击评论按钮的功能;step4检查发表评论成功后文章详情顶部的评论内容')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----开始:'+now)
        sleep(4)
        #发现
        #driver.find_element_by_accessibility_id('发现').click()
        #sleep(2)
        for i in range(3):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':400,'toX':50,'toY':100,'duration':1.0})
            sleep(2)
        driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        #检查文章的各个元素是否存在
        c1=fun_articleui_check(self)
        sleep(2)
        if c1 == True:
            print('推荐tab里文章各个被检查元素都检查完毕')
            sleep(2)
            #点击评论
            driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeButton[3]').click()
            sleep(3)
            #driver.find_element_by_accessibility_id('写评论').click()
            driver.find_element_by_xpath('//XCUIElementTypeStaticText[contains(@name,"我也来说~")]').click()
            sleep(2)
            combtn=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
            combtn.click()
            sleep(1)
            now0=time.strftime('%Y-%m-%d %H_%M_%S')
            combtn.send_keys('我用Python评论文章:'+now0)
            sleep(1)
            t0='我用Python评论文章:'+now0
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Send"]').click()
            sleep(3)
            #check published text here
            title=driver.find_elements_by_xpath('//XCUIElementTypeTextView[contains(@value,t0)]')
            #print(len(title))
            if len(title) != 0:
                print('评论的文字检查通过')
                sleep(1)
            else:
                print('评论的文字检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorComment_R_tc019.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
        driver.find_element_by_xpath('//XCUIElementTypeButton[@name="all page back grey icon"]').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_openmultichat_tc020
#Purpose:发现页面发起群聊功能的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_faxian_openmultichat_tc020(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查发现首页右上角+号是否存在；')
        print('step2检查点击+号后发起群聊按钮是否存在；step3发起群聊并发送内容功能是否正常；step4检查发布内容里文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----开始:'+now)
        sleep(4)
        #我的
        #driver.find_element_by_accessibility_id('我的').click()
        #sleep(2)
        #+
        c1=bp_is_plusexist(self)
        if c1 == True:
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #建群聊
            c2=bp_is_openmultichatexist(self)
            if c2 == True:
                driver.find_element_by_accessibility_id('建群聊').click()
                sleep(3)
                #cb=driver.find_elements_by_xpath('//XCUIElementTypeImage[@name="chat_unslected_icon"]')
                cb=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')
                sleep(2)
                for i in range(6):
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[i].click()
                    sleep(1)
                #确定    
                driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
                sleep(2)
                msg=driver.find_element_by_id('chat_input_textView')
                msg.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                msg.send_keys('我用Python群聊:'+now0)
                sleep(1)
                #发送
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Send"]').click()
                sleep(1)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(1)
                #朋友
                driver.find_element_by_accessibility_id('朋友').click()
                sleep(2)
                #检查群聊的发送内容是否正确
                t=driver.find_elements_by_accessibility_id('我用Python群聊:'+now0)
                sleep(2)
                #print(len(t))
                if len(t) != 0:
                    print('群聊的发送内容正确')
                    sleep(1)
                else:
                    print('群聊的发送内容不正确，请检查')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorMultiChatText_R_tc020.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----结束:'+now)

#*******************************************************************
#TC Name:test_pengyou_dismissmultichat_tc021
#Purpose:朋友页面群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************************
    def test_pengyou_dismissmultichat_tc021(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊功能')
        print('step1进入已发起的群聊，检查踢人出群聊的功能是否正常;step2检查邀请朋友加入群聊的功能是否正常')
        print('step3检查解散并退出群聊的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊----开始:'+now)
        sleep(4)
        #朋友
        driver.find_element_by_accessibility_id('朋友').click()
        sleep(5)
        #群聊
        mul=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"群聊")]')
        if len(mul) != 0:
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"群聊")]')[0].click()
            sleep(2)
            #...
            driver.find_element_by_accessibility_id('im btn more').click()
            sleep(4)
            #-
            #driver.find_element_by_xpath('//XCUIElementTypeImage[@value="chat_delete_icon"]').click()
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":54, "y":327})
            sleep(2)
            name1=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(1)
            driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(3)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
            #检查是否已被移出群组
            r_msg=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"被踢出群组")]')
            sleep(1)
            #'你将'+name1+'移出群组'
            if len(r_msg) != 0:
                print('踢人出群聊的功能检查通过')
                sleep(1)
            else:
                print('踢人出群聊的功能检查没有通过，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorKickoff_R_tc021.png'
                driver.get_screenshot_as_file(sf1)
            sleep(1)
            #...
            driver.find_element_by_accessibility_id('im btn more').click()
            sleep(2)
            #+
            #driver.find_element_by_xpath('//XCUIElementTypeImage[@value="chat_add_icon"]').click()
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":232, "y":236})
            sleep(2)
            name2=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            sleep(1)
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(1)
            driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(4)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(3)
            #检查是否已被邀请加入群组
            #'你邀请'+name2+'加入了群组':if notes added, it could be wrong
            a_msg=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"加入了群组")]')
            sleep(1)
            #print(name2)
            if len(a_msg) != 0:
                print('邀请朋友加入群聊的功能检查通过')
                sleep(1)
            else:
                print('邀请朋友加入群聊的功能检查没有通过，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorJoin_R_tc021.png'
                driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('im btn more').click()
            sleep(2)
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':200,'duration':1.0})
            sleep(2)
            #解散并删除
            driver.find_element_by_accessibility_id('解散并删除').click()
            sleep(1)
            driver.find_element_by_accessibility_id('确定').click()
            sleep(4)
            #检查解散的群聊是否还存在
            title1=driver.find_elements_by_accessibility_id('群聊')
            if len(title1) == 0:
                print('解散并退出群聊的功能检查通过')
                sleep(1)
            else:
                print('解散并退出群聊的功能检查没有通过，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/ios/'+now+'_errorDismissMultiChat_R_tc021.png'
                driver.get_screenshot_as_file(sf3)
            sleep(2)
        else:
            print('没有群聊可以操作，请先发起群聊')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='../../test_report/ios/'+now+'_errorNoMultiChat_R_tc021.png'
            driver.get_screenshot_as_file(sf4)
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_add2basket_tc022
#Purpose:检查惊喜页面用户添加商品到购物车的功能测试
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*********************************************************************************************
    def test_jingxi_add2basket_tc022(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面用户添加商品到购物车的功能----step1进入惊喜页面')
        print('step2翻页找到所需兑换的商品；step3把商品加入购物车；step4点击购物车图标进入购物车页面')
        print('step5购物车页面UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(4)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        u=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]')
        if len(u) != 0:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]').click()
            sleep(9)
            page=driver.page_source
            sleep(2)
            #加入购物车
            add2b=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="加入购物车"]')
            sleep(2)
            if len(add2b) != 0:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(3)
                driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(3)
                #点击购物车图标
                ###driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="1"])').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':76, 'y':632})
                sleep(6)
                #检查购物车页面ui
                chk=fun_cartui_check(self)
                if chk == True:
                    print('购物车页面UI检查成功')
                    sleep(1)
                else:
                    print('购物车页面UI检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorCartUI_R_tc022.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)
                #37,41
                ###driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':41})
                sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':40})
            sleep(2)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':40})
            sleep(2)
        else:
            print('需要兑换的商品不存在，请重新挑选')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_basket2exchange_tc023
#Purpose:检查惊喜页面从购物车下单兑换商品的功能
#Pre-c#OS:iOS
#Device:iPhone7
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*********************************************************************************************
    def test_jingxi_basket2exchange_tc023(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:惊喜_用户从购物车下单兑换商品的功能----step1进入惊喜页面')
        print('step2点击购物车图标进入购物车页面；step3点击编辑按钮进入编辑页面；step4改变所选商品的规格：颜色')
        print('step5改变所选商品的数量;step6改变收货地址;step7立即下单检查订单是否已提交')
        print('step8查看订单检查商品状态是否为未发货')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(4)
        #此刻
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        #点击购物车图标
        #283,41
        driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther').click()
        sleep(6)
        #refresh
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':100,'toX':50,'toY':500,'duration':1.0})
        #sleep(2)
        chk0=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"去添加点什么吧")]')
        sleep(2)
        if len(chk0) != 0:
            print('购物车里没有商品，请先去惊喜页面添加')
            sleep(1)
        else:
            #print('Yes')
            sleep(1)
            #检查购物车页面ui
            chk=fun_cartui_check(self)
            if chk == True:
                print('购物车页面UI检查成功')
                sleep(2)
                #285,43
                driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="编辑"]')[4].click()
                sleep(6)
                try:
                    #改变商品数量
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':334, 'y':275})
                    sleep(3)
                    #完成
                    driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="完成"]')[4].click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('立即购买').click()
                    sleep(3)
                    #改变收货地址
                    ###driver.find_element_by_xpath('//XCUIElementTypeOther[contains(@name,"赵子龙")]').click()
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':289, 'y':139})
                    sleep(2)
                    #第二个地址
                    driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('立即下单').click()
                    sleep(1)
                    driver.find_element_by_accessibility_id('确定').click()
                    sleep(3)
                    chk=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="订单已提交"]')
                    sleep(1)
                    if len(chk) == 0:
                        print('订单已提交检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftOrder_R_tc023.png'
                        driver.get_screenshot_as_file(sf1)
                        sleep(2)
                    else:
                        print('订单已提交检查通过')
                        sleep(2)
                        #查看订单
                        driver.find_element_by_accessibility_id('查看订单').click()
                        sleep(6)
                        #检查商品状态
                        chk1=driver.find_elements_by_xpath('//XCUIElementTypeOther[contains(@name,"FE冠军系列手机壳")]')
                        chk2=driver.find_elements_by_xpath('//XCUIElementTypeOther[contains(@name,"已付款")]')
                        sleep(1)
                        if len(chk1) != 0 and len(chk2) != 0:
                            print('订单里商品状态检查通过')
                            sleep(1)
                        else:
                            print('订单里商品状态检查失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf1='../../test_report/ios/'+now+'_errorGiftStatus_R_tc023.png'
                            driver.get_screenshot_as_file(sf1)
                        sleep(2)
                except Exception as e:
                    print('发生异常：'+str(e))
                    sleep(2)
                    pass
            else:
                print('购物车页面UI检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorCartUI_R_tc023.png'
                driver.get_screenshot_as_file(sf1)
                sleep(2)
        driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':41})
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_用户从购物车下单兑换商品的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_checkin_tc025
#Purpose:我的页面点击签到及检查当日签到积分是否能正常获得的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_wode_checkin_tc025(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查我的页面右上角点击签到是否存在；')
        print('step2检查点击签到功能是否正常；step3到积分明细页面检查当日签到的积分是否已经获得')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(2)
        #点击签到accessibility_id('点击签到')
        chk=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="点击签到"]')
        if len(chk) != 0:
            driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="点击签到"]').click()
            sleep(2)
        else:
            print('今日已经签到过，请明日再来')
        sleep(1)
        #检查积分
        driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[2]').click()
        sleep(2)
        cb=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="每日签到"]')
        #print(len(cb))
        nowtm=time.strftime('%Y.%m.%d')
        tm=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name, nowtm)]')
        sleep(1)
        if len(cb) != 0 and len(tm) != 0:
            print('每日签到获取积分功能检查通过')
            sleep(1)
        else:
            print('每日签到获取积分功能检查失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/ios/'+now+'_errorCheckinScore_R_tc025.png'
            driver.get_screenshot_as_file(sf2)
        sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_nicknameheadicon_tc028
#Purpose:朋友页面修改群聊昵称和头像功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/22]
#*******************************************************
    def test_pengyou_nicknameheadicon_tc028(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_修改群聊昵称和头像功能---step1检查朋友页面群聊是否存在；')
        print('step2进入群聊修改群组名称；step3检查群组名称是否修改成功')
        #；step4检查修改群组头像功能是否正常
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----开始:'+now)
        sleep(4)
        #朋友
        try:
            driver.find_element_by_accessibility_id('朋友').click()
            sleep(6)
            t=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"群聊")]')
            sleep(1)
            if len(t) != 0:
                driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"群聊")]')[0].click()
                sleep(2)
                driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[contains(@name,"群聊")]/XCUIElementTypeButton[2]').click()
                sleep(2)
                #修改群组名称
                driver.find_element_by_xpath('//XCUIElementTypeStaticText[contains(@name,"群聊")]').click()
                sleep(1)
                edit=driver.find_element_by_class_name('XCUIElementTypeTextField')
                edit.click()
                sleep(1)
                edit.clear()
                sleep(1)
                edit.send_keys('群聊new')
                sleep(1)
                driver.find_element_by_accessibility_id('保存').click()
                sleep(2)
                nk=driver.find_elements_by_accessibility_id('群聊new')
                if len(nk) != 0:
                    print('群组的名称已经修改成功')
                else:
                    print('群组的名称没有修改成功，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorName_R.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(1)
                """
                #修改头像
                driver.find_element_by_accessibility_id('群组头像').click()
                sleep(1)
                #拍照
                driver.find_element_by_accessibility_id('拍照').click()
                sleep(3)
                ok=driver.find_elements_by_accessibility_id('好')
                if len(ok) != 0:
                    driver.find_element_by_accessibility_id('好').click()
                    sleep(2)
                driver.find_element_by_accessibility_id('FrontBackFacingCameraChooser').click()
                sleep(2)
                driver.find_element_by_accessibility_id('PhotoCapture').click()
                sleep(2)
                driver.find_element_by_accessibility_id('使用照片').click()
                sleep(10)
                #修改头像
                driver.find_element_by_accessibility_id('群组头像').click()
                sleep(1)
                #从手机相册选择
                driver.find_element_by_accessibility_id('从手机相册选择').click()
                sleep(2)
                #屏幕快照
                driver.find_element_by_accessibility_id('屏幕快照').click()
                sleep(2)
                for i in range(2):
                    self.driver.execute_script("mobile: scroll", {"direction": "up"})
                    sleep(2)
                driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
                sleep(2)
                #选取
                driver.find_element_by_accessibility_id('选取').click()
                sleep(10)
                """
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(1)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(1)
            else:
                print('没有群聊可以操作，请先发起群聊')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/ios/'+now+'_errorNoMultichat_R_tc028.png'
                driver.get_screenshot_as_file(sf3)
            sleep(2)
        except Exception as e:
            print('发生异常：'+str(e))
            sleep(1)
            pass
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_searchwatch_tc029
#Purpose:朋友页面搜索好友并打开个人主页进行关注
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/21]
#*******************************************************
    def test_pengyou_searchwatch_tc029(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_朋友页面搜索好友并打开个人主页进行关注---')
        print('step1朋友页面点+号，检查添加朋友按钮是否存在；step2输入好友名称进行搜索；')
        print('step3点击搜索出的朋友打开他的个人主页；step4检查关注功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----开始:'+now)
        sleep(4)
        #朋友
        driver.find_element_by_accessibility_id('朋友').click()
        sleep(5)
        driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        #点+号
        driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="朋友列表"]/XCUIElementTypeButton[2]').click()
        sleep(1)
        add=driver.find_elements_by_accessibility_id('添加朋友')
        if len(add) != 0:
            driver.find_element_by_accessibility_id('添加朋友').click()
            sleep(2)
            edit=driver.find_element_by_xpath('//XCUIElementTypeSearchField[@name="昵称/手机号"]')
            edit.click()
            sleep(0.5)
            driver.find_element_by_xpath('//XCUIElementTypeSearchField[@name="昵称/手机号"]').set_value('张三')
            sleep(1)
            #search
            driver.find_element_by_accessibility_id('Search').click()  
            sleep(3)
            ff=driver.find_elements_by_class_name('XCUIElementTypeCell')
            sleep(2)
            #print(len(ff))
            if len(ff) != 0:
                print('搜索好友功能检查通过')
                sleep(1)
                driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
                sleep(4)
                #关注
                t=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="关注"]')
                if len(t) == 2:
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="关注"]')[1].click()
                    sleep(3)
                    tt=driver.find_elements_by_accessibility_id('已关注')
                    if len(tt) != 0:
                        print('好友已经关注成功')
                        sleep(1)
                    else:
                        print('好友没有关注成功，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorWatch_R_tc029.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(1)
                else:
                    print('该好友你以前已经关注过了，无需再操作')
                    sleep(1)
                driver.find_element_by_accessibility_id('full screen back icon').click()
                sleep(2)
                #driver.find_element_by_accessibility_id('all page back black icon').click()
                #sleep(2)
            else:
                print('搜索好友功能检查失败，请检查原因')
                sleep(1)
                #取消
                driver.find_element_by_accessibility_id('取消').click() 
                sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
        else:
            print('没有添加朋友按钮，请检查原因')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/ios/'+now+'_errorNoAddFriend_R_tc029.png'
            driver.get_screenshot_as_file(sf3)
            sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()  
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----结束:'+now)

#*******************************************************
#TC Name:test_wode_resetsecupwd_tc030
#Purpose:我的页面设置里重置服务安全密码的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/22]
#*******************************************************
    def test_wode_resetsecupwd_tc030(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点设置；')
        print('step2点击服务安全密码；step3检查重置服务安全密码的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(2)
        #self.driver.execute_script("mobile: scroll", {"direction": "down"})
        driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":500,"toX":50,"toY":200,"duration":1.0})
        sleep(2)
        driver.find_element_by_accessibility_id('设置').click()
        sleep(2)
        #服务安全密码
        driver.find_element_by_accessibility_id('服务安全密码').click()
        sleep(3)
        code=driver.find_element_by_class_name('XCUIElementTypeTextField')
        code.click()
        code.send_keys('112233')
        sleep(1)
        driver.find_element_by_accessibility_id('下一步').click()
        sleep(2)
        #身份类型
        driver.find_elements_by_class_name('XCUIElementTypeTextField')[0].click()
        sleep(1)
        driver.find_element_by_accessibility_id('确定').click()
        sleep(2)
        idnum=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
        idnum.click()
        idnum.send_keys('340103197301142518')
        sleep(1)
        #完成
        driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        sleep(1)
        #下一步
        driver.find_element_by_accessibility_id('下一步').click()
        sleep(2)
        p=[]
        for i in range(6):
            r=random.randint(0,9)
            p.append(str(r))
        print('重置的密码是：'+str(p))
        sleep(1)
        for j in range(6):
            driver.find_element_by_accessibility_id(p[j]).click()
        sleep(1)
        for j in range(6):
            driver.find_element_by_accessibility_id(p[j]).click()
        sleep(1)
        sleep(2)
        chk=driver.find_elements_by_accessibility_id('重置成功')
        if len(chk) != 0:
            print('服务安全密码重置成功')
            sleep(1)
        else:
            print('服务安全密码重置失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/ios/'+now+'_errorResetSecupwd_R_tc030.png'
            driver.get_screenshot_as_file(sf2)
        sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_addeditaddress_tc031
#Purpose:我的页面里地址管理页面新增和编辑一个收货地址的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/22]
#*******************************************************
    def test_wode_addeditaddress_tc031(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点击头像')
        print('step2点击编辑个人信息；step3点击我的地址进入地址管理页面;step4检查添加新地址的功能是否正常')
        print('step5检查编辑地址的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Sam8202"]').click()
        sleep(2)
        #编辑个人信息
        driver.find_element_by_accessibility_id('编辑个人信息').click()
        sleep(2)
        #我的地址
        driver.find_element_by_accessibility_id('我的地址').click()
        sleep(2)
        #添加新地址
        add=driver.find_elements_by_accessibility_id('添加新地址')
        if len(add) != 0:
            print('添加新地址按钮存在,检查通过')
            sleep(1)
            driver.find_element_by_accessibility_id('添加新地址').click()
            sleep(1)
            name=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
            name.click()
            r=random.randint(10,99)
            sleep(1)
            name.send_keys('测试'+str(r))
            sleep(1)
            pnum=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
            pnum.click()
            r2=random.randint(10,99)
            sleep(1)
            pnum.send_keys('138160328'+str(r2))
            sleep(1)
            #完成
            driver.find_element_by_accessibility_id('Toolbar Done Button').click()
            sleep(1)
            #选择所在地区
            driver.find_element_by_accessibility_id('选择所在地区').click()
            sleep(2)
            #确定
            driver.find_element_by_accessibility_id('确定').click()
            sleep(1)
            #街道/楼牌号等
            addr=driver.find_element_by_class_name('XCUIElementTypeTextView')
            addr.click()
            r3=random.randint(100,999)
            sleep(1)
            addr.send_keys('中山北路'+str(r3)+'号')
            sleep(1)
            #完成
            driver.find_element_by_accessibility_id('Toolbar Done Button').click()
            sleep(1)
            #保存
            driver.find_element_by_accessibility_id('保存').click()
            sleep(1)
            #检查toast
            save1=driver.find_elements_by_accessibility_id('保存成功')
            if len(save1) != 0:
                print('新增地址成功')
            else:
                print('新增地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorAddnewaddr_R_tc031.png'
                driver.get_screenshot_as_file(sf2)
        else:
            print('添加新地址按钮不存在，请检查原因')
            sleep(1)
        #编辑
        edi=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="编辑"]')
        if len(edi) != 0:
            print('编辑按钮存在,检查通过')
            sleep(1)
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="编辑"]').click()
            sleep(1)
            name=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
            name.click()
            #old=name.get_attribute('value')
            r4=random.randint(10,99)
            sleep(1)
            name.send_keys(str(r4))
            sleep(1)
            #保存
            driver.find_element_by_accessibility_id('保存').click()
            sleep(1)
            #检查toast
            save2=driver.find_elements_by_accessibility_id('修改成功')
            if len(save2) != 0:
                print('编辑地址成功')
            else:
                print('编辑地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorEditaddr_R_tc031.png'
                driver.get_screenshot_as_file(sf1)
        else:
            print('编辑按钮不存在，请检查原因')
            sleep(1)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        driver.find_element_by_accessibility_id('full screen back icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershowpic_tc032
#Purpose:发现页面体验tab活动的晒图功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/23]
#*******************************************************
    def test_faxian_expershowpic_tc032(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的晒图功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查晒图功能是否正常;step4检查晒图的文字是否正确')
        print('step5检查晒图的9张图片数量是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----开始:'+now)
        sleep(4)
        #体验
        driver.find_element_by_accessibility_id('体验').click()
        sleep(2)
        driver.find_element_by_xpath('//XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(2)
        for i in range(2):
            driver.execute_script("mobile: dragFromToForDuration",{"fromX":50,"fromY":500,"toX":50,"toY":100,"duration":1.0})
            sleep(2)
        sleep(2)
        driver.find_element_by_accessibility_id('蔚来上海二号店').click()
        sleep(2)
        #徐家汇活动之还未开始
        driver.find_element_by_accessibility_id('徐家汇活动之还未开始').click()
        sleep(4)
        #晒图
        #river.execute_script("mobile: tap", {"touchCount":"1", "x":330, "y":620})
        show=driver.find_elements_by_xpath('//XCUIElementTypeLink[@name="晒图"]')
        sleep(2)
        if len(show) != 0:
            print('晒图按钮存在,检查通过')
            sleep(1)
            driver.find_element_by_xpath('//*[@name="晒图"]').click()
            sleep(2)
            #+
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":65, "y":264})
            sleep(2)
            #好
            allow=driver.find_elements_by_accessibility_id('好')
            if len(allow) != 0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(2)
            for i in range(1,10):
                driver.find_elements_by_ios_predicate('name=="compose guide check box defaul"')[i].click()
                sleep(1)
            driver.find_element_by_accessibility_id('完成(9/9)').click()
            sleep(1)
            word=driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
            word.click()
            sleep(1)
            now0=time.strftime('%Y-%m-%d %H_%M_%S')
            word.send_keys('人生苦短体验晒图:'+now0)
            sleep(1)
            driver.find_element_by_accessibility_id('发布').click()
            sleep(13)
            driver.execute_script("mobile: scroll", {"direction": "down"})
            sleep(2)
            #check numbers of pictures and published text here
            title=driver.find_elements_by_xpath('//XCUIElementTypeTextView[contains(@value,"人生苦短体验晒图:")]')
            sleep(2)
            if len(title) != 0:
                print('体验晒图的文字检查通过')
                sleep(1)
            else:
                print('体验晒图的文字检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorShowpicText_R_tc032.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            number=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="9"]')
            #print(number.text)
            if len(number) != 0:
                print('体验晒图的上传9张图片检查通过')
                sleep(1)
            else:
                print('体验晒图的上传9张图片检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorPic9_R_tc032.png'
                driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(4)
        else:
            print('晒图按钮不存在/找不到，请检查原因')
            sleep(2)
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":32, "y":42})
        #driver.find_element_by_xpath('//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnowatfriend_tc033
#Purpose:检查发现页面的发布此刻并@好友的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/24]
#*******************************************************
    def test_faxian_publishnowatfriend_tc033(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻并@好友的功能----step1检查发现首页右上角+号是否存在；')
        print('step2检查发布此刻按钮是否存在；step3发布并@好友功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片；')
        print('step5检查发布文字是否正确;step6退出当前账号并已@的好友账号登录app;step7检查朋友页面里是否收到@通知')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----开始:'+now)
        sleep(4)
        #发现
        #driver.find_element_by_accessibility_id('//*[@text="发现"]').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #发布此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                print('发此刻按钮存在，检查通过')
                sleep(1)
                driver.find_element_by_accessibility_id('发此刻').click()
                sleep(2)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':55, 'y':264})
                sleep(2)
                #好
                allow=driver.find_elements_by_accessibility_id('好')
                if len(allow) != 0:
                    driver.find_element_by_accessibility_id('好').click()
                    sleep(2)
                sleep(1)
                for i in range(1,10):
                    driver.find_elements_by_ios_predicate('name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                driver.find_element_by_accessibility_id('完成(9/9)').click()
                sleep(1)
                word=driver.find_element_by_xpath('//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('I love China:'+now0)
                sleep(1)
                #@
                driver.find_element_by_accessibility_id('atSome btn').click()
                sleep(1)
                #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':200,'duration':1.0})
                #sleep(2)
                driver.find_element_by_accessibility_id('Sam8198').click()
                sleep(1)
                driver.find_element_by_accessibility_id('发布').click()
                sleep(13)
                #check numbers of pictures and published text here
                title=driver.find_elements_by_xpath('//XCUIElementTypeTextView[contains(@value,"I love China:")]')
                if len(title) != 0:
                    print('发布内容的文字检查通过')
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorText_R_tc033.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)
                number=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="9"]')
                if len(number) != 0:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPic9_R_tc033.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(2)
                #logout
                #我的
                driver.find_element_by_accessibility_id('我的').click()
                sleep(3)
                driver.execute_script('mobile: dragFromToForDuration',{'fromX':250,'fromY':550,'toX':250,'toY':200,'duration':1.0})
                sleep(2)
                #设置
                driver.find_element_by_accessibility_id('设置').click()
                sleep(1)
                driver.find_element_by_accessibility_id('退出登录').click()
                sleep(1)
                driver.find_element_by_accessibility_id('确认').click()
                sleep(2)
                driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':200,'toX':50,'toY':550,'duration':1.0})
                sleep(3)
                #relogin as 'Sam8198'
                #not working now
                #driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="注册/登录"]').click()
                driver.execute_script("mobile: tap", {"touchCount":"1", "x":67, "y":100})
                sleep(2)
                #登录页面
                mobile_no=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
                mobile_no.click()
                sleep(1)
                mobile_no.send_keys('98762648198')
                sleep(1)
                code=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
                code.click()
                sleep(1)
                code.send_keys('112233')
                sleep(1)
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="注册/登录"]').click()
                sleep(7)
                #朋友
                driver.find_element_by_accessibility_id('朋友').click()
                sleep(5)
                #检查好友'Sam8198'是否收到@通知
                fb=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"@了你")]')
                if len(fb) != 0:
                    print('好友收到@通知检查通过')
                else:
                    print('好友收到@通知检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_error#friend_R_tc033.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(2)
                #relogin
                bp_is_loggedin(self)
                sleep(1)
                bp_normalloginmp(self)
                sleep(2)
            else:
                print('发此刻按钮不存在，请检查原因')
                sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcshare_tc034
#Purpose:检查发现页面此刻tab下的ugc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/24]
#*******************************************************
    def test_faxian_ugcshare_tc034(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的分享功能----开始:'+now)
        sleep(4)
        #此刻
        driver.find_element_by_accessibility_id('此刻').click()
        sleep(3)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if len(u) != 0:
            print('UGC存在，检查通过')
            sleep(2)
            #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':200,'duration':1.0})
            #sleep(2)
            driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
            sleep(2)
            #...more icon 原来
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #微信
            wh=driver.find_elements_by_accessibility_id('微信')
            if len(wh) != 0:
                print('分享到微信按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('微信').click()
                sleep(8)
                driver.find_element_by_accessibility_id('王小龙').click()
                sleep(3)
                words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                sleep(2)
                if len(words) != 0:
                    words[0].click()
                    sleep(1)
                    now0=time.strftime('%Y-%m-%d %H_%M_%S')
                    words[0].send_keys('我用Python_UGC微信好友:'+now0)
                    sleep(1)
                #发送
                driver.find_element_by_accessibility_id('发送').click()
                sleep(1)
                driver.find_element_by_accessibility_id('返回蔚来').click()
                sleep(1)
                #检查toast
                save1=driver.find_elements_by_accessibility_id('分享成功')
                if len(save1) != 0:
                    print('分享微信成功')
                else:
                    print('分享微信失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorsharewechat_R_tc034.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(1)
            else:
                print('分享到微信按钮不存在，请检查原因')
            sleep(2)
            #...
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #朋友圈
            pyq=driver.find_elements_by_accessibility_id('朋友圈')
            if len(pyq) != 0:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('朋友圈').click()
                sleep(8)
                word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.send_keys('我用Python_UGC朋友圈:'+now2)
                sleep(1)
                #发表
                driver.find_element_by_accessibility_id('发表').click()
                sleep(1)
                #检查toast
                save2=driver.find_elements_by_accessibility_id('分享成功')
                if len(save2) != 0:
                    print('分享朋友圈成功')
                else:
                    print('分享朋友圈失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R_tc034.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(2)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
                sleep(1)
            #...
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #微博
            wb=driver.find_elements_by_accessibility_id('微博')
            if len(wb) != 0:
                print('分享到微博按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('微博').click()
                sleep(6)
                #发送
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="转发到微博"]').click()
                sleep(1)
                #检查toast
                save3=driver.find_elements_by_accessibility_id('分享成功')
                if len(save3) != 0:
                    print('分享微博成功')
                else:
                    print('分享微博失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/ios/'+now+'_errorsharewebo_R_tc034.png'
                    driver.get_screenshot_as_file(sf3)
                sleep(2)
            else:
                print('分享到微博按钮不存在，请检查原因')
            sleep(2)
            #...
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #我的朋友
            mf=driver.find_elements_by_accessibility_id('我的朋友')
            if len(mf) != 0:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('我的朋友').click()
                sleep(2)
                driver.find_element_by_accessibility_id('朋友').click()
                sleep(2)
                #Sam8201
                driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                sleep(1)
                #发送
                #检查toast
                save4=driver.find_elements_by_accessibility_id('分享成功')
                if len(save4) != 0:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/ios'+now+'_errorsharemyfriend_R_tc034.png'
                    driver.get_screenshot_as_file(sf4)
                sleep(2)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeButton[@name="all page back grey icon"]').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcdel_tc035
#Purpose:检查发现页面此刻tab下的ugc的删除功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/27]
#*******************************************************
    def test_faxian_ugcdel_tc035(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的...按钮；step4检查删除按钮是否存在')
        print('step5检查删除ugc功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的删除功能----开始:'+now)
        sleep(4)
        #此刻
        driver.find_element_by_accessibility_id('此刻').click()
        sleep(3)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if len(u) != 0:
            print('UGC存在，检查通过')
            sleep(2)
            my=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="Sam8202"]')
            sleep(2)
            #print(len(my))
            if len(my) != 0:
                driver.find_element_by_accessibility_id('Sam8202').click()
                sleep(2)
                #和分享按钮合并
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="icon share gray background new"]').click()
                sleep(2)
                #删除
                d=driver.find_elements_by_accessibility_id('删除')
                if len(d) != 0:
                    print('删除按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('删除').click()
                    sleep(1)
                    driver.find_element_by_accessibility_id('确认').click()
                    sleep(1)
                    #检查toast
                    save1=driver.find_elements_by_accessibility_id('删除成功')
                    if len(save1) != 0:
                        print('删除ugc成功')
                    else:
                        print('删除ugc失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorDelUgc_R_tc035.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(2)
                else:
                    print('删除按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('不是本人发布的ugc，没有删除的权限')
                sleep(2)
        else:
            print('UGC不存在,无法执行删除操作')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的删除功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_im_tc036
#Purpose:检查朋友页面IM聊天信息复制、删除、撤回、转发
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/30]
#*******************************************************
    def test_pengyou_im_tc036(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:朋友_IM聊天信息复制、删除、撤回、转发功能----step1朋友页面找到一个朋友发起聊天')
        print('step2发送一条消息；step3检查复制消息功能；step4检查删除消息功能')
        print('step5检查转发消息功能;step6检查撤回消息功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----开始:'+now)
        sleep(4)
        #朋友
        driver.find_element_by_accessibility_id('朋友').click()
        sleep(5)
        driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if len(u) != 0:
            driver.find_elements_by_class_name('XCUIElementTypeCell')[0].click()
            sleep(3)
            #聊天
            driver.find_element_by_accessibility_id('聊天').click()
            sleep(2)
            #发送文本信息
            word=driver.find_element_by_accessibility_id('chat_input_textView')
            word.click()
            sleep(1)
            word.send_keys('测试im')
            sleep(1)
            #发送
            driver.find_element_by_accessibility_id('Send').click()
            sleep(2)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':100, 'y':200})
            sleep(1)
            #长按im
            d=driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="测试im"]')
            driver.execute_script('mobile: touchAndHold',{'element':d,'duration':1.0})
            sleep(1)
            #复制
            cp=driver.find_elements_by_accessibility_id('复制')
            if len(cp) != 0:
                print('复制消息按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('复制').click()
                sleep(1)
                word.click()
                sleep(1)
                driver.execute_script('mobile: touchAndHold',{'element':word,'duration':1.0})
                sleep(1)
                #粘贴
                driver.find_element_by_accessibility_id('粘贴').click()
                sleep(1)
                driver.find_element_by_accessibility_id('Send').click()
                sleep(1)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':100, 'y':200})
                sleep(1)
                #检查
                c=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="测试im"]')
                #print(len(c))
                if len(c) != 1:
                    print('复制消息成功')
                else:
                    print('复制消息失败，请检查原因')
                sleep(2)
            else:
                print('复制消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d=driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="测试im"]')
            driver.execute_script('mobile: touchAndHold',{'element':d,'duration':1.0})
            sleep(1)
            #删除消息
            de=driver.find_elements_by_accessibility_id('删除')
            if len(de) != 0:
                print('删除消息按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('删除').click()
                sleep(1)
                #检查
                c2=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="测试im"]')
                #print(len(c2))
                if len(c2) == 1:
                    print('删除消息成功')
                else:
                    print('删除消息失败，请检查原因')
                sleep(2)
            else:
                print('删除消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d=driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="测试im"]')
            driver.execute_script('mobile: touchAndHold',{'element':d,'duration':1.0})
            sleep(1)
            #转发消息
            de=driver.find_elements_by_accessibility_id('转发')
            if len(de) != 0:
                print('转发消息按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('转发').click()
                sleep(1)
                driver.find_element_by_accessibility_id('朋友').click()
                sleep(1)
                fri=driver.find_elements_by_class_name('XCUIElementTypeCell')
                if len(fri) != 0:
                    #1nd friend
                    driver.find_elements_by_class_name('XCUIElementTypeCell')[1].click()
                else:
                    print('没有其他朋友可以转发消息')
                    sleep(1)
                    driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
            else:
                print('转发消息按钮不存在，请检查原因')
                sleep(2)
            #新发一条im
            word.click()
            sleep(1)
            word.send_keys('测试撤回im')
            sleep(1)
            #发送
            driver.find_element_by_accessibility_id('Send').click()
            sleep(1)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':100, 'y':200})
            sleep(1)
            #长按im
            d=driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="测试撤回im"]')
            driver.execute_script('mobile: touchAndHold',{'element':d,'duration':1.0})
            sleep(1)
            #撤回消息
            wd=driver.find_elements_by_accessibility_id('撤回')
            if len(wd) != 0:
                print('撤回消息按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('撤回').click()
                sleep(1)
                #检查
                w=driver.find_elements_by_accessibility_id('你撤回了一条消息')
                if len(w) != 0:
                    print('撤回消息成功')
                else:
                    print('撤回消息失败，请检查原因')
                sleep(2)
            else:
                print('撤回消息按钮不存在，请检查原因')
                sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(1)
        else:
            print('朋友不存在，无法执行聊天相关操作')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----结束:'+now)
    
#*******************************************************
#TC Name:test_faxian_infopgcshare_tc037
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/29]
#*******************************************************
    def test_faxian_infopgcshare_tc037(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的pgc的分享功能----step1进入发现页面资讯tab')
        print('step2PGC的UI检查；step3进入pgc文章页面点右下角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----开始:'+now)
        sleep(4)
        #此刻
        driver.find_element_by_accessibility_id('资讯').click()
        sleep(3)
        for i in range(4):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':45,'duration':1.0})
            sleep(2)
        #driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        #检查发现页面资讯tab下的pgc的的各个元素是否存在
        c=fun_pgcui_check(self)
        if c == True:
            print('发现页面资讯tab下的pgc的各个被检查元素都检查完毕')
            sleep(1)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if len(u) != 0:
            print('PGC存在，检查通过')
            sleep(2)
            driver.find_element_by_accessibility_id('测试文章改版 - 1').click()
            sleep(6)
            #左上角按钮
            sh=driver.find_elements_by_xpath('(//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[2]')
            if len(sh) != 0:
                print('分享按钮存在，检查通过')
                sleep(2)
                #driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[2]').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':343, 'y':42})
                sleep(2)
                #微信
                wh=driver.find_elements_by_accessibility_id('微信')
                if len(wh) != 0:
                    print('分享到微信按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微信').click()
                    sleep(6)
                    driver.find_element_by_accessibility_id('王小龙').click()
                    sleep(3)
                    words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if len(words) != 0:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].send_keys('人生苦短PGC微信好友:'+now0)
                        sleep(1)
                    #发送
                    driver.find_element_by_accessibility_id('发送').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save1) != 0:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorPGCsharewechat_R_tc037.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                #share
                driver.find_element_by_xpath('//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[2]').click()
                sleep(2)
                #朋友圈
                pyq=driver.find_elements_by_accessibility_id('朋友圈')
                if len(pyq) != 0:
                    print('分享到朋友圈按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('朋友圈').click()
                    sleep(8)
                    word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.send_keys('人生苦短PGC朋友圈:'+now2)
                    sleep(1)
                    #发表
                    driver.find_element_by_accessibility_id('发表').click()
                    sleep(1)
                    #检查toast
                    save2=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save2) != 0:
                        print('分享朋友圈成功')
                        sleep(1)
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorPGCsharewechatpyq_R_tc037.png'
                        driver.get_screenshot_as_file(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[2]').click()
                sleep(2)
                #微博
                wb=driver.find_elements_by_accessibility_id('微博')
                if len(wb) != 0:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微博').click()
                    sleep(6)
                    #发送
                    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save3) != 0:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorPGCsharewebo_R_tc037.png'
                        driver.get_screenshot_as_file(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[2]').click()
                sleep(2)
                #我的朋友
                mf=driver.find_elements_by_accessibility_id('我的朋友')
                if len(mf) != 0:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('我的朋友').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('朋友').click()
                    sleep(2)
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                    sleep(1)
                    #检查toast
                    save4=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save4) != 0:
                        print('分享我的朋友成功')
                        sleep(1)
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorPGCsharemyfriend_R_tc037.png'
                        driver.get_screenshot_as_file(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在，请检查原因')
                sleep(2)
            #driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="测试文章改版 - 1"])[1]/XCUIElementTypeOther[1]').click()
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':32, 'y':42})
            sleep(2)
        else:
            print('PGC不存在，无法执行分享操作')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_experjoin_tc038
#Purpose:发现页面体验tab活动的报名功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_faxian_experjoin_tc038(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的报名功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查报名功能是否正常;step4进入我的->我的活动页面')
        print('step5点击查看行程单;step6检查活动订单里活动的时间是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的报名功能----开始:'+now)
        sleep(4)
        #体验
        driver.find_element_by_accessibility_id('体验').click()
        sleep(4)
        driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(2)
        driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':150,'duration':1.0})
        sleep(2)
        driver.find_element_by_accessibility_id('蔚来上海三号店').click()
        sleep(2)
        driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':400,'toX':50,'toY':100,'duration':1.0})
        sleep(2)
        page=driver.page_source
        sleep(2)
        #自动化测试活动1
        driver.find_element_by_accessibility_id('自动化测试活动1').click()
        sleep(8)
        page=driver.page_source
        sleep(2)
        #报名
        joins=driver.find_elements_by_xpath('//XCUIElementTypeLink[@name="报名"]')
        sleep(2)
        if len(joins) != 0:
            print('报名按钮存在,检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeLink[@name="报名"]').click()
            sleep(4)
            #场次
            #driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="10.28 / 00:00"]').click()
            #sleep(1)
            #driver.find_element_by_xpath('//XCUIElementTypeStaticText[contains(@name,"稍等哈活动")]').click()
            #sleep(2)
            #+限购1张
            #driver.find_element_by_xpath('//XCUIElementTypeButton[@name="+"]').click()
            #sleep(1)
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':350,'fromY':450,'toX':350,'toY':100,'duration':1.0})
            sleep(2)
            #姓名
            name=driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
            name.click()
            name.send_keys('测试员')
            sleep(1)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(1)
            #mobile
            mb=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
            mb.click()
            sleep(1)
            mb.send_keys('18930018802')
            sleep(1)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(3)
            #性别
            """
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="性别"]').click()
            sleep(1)
            #确定
            driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #血型
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="血型"]').click()
            sleep(1)
            #确定
            driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #证件类型
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="证件类型"]').click()
            sleep(1)
            #确定
            driver.find_element_by_xpath('//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #证件号码
            em=driver.find_elements_by_class_name('XCUIElementTypeTextField')[2]
            em.click()
            sleep(1)
            em.send_keys('340103197301142518')
            sleep(1)
            driver.find_element_by_accessibility_id('完成').click()
            sleep(2)
            #driver.find_element_by_class_name('XCUIElementTypeSwitch').click()
            #sleep(1)
            """
            #购买
            driver.find_element_by_accessibility_id('购买').click()
            sleep(1)
            #确认
            driver.find_element_by_accessibility_id('确认').click()
            sleep(3)
            #checking
            ch=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="预约成功"]')
            if len(ch) == 0:
                print('报名失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorJoin_R_tc038.png'
                driver.get_screenshot_as_file(sf1)
                sleep(2)
            else:
                print('报名成功')
                sleep(2)
                driver.find_element_by_accessibility_id('完成').click()
                sleep(4)
                #driver.find_element_by_xpath('//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':30, 'y':22})
                sleep(3)
                #driver.find_element_by_xpath('//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':32, 'y':42})
                sleep(2)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                #driver.execute_script('mobile: tap', {'touchCount':'1', 'x':27, 'y':42})
                sleep(2)
                #我的
                driver.find_element_by_accessibility_id('我的').click()
                sleep(4)
                driver.find_element_by_accessibility_id('我的活动').click()
                sleep(3)
                ch2=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@value,"11月29日")]')
                if len(ch2) != 0:
                    print('活动订单里活动时间检查通过')
                    sleep(1)
                else:
                    print('活动订单里活动时间检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorMyActivity_R_tc038.png'
                    driver.get_screenshot_as_file(sf2)
                    sleep(2)
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="all page back black icon"]').click()
                sleep(2)
        else:
            print('报名按钮不存在，请检查原因')
            sleep(2)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':32, 'y':42})
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的报名功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_canceljoin_tc039
#Purpose:我的页面我的活动里取消报名的功能
#OS:iOS
#Device:iPhone7
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_wode_canceljoin_tc039(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面我的活动里取消报名的功能---step1进入我的->我的活动页面')
        print('step2点击查看行程单；step3检查取消报名按钮是否存在;step4检查取消报名功能是否正常')
        print('step5检查活动订单里是否暂无活动预约')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——我的活动里取消报名的功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(4)
        #我的活动
        driver.find_element_by_accessibility_id('我的活动').click()
        sleep(3)
        ch=driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="取消报名"]')
        if len(ch) != 0:
            print('取消报名按钮存在，检查通过')
            sleep(1)
            driver.find_element_by_accessibility_id('取消报名').click()
            sleep(1)
            #是
            driver.find_element_by_accessibility_id('是').click()
            sleep(1)
            #checking
            ch1=driver.find_elements_by_accessibility_id('取消成功')
            if len(ch1) != 0:
                print('取消报名成功')
                sleep(4)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
                #我的活动
                driver.find_element_by_accessibility_id('我的活动').click()
                sleep(4)
                #暂无活动预约
                ch2=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="自动化测试活动1"]')
                if len(ch2) == 0:
                    print('我的预约活动已取消报名，检查通过')
                    sleep(1)
                else:
                    print('我的预约活动取消报名失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf0='../../test_report/ios/'+now+'_errorActivityList_R.png'
                    driver.get_screenshot_as_file(sf0)
                    sleep(2)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
            else:
                print('取消报名失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorCancel_R_tc039.png'
                driver.get_screenshot_as_file(sf1)
                sleep(2)
        else:
            print('取消报名按钮不存在，请检查原因')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/ios/'+now+'_errorNoCancelJoin_R_tc039.png'
            driver.get_screenshot_as_file(sf2)
            sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——我的活动里取消报名的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershare_tc040
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_faxian_expershare_tc040(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:发现_发现页面体验tab下的活动的分享功能----step1进入发现页面体验tab')
        print('step2找到活动进入；step3检查并点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----开始:'+now)
        sleep(4)
        #体验
        driver.find_element_by_accessibility_id('体验').click()
        sleep(4)
        driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(4)
        for i in range(2):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':100,'duration':1.0})
            sleep(2)
        driver.find_element_by_accessibility_id('蔚来上海二号店').click()
        sleep(2)
        #徐家汇活动之还未开始
        driver.find_element_by_accessibility_id('徐家汇活动之还未开始').click()
        sleep(6)
        page=driver.page_source
        sleep(2)
        #分享图标
        share=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[3]')
        sleep(2)
        if len(share) != 0:
            print('分享按钮存在，检查通过')
            sleep(2)
            #share
            #driver.find_element_by_ios_class_chain('*/XCUIElementTypeOther[2]').click()
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':345, 'y':42})
            sleep(2)
            #微信
            wh=driver.find_elements_by_accessibility_id('微信')
            if len(wh) != 0:
                print('分享到微信按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('微信').click()
                sleep(6)
                driver.find_element_by_accessibility_id('王小龙').click()
                sleep(3)
                words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                sleep(2)
                if len(words) != 0:
                    words[0].click()
                    sleep(1)
                    now0=time.strftime('%Y-%m-%d %H_%M_%S')
                    words[0].send_keys('我用Python_PGC微信好友:'+now0)
                    sleep(1)
                #发送
                driver.find_element_by_accessibility_id('发送').click()
                sleep(2)
                driver.find_element_by_accessibility_id('返回蔚来').click()
                sleep(1)
                #检查toast
                save1=driver.find_elements_by_accessibility_id('分享成功')
                if len(save1) != 0:
                    print('分享微信好友成功')
                    sleep(1)
                else:
                    print('分享微信好友失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPGCsharewechat_R_tc040.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)
            else:
                print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
            #share
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':345, 'y':42})
            sleep(2)
            #朋友圈
            pyq=driver.find_elements_by_accessibility_id('朋友圈')
            if len(pyq) != 0:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(1)
                driver.find_element_by_accessibility_id('朋友圈').click()
                sleep(8)
                word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.send_keys('我用Python_PGC朋友圈:'+now2)
                sleep(1)
                #发表
                driver.find_element_by_accessibility_id('发表').click()
                sleep(1)
                #检查toast
                save2=driver.find_elements_by_accessibility_id('分享成功')
                if len(save2) != 0:
                    print('分享朋友圈成功')
                    sleep(1)
                else:
                    print('分享朋友圈失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPGCsharewechatpyq_R_tc040.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(1)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
            sleep(2)
            #share
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':345, 'y':42})
            sleep(2)
            #微博
            wb=driver.find_elements_by_accessibility_id('微博')
            if len(wb) != 0:
                print('分享到微博按钮存在，检查通过')
                sleep(2)
                driver.find_element_by_accessibility_id('微博').click()
                sleep(6)
                #发送
                driver.find_element_by_xpath('//XCUIElementTypeButton[@name="转发到微博"]').click()
                sleep(1)
                #检查toast
                save3=driver.find_elements_by_accessibility_id('分享成功')
                if len(save3) != 0:
                    print('分享微博成功')
                    sleep(1)
                else:
                    print('分享微博失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/ios/'+now+'_errorPGCsharewebo_R_tc040.png'
                    driver.get_screenshot_as_file(sf3)
                sleep(1)
            else:
                print('分享到新浪微博按钮不存在，请检查原因')
            sleep(2)
            #share
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':345, 'y':42})
            sleep(2)
            #我的朋友
            mf=driver.find_elements_by_accessibility_id('我的朋友')
            if len(mf) != 0:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(1)
                driver.find_element_by_accessibility_id('我的朋友').click()
                sleep(2)
                driver.find_element_by_accessibility_id('朋友').click()
                sleep(2)
                driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                sleep(1)
                #检查toast
                save4=driver.find_elements_by_accessibility_id('分享成功')
                if len(save4) != 0:
                    print('分享我的朋友成功')
                    sleep(1)
                else:
                    print('分享我的朋友失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/ios/'+now+'_errorPGCsharemyfriend_R_tc040.png'
                    driver.get_screenshot_as_file(sf4)
                sleep(1)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(2)
        else:
            print('分享按钮不存在/未找到，请检查原因')
            sleep(2)
        driver.execute_script('mobile: tap', {'touchCount':'1', 'x':30, 'y':42})
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_giftshare_tc041
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_jingxi_giftshare_tc041(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面的商品的分享功能----step1进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----开始:'+now)
        sleep(4)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        u=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]')
        if len(u) != 0:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]').click()
            #u[0].click()
            sleep(8)
            #分享图标
            share=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="横幅"]/XCUIElementTypeOther[2]')
            sleep(2)
            if len(share) != 0:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':338, 'y':58})
                sleep(2)
                #微信
                wh=driver.find_elements_by_accessibility_id('微信')
                if len(wh) != 0:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微信').click()
                    sleep(9)
                    driver.find_element_by_accessibility_id('王小龙').click()
                    sleep(3)
                    words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if len(words) != 0:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].send_keys('我用Python_Gift微信好友:'+now0)
                        sleep(1)
                    #发送
                    driver.find_element_by_accessibility_id('发送').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save1) != 0:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc041.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                #share
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':338, 'y':58})
                sleep(2)
                #朋友圈
                pyq=driver.find_elements_by_accessibility_id('朋友圈')
                if len(pyq) != 0:
                    print('分享到朋友圈按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('朋友圈').click()
                    sleep(8)
                    word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.send_keys('我用Python_Gift朋友圈:'+now2)
                    sleep(1)
                    #发表
                    driver.find_element_by_accessibility_id('发表').click()
                    sleep(1)
                    #检查toast
                    save2=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save2) != 0:
                        print('分享朋友圈成功')
                        sleep(1)
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc041.png'
                        driver.get_screenshot_as_file(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':338, 'y':58})
                sleep(2)
                #微博
                wb=driver.find_elements_by_accessibility_id('微博')
                if len(wb) != 0:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微博').click()
                    sleep(6)
                    #发送
                    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save3) != 0:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc041.png'
                        driver.get_screenshot_as_file(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':338, 'y':58})
                sleep(2)
                #我的朋友
                mf=driver.find_elements_by_accessibility_id('我的朋友')
                if len(mf) != 0:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('我的朋友').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('朋友').click()
                    sleep(2)
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                    sleep(1)
                    #检查toast
                    save4=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save4) != 0:
                        print('分享我的朋友成功')
                        sleep(1)
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc041.png'
                        driver.get_screenshot_as_file(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':24, 'y':58})
            sleep(2)
        else:
            print('需要兑换的商品不存在/未找到，请检查原因')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_visitor_tc042
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:android
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/10]
#*******************************************************
    def test_jingxi_visitor_tc042(self):
        driver=self.driver
        print('TC_访客模式点击我的页面各个菜单，检查点:惊喜_惊喜页面的商品详细页面的访客模式检查----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择一款商品点击进入商品详细页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('惊喜_惊喜页面的商品详细页面的访客模式检查----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(2)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(6)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        u=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]')
        if len(u) != 0:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]').click()
            sleep(8)
            page=driver.page_source
            sleep(2)
            f=fun_getjingxiloginmenu(self)
            sleep(2)
            #check the menu by turn
            for j in range(0,2):
                driver.find_element_by_xpath(f[0][j]).click()
                sleep(2)
                print('检查的元素名称：'+f[1][j])
                sleep(1)
                bp_is_loginshow(self)
                sleep(2)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
            #机器人图标
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':32, 'y':632})
            sleep(2)
            bp_is_loginshow(self)
            sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
            #购物车图标
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':76, 'y':632})
            sleep(2)
            bp_is_loginshow(self)
            sleep(2)
            driver.find_element_by_accessibility_id('all page back black icon').click()
            sleep(2)
            #driver.find_element_by_xpath('//XCUIElementTypeOther[@name="横幅"]/XCUIElementTypeOther[1]').click()
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
            sleep(2)
            driver.find_element_by_accessibility_id('我的').click()
            sleep(3)
            bp_normalloginmp(self)
            sleep(2)
        else:
            print('需要兑换的商品不存在/未找到，请重新挑选')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面的商品详细页面的访客模式检查----结束:'+now)

#************************************************************************************************************
#TC Name:test_jingxi_cartcheck_tc043
#Purpose:检查用户模式选择多款商品加入购物车后购物车图标角标的变化检查
#OS:android
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/10]
#************************************************************************************************************
    def test_jingxi_cartcheck_tc043(self):
        driver=self.driver
        print('TC_用户模式进入惊喜页面，检查点:惊喜_选择多款商品加入购物车后购物车图标角标的变化----step1用户模式进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面；step3点击加入购物车按钮检查购物车图标角标数字是否为1')
        print('step4点击购物车图标进入购物车详细页面，检查左下角是否显示已选(1)')
        print('step5选择第二款商品点击进入商品详细页面;step6点击加入购物车按钮检查购物车图标角标数字是否为2')
        print('step7点击购物车图标进入购物车详细页面，检查左下角是否显示已选(2)')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('惊喜_选择多款商品加入购物车后购物车图标角标的变化检查----开始:'+now)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        u1=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]')
        if len(u1) != 0:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]').click()
            sleep(6)
            page=driver.page_source
            sleep(2)
            add2b=driver.find_elements_by_accessibility_id('加入购物车')
            sleep(2)
            if len(add2b) != 0:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                add2b[0].click()
                sleep(3)
                add2b[0].click()
                sleep(3)
                #购物车角标
                ch1=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="1"]')
                if len(ch1) != 0:
                    print('购物车图标角标数字为1检查成功')
                    sleep(2)
                    #点击购物车图标
                    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="1"]').click()
                    sleep(4)
                    ch1a=driver.find_elements_by_xpath('//XCUIElementTypeOther[contains(@name,"已选(1)")]')
                    if len(ch1a) != 0:
                        print('购物车详细页面左下角显示已选(1)检查通过')
                        sleep(1)
                    else:
                        print('购物车详细页面左下角显示已选(1)检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1a='../../test_report/ios/'+now+'_errorCartGift1a_R_tc043.png'
                        driver.get_screenshot_as_file(sf1a)
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                    sleep(2)
                    u2=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="儿童硅胶餐垫套装 儿童硅胶餐垫套装 1"]')
                    if len(u2) != 0:
                        print('需要兑换的商品2存在，检查通过')
                        sleep(2)
                        driver.find_element_by_xpath('//XCUIElementTypeOther[@name="儿童硅胶餐垫套装 儿童硅胶餐垫套装 1"]').click()
                        sleep(8)
                        page=driver.page_source
                        sleep(2)
                        add2b=driver.find_element_by_accessibility_id('加入购物车')
                        sleep(2)
                        add2b.click()
                        sleep(3)
                        add2b.click()
                        sleep(5)
                        #购物车角标
                        ch1=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="2"]')
                        if len(ch1) != 0:
                            print('购物车图标角标数字为2检查成功')
                            sleep(2)
                            #点击购物车图标
                            driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="2"]').click()
                            sleep(4)
                            ch2a=driver.find_elements_by_xpath('//XCUIElementTypeOther[contains(@name,"已选(2)")]')
                            if len(ch2a) != 0:
                                print('购物车详细页面左下角显示已选(2)检查通过')
                                sleep(1)
                            else:
                                print('购物车详细页面左下角显示已选(2)检查失败，请检查原因')
                                sleep(1)
                                now=time.strftime('%Y-%m-%d %H_%M_%S')
                                sf2a='../../test_report/ios/'+now+'_errorCartGift2a_R_tc043.png'
                                driver.get_screenshot_as_file(sf2a)
                            sleep(2)
                            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                            sleep(2)
                            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                            sleep(2)
                            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                            sleep(2)
                        else:
                            print('购物车图标角标数字为2检查失败，请检查原因')
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf2='../../test_report/ios/'+now+'_errorCartGift2_R_tc043.png'
                            driver.get_screenshot_as_file(sf2)
                        sleep(2)
                    else:
                        print('需要兑换的商品2不存在/未找到，请重新挑选')
                        sleep(2)
                else:
                    print('购物车图标角标数字为1检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorCartGift1_R_tc043.png'
                    driver.get_screenshot_as_file(sf1)
                    sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                sleep(2)
        else:
            print('需要兑换的商品1不存在/未找到，请重新挑选')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_选择多款商品加入购物车后购物车图标角标的变化检查----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_clearcart_tc044
#Purpose:检查用户模式惊喜选择多款商品加入购物车后清空购物车的功能检查
#OS:android
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/10]
#*******************************************************
    def test_jingxi_clearcart_tc044(self):
        driver=self.driver
        print('TC_用户模式进入惊喜页面，检查点:惊喜_选择多款商品加入购物车后清空购物车的功能检查----step1用户模式进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面点击加入购物车按钮')
        print('step3选择第二款商品点击进入商品详细页面点击加入购物车按钮')
        print('step4点击购物车图标进入购物车详细页面，点击编辑，点击全选，再点击删除所选，确定')
        print('step5检查此时购物车是否没有任何商品')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('惊喜_选择多款商品加入购物车后清空购物车的功能检查----开始:'+now)
        #惊喜
        driver.find_element_by_accessibility_id('惊喜').click()
        sleep(8)
        for i in range(8):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        #driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':250,'duration':1.0})
        sleep(2)
        u1=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]')
        if len(u1) != 0:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            driver.find_element_by_xpath('//XCUIElementTypeOther[@name="FE冠军系列手机壳 蔚来FE冠军系列手机壳 1000"]').click()
            sleep(6)
            page=driver.page_source
            sleep(2)
            add2b=driver.find_elements_by_accessibility_id('加入购物车')
            sleep(2)
            if len(add2b) != 0:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                add2b[0].click()
                sleep(3)
                add2b[0].click()
                sleep(3)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                sleep(2)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                sleep(2)
                u2=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="儿童硅胶餐垫套装 儿童硅胶餐垫套装 1"]')
                if len(u2) != 0:
                    print('需要兑换的商品2存在，检查通过')
                    sleep(2)
                    driver.find_element_by_xpath('//XCUIElementTypeOther[@name="儿童硅胶餐垫套装 儿童硅胶餐垫套装 1"]').click()
                    sleep(6)
                    page=driver.page_source
                    sleep(2)
                    add2b=driver.find_element_by_accessibility_id('加入购物车')
                    sleep(2)
                    add2b.click()
                    sleep(3)
                    add2b.click()
                    sleep(3)
                    #点击购物车图标
                    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="2"]').click()
                    sleep(4)
                    ch2a=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="编辑"]')
                    if len(ch2a) != 0:
                        print('编辑按钮存在，检查通过')
                        sleep(2)
                        driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="编辑"]')[4].click()
                        sleep(2)
                        #driver.find_element_by_xpath('//XCUIElementTypeOther[contains(@name,"全选")]').click()
                        driver.execute_script('mobile: tap', {'touchCount':'1', 'x':28, 'y':630})
                        sleep(2)
                        #删除所选
                        driver.find_element_by_accessibility_id('删除所选').click()
                        sleep(1)
                        driver.find_element_by_accessibility_id('确定').click()
                        sleep(3)
                        chk0=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"去添加点什么吧")]')
                        sleep(2)
                        if len(chk0) != 0:
                            print('购物车已清空')
                            sleep(1)
                        else:
                            print('购物车未被清空，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf3='../../test_report/ios/'+now+'_errorCartNoEdit_R_tc044.png'
                            driver.get_screenshot_as_file(sf3)
                            sleep(2)
                            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                            sleep(2)
                    else:
                        print('编辑按钮不存在，检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2a='../../test_report/ios/'+now+'_errorCartNoEdit_R_tc044.png'
                        driver.get_screenshot_as_file(sf2a)
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                    sleep(2)
                else:
                    print('需要兑换的商品2不存在/未找到，请重新挑选')
                    sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
                driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                sleep(2)
        else:
            print('需要兑换的商品1不存在/未找到，请重新挑选')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_选择多款商品加入购物车后清空购物车的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_activityshow_tc046
#Purpose:检查用户模式点击我的页面各个菜单的预期动作
#OS:android
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/15]
#*******************************************************
    def test_wode_activityshow_tc046(self):
        driver=self.driver
        print('TC_用户模式点击我的我的活动菜单，检查点:我的_我的活动晒图功能检查----')
        print('step1进入我的活动页面；step2检查是否有晒图按钮；step3检查晒图功能是否正常')
        print('step4检查晒图的文字是否正确;step5检查晒图的9张图片数量是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的活动晒图功检查----开始:'+now)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(4)
        driver.find_element_by_accessibility_id('我的活动').click()
        sleep(3)
        u=driver.find_elements_by_accessibility_id('晒图')
        if len(u) != 0:
            print('晒图按钮存在，检查通过')
            sleep(2)
            driver.find_element_by_accessibility_id('晒图').click()
            sleep(2)
            #+
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":55, "y":264})
            sleep(2)
            #好
            allow=driver.find_elements_by_accessibility_id('好')
            if len(allow) != 0:
                driver.find_element_by_accessibility_id('好').click()
                sleep(2)
            sleep(1)
            try:
                for i in range(9):
                    #driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="compose guide check box defaul"]')[i].click()
                    driver.find_elements_by_ios_predicate('name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                driver.find_element_by_accessibility_id('完成(9/9)').click()
                sleep(2)
                word=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('我用Python_晒图'+now0)
                t0='我用Python_晒图_'+now0
                sleep(1)
                driver.find_element_by_accessibility_id('发布').click()
                sleep(9)
                driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':550,'toX':50,'toY':50,'duration':1.0})
                sleep(2)
                #check numbers of pictures and published text here
                title=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,t0)]')
                sleep(2)
                if len(title) != 0 :
                    print('晒图的文字检查通过')
                    sleep(1)
                else:
                    print('晒图的文字检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPublishText_R_tc046.png'
                    driver.get_screenshot_as_file(sf1)
                sleep(2)
                number=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="9"]')
                if len(number) != 0:
                    print('晒图的上传9张图片检查通过')
                    sleep(1)
                else:
                    print('晒图的上传9张图片检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R_tc046.png'
                    driver.get_screenshot_as_file(sf2)
                sleep(2)
                driver.find_element_by_accessibility_id('all page back black icon').click()
                sleep(2)
            except Exception as e:
                print('发生异常：'+str(e))
                sleep(2)
                pass
        else:
            print('晒图按钮不存在，请检查原因')
        sleep(2)
        driver.find_element_by_accessibility_id('all page back black icon').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的活动晒图功检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_es8ordershare_tc047
#Purpose:检查我的ES8订单的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_wode_es8ordershare_tc047(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的_我的ES8订单的分享功能----step1进入我的页面')
        print('step2进入我的es8订单点击进入订单详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的ES8订单的分享功能----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(4)
        driver.find_element_by_accessibility_id('我的ES8订单').click()
        sleep(8)
        car=driver.find_elements_by_accessibility_id('ES8基准版')
        if len(car) != 0:
            driver.find_element_by_accessibility_id('ES8基准版').click()
            sleep(4)
            #分享图标
            share=driver.find_elements_by_accessibility_id('navigationbar btn share')
            sleep(2)
            if len(share) != 0:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                driver.find_element_by_accessibility_id('navigationbar btn share').click()
                sleep(2)
                #微信好友
                wh=driver.find_elements_by_accessibility_id('微信好友')
                if len(wh) != 0:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微信好友').click()
                    sleep(6)
                    driver.find_element_by_accessibility_id('王小龙').click()
                    sleep(3)
                    words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if len(words) != 0:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].send_keys('人生苦短我的ES8订单微信好友:'+now0)
                        sleep(1)
                    #发送
                    driver.find_element_by_accessibility_id('发送').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save1) != 0:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc047.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.find_element_by_accessibility_id('navigationbar btn share').click()
                sleep(2)
                #微信朋友圈
                pyq=driver.find_elements_by_accessibility_id('微信朋友圈')
                if len(pyq) != 0:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('微信朋友圈').click()
                    sleep(8)
                    word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.send_keys('人生苦短我的ES8订单微信朋友圈:'+now2)
                    sleep(1)
                    #发表
                    driver.find_element_by_accessibility_id('发表').click()
                    sleep(1)
                    #检查toast
                    save2=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save2) != 0:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc047.png'
                        driver.get_screenshot_as_file(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                driver.find_element_by_accessibility_id('navigationbar btn share').click()
                sleep(2)
                """
                #微博no such menu now
                wb=driver.find_elements_by_accessibility_id('微博')
                if len(wb) != 0:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微博').click()
                    sleep(6)
                    #发送
                    driver.find_element_by_accessibility_id('发送').click()
                    sleep(1)
                    #检查toast
                    save3=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save3) != 0:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc047.png'
                        driver.get_screenshot_as_file(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                """
                #share
                driver.find_element_by_accessibility_id('navigationbar btn share').click()
                sleep(2)
                #NIO好友
                mf=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name="NIO好友"]')
                if len(mf) != 0:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="NIO好友"]').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('朋友').click()
                    sleep(1)
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                    sleep(1)
                    #检查toast
                    save4=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save4) != 0:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc047.png'
                        driver.get_screenshot_as_file(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            #driver.execute_script('mobile: tap', {'touchCount':'1', 'x':24, 'y':58})
            driver.find_element_by_accessibility_id('navigationbar btn back black1').click()   
            sleep(2)
        else:
            print('暂无订单，无法执行该脚本')
            sleep(2)
        driver.find_element_by_accessibility_id('navigationbar btn back black1').click()   
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的ES8订单的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_joinnio_tc048
#Purpose:检查我的页面加入蔚来功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_wode_joinnio_tc048(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:我的_我的_加入蔚来----step1进入我的页面')
        print('step2进入加入蔚来页面；step3点击蔚来总部；step4点击软件开发')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_加入蔚来----开始:'+now)
        sleep(4)
        #我的
        driver.find_element_by_accessibility_id('我的').click()
        sleep(3)
        driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':200,'duration':1.0})
        sleep(2)
        driver.find_element_by_accessibility_id('加入蔚来').click()
        sleep(6)
        page=driver.page_source
        sleep(2)
        #蔚来总部
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":388, "y":249})
        ###driver.find_element_by_xpath('//XCUIElementTypeOther[@name="NIO"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]').click()
        sleep(5)
        #软件开发
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":388, "y":347})
        ###driver.find_element_by_xpath('//XCUIElementTypeOther[@name="NIO"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]').click()
        sleep(4)
        #允许
        allow=driver.find_elements_by_accessibility_id('允许')
        if len(allow) != 0:
            driver.find_element_by_accessibility_id('允许').click()
            sleep(2)
        #好
        allow2=driver.find_elements_by_accessibility_id('好')
        if len(allow2) != 0:
            driver.find_element_by_accessibility_id('好').click()
            sleep(2)                                
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='../../test_report/ios/'+now+'_devJobs_R_tc048.png'
        driver.get_screenshot_as_file(sf1)
        sleep(3)
        driver.find_element_by_accessibility_id('返回').click()
        sleep(2)
        driver.find_element_by_accessibility_id('返回“蔚来Test”').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_加入蔚来----结束:'+now)

#*******************************************************
#TC Name:test_aiche_cityplan_tc049
#Purpose:检查爱车页面里查询上海市城市服务规划
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_cityplan_tc049(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:爱车_查询上海市城市服务规划----step1进入爱车页面')
        print('step2点击城市服务查询页面；step3选择山西省->太原市;step4检查太原市城市服务规划是否显示正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_查询太原市城市服务规划----开始:'+now)
        sleep(4)
        #爱车
        driver.find_element_by_accessibility_id('爱车').click()
        sleep(5)
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":188, "y":613})
        sleep(2)
        for i in range(3):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        city=driver.find_elements_by_accessibility_id('城市服务查询')
        if len(city) != 0:
            print('城市服务查询按钮找到')
            sleep(2)
            driver.find_element_by_accessibility_id('城市服务查询').click()
            sleep(4)
            driver.find_element_by_accessibility_id('上海市').click()
            sleep(2)
            driver.find_element_by_accessibility_id('山西省').click()
            sleep(2)
            driver.find_element_by_accessibility_id('太原市').click()
            sleep(4)
            #代客上牌
            ch1=driver.find_elements_by_accessibility_id('NIO城市服务规划')
            ch2=driver.find_elements_by_accessibility_id('太原市')
            ch3=driver.find_elements_by_accessibility_id('代客上牌')
            if len(ch1) != 0 and len(ch2) != 0 and len(ch3) != 0:
                print('太原市城市服务规划显示正常')
                sleep(1)
            else:
                print('太原市城市服务规划显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errSHcityplan_R_tc049.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            driver.find_element_by_accessibility_id('nav back btn').click()
            sleep(2)
        else:
            print('城市服务查询按钮未找到/不存在，请检查原因')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_查询太原市城市服务规划----结束:'+now)

#*******************************************************
#TC Name:test_aiche_rechargemap_tc050
#Purpose:检查爱车页面里查询充电地图及查看充电桩信息
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_rechargemap_tc050(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图及查看充电桩信息----step1进入爱车页面')
        print('step2点击充电地图；step3点击一个充电桩;step4检查充电桩信息是否显示正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_充电地图及查看充电桩信息----开始:'+now)
        sleep(4)
        #爱车
        driver.find_element_by_accessibility_id('爱车').click()
        sleep(6)
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":188, "y":613})
        sleep(2)
        for i in range(4):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        cmap=driver.find_elements_by_accessibility_id('充电地图')
        if len(cmap) != 0:
            print('充电地图按钮找到')
            sleep(2)
            driver.find_element_by_accessibility_id('充电地图').click()
            sleep(4)
            page=driver.page_source
            sleep(2)
            #driver.find_element_by_id('cn.com.weilaihui3:id/charging_pile_drag_view').click()
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":268, "y":239})
            sleep(4)
            ch1=driver.find_elements_by_accessibility_id('上海曹安景林苑充电站')
            if len(ch1) != 0:
                print('充电桩信息显示正常')
                sleep(1)
            else:
                print('充电桩信息显示不正常，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errPileStatus_R_tc050.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            driver.find_element_by_accessibility_id('routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_充电地图及查看充电桩信息----结束:'+now)

#*******************************************************
#TC Name:test_aiche_milecalculator_tc051
#Purpose:检查爱车页面里ES8里程计算器
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_milecalculator_tc051(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:爱车_ES8里程计算器----step1进入爱车页面')
        print('step2点击ES8里程计算器；step3改变行驶速度;step4改变车外温度;step5打开空调;step6改变轮毂尺寸检查里程计算是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_ES8里程计算器----开始:'+now)
        sleep(4)
        #爱车
        driver.find_element_by_accessibility_id('爱车').click()
        sleep(6)
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":188, "y":613})
        sleep(2)
        for i in range(3):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        cmap=driver.find_elements_by_accessibility_id('ES8里程计算器')
        if len(cmap) != 0:
            print('ES8里程计算器按钮找到')
            sleep(2)
            driver.find_element_by_accessibility_id('ES8里程计算器').click()
            sleep(4)
            page=driver.page_source
            sleep(2)
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':530,'toX':50,'toY':503,'duration':1.0})
            sleep(2)
            #改变行驶速度
            #>
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':324, 'y':373})
            sleep(1)
            res1=driver.find_elements_by_accessibility_id('393')
            if len(res1) != 0:
                print('改变行驶速度后里程计算正确')
                sleep(1)
            else:
                print('改变行驶速度后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errMileV_R_tc051.png'
                driver.get_screenshot_as_file(sf1)
            sleep(2)
            #改变车外温度>
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':175, 'y':476})
            sleep(1)
            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':175, 'y':476})
            sleep(1)
            res2=driver.find_elements_by_accessibility_id('387')
            if len(res2) != 0:
                print('改变车外温度后里程计算正确')
                sleep(1)
            else:
                print('改变车外温度后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errMileTemp_R_tc051.png'
                driver.get_screenshot_as_file(sf2)
            sleep(2)
            #打开空调
            driver.find_element_by_accessibility_id('OFF').click()
            sleep(1)
            res3=driver.find_elements_by_accessibility_id('309')
            if len(res3) != 0:
                print('打开空调后里程计算正确')
                sleep(1)
            else:
                print('打开空调后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/ios/'+now+'_errMileAir_R_tc051.png'
                driver.get_screenshot_as_file(sf3)
            sleep(2)
            #改变轮毂尺寸
            driver.find_element_by_accessibility_id('21英寸').click()
            sleep(1)
            res4=driver.find_elements_by_accessibility_id('301')
            if len(res4) != 0:
                print('改变轮毂尺寸后里程计算正确')
                sleep(1)
            else:
                print('改变轮毂尺寸后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf4='../../test_report/ios/'+now+'_errMileDem_R_tc051.png'
                driver.get_screenshot_as_file(sf4)
            sleep(2)
            driver.find_element_by_accessibility_id('nav back btn').click()
            sleep(2)
        else:
            print('ES8里程计算器按钮未找到/不存在，请检查原因')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_ES8里程计算器----结束:'+now)

#*******************************************************
#TC Name:test_aiche_es8content_tc052
#Purpose:检查爱车页面ES8配置表浏览及分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_es8content_tc052(self):
        driver=self.driver
        print('TC_检查手机号码登录APP，检查点:爱车_ES8配置表浏览及分享功能----step1进入爱车页面')
        print('step2进入ES8配置表；step3点右上角的分享按钮（先检查是否存在)；step4检查分享微信好友功能是否正常')
        print('step5检查分享微信朋友圈功能是否正常;step6检查分享微博好友功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_ES8配置表浏览及分享功能----开始:'+now)
        sleep(4)
        #爱车
        driver.find_element_by_accessibility_id('爱车').click()
        sleep(6)
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":188, "y":613})
        sleep(2)
        for i in range(3):
            driver.execute_script('mobile: dragFromToForDuration',{'fromX':50,'fromY':500,'toX':50,'toY':50,'duration':1.0})
            sleep(2)
        driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        cmap=driver.find_elements_by_accessibility_id('ES8配置表')
        if len(cmap) != 0:
            print('ES8配置表按钮找到')
            sleep(2)
            #
            driver.find_element_by_xpath('//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[6]').click()
            sleep(6)
            page=driver.page_source
            sleep(2)
            #
            driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="个性化"]').click()
            sleep(3)
            driver.find_element_by_accessibility_id('选装包').click()
            sleep(3)
            driver.find_element_by_accessibility_id('附件').click()
            sleep(3)
            #分享图标
            share=driver.find_elements_by_accessibility_id('nav share btn')
            sleep(2)
            if len(share) != 0:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                driver.find_element_by_accessibility_id('nav share btn').click()
                sleep(2)
                #微信好友
                wh=driver.find_elements_by_accessibility_id('微信好友')
                if len(wh) != 0:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微信好友').click()
                    sleep(6)
                    driver.find_element_by_accessibility_id('王小龙').click()
                    sleep(3)
                    words=driver.find_elements_by_xpath('//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if len(words) != 0:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].send_keys('人生苦短我的ES8订单微信好友:'+now0)
                        sleep(1)
                    #发送
                    driver.find_element_by_accessibility_id('发送').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save1) != 0:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc052.png'
                        driver.get_screenshot_as_file(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    driver.find_element_by_accessibility_id('letter btn close').click()
                sleep(2)
                #share
                driver.find_element_by_accessibility_id('nav share btn').click()
                sleep(2)
                #微信朋友圈
                pyq=driver.find_elements_by_accessibility_id('微信朋友圈')
                if len(pyq) != 0:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('微信朋友圈').click()
                    sleep(8)
                    word2=driver.find_element_by_xpath('//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.send_keys('人生苦短我的ES8订单微信朋友圈:'+now2)
                    sleep(1)
                    #发表
                    driver.find_element_by_accessibility_id('发表').click()
                    sleep(1)
                    #检查toast
                    save2=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save2) != 0:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc052.png'
                        driver.get_screenshot_as_file(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    driver.find_element_by_accessibility_id('letter btn close').click()
                sleep(2)
                #share
                driver.find_element_by_accessibility_id('nav share btn').click()
                sleep(2)
                #微博
                wb=driver.find_elements_by_accessibility_id('微博')
                if len(wb) != 0:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    driver.find_element_by_accessibility_id('微博').click()
                    sleep(6)
                    #发送
                    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save3) != 0:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc052.png'
                        driver.get_screenshot_as_file(sf3)
                    sleep(1)
                else:
                    print('分享到微博按钮不存在，请检查原因')
                    sleep(2)
                    driver.find_element_by_accessibility_id('letter btn close').click()
                sleep(2)
                #share
                driver.find_element_by_accessibility_id('nav share btn').click()
                sleep(2)
                #NIO好友
                mf=driver.find_elements_by_accessibility_id('NIO好友')
                if len(mf) != 0:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(1)
                    driver.find_element_by_accessibility_id('NIO好友').click()
                    sleep(2)
                    driver.find_element_by_accessibility_id('朋友').click()
                    sleep(2)
                    driver.find_elements_by_xpath('//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
                    sleep(1)
                    #检查toast
                    save4=driver.find_elements_by_accessibility_id('分享成功')
                    if len(save4) != 0:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc052.png'
                        driver.get_screenshot_as_file(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
                    driver.find_element_by_accessibility_id('letter btn close').click()
                sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            driver.find_element_by_accessibility_id('nav back btn').click()   
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_爱车_ES8配置表浏览及分享功能----结束:'+now)
        
if __name__ == '__main__':unittest.main()
