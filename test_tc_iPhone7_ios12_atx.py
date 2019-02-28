#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhone7
#version:iOS12.1
#author: Sam Wang
#update date: created by Sam [2018-09-28]

import wda
import unittest
import time
import os
import random
from time import sleep

from HTMLTestReportEN import HTMLTestRunner

from common_iPhone7_ios12_atx import fun_myfansui_check
from common_iPhone7_ios12_atx import fun_mywatchui_check
from common_iPhone7_ios12_atx import fun_mypublishui_check
from common_iPhone7_ios12_atx import bp_is_loggedin
from common_iPhone7_ios12_atx import fun_getinfo
from common_iPhone7_ios12_atx import bp_normalloginmp
from common_iPhone7_ios12_atx import bp_is_loginshow
from common_iPhone7_ios12_atx import fun_getloginmenu
from common_iPhone7_ios12_atx import bp_is_plusexist
from common_iPhone7_ios12_atx import bp_is_publishnowexist
from common_iPhone7_ios12_atx import bp_is_openmultichatexist
from common_iPhone7_ios12_atx import fun_findui_check
from common_iPhone7_ios12_atx import fun_personalinfoui_check
from common_iPhone7_ios12_atx import fun_scoredetailui_check
from common_iPhone7_ios12_atx import fun_giftui_check
from common_iPhone7_ios12_atx import fun_articleui_check
from common_iPhone7_ios12_atx import fun_cartui_check
from common_iPhone7_ios12_atx import fun_pgcui_check
#from common_iPhone7_ios12_atx import fun_getjingxiloginmenu

c=wda.Client('http://localhost:8100')

class Weilai_test(unittest.TestCase):


    def setUp(self):
        sleep(1)

    def tearDown(self):
        # end the session
        sleep(1)

#*******************************************************
#TC Name:test_wode_fans_tc001
#Purpose:检查我的页面点击粉丝后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_fans_tc001(self):
        print('TC_检查用户模式打开APP，检查点:我的_粉丝功能----step1检查我的页面点击粉丝后页面各个元素是否存在')
        print('step2取消互相关注/关注；step3检查被取消互相关注/关注的粉丝关系是否变成+关注/互相关注')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #s=c.session()
        #我的
        s(id='我的').click()
        sleep(3)
        #粉丝
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[5]').click()
        s(id='粉丝').click()
        sleep(2)
        #检查粉丝面的各个元素是否存在
        c1=fun_myfansui_check(self)
        sleep(2)
        if c1 == True:
            print('粉丝页面上各个被检查元素都检查完毕')
            sleep(1)
            #取消互相关注
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            #...
            s(id='icon more white').click()
            sleep(1)
            s(id='取消关注').click()
            sleep(1)
            #check the message of toast
            n1=s(id='取消成功')
            if n1.exists:
                print('取消互相关注的功能检查通过--聊天-->关注')
            else:
                print('取消互相关注的功能检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorCancelWatch_R.png'
                c.screenshot(sf2)
            sleep(1)
            s(id='full screen back icon').click()
            sleep(2)
            #+关注
            s(id='关注').click()
            sleep(1)
            #check the message of toast
            n2=s(id='关注成功')
            if n2.exists:
                print('+关注的功能检查通过--关注-->聊天')
            else:
                print('+关注的功能检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorPlusWatch_R.png'
                c.screenshot(sf2)
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_watch_tc002
#Purpose:检查我的页面点击关注后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_watch_tc002(self):
        print('TC_检查用户模式打开APP，检查点:我的_关注功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2检查取消关注是否成功；step3检查加关注是否成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        #关注
        s(id='关注').click()
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[4]').click()
        sleep(2)
        #检查发布关注面的各个元素是否存在
        c1=fun_mywatchui_check(self)
        sleep(1)
        if c1 == True:
            print('关注页面上各个被检查元素都正常显示.')
            sleep(1)
            #取消关注
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            #...
            s(id='icon more white').click()
            sleep(1)
            s(id='取消关注').click()
            sleep(1)
            #check the toast
            n=s(id='取消成功')
            if n.exists:
                print('取消关注的功能检查通过--聊天-->关注')
            else:
                print('取消关注的功能检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorCancelCare_R.png'
                c.screenshot(sf1)
            sleep(1)
            s(id='full screen back icon').click()
            sleep(2)
            s(id='关注').click()
            sleep(1)
            m=s(id='关注成功')
            if m.exists:
                print('+关注的功能检查通过--关注-->聊天')
            else:
                print('+关注的功能检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorAddCare_R.png'
                c.screenshot(sf1)
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_publish_tc003
#Purpose:检查我的页面点击发布后弹出页面的各项功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_publish_tc003(self):
        print('TC_检查用户模式打开APP，检查点:我的_发布功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2发布功能是否正常；step3检查发布内容里是否可以一次最大上传9张图片；step4检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        #发布
        s(id='发布').click()
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[3]').click()
        sleep(2)
        #检查发布页面的各个元素是否存在
        c1=fun_mypublishui_check(self)
        sleep(2)
        if c1 == True:
            print('发布页面上各个被检查元素都检查完毕')
            sleep(1)
            #发布
            #s(predicate='type==XCUIElementTypeButton AND name=="icon camera"').click()
            s(xpath='//XCUIElementTypeButton[@name="icon camera"]').click()
            sleep(3)
            #+
            s.tap(55,264)
            sleep(2)
            #好
            allow=s(id='好')
            if allow.exists:
                s(id='好').click()
                sleep(2)
            sleep(1)
            try:
                for i in range(9):
                    #s(xpath='//XCUIElementTypeButton[@name="compose guide check box defaul"]')[i].click()
                    s(predicate='name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                s(id='完成(9/9)').click()
                sleep(2)
                word=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.set_text('I love Shanghai_评论_'+now0)
                t0='I love Shanghai_评论_'+now0
                sleep(1)
                s(id='发布').click()
                sleep(9)
                #ios doesn't need to refresh
                #check numbers of pictures and published text here
                title=s(xpath='//XCUIElementTypeStaticText[contains(@name,t0)]')
                sleep(2)
                #print(t0)
                if title.exists :
                    print('发布内容的文字检查通过')
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPublishText_R.png'
                    c.screenshot(sf1)
                sleep(2)
                number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                if number.exists:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R.png'
                    c.screenshot(sf2)
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            except Exception as e:
                print('发生异常：'+str(e))
                sleep(1)
                pass
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginmp_tc004
#Purpose:检查用户用手机号+验证码重新登录app的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_loginmp_tc004(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用手机号码重新登录，如果已登录先退出账号----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择用手机号+验证码登录；step4检查登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('客户重新登录账号----开始:'+now)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        f=fun_getinfo(self)
        sleep(2)
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        s.tap(67,100)
        sleep(1)
        s(className='XCUIElementTypeTextField')[0].click()
        sleep(1)
        s(className='XCUIElementTypeTextField')[0].set_text(str(f[0]))
        sleep(1)
        s(className='XCUIElementTypeTextField')[2].click()
        sleep(1)
        s(className='XCUIElementTypeTextField')[2].set_text(str(f[1]))
        #code.set_text('112233')
        #完成
        #s(id='Toolbar Done Button').click()
        sleep(1)
        s(xpath='//XCUIElementTypeButton[@name="注册/登录"]').click()
        sleep(7)
        #s.swipe(50,300,50,500,0.5)
        #sleep(2)
        name=s(xpath='//XCUIElementTypeStaticText[@name="Sam8202"]')
        if name.exists:
            print('登录成功！')
        else:
            print('登录失败！')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf='../../test_report/ios/'+now+'_errornormalLogin_R.png'
            c.screenshot(sf)
        sleep(1)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_客户重新登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_visitor_tc005
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_visitor_tc005(self):
        print('TC_访客模式点击我的页面各个菜单，检查点:点击我的页面各个菜单是否跳转到用户登录页面----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3点击我的页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面;step5点击加入蔚来跳转页面是否正常显示;step6点击设置弹出页面是否正常显示;')
        print('step7用原来账号和验证码重新登录app')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_访客模式点击我的页面各个菜单跳转页面----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(2)
        #我的
        s(id='我的').click()
        sleep(2)
        menu_name=fun_getloginmenu(self)
        sleep(1)
        #check the menu by turn
        for j in range(1,8):
            menu=s(id=menu_name[j])
            menu.click()
            sleep(2)
            print('检查的菜单名称：'+menu_name[j])
            bp_is_loginshow(self)
            s(id='all page back grey icon').click()
            sleep(2)
        s.swipe(150,550,150,250,0.5)
        sleep(2)
        #加入蔚来
        s(id='加入蔚来').click()
        sleep(9)
        #所有职位
        tl=s(id='返回“蔚来QA”')
        if not tl.exists:
            print('访客模式点击加入蔚来跳转页面不正常，请检查')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='../../test_report/ios/'+now+'_errorJoinNIO_R.png'
            c.screenshot(sf0)
        else:
            print('访客模式点击加入蔚来跳转页面正常显示')
        sleep(2)
        s(id='返回“蔚来QA”').click()
        sleep(2)
        #设置
        s(id='设置').click()
        sleep(2)
        out=s(id='退出登录')
        if out.exists:
            print('访客模式点击设置跳转页面不正常，请检查')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorSettings_R.png'
            c.screenshot(sf1)
        else:
            print('访客模式点击设置跳转页面正常显示')
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_访客模式点击我的页面各个菜单跳转页面----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnow_tc006
#Purpose:检查发现页面的发布功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_publishnow_tc006(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻功能----step1检查发现首页右上角+号是否存在')
        print('step2检查发布此刻按钮是否存在；step3发布功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片')
        print('step5检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #发布此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                s(id='发此刻').click()
                sleep(2)
                #s(xpath='//xxxx').click()
                s.tap(55,264)
                sleep(3)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                    sleep(2)
                try:
                    for i in range(9):
                        s(predicate='name=="compose guide check box defaul"')[i].click()
                        sleep(1)
                    sleep(1)
                    s(id='完成(9/9)').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].set_text('I love Shanghai:'+now0)
                        t0='I love Shanghai:'+now0
                        sleep(1)
                        #print(t0)
                        s(id='发布').click()
                        sleep(9)
                        #check numbers of pictures and published text here
                        title=s(xpath='//XCUIElementTypeStaticText[contains(@name,t0)]')
                        sleep(1)
                        if title.exists:
                            print('发布内容的文字检查通过')
                        else:
                            print('发布内容的文字检查失败，请检查原因')
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf1='../../test_report/ios/'+now+'_errorText_R.png'
                            c.screenshot(sf1)
                        sleep(2)
                        number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                        if number.exists:
                            print('发布内容的上传9张图片检查通过')
                        else:
                            print('发布内容的上传9张图片检查失败，请检查原因')
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf2='../../test_report/ios/'+now+'_errorPic9_R.png'
                            c.screenshot(sf2)
                        sleep(2)
                    else:
                        print('发布文字框没有获取，请重新尝试')
                        sleep(2)
                except Exception as e:
                    print('发生异常：'+str(e))
                    sleep(1)
                    pass
            s.close()
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            print('TC_发现_发布此刻----结束:'+now)

#*******************************************************
#TC Name:test_wode_deletepublished_tc007
#Purpose:检查我的页面的删除已发布内容的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_deletepublished_tc007(self):
        print('TC_检查手机号码登录APP，检查点:我的——删除已发布的内容---step1点击我的页面发布;step2检查是否有已发布的内容,')
        print('有的话点击它进入详细页面再点击右上角按钮，执行删除动作;step3检查被删除的发布内容是否删除成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_删除已发布的内容----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(id='发布').click()
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[3]').click()
        sleep(2)
        p=s(className='XCUIElementTypeCell')
        if p.exists:
            s(xpath='//XCUIElementTypeStaticText[@name="Sam8202"]')[0].click()
            sleep(2)
            s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(1)
            #删除
            s(id='删除').click()
            sleep(1)
            #确认
            s(id='确认').click()
            sleep(1)
            ch=s(id='删除成功')
            if not ch.exists:
                print('发布的内容删除失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorDeleted_R.png'
                c.screenshot(sf1)
            else:
                print('发布的内容删除成功')
            sleep(1)
        else:
            print('没有已发布的内容可以删除！')
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_删除已发布的内容----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwechat_tc008
#Purpose:检查用户能否用微信账号登录app
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_loginwechat_tc008(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微信登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微信登录；step4检查微信登录的账号是否正确')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----开始:'+now)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        g=bp_is_loggedin(self)
        sleep(1)
        #登录页面
        #s(id='注册/登录').click()
        s.tap(67,100)
        sleep(1)
        #微信登录
        btn=s(id='log in wechat icon')
        if btn.exists:
            print('微信登录按钮存在')
            s(id='log in wechat icon').click()
            sleep(7)
            #s(id='确认登录').click()
            #sleep(5)
            name=s(id='Sam8202')
            if name.exists:
                print('微信登录成功！')
            else:
                print('微信登录失败！')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWechat_R.png'
                c.screenshot(sf0)
            sleep(1)
        else:
            print('微信登录按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R.png'
            c.screenshot(sf1)
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwebo_tc009
#Purpose:检查用户能否用微博账号登录app
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_loginwebo_tc009(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微博登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微博登录；step4检查微博登录的账号是否正确')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----开始:'+now)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        #s(id='注册/登录').click()
        s.tap(67,100)
        sleep(1)
        #微博登录
        btn=s(id='log in microblog icon')
        if btn.exists:
            print('微博登录按钮存在')
            s(id='log in microblog icon').click()
            sleep(5)
            s(id='确认').click()
            sleep(7)
            name=s(xpath='//XCUIElementTypeStaticText[@name="Sam8202"]')
            if name.exists:
                print('微博登录成功！')
            else:
                print('微博登录失败！')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWebo_R.png'
                c.screenshot(sf0)
        else:
            print('微博登录按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R.png'
            c.screenshot(sf1)
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tabcheck_tc010
#Purpose:检查发现页面tab上元素和推荐、此刻子tab页上元素是否存在
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_tabcheck_tc010(self):
        print('TC_检查用户模式打开APP，检查点:发现_tabUI检查功能----step1检查发现页面tab上各子tab元素是否存在;')
        print('step2检查推荐子tab页上各元素是否存在;step3检查此刻子tab页上各元素是否存在')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        for i in range(5):
            s.swipe(50,550,50,50,0.5)
            sleep(2)
        s.swipe(50,550,50,295,0.5)
        sleep(2)
        #检查发现页面的各个元素是否存在
        c1=fun_findui_check(self)
        if c1 == True:
            print('发现页面tab上各子tab元素检查通过')
        else:
            print('发现页面tab上各子tab元素检查失败，请检查原因')
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_personalinfo_tc011
#Purpose:我的个人信息页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_personalinfo_tc011(self):
        print('TC_检查手机号码登录APP，检查点:个人信息页面上元素UI检查和相关元素的功能检查----step1进入个人信息页面；')
        print('step2个人信息页面上元素UI检查;step3检查点击头像的功能;step4检查昵称和简称是否可以编辑;step5检查性别是否')
        print('可以改变;step6检查常驻地区页面是否可以进入;step7检查地址管理页面是否可以进入;step8检查用户隐私条款页面')
        print('是否可以进入;step9检查修改的个人信息是否可以保存成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(id='Sam8202').click()
        sleep(2)
        #编辑个人信息
        s(id='编辑个人信息').click()
        sleep(2)
        #检查发布页面的各个元素是否存在
        c1=fun_personalinfoui_check(self)
        sleep(2)
        if c1 == True:
            print('个人信息页面上各个被检查元素都检查完毕')
            sleep(1)
            #点击头像
            head=s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton')
            head.click()
            sleep(2)
            #拍照
            ph=s(id='拍照')
            if ph.exists:
                print('拍照按钮存在')
                s(id='拍照').click()
                sleep(1)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                    sleep(2)
                phbtn=s(xpath='//XCUIElementTypeButton[@name="PhotoCapture"]')
                if phbtn.exists:
                    print('手机相机已正常弹出')
                else:
                    print('手机相机没有正常弹出，请检查原因')
                sleep(1)
                s(id='取消').click()
                sleep(1)
            else:
                print('拍照按钮不存在，请检查')
            sleep(2)
            s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(2)
            #从手机相册选择
            pic=s(id='从手机相册选择')
            if pic.exists:
                print('从手机相册选择按钮存在')
                s(id='从手机相册选择').click()
                sleep(1)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                    sleep(2)
                picbtn=s(xpath='//XCUIElementTypeOther[@name="照片"]')
                if picbtn.exists:
                    print('手机相册可以正常调用')
                else:
                    print('手机相册不可以正常调用，请检查原因')
                sleep(1)
                s(id='取消').click()
                sleep(1)
            else:
                print('从手机相册选择按钮不存在，请检查')
            sleep(2)
            s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(2)
            #取消
            can=s(id='取消')
            if can.exists:
                print('取消按钮存在')
                s(id='取消').click()
                sleep(2)
            else:
                print('取消按钮不存在，请检查')
            sleep(1)
            #昵称
            nick=s(xpath='//XCUIElementTypeTextField[@value="Sam8202"]')
            nick.click()
            sleep(1)
            #focused=true;
            c1=s(xpath='//XCUIElementTypeButton[@name="清除文本"]')
            if c1.exists:
                print('昵称可以被编辑')
            else:
                print('昵称不可以被编辑，请检查原因')
            sleep(1)
            s(id='清除文本').click()
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
            s(id='确定').click()
            sleep(2)
            s(id='编辑个人信息').click()
            sleep(2)
            #简介
            """
            intro=s(xpath='//XCUIElementTypeTextField[@value="测试D"]')
            intro.click()
            sleep(1)
            c2=s(xpath='//XCUIElementTypeButton[@name="清除文本"]')
            if c2.exists:
                print('简介可以被编辑')
            else:
                print('简介不可以被编辑，请检查原因')
            sleep(1)
            #完成
            s.tap(331,382)
            sleep(1)
            """
            #性别
            man=s(xpath='//XCUIElementTypeButton[@name="default address not choose"]')[0]
            #woman=s(xpath='//XCUIElementTypeButton[@name="default address not choose"]')[2]
            woman=s(xpath='//XCUIElementTypeStaticText[@name="女"]')
            #checked=true
            c_man=man.get().value
            #c_woman=woman.get().value
            #print(str(c_man))
            #print(str(c_woman))
            if c_man == '1':
                woman.click()
                sleep(1)
                c_woman=s(xpath='//XCUIElementTypeButton[@name="default address not choose"]')[1].get().value
                if c_woman == '1':
                    print('用户性别可以从男改变成女')
                else:
                    print('用户性别无法从男改变成女')
            else:
                man.click()
                sleep(1)
                c_man=man.get().value
                if c_man == '1':
                    print('用户性别可以从女改变成男')
                else:
                    print('用户性别无法从女改变成男')
            sleep(2)
            #地区
            s(xpath='//XCUIElementTypeStaticText[@name="地区"]').click()
            sleep(3)
            ct=s(xpath='//XCUIElementTypeButton[@name="天津市"]')
            if ct.exists:
                print('常驻地区页面可以进入')
            else:
                print('常驻地区页面不可以进入，请检查原因')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            #我的地址
            s(xpath='//XCUIElementTypeStaticText[@name="我的地址"]').click()
            sleep(3)
            addr=s(xpath='//XCUIElementTypeButton[@name="默认地址"]')
            if addr.exists:
                print('地址管理页面可以进入')
            else:
                print('地址管理页面没有默认地址，请添加新地址')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            #保存
            #s(xpath='//XCUIElementTypeButton[@name="保存"]').click()
            s(id='保存').click()
            sleep(1)
            save=s(id='保存成功')
            if save.exists:
                print('----修改的个人信息可以保存成功')
            else:
                print('----修改的个人信息没有保存成功，请检查')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf='../../test_report/ios/'+now+'_errorSaveInfo_R.png'
                c.screenshot(sf)
            sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
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
        print('TC_检查手机号码登录APP，检查点:惊喜页面上元素UI检查----step1惊喜页面上任意礼品的元素UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        for i in range(6):
            s.swipe(50,550,50,70,0.5)
            sleep(2)
        #driver.execute_script("mobile: scroll", {"direction": "down"})
        sleep(2)
        #惊喜页面的各个元素是否存在
        c1=fun_giftui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素都检查完毕')
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_instuninstversioncheck_tc015
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_instuninstversioncheck_tc015(self):
        print('TC_检查手机号码登录APP，检查点:兼容性测试：安装和卸载app功能----step1卸载app')
        print('step2检查app是否存在；step3重新安装app；step4检查app是不是最新/所需版本')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #home
        #s(id='我的').click()
        #sleep(2)
        c.home()
        #卸载app
        driver.remove_app('com.do1.WeiLaiApp.inhouse')
        sleep(3)
        #check if app is uninstalled
        ch=driver.is_app_installed('com.do1.WeiLaiApp.inhouse')
        sleep(1)
        if ch == True:
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
            allow=s(id='允许')
            if allow.exists:
                s(id='允许').click()
                sleep(2)
            allow=s(id='允许')
            if allow.exists:
                s(id='允许').click()
                sleep(2)
            #我的
            s(id='我的').click()
            sleep(3)
            s.swipe(150,550,150,250,0.5)
            sleep(2)
            #设置
            s(id='设置').click()
            sleep(2)
            n=s(xpath='//XCUIElementTypeStaticText[@name="2.9.5 build:0"]')
            if n.exists:
                print('重新安装app后版本检查通过')
            else:
                print('重新安装app后版本检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf='../../test_report/ios/'+now+'_errorVersonCheck_R.png'
                c.screenshot(sf)
            sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_scores_tc016
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_scores_tc016(self):
        print('TC_检查手机号码登录APP，检查点:积分明细页面上元素UI检查和相关元素的功能检查----step1进入积分明细页面；')
        print('step2页面上元素UI检查;step3检查点击积分规则按钮的功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[2]').click()
        sleep(3)
        #检查积分明细页面的各个元素是否存在
        c1=fun_scoredetailui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素都检查完毕')
            sleep(1)
            #点击？号
            s(xpath='//XCUIElementTypeButton[@name="integration rule"]').click()
            sleep(3)
            #拍照
            t=s(xpath='//XCUIElementTypeOther[@name="积分规则"]')
            if t.exists:
                print('积分规则页面存在')
            else:
                print('积分规则页面不存在，请检查')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_remarkfriend_tc018
#Purpose:朋友页面对好友设置备注并检查备注是否生效
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_remarkfriend_tc018(self):
        print('TC_检查手机号码登录APP，检查点:对好友设置备注并检查备注是否生效----step1从朋友页面进入朋友列表页面')
        print('step2选择一个朋友进入朋友详细信息页面；step3检查点击设置备注按钮的功能;step4检查备注是否生效')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(5)
        s(xpath='//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        f=s(className='XCUIElementTypeCell')
        sleep(2)
        if f.exists:
            old=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(3)
            s(id='icon more white').click()
            sleep(2)
            combtn=s(id='设置备注')
            sleep(1)
            if combtn.exists:
                s(id='设置备注').click()
                sleep(2)
                edit=s(className='XCUIElementTypeTextField')
                edit.click()
                sleep(1)
                edit.clear_text()
                sleep(1)
                edit.set_text(old+'的备注')
                sleep(1)
                s(id='保存').click()
                sleep(3)
                #print(old)
                #print(old+'的备注')
                cc=s(id=old+'的备注')
                sleep(2)
                if cc.exists:
                    print('好友的备注设置已经生效')
                else:
                    print('好友的备注设置没有生效，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorRemark_R.png'
                    c.screenshot(sf1)
                sleep(2)   
            else:
                print('设置备注的按钮不存在，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorNoRemark_R.png'
                c.screenshot(sf2)
                sleep(1)
                s(id='取消').click()
                sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('没有好友可以设置备注，请先添加好友')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/ios/'+now+'_errorNoFriend_R.png'
            c.screenshot(sf3)
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_article_tc019
#Purpose:发现页面推荐tab里文章元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_article_tc019(self):
        print('TC_检查手机号码登录APP，检查点:发现页面推荐tab里文章元素UI检查和评论的功能检查----step1从发现页面推荐tab页找到一个文章')
        print('step2文章详情页面上元素UI检查;step3检查点击评论按钮的功能;step4检查发表评论成功后文章详情顶部的评论内容')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        #s(id='发现').click()
        #sleep(2)
        for i in range(3):
            s.swipe(150,500,150,100,0.5)
            sleep(2)
        #检查文章的各个元素是否存在
        c1=fun_articleui_check(self)
        sleep(2)
        if c1 == True:
            print('推荐tab里文章各个被检查元素都检查完毕')
            sleep(1)
            #点击评论
            s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeButton[2]').click()
            sleep(3)
            #s(id='写评论').click()
            s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]').click()
            sleep(2)
            combtn=s(xpath='//XCUIElementTypeStaticText[@name="请输入你的评论"]')
            combtn.click()
            sleep(1)
            now0=time.strftime('%Y-%m-%d %H_%M_%S')
            combtn.set_text('测试评论文章:'+now0)
            sleep(1)
            s(xpath='//XCUIElementTypeButton[@name="发布"]').click()
            sleep(3)
            #check published text here
            title=s(xpath='//XCUIElementTypeStaticText[contains(@name,"测试评论文章:")]')
            #print(len(title))
            if title.exists:
                print('评论的文字检查通过')
            else:
                print('评论的文字检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorComment_R.png'
                c.screenshot(sf1)
            sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_openmultichat_tc020
#Purpose:发现页面发起群聊功能的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_openmultichat_tc020(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查发现首页右上角+号是否存在；')
        print('step2检查点击+号后发起群聊按钮是否存在；step3发起群聊并发送内容功能是否正常；step4检查发布内容里文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        #s(id='我的').click()
        #sleep(2)
        #+
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #建群聊
            c2=bp_is_openmultichatexist(self)
            if c2 == True:
                s(id='建群聊').click()
                sleep(3)
                #cb=s(xpath='//XCUIElementTypeImage[@name="chat_unslected_icon"]')
                cb=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')
                sleep(2)
                for i in range(len(cb)-1):
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[i].click()
                    sleep(1)
                #确定    
                s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
                sleep(2)
                msg=s(id='chat_input_textView')
                msg.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                msg.set_text('Test群聊:'+now0)
                sleep(1)
                #发送
                s(xpath='//XCUIElementTypeButton[@name="Send"]').click()
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                #朋友
                s(id='朋友').click()
                sleep(2)
                #检查群聊的发送内容是否正确
                t=s(id='Test群聊:'+now0)
                sleep(2)
                #print(len(t))
                if t.exists:
                    print('群聊的发送内容正确')
                else:
                    print('群聊的发送内容不正确，请检查')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorMultiChatText_R.png'
                    c.screenshot(sf2)
                sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----结束:'+now)

#*******************************************************************
#TC Name:test_pengyou_dismissmultichat_tc021
#Purpose:朋友页面群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊的功能检查
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************************
    def test_pengyou_dismissmultichat_tc021(self):
        print('TC_检查手机号码登录APP，检查点:朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊功能')
        print('step1进入已发起的群聊，检查踢人出群聊的功能是否正常;step2检查邀请朋友加入群聊的功能是否正常')
        print('step3检查解散并退出群聊的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(5)
        #群聊
        mul=s(xpath='//XCUIElementTypeStaticText[contains(@name,"群聊")]')
        if mul.exists:
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"群聊")]')[0].click()
            sleep(2)
            s(xpath='//XCUIElementTypeNavigationBar[contains(@name,"群聊")]/XCUIElementTypeButton[2]').click()
            sleep(4)
            #-
            s(xpath='//XCUIElementTypeImage[@value="chat_delete_icon"]').click()
            sleep(2)
            name1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(1)
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
            #检查是否已被移出群组
            r_msg=s(id='你将'+name1+'移出了群组')
            sleep(1)
            #'你将'+name1+'移出群组'
            if r_msg.exists:
                print('踢人出群聊的功能检查通过')
            else:
                print('踢人出群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorKickoff_R.png'
                c.screenshot(sf1)
            sleep(1)
            #s(id='all page back grey icon').click()
            #sleep(2)
            s(xpath='//XCUIElementTypeNavigationBar[contains(@name,"群聊")]/XCUIElementTypeButton[2]').click()
            sleep(2)
            #+
            s(xpath='//XCUIElementTypeImage[@value="chat_add_icon"]').click()
            sleep(2)
            name2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].text
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(1)
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(3)
            #检查是否已被邀请加入群组
            #'你邀请'+name2+'加入了群组':if notes added, it could be wrong
            a_msg=s(xpath='//XCUIElementTypeStaticText[contains(@name,"加入了群组")]')
            sleep(1)
            #print(name2)
            if a_msg.exists:
                print('邀请朋友加入群聊的功能检查通过')
            else:
                print('邀请朋友加入群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorJoin_R.png'
                c.screenshot(sf2)
            sleep(1)
            s(xpath='//XCUIElementTypeNavigationBar[contains(@name,"群聊")]/XCUIElementTypeButton[2]').click()
            sleep(2)
            #解散并删除
            s(id='解散并删除').click()
            sleep(1)
            s(id='确定').click()
            sleep(2)
            #检查解散的群聊是否还存在
            title1=s(id='群聊')
            if title1.exists:
                print('解散并退出群聊的功能检查通过')
            else:
                print('解散并退出群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/ios/'+now+'_errorDismissMultiChat_R.png'
                c.screenshot(sf3)
            sleep(2)
        else:
            print('没有群聊可以操作，请先发起群聊')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='../../test_report/ios/'+now+'_errorNoMultiChat_R.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群----结束:'+now)

#*******************************************************
#TC Name:test_wode_checkin_tc025
#Purpose:我的页面点击签到及检查当日签到积分是否能正常获得的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_checkin_tc025(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查我的页面右上角点击签到是否存在；')
        print('step2检查点击签到功能是否正常；step3到积分明细页面检查当日签到的积分是否已经获得')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        #点击签到accessibility_id('点击签到')
        chk=s(xpath='//XCUIElementTypeStaticText[@name="点击签到"]')
        if chk.exists:
            s(xpath='//XCUIElementTypeStaticText[@name="点击签到"]').click()
            sleep(2)
        else:
            print('今日已经签到过，请明日再来')
        sleep(1)
        #检查积分
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[2]').click()
        sleep(2)
        cb=s(xpath='//XCUIElementTypeStaticText[@name="每日签到"]')
        #print(len(cb))
        nowtm=time.strftime('%Y.%m.%d')
        tm=s(xpath='//XCUIElementTypeStaticText[contains(@name, nowtm)]')
        sleep(1)
        if cb.exists and tm.exists:
            print('每日签到获取积分功能检查通过')
        else:
            print('每日签到获取积分功能检查失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/ios/'+now+'_errorCheckinScore_R.png'
            c.screenshot(sf2)
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_nicknameheadicon_tc028
#Purpose:朋友页面修改群聊昵称和头像功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_nicknameheadicon_tc028(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_修改群聊昵称和头像功能---step1检查朋友页面群聊是否存在；')
        print('step2进入群聊修改群组名称；step3检查群组名称是否修改成功；step4检查修改群组头像功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        try:
            s(id='朋友').click()
            sleep(6)
            t=s(xpath='//XCUIElementTypeStaticText[contains(@name,"群聊")]')
            sleep(1)
            if t.exists:
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"群聊")]')[0].click()
                sleep(2)
                s(xpath='//XCUIElementTypeNavigationBar[contains(@name,"群聊")]/XCUIElementTypeButton[2]').click()
                sleep(2)
                #修改群组名称
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"群聊")]').click()
                sleep(1)
                edit=s(className='XCUIElementTypeTextField')
                edit.click()
                sleep(1)
                edit.clear_text()
                sleep(1)
                edit.set_text('群聊new')
                sleep(1)
                s(id='保存').click()
                sleep(2)
                nk=s(id='群聊new')
                if nk.exists:
                    print('群组的名称已经修改成功')
                else:
                    print('群组的名称没有修改成功，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorName_R.png'
                    c.screenshot(sf1)
                sleep(1)
                #修改头像
                s(id='群组头像').click()
                sleep(1)
                #拍照
                s(id='拍照').click()
                sleep(3)
                ok=s(id='好')
                if ok.exists:
                    s(id='好').click()
                    sleep(2)
                s(id='FrontBackFacingCameraChooser').click()
                sleep(2)
                s(id='PhotoCapture').click()
                sleep(2)
                s(id='使用照片').click()
                sleep(10)
                #修改头像
                s(id='群组头像').click()
                sleep(1)
                #从手机相册选择
                s(id='从手机相册选择').click()
                sleep(2)
                #屏幕快照
                s(id='屏幕快照').click()
                sleep(2)
                for i in range(2):
                    s.swipe(150,550,150,250,0.5)
                    sleep(2)
                s(className='XCUIElementTypeCell')[0].click()
                sleep(2)
                #选取
                s(id='选取').click()
                sleep(10)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            else:
                print('没有群聊可以操作，请先发起群聊')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/ios/'+now+'_errorNoMultichat_R.png'
                c.screenshot(sf3)
            sleep(2)
        except Exception as e:
            print('发生异常：'+str(e))
            sleep(1)
            pass
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_searchwatch_tc029
#Purpose:朋友页面搜索好友并打开个人主页进行关注
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_searchwatch_tc029(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_朋友页面搜索好友并打开个人主页进行关注---')
        print('step1朋友页面点+号，检查添加朋友按钮是否存在；step2输入好友名称进行搜索；')
        print('step3点击搜索出的朋友打开他的个人主页；step4检查关注功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(5)
        s(xpath='//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        #点+号
        s(xpath='//XCUIElementTypeNavigationBar[@name="朋友列表"]/XCUIElementTypeButton[2]').click()
        sleep(1)
        add=s(id='添加朋友')
        if add.exists:
            s(id='添加朋友').click()
            sleep(2)
            edit=s(xpath='//XCUIElementTypeSearchField[@name="昵称/手机号"]')
            edit.click()
            sleep(0.5)
            s(xpath='//XCUIElementTypeSearchField[@name="昵称/手机号"]').set_text('张三')
            sleep(1)
            #search
            s(id='Search').click()  
            sleep(3)
            ff=s(className='XCUIElementTypeCell')
            sleep(2)
            #print(len(ff))
            if ff.exists:
                print('搜索好友功能检查通过')
                sleep(1)
                s(className='XCUIElementTypeCell')[1].click()
                sleep(4)
                #关注
                t=s(xpath='//XCUIElementTypeStaticText[@name="关注"]')
                if t.count == 2:
                    s(xpath='//XCUIElementTypeStaticText[@name="关注"]')[1].click()
                    sleep(3)
                    tt=s(id='已关注')
                    if tt.exists:
                        print('好友已经关注成功')
                    else:
                        print('好友没有关注成功，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorWatch_R.png'
                        c.screenshot(sf1)
                    sleep(1)
                else:
                    print('该好友你以前已经关注过了，无需再操作')
                    sleep(1)
                s(id='full screen back icon').click()
                sleep(2)
                #s(id='all page back grey icon').click()
                #sleep(2)
            else:
                print('搜索好友功能检查失败，请检查原因')
                sleep(1)
                #取消
                s(id='取消').click() 
                sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('没有添加朋友按钮，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/ios/'+now+'_errorNoAddFriend_R.png'
            c.screenshot(sf3)
            sleep(2)
        s(id='all page back grey icon').click()  
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----结束:'+now)

#*******************************************************
#TC Name:test_wode_resetsecupwd_tc030
#Purpose:我的页面设置里重置服务安全密码的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_resetsecupwd_tc030(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点设置；')
        print('step2点击服务安全密码；step3检查重置服务安全密码的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe(150,550,150,250,0.5)
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #服务安全密码
        s(id='服务安全密码').click()
        sleep(3)
        code=s(className='XCUIElementTypeTextField')
        code.click()
        code.set_text('112233')
        sleep(1)
        s(id='下一步').click()
        sleep(2)
        #身份类型
        s(className='XCUIElementTypeTextField')[0].click()
        sleep(1)
        s(text='确定').click()
        sleep(2)
        idnum=s(className='XCUIElementTypeTextField')[2]
        idnum.click()
        idnum.set_text('340103197301142518')
        sleep(1)
        #完成
        s(id='Toolbar Done Button').click()
        sleep(1)
        #下一步
        s(id='下一步').click()
        sleep(2)
        p=[]
        for i in range(6):
            r=random.randint(0,9)
            p.append(str(r))
        print('重置的密码是：'+str(p))
        sleep(1)
        for j in range(6):
            s(id=p[j]).click()
        sleep(1)
        for j in range(6):
            s(id=p[j]).click()
        sleep(1)
        sleep(2)
        chk=s(id='重置成功')
        if chk.exists:
            print('服务安全密码重置成功')
        else:
            print('服务安全密码重置失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/ios/'+now+'_errorResetSecupwd_R.png'
            c.screenshot(sf2)
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_addeditaddress_tc031
#Purpose:我的页面里地址管理页面新增和编辑一个收货地址的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_addeditaddress_tc031(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点击头像')
        print('step2点击编辑个人信息；step3点击我的地址进入地址管理页面;step4检查添加新地址的功能是否正常')
        print('step5检查编辑地址的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(xpath='//XCUIElementTypeStaticText[@name="Sam8202"]').click()
        sleep(2)
        #编辑个人信息
        s(id='编辑个人信息').click()
        sleep(2)
        #我的地址
        s(id='我的地址').click()
        sleep(2)
        #添加新地址
        add=s(id='添加新地址')
        if add.exists:
            print('添加新地址按钮存在,检查通过')
            sleep(1)
            s(id='添加新地址').click()
            sleep(1)
            name=s(className='XCUIElementTypeTextField')[0]
            name.click()
            r=random.randint(10,99)
            sleep(1)
            name.set_text('测试'+str(r))
            sleep(1)
            pnum=s(className='XCUIElementTypeTextField')[2]
            pnum.click()
            r2=random.randint(10,99)
            sleep(1)
            pnum.set_text('138160328'+str(r2))
            sleep(1)
            #完成
            s(id='Toolbar Done Button').click()
            sleep(1)
            #选择所在地区
            s(id='选择所在地区').click()
            sleep(2)
            #确定
            s(id='确定').click()
            sleep(1)
            #街道/楼牌号等
            addr=s(className='XCUIElementTypeTextView')
            addr.click()
            r3=random.randint(100,999)
            sleep(1)
            addr.set_text('中山北路'+str(r3)+'号')
            sleep(1)
            #完成
            s(id='Toolbar Done Button').click()
            sleep(1)
            #保存
            s(id='保存').click()
            sleep(1)
            #检查toast
            save1=s(id='保存成功')
            if save1.exists:
                print('新增地址成功')
            else:
                print('新增地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorAddnewaddr_R.png'
                c.screenshot(sf2)
        else:
            print('添加新地址按钮不存在，请检查原因')
            sleep(1)
        #编辑
        edi=s(xpath='//XCUIElementTypeButton[@name="编辑"]')
        if edi.exists:
            print('编辑按钮存在,检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeButton[@name="编辑"]').click()
            sleep(1)
            name=s(className='XCUIElementTypeTextField')[0]
            name.click()
            #old=name.get_attribute('value')
            r4=random.randint(10,99)
            sleep(1)
            name.set_text(str(r4))
            sleep(1)
            #保存
            s(id='保存').click()
            sleep(1)
            #检查toast
            save2=s(id='修改成功')
            if save2.exists:
                print('编辑地址成功')
            else:
                print('编辑地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorEditaddr_R.png'
                c.screenshot(sf1)
        else:
            print('编辑按钮不存在，请检查原因')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='full screen back icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershowpic_tc032
#Purpose:发现页面体验tab活动的晒图功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_expershowpic_tc032(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的晒图功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查晒图功能是否正常;step4检查晒图的文字是否正确')
        print('step5检查晒图的9张图片数量是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(2)
        s(xpath='//XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(2)
        for i in range(2):
            s.swipe(150,550,150,100,0.5)
            sleep(2)
        sleep(1)
        s(id='蔚来上海二号店').click()
        sleep(4)
        #徐家汇活动之还未开始
        s(id='徐家汇活动之还未开始').click()
        sleep(4)
        #晒图
        show=s(xpath='//XCUIElementTypeLink[@name="晒图"]')
        sleep(2)
        if show.exists:
            print('晒图按钮存在,检查通过')
            sleep(1)
            show[0].click()
            sleep(2)
            #+
            s.tap(65,264)
            sleep(2)
            #好
            allow=s(id='好')
            if allow.exists:
                s(id='好').click()
                sleep(2)
            for i in range(1,10):
                s(predicate='name=="compose guide check box defaul"')[i].click()
                sleep(1)
            s(id='完成(9/9)').click()
            sleep(1)
            word=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
            word.click()
            sleep(1)
            now0=time.strftime('%Y-%m-%d %H_%M_%S')
            word.set_text('ios体验晒图:'+now0)
            sleep(1)
            s(id='发布').click()
            sleep(15)
            s.swipe(150,500,150,200,0.5)
            sleep(2)
            #check numbers of pictures and published text here
            title=s(xpath='//XCUIElementTypeTextView[contains(@value,"ios体验晒图:")]')
            sleep(2)
            if title.exists:
                print('体验晒图的文字检查通过')
            else:
                print('体验晒图的文字检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorShowpicText_R.png'
                c.screenshot(sf1)
            sleep(2)
            number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
            if number.exists:
                print('体验晒图的上传9张图片检查通过')
            else:
                print('体验晒图的上传9张图片检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/ios/'+now+'_errorPic9_R.png'
                c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(3)
        else:
            print('晒图按钮不存在/找不到，请检查原因')
            sleep(2)
        #s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
        #sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnowatfriend_tc033
#Purpose:检查发现页面的发布此刻并@好友的功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_publishnowatfriend_tc033(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻并@好友的功能----step1检查发现首页右上角+号是否存在；')
        print('step2检查发布此刻按钮是否存在；step3发布并@好友功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片；')
        print('step5检查发布文字是否正确;step6退出当前账号并已@的好友账号登录app;step7检查朋友页面里是否收到@通知')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='//*[@text="发现"]').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #发布此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                print('发此刻按钮存在，检查通过')
                sleep(1)
                s(id='发此刻').click()
                sleep(2)
                s.tap(55,264)
                sleep(2)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                    sleep(2)
                sleep(1)
                for i in range(1,10):
                    s(predicate='name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                s(id='完成(9/9)').click()
                sleep(1)
                word=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.set_text('I love China:'+now0)
                sleep(1)
                #@
                s(id='atSome btn').click()
                sleep(1)
                s.swipe(150,550,150,200,0.5)
                sleep(2)
                s(id='Sam8198').click()
                sleep(1)
                s(id='发布').click()
                sleep(13)
                #check numbers of pictures and published text here
                title=s(xpath='//XCUIElementTypeTextView[contains(@value,"I love China:")]')
                if title.exists:
                    print('发布内容的文字检查通过')
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorText_R.png'
                    c.screenshot(sf1)
                sleep(2)
                number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                if number.exists:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPic9_R.png'
                    c.screenshot(sf2)
                sleep(2)
                #logout
                #我的
                s(id='我的').click()
                sleep(3)
                s.swipe(150,550,150,200,0.5)
                sleep(2)
                #设置
                s(id='设置').click()
                sleep(1)
                s(id='退出登录').click()
                sleep(1)
                s(id='确认').click()
                sleep(2)
                s.swipe(150,200,150,550,0.5)
                sleep(3)
                #relogin as 'Sam8198'
                #not working now
                #s(xpath='//XCUIElementTypeStaticText[@name="注册/登录"]').click()
                s.tap(67,100)
                sleep(2)
                #登录页面
                mobile_no=s(className='XCUIElementTypeTextField')[0]
                mobile_no.click()
                sleep(1)
                mobile_no.set_text('98762648198')
                sleep(1)
                code=s(className='XCUIElementTypeTextField')[2]
                code.click()
                sleep(1)
                code.set_text('112233')
                sleep(1)
                s(xpath='//XCUIElementTypeButton[@name="注册/登录"]').click()
                sleep(7)
                #朋友
                s(id='朋友').click()
                sleep(5)
                #检查好友'Sam8198'是否收到@通知
                fb=s(xpath='//XCUIElementTypeStaticText[contains(@name,"@了你")]')
                if fb.exists:
                    print('好友收到@通知检查通过')
                else:
                    print('好友收到@通知检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_error#friend_R.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('发此刻按钮不存在，请检查原因')
                sleep(1)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcshare_tc034
#Purpose:检查发现页面此刻tab下的ugc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_ugcshare_tc034(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的分享功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='此刻').click()
        sleep(3)
        u=s(className='XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            #s.swipe(150,500,150,200,0.5)
            #sleep(2)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')[0].click()
            sleep(2)
            #...
            s(id='more icon').click()
            sleep(2)
            #微信
            wh=s(id='微信')
            if wh.exists:
                print('分享到微信按钮存在，检查通过')
                sleep(2)
                s(id='微信').click()
                sleep(8)
                s(id='王小龙').click()
                sleep(2)
                """
                #/XCUIElementTypeTextView
                #words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]')
                words=s(className='XCUIElementTypeTextView',value='给朋友留言')
                sleep(1)
                if words.exists:
                    words.click()
                    sleep(1)
                    now0=time.strftime('%Y-%m-%d %H_%M_%S')
                    sleep(0.5)
                    words.set_text('测试UGC微信好友:'+now0)
                    sleep(1)
                """
                #发送
                s(id='发送').click()
                sleep(1)
                s(id='返回蔚来').click()
                sleep(1)
                #检查toast
                save1=s(id='分享成功')
                if save1.exists:
                    print('分享微信成功')
                else:
                    print('分享微信失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorsharewechat_R.png'
                    c.screenshot(sf1)
                sleep(1)
            else:
                print('分享到微信按钮不存在，请检查原因')
            sleep(2)
            #...
            s(id='more icon').click()
            sleep(2)
            #朋友圈
            pyq=s(id='朋友圈')
            if pyq.exists:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(2)
                s(id='朋友圈').click()
                sleep(8)
                word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.set_text('测试UGC朋友圈:'+now2)
                sleep(1)
                #发表
                s(id='发表').click()
                sleep(1)
                #检查toast
                save2=s(id='分享成功')
                if save2.exists:
                    print('分享朋友圈成功')
                else:
                    print('分享朋友圈失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
                sleep(1)
            #...
            s(id='more icon').click()
            sleep(2)
            #微博
            wb=s(id='微博')
            if wb.exists:
                print('分享到微博按钮存在，检查通过')
                sleep(2)
                s(id='微博').click()
                sleep(6)
                #发送
                s(id='发送').click()
                sleep(1)
                #检查toast
                save3=s(id='分享成功')
                if save3.exists:
                    print('分享微博成功')
                else:
                    print('分享微博失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/ios/'+now+'_errorsharewebo_R.png'
                    c.screenshot(sf3)
                sleep(2)
            else:
                print('分享到微博按钮不存在，请检查原因')
            sleep(2)
            #...
            s(id='more icon').click()
            sleep(2)
            #我的朋友
            mf=s(id='我的朋友')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(2)
                s(id='我的朋友').click()
                sleep(2)
                #Sam8201
                s(id='Sam8201').click()
                sleep(1)
                #发送
                #检查toast
                save4=s(id='分享成功')
                if save4.exists:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/ios'+now+'_errorsharemyfriend_R.png'
                    c.screenshot(sf4)
                sleep(2)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcdel_tc035
#Purpose:检查发现页面此刻tab下的ugc的删除功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_ugcdel_tc035(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的...按钮；step4检查删除按钮是否存在')
        print('step5检查删除ugc功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的删除功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='此刻').click()
        sleep(3)
        u=s(className='XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            my=s(xpath='//XCUIElementTypeStaticText[@name="Sam8202"]')
            sleep(2)
            #print(len(my))
            if my.exists:
                s(id='Sam8202').click()
                sleep(2)
                #...
                s(id='more icon').click()
                sleep(2)
                #删除
                d=s(id='删除')
                if d.exists:
                    print('删除按钮存在，检查通过')
                    sleep(2)
                    s(id='删除').click()
                    sleep(1)
                    s(id='确认').click()
                    sleep(1)
                    #检查toast
                    save1=s(id='删除成功')
                    if save1.exists:
                        print('删除ugc成功')
                    else:
                        print('删除ugc失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorDelUgc_R.png'
                        c.screenshot(sf1)
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
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_此刻tab下的ugc的删除功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_im_tc036
#Purpose:检查朋友页面IM聊天信息复制、删除、撤回、转发
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_im_tc036(self):
        print('TC_检查手机号码登录APP，检查点:朋友_IM聊天信息复制、删除、撤回、转发功能----step1朋友页面找到一个朋友发起聊天')
        print('step2发送一条消息；step3检查复制消息功能；step4检查删除消息功能')
        print('step5检查转发消息功能;step6检查撤回消息功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(5)
        myf=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam2")]')
        sleep(1)
        if myf.exists:
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam2")]').click()
            sleep(2)
            #和分享按钮合并
            s(id='im btn more').click()
            sleep(2)
            #删除并退出
            butt=s(id='删除并退出')
            if butt.exists:
                s(id='删除并退出').click()
                sleep(1)
                s(id='确定').click()
                sleep(1)
        sleep(3)
        s(id='friends go friendlist').click()
        sleep(2)
        u=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam2")]')
        if u.exists:
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam2")]').click()
            sleep(4)
            #聊天
            s(id='聊天').click()
            sleep(2)
            #发送文本信息
            word=s(id='chat_input_textView')
            word.click()
            sleep(1)
            word.set_text('测试im')
            sleep(1)
            #发送
            s(id='Send').click()
            sleep(2)
            s.tap(100,200)
            sleep(1)
            #长按im
            d=s(xpath='//XCUIElementTypeStaticText[@name="测试im"]')
            d.tap_hold(1.0)
            sleep(1)
            #复制
            cp=s(id='复制')
            if cp.exists:
                print('复制消息按钮存在，检查通过')
                sleep(2)
                s(id='复制').click()
                sleep(1)
                word.click()
                sleep(1)
                word.tap_hold(1.0)
                sleep(1)
                #粘贴
                s(id='粘贴').click()
                sleep(1)
                s(id='Send').click()
                sleep(1)
                s.tap(100,200)
                sleep(1)
                #检查
                c1=s(xpath='//XCUIElementTypeStaticText[@name="测试im"]')
                if c1.count != 1:
                    print('复制消息成功')
                else:
                    print('复制消息失败，请检查原因')
                sleep(2)
            else:
                print('复制消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d0=s(xpath='//XCUIElementTypeStaticText[@name="测试im"]')
            d0.tap_hold(1.0)
            sleep(1)
            #删除消息
            de=s(id='删除')
            if de.exists:
                print('删除消息按钮存在，检查通过')
                sleep(2)
                s(id='删除').click()
                sleep(2)
                #检查
                c2=s(xpath='//XCUIElementTypeStaticText[@name="测试im"]')
                if c2.count == 1:
                    print('删除消息成功')
                else:
                    print('删除消息失败，请检查原因')
                sleep(2)
            else:
                print('删除消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d1=s(xpath='//XCUIElementTypeStaticText[@name="测试im"]')
            d1.tap_hold(1.0)
            sleep(1)
            #转发消息
            df=s(id='转发')
            if df.exists:
                print('转发消息按钮存在，检查通过')
                sleep(2)
                s(id='转发').click()
                sleep(1)
                s(id='朋友').click()
                sleep(1)
                fri=s(className='XCUIElementTypeCell')
                if fri.exists:
                    #1nd friend
                    s(className='XCUIElementTypeCell')[1].click()
                else:
                    print('没有其他朋友可以转发消息')
                    sleep(1)
                    s(id='all page back grey icon').click()
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('转发消息按钮不存在，请检查原因')
                sleep(2)
            #新发一条im
            word.click()
            sleep(1)
            word.set_text('测试撤回im')
            sleep(1)
            #发送
            s(id='Send').click()
            sleep(1)
            s.tap(100,200)
            sleep(2)
            #长按im
            d2=s(xpath='//XCUIElementTypeStaticText[@name="测试撤回im"]')
            d2.tap_hold(1.0)
            sleep(1)
            #撤回消息
            wd=s(id='撤回')
            if wd.exists:
                print('撤回消息按钮存在，检查通过')
                sleep(2)
                s(id='撤回').click()
                sleep(1)
                #检查
                w=s(id='你撤回了一条消息')
                if w.exists:
                    print('撤回消息成功')
                else:
                    print('撤回消息失败，请检查原因')
                sleep(2)
            else:
                print('撤回消息按钮不存在，请检查原因')
                sleep(2)
            s(id='all page back grey icon').click()
            sleep(1)
        else:
            print('朋友不存在，无法执行聊天相关操作')
            sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----结束:'+now)
    
#*******************************************************
#TC Name:test_faxian_infopgcshare_tc037
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_infopgcshare_tc037(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的pgc的分享功能----step1进入发现页面资讯tab')
        print('step2PGC的UI检查；step3进入pgc文章页面点右下角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='资讯').click()
        sleep(3)
        for i in range(2):
            s.swipe(150,500,150,150,0.5)
            sleep(2)
        #检查发现页面资讯tab下的pgc的的各个元素是否存在
        c1=fun_pgcui_check(self)
        if c1 == True:
            print('发现页面资讯tab下的pgc的各个被检查元素都检查完毕')
            sleep(1)
        u=s(className='XCUIElementTypeCell')
        if u.exists:
            print('PGC存在，检查通过')
            sleep(2)
            s(text='积分竞猜').click()
            sleep(3)
            #左上角按钮
            sh=s(id='icon share gray background')
            if sh.exists:
                print('分享按钮存在，检查通过')
                sleep(2)
                s(id='icon share gray background').click()
                sleep(2)
                #微信
                wh=s(id='微信')
                if wh.exists:
                    print('分享到微信按钮存在，检查通过')
                    sleep(2)
                    s(id='微信').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(2)
                    """
                    words=s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].set_text('人生苦短PGC微信好友:'+now0)
                        sleep(1)
                    """
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                    else:
                        print('分享微信好友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/android/'+now+'_errorPGCsharewechat_R.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                #share
                s(id='icon share gray background').click()
                sleep(2)
                #朋友圈
                pyq=s(id='朋友圈')
                if pyq.exists:
                    print('分享到朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.set_text('人生苦短PGC朋友圈:'+now2)
                    sleep(1)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                    else:
                        print('分享朋友圈失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorPGCsharewechatpyq_R.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                s(id='icon share gray background').click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    #发送
                    s(id='发送').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                    else:
                        print('分享微博失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorPGCsharewebo_R.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                s(id='icon share gray background').click()
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(1)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='Sam8201').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                    else:
                        print('分享我的朋友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorPGCsharemyfriend_R.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在，请检查原因')
                sleep(2)
            s(id='Live back icon').click()
            sleep(2)
        else:
            print('PGC不存在，无法执行分享操作')
            sleep(2)
        s.close()
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
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的报名功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查报名功能是否正常;step4进入我的->我的活动页面')
        print('step5点击查看行程单;step6检查活动订单里活动的时间是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的报名功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(4)
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(2)
        for i in range(2):
            s.swipe(150,550,150,150,0.5)
            sleep(2)
        s(id='蔚来上海二号店').click()
        sleep(2)
        s(id='更多活动').click()
        sleep(2)
        #自动化测试活动
        s(id='自动化测试活动').click()
        sleep(4)
        #page=driver.page_source
        #sleep(2)
        #报名
        joins=s(xpath='//XCUIElementTypeLink[@name="报名"]')
        sleep(2)
        if joins.exists:
            print('报名按钮存在,检查通过')
            sleep(2)
            joins[0].click()
            sleep(4)
            #场次
            #s(xpath='//XCUIElementTypeStaticText[@name="10.24 / 00:00"]').click()
            #sleep(1)
            #s(xpath='//XCUIElementTypeStaticText[@name="粉丝票"]').click()
            #sleep(2)
            #+限购1张
            #s(xpath='//XCUIElementTypeButton[@name="+"]').click()
            #sleep(1)
            s.swipe(150,550,150,50,0.5)
            sleep(2)
            #姓名
            name=s(className='XCUIElementTypeTextField')[0]
            name.click()
            name.set_text('测试员')
            sleep(1)
            s(id='完成').click()
            sleep(1)
            #mobile
            mb=s(className='XCUIElementTypeTextField')[2]
            mb.click()
            sleep(1)
            mb.set_text('18930018801')
            sleep(1)
            s(id='完成').click()
            sleep(3)
            #性别
            s(xpath='//XCUIElementTypeOther[@name="性别"]').click()
            sleep(1)
            #确定
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #血型
            s(xpath='//XCUIElementTypeOther[@name="血型"]').click()
            sleep(1)
            #确定
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #证件类型
            s(xpath='//XCUIElementTypeOther[@name="证件类型"]').click()
            sleep(1)
            #确定
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #证件号码
            em=s(className='XCUIElementTypeTextField')[3]
            em.click()
            sleep(1)
            em.set_text('340103197301142518')
            sleep(1)
            s(id='完成').click()
            sleep(2)
            #s(className='XCUIElementTypeSwitch').click()
            #sleep(1)
            #购买
            s(id='购买').click()
            sleep(1)
            #确认
            s(id='确认').click()
            sleep(3)
            #checking
            ch=s(xpath='//XCUIElementTypeStaticText[contains(@name,"预约成功")]')
            if not ch.exists:
                print('报名失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/ios/'+now+'_errorJoin_R.png'
                c.screenshot(sf1)
                sleep(2)
            else:
                print('报名成功')
                sleep(2)
                s(id='完成').click()
                sleep(4)
                #s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]').click()
                s.tap(30,42)
                sleep(2)
                #s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
                s.tap(30,42)
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
                #我的
                s(id='我的').click()
                sleep(4)
                s(id='我的活动').click()
                sleep(3)
                ch2=s(xpath='//XCUIElementTypeStaticText[contains(@value,"10月24日")]')
                if ch2.exists:
                    print('活动订单里活动时间检查通过')
                    sleep(2)
                else:
                    print('活动订单里活动时间检查失败，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorMyActivity_R.png'
                    c.screenshot(sf2)
                    sleep(2)
        else:
            print('报名按钮不存在，请检查原因')
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
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
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面我的活动里取消报名的功能---step1进入我的->我的活动页面')
        print('step2点击查看行程单；step3检查取消报名按钮是否存在;step4检查取消报名功能是否正常')
        print('step5检查活动订单里是否暂无活动预约')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——我的活动里取消报名的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(4)
        #我的活动
        s(id='我的活动').click()
        sleep(3)
        ch=s(xpath='//XCUIElementTypeButton[@name="取消报名"]')
        if ch.exists:
            print('取消报名按钮存在，检查通过')
            sleep(1)
            s(id='取消报名').click()
            sleep(1)
            #是
            s(id='是').click()
            sleep(1)
            #checking
            ch1=s(id='取消成功')
            if ch1.exists:
                print('取消报名成功')
                sleep(4)
                s(id='all page back grey icon').click()
                sleep(2)
                #我的活动
                s(id='我的活动').click()
                sleep(4)
                #暂无活动预约
                ch2=s(xpath='//XCUIElementTypeStaticText[@name="自动化测试活动"]')
                if not ch2.exists:
                    print('我的预约活动已取消报名，检查通过')
                    sleep(2)
                else:
                    print('我的预约活动取消报名失败，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf0='../../test_report/android/'+now+'_errorActivityList_R.png'
                    c.screenshot(sf0)
                    sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('取消报名失败，请检查原因')
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorCancel_R.png'
                c.screenshot(sf1)
                sleep(2)
        else:
            print('取消报名按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorNoCancelJoin_R.png'
            c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
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
        print('TC_检查手机号码登录APP，检查点:发现_发现页面体验tab下的活动的分享功能----step1进入发现页面体验tab')
        print('step2找到活动进入；step3检查并点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(4)
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(4)
        for i in range(2):
            s.swipe(150,550,150,150,0.5)
            sleep(2)
        s(id='蔚来上海二号店').click()
        sleep(2)
        #徐家汇活动之还未开始
        s(id='徐家汇活动之还未开始').click()
        sleep(6)
        #分享图标
        share=s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[2]')
        sleep(2)
        if share.exists:
            print('分享按钮存在，检查通过')
            sleep(2)
            #share
            s.tap(345,42)
            sleep(2)
            #微信
            wh=s(id='微信')
            if wh.exists:
                print('分享到微信按钮存在，检查通过')
                sleep(2)
                s(id='微信').click()
                sleep(6)
                s(id='王小龙').click()
                sleep(3)
                words=s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                sleep(2)
                if words.exists:
                    words[0].click()
                    sleep(1)
                    now0=time.strftime('%Y-%m-%d %H_%M_%S')
                    words[0].set_text('测试PGC微信好友:'+now0)
                    sleep(1)
                #发送
                s(id='发送').click()
                sleep(2)
                s(id='返回蔚来').click()
                sleep(1)
                #检查toast
                save1=s(id='分享成功')
                if save1.exists:
                    print('分享微信好友成功')
                else:
                    print('分享微信好友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPGCsharewechat_R_tc040.png'
                    c.screenshot(sf1)
                sleep(2)
            else:
                print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
            #share
            s.tap(345,42)
            sleep(2)
            #朋友圈
            pyq=s(id='朋友圈')
            if pyq.exists:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(1)
                s(id='朋友圈').click()
                sleep(8)
                word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.set_text('测试PGC朋友圈:'+now2)
                sleep(1)
                #发表
                s(id='发表').click()
                sleep(1)
                #检查toast
                save2=s(id='分享成功')
                if save2.exists:
                    print('分享朋友圈成功')
                else:
                    print('分享朋友圈失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPGCsharewechatpyq_R_tc040.png'
                    c.screenshot(sf2)
                sleep(1)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
            sleep(2)
            #share
            s.tap(345,42)
            sleep(2)
            #微博
            wb=s(id='微博')
            if wb.exists:
                print('分享到微博按钮存在，检查通过')
                sleep(2)
                s(id='微博').click()
                sleep(6)
                #发送
                s(id='发送').click()
                sleep(1)
                #检查toast
                save3=s(id='分享成功')
                if save3.exists:
                    print('分享微博成功')
                else:
                    print('分享微博失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/ios/'+now+'_errorPGCsharewebo_R_tc040.png'
                    c.screenshot(sf3)
                sleep(1)
            else:
                print('分享到新浪微博按钮不存在，请检查原因')
            sleep(2)
            #share
            s.tap(345,42)
            sleep(2)
            #我的朋友
            mf=s(id='我的朋友')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(1)
                s(id='我的朋友').click()
                sleep(2)
                s(id='Sam8201').click()
                sleep(1)
                #检查toast
                save4=s(id='分享成功')
                if save4.exists:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/ios/'+now+'_errorPGCsharemyfriend_R_tc040.png'
                    c.screenshot(sf4)
                sleep(1)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(2)
        else:
            print('分享按钮不存在/未找到，请检查原因')
            sleep(2)
        s.tap(30,42)
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_giftshare_tc041
#Purpose:检查惊喜页面的商品的分享功能
#OS:iOS
#Device:iPhone7
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_jingxi_giftshare_tc041(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面的商品的分享功能----step1进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        s.swipe(150,500,150,100,0.5)
        sleep(2)
        u=s(xpath='//XCUIElementTypeOther[@name="防水环保袋 500"]')
        if u.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(3)
            s(xpath='//XCUIElementTypeOther[@name="防水环保袋 500"]').click()
            sleep(8)
            #分享图标
            share=s(xpath='//XCUIElementTypeOther[@name="横幅"]/XCUIElementTypeOther[2]')
            sleep(2)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s.tap(338,58)
                sleep(2)
                #微信
                wh=s(id='微信')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words[0].click()
                        sleep(1)
                        now0=time.strftime('%Y-%m-%d %H_%M_%S')
                        words[0].set_text('测试Gift微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(1)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                    else:
                        print('分享微信好友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc041.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                #share
                s.tap(338,58)
                sleep(2)
                #朋友圈
                pyq=s(id='朋友圈')
                if pyq.exists:
                    print('分享到朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.set_text('测试Gift朋友圈:'+now2)
                    sleep(1)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                    else:
                        print('分享朋友圈失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc041.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(338,58)
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    #发送
                    s(id='发送').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                    else:
                        print('分享微博失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc041.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(338,58)
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(1)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='Sam8201').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                    else:
                        print('分享我的朋友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc041.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            s.tap(24,58)
            sleep(2)
        else:
            print('需要兑换的商品不存在/未找到，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----结束:'+now)

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
        print('TC_用户模式进入惊喜页面，检查点:惊喜_选择多款商品加入购物车后购物车图标角标的变化----step1用户模式进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面；step3点击加入购物车按钮检查购物车图标角标数字是否为1')
        print('step4点击购物车图标进入购物车详细页面，检查左下角是否显示已选(1)')
        print('step5选择第二款商品点击进入商品详细页面;step6点击加入购物车按钮检查购物车图标角标数字是否为2')
        print('step7点击购物车图标进入购物车详细页面，检查左下角是否显示已选(2)')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('惊喜_选择多款商品加入购物车后购物车图标角标的变化检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(6)
        s.swipe(50,500,50,200,1.0)
        sleep(2)
        u1=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="BeatsX无线蓝牙耳机 8990"]')
        if len(u1) != 0:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            u1[0].click()
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
                    else:
                        print('购物车详细页面左下角显示已选(1)检查失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1a='../../test_report/ios/'+now+'_errorCartGift1a_R.png'
                        driver.get_screenshot_as_file(sf1a)
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                    sleep(2)
                    driver.execute_script('mobile: tap', {'touchCount':'1', 'x':34, 'y':58})
                    sleep(2)
                    #driver.swipe(50,500,50,300,1000)
                    #sleep(3)
                    u2=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE系列 折叠雨伞 2900"]')
                    if len(u2) != 0:
                        print('需要兑换的商品2存在，检查通过')
                        sleep(2)
                        u2[0].click()
                        sleep(8)
                        page=driver.page_source
                        sleep(2)
                        add2b=driver.find_element_by_accessibility_id('加入购物车')
                        sleep(2)
                        add2b.click()
                        sleep(3)
                        add2b.click()
                        sleep(3)
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
                            else:
                                print('购物车详细页面左下角显示已选(2)检查失败，请检查原因')
                                now=time.strftime('%Y-%m-%d %H_%M_%S')
                                sf2a='../../test_report/ios/'+now+'_errorCartGift2a_R.png'
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
                            sf2='../../test_report/android/'+now+'_errorCartGift2_R.png'
                            driver.get_screenshot_as_file(sf2)
                        sleep(2)
                    else:
                        print('需要兑换的商品2不存在/未找到，请重新挑选')
                        sleep(2)
                else:
                    print('购物车图标角标数字为1检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorCartGift1_R.png'
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
        sleep(6)
        driver.swipe(50,500,50,200,1000)
        sleep(2)
        u1=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="BeatsX无线蓝牙耳机 8990"]')
        if len(u1) != 0:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            u1[0].click()
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
                u2=driver.find_elements_by_xpath('//XCUIElementTypeOther[@name="FE系列 折叠雨伞 2900"]')
                if len(u2) != 0:
                    print('需要兑换的商品2存在，检查通过')
                    sleep(2)
                    u2[0].click()
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
                        chk0=driver.find_elements_by_xpath('//XCUIElementTypeStaticText[@name=" 去添加点什么吧 "]')
                        sleep(2)
                        if len(chk0) != 0:
                            print('购物车已清空')
                            sleep(1)
                        else:
                            print('购物车未被清空，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf3='../../test_report/ios/'+now+'_errorCartNoEdit_R.png'
                            driver.get_screenshot_as_file(sf3)
                            sleep(2)
                            driver.execute_script('mobile: tap', {'touchCount':'1', 'x':37, 'y':42})
                            sleep(2)
                    else:
                        print('编辑按钮不存在，检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2a='../../test_report/ios/'+now+'_errorCartNoEdit_R.png'
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
        print('TC_用户模式点击我的我的活动菜单，检查点:我的_我的活动晒图功能检查----')
        print('step1进入我的活动页面；step2检查是否有晒图按钮；step3检查晒图功能是否正常')
        print('step4检查晒图的文字是否正确;step5检查晒图的9张图片数量是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的活动晒图功检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(4)
        s(id='我的活动').click()
        sleep(3)
        u=s(id='晒图')
        if u.exists:
            print('晒图按钮存在，检查通过')
            sleep(2)
            u.click()
            sleep(2)
            #+
            s.tap(55,264)
            sleep(2)
            #好
            allow=s(id='好')
            if allow.exists:
                s(id='好').click()
                sleep(2)
            sleep(1)
            try:
                for i in range(9):
                    #s(xpath='//XCUIElementTypeButton[@name="compose guide check box defaul"]')[i].click()
                    s(predicate='name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                s(id='完成(9/9)').click()
                sleep(2)
                word=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                sleep(2)
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.set_text('人生苦短评论_'+now0)
                t0='人生苦短评论_'+now0
                sleep(1)
                s(id='发布').click()
                sleep(12)
                #ios doesn't need to refresh
                #check numbers of pictures and published text here
                title=s(xpath='//XCUIElementTypeStaticText[contains(@name,t0)]')
                sleep(2)
                #print(t0)
                if title.exists :
                    print('晒图的文字检查通过')
                else:
                    print('晒图的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/ios/'+now+'_errorPublishText_R_tc046.png'
                    c.screenshot(sf1)
                sleep(2)
                number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                if number.exists:
                    print('晒图的上传9张图片检查通过')
                else:
                    print('晒图的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R_tc046.png'
                    c.screenshot(sf2)
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            except Exception as e:
                print('发生异常：'+str(e))
                sleep(1)
                pass
        else:
            print('晒图按钮不存在，请检查原因')
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的活动晒图功检查----结束:'+now)

        
if __name__ == '__main__':unittest.main()
