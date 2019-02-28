#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhone7 Plus
#version:iOS12.1.3
#author: Sam Wang
#update date: created by Sam [2019-01-28]

import wda
import unittest
import time
import os
import random
from time import sleep

from HTMLTestReportEN import HTMLTestRunner

from common_iPhone7p_ios12_stg_atx import fun_myfansui_check
from common_iPhone7p_ios12_stg_atx import fun_mywatchui_check
from common_iPhone7p_ios12_stg_atx import fun_mypublishui_check
from common_iPhone7p_ios12_stg_atx import bp_is_loggedin
from common_iPhone7p_ios12_stg_atx import fun_getinfo
from common_iPhone7p_ios12_stg_atx import bp_normalloginmp
from common_iPhone7p_ios12_stg_atx import bp_is_loginshow
from common_iPhone7p_ios12_stg_atx import fun_getloginmenu
from common_iPhone7p_ios12_stg_atx import bp_is_plusexist
from common_iPhone7p_ios12_stg_atx import bp_is_publishnowexist
from common_iPhone7p_ios12_stg_atx import bp_is_openmultichatexist
from common_iPhone7p_ios12_stg_atx import fun_findui_check
from common_iPhone7p_ios12_stg_atx import fun_personalinfoui_check
from common_iPhone7p_ios12_stg_atx import fun_scoredetailui_check
from common_iPhone7p_ios12_stg_atx import fun_giftui_check
from common_iPhone7p_ios12_stg_atx import fun_articleui_check
from common_iPhone7p_ios12_stg_atx import fun_cartui_check
from common_iPhone7p_ios12_stg_atx import fun_pgcui_check
#from common_iPhone7p_ios12_stg_atx import fun_getjingxiloginmenu
from common_iPhone7p_ios12_stg_atx import bp_is_initpicexist
from common_iPhone7p_ios12_stg_atx import fun_getjingxiloginmenu
from common_iPhone7p_ios12_stg_atx import bp_deleteaddress
#from common_iPhone7p_ios12_stg_atx import fun_pinch
#from common_iPhone7p_ios12_stg_atx import fun_zoom
from common_iPhone7p_ios12_stg_atx import fun_lightedui_check
from common_iPhone7p_ios12_stg_atx import fun_notlightedui_check
from common_iPhone7p_ios12_stg_atx import fun_mostsiteui_check
from common_iPhone7p_ios12_stg_atx import fun_activityui_check
from common_iPhone7p_ios12_stg_atx import fun_livecastui_check
from common_iPhone7p_ios12_stg_atx import bp_normalloginmp_carowner
from common_iPhone7p_ios12_stg_atx import bp_normalloginmp_notenoughscore
from common_iPhone7p_ios12_stg_atx import bp_normalloginmp_zeroscore

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
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_fans_tc001(self):
        print('TC_检查用户模式打开APP，检查点:我的_粉丝功能----step1检查我的页面点击粉丝后页面各个元素是否存在')
        print('step2取消互相关注/关注；step3检查被取消互相关注/关注的粉丝关系是否变成+关注/互相关注')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----开始:'+now)
        sleep(1)
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorPlusWatch_R.png'
                c.screenshot(sf2)
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_watch_tc002
#Purpose:检查我的页面点击关注后弹出页面的各项功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_watch_tc002(self):
        print('TC_检查用户模式打开APP，检查点:我的_关注功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2检查取消关注是否成功；step3检查加关注是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        #关注
        s(id='关注').click()
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[4]').click()
        sleep(3)
        #检查发布关注面的各个元素是否存在
        c1=fun_mywatchui_check(self)
        sleep(2)
        if c1 == True:
            print('关注页面上各个被检查元素都正常显示.')
            sleep(1)
            #取消关注
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[0].click()
            sleep(4)
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorAddCare_R.png'
                c.screenshot(sf1)
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_关注页面元素检查和取消关注和加关注的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_publish_tc003
#Purpose:检查我的页面点击发布后弹出页面的各项功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_publish_tc003(self):
        print('TC_检查用户模式打开APP，检查点:我的_发布功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2发布功能是否正常；step3检查发布内容里是否可以一次最大上传9张图片；step4检查发布文字是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_发布页面元素检查和发布功能----开始:'+now)
        sleep(1)
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
            s.tap(57,266)
            sleep(2)
            #好
            allow=s(id='好')
            if allow.exists:
                s(id='好').click()
            sleep(2)
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
            now0=time.strftime('%Y%m%d_%H%M%S')
            word.set_text('I love Shanghai_发布_'+now0)
            t0='I love Shanghai_发布_'+now0
            sleep(1)
            s(id='发布').click()
            sleep(2)
            #ios doesn't need to refresh
            #check numbers of pictures and published text here
            title=s(xpath='//XCUIElementTypeStaticText[contains(@name,t0)]')
            sleep(1)
            if title.exists :
                print('发布内容的文字检查通过')
            else:
                print('发布内容的文字检查失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorPublishText_R_stg_atx_tc003.png'
                c.screenshot(sf1)
            sleep(2)
            number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
            if number.exists:
                print('发布内容的上传9张图片检查通过')
            else:
                print('发布内容的上传9张图片检查失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R_stg_atx_tc003.png'
                c.screenshot(sf2)
            sleep(2)
            s(id='icon camera').click()
            sleep(2)
            word=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
            sleep(2)
            word.click()
            sleep(1)
            now0=time.strftime('%Y%m%d_%H%M%S')
            word.set_text('发布降序_'+now0)
            t='发布降序_'+now0
            sleep(1)
            s(id='发布').click()
            sleep(1)
            title0=s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextView').get().value
            if t in title0:
                print('发布降序排列验证检查通过')
                sleep(1)
            else:
                print('发布降序排列验证检查失败,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorPublishOrder_R_stg_atx_tc003.png'
                c.screenshot(sf3)
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_发布页面元素检查和发布功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginmp_tc004
#Purpose:检查用户用手机号+验证码重新登录app的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/28]
#*******************************************************
    def test_wode_loginmp_tc004(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用手机号码重新登录，如果已登录先退出账号----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择用手机号+验证码登录；step4检查登录的账号是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('客户重新登录账号----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        s.tap(67,100)
        sleep(1)
        s(className='XCUIElementTypeTextField')[0].click()
        sleep(1)
        s(className='XCUIElementTypeTextField')[0].set_text('98762396871')
        sleep(1)
        s(className='XCUIElementTypeTextField')[2].click()
        sleep(1)
        s(className='XCUIElementTypeTextField')[2].set_text('867129')
        #code.set_text('112233')
        #完成
        #s(id='Toolbar Done Button').click()
        sleep(1)
        s(xpath='//XCUIElementTypeButton[@name="注册/登录"]').click()
        sleep(5)
        s(id='返回').click()
        sleep(2)
        #s.swipe(50,300,50,500,0.5)
        #sleep(2)
        name=s(xpath='//XCUIElementTypeStaticText[@name="SamSTG"]')
        if name.exists:
            print('登录成功！')
            sleep(1)
        else:
            print('登录失败！')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf='../../test_report/ios/'+now+'_errornormalLogin_R_stg_atx_tc004.png'
            c.screenshot(sf)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_客户重新登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_visitor_tc005
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_visitor_tc005(self):
        print('TC_访客模式点击我的页面各个菜单，检查点:点击我的页面各个菜单是否跳转到用户登录页面----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3点击我的页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面;step5点击加入蔚来跳转页面是否正常显示;step6点击设置弹出页面是否正常显示;')
        print('step7用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
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
            now=time.strftime('%Y%m%d_%H%M%S')
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
            now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_访客模式点击我的页面各个菜单跳转页面----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnow_tc006
#Purpose:检查发现页面的发布功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_publishnow_tc006(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻功能----step1检查发现首页右上角+号是否存在')
        print('step2检查发布此刻按钮是否存在；step3发布功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片')
        print('step5检查发布文字是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_发布此刻----开始:'+now)
        sleep(1)
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
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        words.set_text('I love Shanghai:'+now0)
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
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf1='../../test_report/ios/'+now+'_errorText_R.png'
                            c.screenshot(sf1)
                        sleep(2)
                        number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                        if number.exists:
                            print('发布内容的上传9张图片检查通过')
                        else:
                            print('发布内容的上传9张图片检查失败，请检查原因')
                            now=time.strftime('%Y%m%d_%H%M%S')
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
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_发布此刻----结束:'+now)

#*******************************************************
#TC Name:test_wode_deletepublished_tc007
#Purpose:检查我的页面的删除已发布内容的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_deletepublished_tc007(self):
        print('TC_检查手机号码登录APP，检查点:我的——删除已发布的内容---step1点击我的页面发布;step2检查是否有已发布的内容,')
        print('有的话点击它进入详细页面再点击右上角按钮，执行删除动作;step3检查被删除的发布内容是否删除成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_删除已发布的内容----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(id='发布').click()
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[3]').click()
        sleep(2)
        p=s(className='XCUIElementTypeCell')
        if p.exists:
            s(xpath='//XCUIElementTypeStaticText[@name="SamSTG"]')[0].click()
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_删除已发布的内容----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwechat_tc008
#Purpose:检查用户能否用微信账号登录app
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_loginwechat_tc008(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微信登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微信登录；step4检查微信登录的账号是否正确')
        sleep(1)
        now=time.strftime('%Y%m%d_%H%M%S')
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
            name=s(id='SamSTG')
            if name.exists:
                print('微信登录成功！')
            else:
                print('微信登录失败！')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWechat_R.png'
                c.screenshot(sf0)
            sleep(1)
        else:
            print('微信登录按钮不存在，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R.png'
            c.screenshot(sf1)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_客户用微信登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwebo_tc009
#Purpose:检查用户能否用微博账号登录app
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_loginwebo_tc009(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微博登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微博登录；step4检查微博登录的账号是否正确')
        sleep(2)
        now=time.strftime('%Y%m%d_%H%M%S')
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
            name=s(xpath='//XCUIElementTypeStaticText[@name="SamSTG"]')
            if name.exists:
                print('微博登录成功！')
            else:
                print('微博登录失败！')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf0='../../test_report/ios/'+now+'_errorLoginWebo_R.png'
                c.screenshot(sf0)
        else:
            print('微博登录按钮不存在，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errorNoButton_R.png'
            c.screenshot(sf1)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_客户用微博登录账号----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tabcheck_tc010
#Purpose:检查发现页面tab上元素和推荐、此刻子tab页上元素是否存在
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_tabcheck_tc010(self):
        print('TC_检查用户模式打开APP，检查点:发现_tabUI检查功能----step1检查发现页面tab上各子tab元素是否存在;')
        print('step2检查推荐子tab页上各元素是否存在;step3检查此刻子tab页上各元素是否存在')
        now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_personalinfo_tc011
#Purpose:我的个人信息页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_personalinfo_tc011(self):
        print('TC_检查手机号码登录APP，检查点:个人信息页面上元素UI检查和相关元素的功能检查----step1进入个人信息页面；')
        print('step2个人信息页面上元素UI检查;step3检查点击头像的功能;step4检查昵称和简称是否可以编辑;step5检查性别是否')
        print('可以改变;step6检查常驻地区页面是否可以进入;step7检查地址管理页面是否可以进入;step8检查用户隐私条款页面')
        print('是否可以进入;step9检查修改的个人信息是否可以保存成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(id='SamSTG').click()
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
            nick=s(xpath='//XCUIElementTypeTextField[@value="SamSTG"]')
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
            intro=s(xpath='//XCUIElementTypeTextField[@value="Sam_STG"]')
            intro.click()
            sleep(1)
            c2=s(xpath='//XCUIElementTypeButton[@name="清除文本"]')
            if c2.exists:
                print('简介可以被编辑')
            else:
                print('简介不可以被编辑，请检查原因')
            sleep(1)
            #完成
            #s.tap(331,382)
            s(id='Toolbar Done Button').click()
            sleep(1)
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf='../../test_report/ios/'+now+'_errorSaveInfo_R.png'
                c.screenshot(sf)
            sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_products_tc013
#Purpose:惊喜页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*******************************************************
    def test_jingxi_products_tc013(self):
        print('TC_检查手机号码登录APP，检查点:惊喜页面上元素UI检查----step1惊喜页面上任意礼品的元素UI检查')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜——惊喜页面上元素UI检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        #s.swipe_up()
        sleep(2)
        #惊喜页面的各个元素是否存在
        c1=fun_giftui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素都检查完毕')
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜——惊喜页面上元素UI检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_instuninstversioncheck_tc015
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_instuninstversioncheck_tc015(self):
        print('TC_检查手机号码登录APP，检查点:兼容性测试：安装和卸载app功能----step1卸载app')
        print('step2检查app是否存在；step3重新安装app；step4检查app是不是最新/所需版本')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf='../../test_report/ios/'+now+'_errorVersonCheck_R.png'
                c.screenshot(sf)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_兼容性测试：安装和卸载app功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_scores_tc016
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_scores_tc016(self):
        print('TC_检查手机号码登录APP，检查点:积分明细页面上元素UI检查和相关元素的功能检查----step1进入积分明细页面；')
        print('step2页面上元素UI检查;step3检查点击积分规则按钮的功能')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(1)
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_livecast_tc017
#Purpose:发现页面资讯tab里直播功能流程及UI检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/12]
#*******************************************************
    def test_faxian_livecast_tc017(self):
        print('TC_检查手机号码登录APP，检查点:发现页面资讯tab里直播功能流程及UI检查----step1从发现页面资讯tab页找到一个直播')
        print('step2直播详情页面上元素UI检查;step3检查点击评论按钮的功能;step4检查发表评论成功后文章详情顶部的评论内容')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——资讯tab里直播功能流程及UI检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #资讯
        s(id='资讯').click()
        sleep(4)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').get().visible
        sleep(1)
        if ch.exists and ch0 == True:
            s(id='自动化专题').click()
            sleep(7)
            s.swipe(50,600,50,100,0.5)
            sleep(2)
            s(id='大叔自动化直播').click()
            sleep(6)
            #检查文章的各个元素是否存在
            c1=fun_livecastui_check(self)
            sleep(1)
            if c1 == True:
                print('直播详情页面各个被检查元素都检查完毕')
                sleep(2)
                """
                //XCUIElementTypeButton[@name="paly icon"]
                //XCUIElementTypeButton[@name="close curtain icon"]
                //XCUIElementTypeButton[@name="small screen full screen icon"]
                """
                #点击评论
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"你的观点")]').click()
                sleep(2)
                combtn=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeTextView')
                combtn.click()
                sleep(1)
                now0=time.strftime('%Y%m%d_%H%M%S')
                combtn.set_text('我用Python评论直播:'+now0)
                sleep(1)
                t0='我用Python评论直播:'+now0
                s(xpath='//XCUIElementTypeButton[@name="发布"]').click()
                sleep(1)
                #check published text here
                chk=s(id='该场直播已结束')
                if (not chk.exists):
                    print('直播评论发布检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorCommentSent_R_stg_tc017.png'
                    c.screenshot(sf1)
                    sleep(1)
                else:
                    print('直播评论发布检查成功')
                sleep(1)
            s(xpath='//XCUIElementTypeButton[@name="all page back black icon"]').click()
            sleep(2)
        else:
            print('自动化专题未找到,请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——资讯tab里直播功能流程及UI检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_remarkfriend_tc018
#Purpose:朋友页面对好友设置备注并检查备注是否生效
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_remarkfriend_tc018(self):
        print('TC_检查手机号码登录APP，检查点:对好友设置备注并检查备注是否生效----step1从朋友页面进入朋友列表页面')
        print('step2选择一个朋友进入朋友详细信息页面；step3检查点击设置备注按钮的功能;step4检查备注是否生效')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----开始:'+now)
        sleep(1)
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
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorRemark_R.png'
                    c.screenshot(sf1)
                sleep(2)   
            else:
                print('设置备注的按钮不存在，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorNoRemark_R.png'
                c.screenshot(sf2)
                sleep(1)
                s(id='取消').click()
                sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('没有好友可以设置备注，请先添加好友')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf3='../../test_report/ios/'+now+'_errorNoFriend_R.png'
            c.screenshot(sf3)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_article_tc019
#Purpose:发现页面推荐tab里文章元素UI检查和相关元素的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_article_tc019(self):
        print('TC_检查手机号码登录APP，检查点:发现页面推荐tab里文章元素UI检查和评论的功能检查----step1从发现页面推荐tab页找到一个文章')
        print('step2文章详情页面上元素UI检查;step3检查点击评论按钮的功能;step4检查发表评论成功后文章详情顶部的评论内容')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        s(id='发现').click()
        sleep(2)
        for i in range(9):
            s.swipe(50,600,50,50,0.5)
            sleep(0.5)
        s.swipe(50,600,50,300,0.5)
        sleep(2)
        #检查文章的各个元素是否存在
        c1=fun_articleui_check(self)
        sleep(2)
        if c1 == True:
            print('推荐tab里文章各个被检查元素都检查完毕')
            sleep(1)
            #点击评论
            s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[11]/XCUIElementTypeButton[3]').click()
            sleep(3)
            #s(id='写评论').click()
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"我也来说~")]').click()
            sleep(2)
            combtn=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
            combtn.click()
            sleep(1)
            now0=time.strftime('%Y%m%d_%H%M%S')
            combtn.set_text('我用Python评论文章:'+now0)
            sleep(1)
            t0='我用Python评论文章:'+now0
            s(xpath='//XCUIElementTypeButton[@name="Send"]').click()
            sleep(3)
            #check published text here
            title=s(xpath='//XCUIElementTypeStaticText[contains(@value,t0)]')
            if title.exists:
                print('评论的文字检查通过')
            else:
                print('评论的文字检查失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorComment_R_stg_tc019.png'
                c.screenshot(sf1)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_openmultichat_tc020
#Purpose:发现页面发起群聊功能的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_openmultichat_tc020(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查发现首页右上角+号是否存在；')
        print('step2检查点击+号后发起群聊按钮是否存在；step3发起群聊并发送内容功能是否正常；step4检查发布内容里文字是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                for i in range((b)-1):
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam")]')[i].click()
                    sleep(1)
                #确定    
                s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
                sleep(2)
                msg=s(id='chat_input_textView')
                msg.click()
                sleep(1)
                now0=time.strftime('%Y%m%d_%H%M%S')
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
                #print(t))
                if t.exists:
                    print('群聊的发送内容正确')
                else:
                    print('群聊的发送内容不正确，请检查')
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorMultiChatText_R.png'
                    c.screenshot(sf2)
                sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('发现_发起群聊功能----结束:'+now)

#*******************************************************************
#TC Name:test_pengyou_dismissmultichat_tc021
#Purpose:朋友页面群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊的功能检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************************
    def test_pengyou_dismissmultichat_tc021(self):
        print('TC_检查手机号码登录APP，检查点:朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊功能')
        print('step1进入已发起的群聊，检查踢人出群聊的功能是否正常;step2检查邀请朋友加入群聊的功能是否正常')
        print('step3检查解散并退出群聊的功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorDismissMultiChat_R.png'
                c.screenshot(sf3)
            sleep(2)
        else:
            print('没有群聊可以操作，请先发起群聊')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoMultiChat_R.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_add2basket_tc022
#Purpose:检查惊喜页面用户添加商品到购物车的功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*********************************************************************************************
    def test_jingxi_add2basket_tc022(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面用户添加商品到购物车的功能----step1进入惊喜页面')
        print('step2翻页找到所需兑换的商品；step3把商品加入购物车；step4点击购物车图标进入购物车页面')
        print('step5购物车页面UI检查')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        #s.swipe(50,580,50,100,0.5)
        sleep(2)
        u1=s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]')
        if u1.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]').click()
            sleep(9)
            #加入购物车
            add2b=s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]')
            sleep(2)
            if add2b.exists:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(3)
                s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(3)
                #点击购物车图标
                ###s(xpath='//XCUIElementTypeStaticText[@name="1"])').click()
                s.tap(84,694)
                sleep(6)
                #检查购物车页面ui
                chk=fun_cartui_check(self)
                if chk == True:
                    print('购物车页面UI检查成功')
                    sleep(1)
                else:
                    print('购物车页面UI检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorCartUI_R_stg_tc022.png'
                    c.screenshot(sf1)
                sleep(2)
                ###s(xpath='//XCUIElementTypeOther[1]/XCUIElementTypeOther').click()
                s.tap(37,41)
                sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
            s.tap(34,40)
            sleep(2)
            s.tap(34,40)
            sleep(2)
        else:
            print('需要兑换的商品不存在，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_basket2exchange_tc023
#Purpose:检查惊喜页面从购物车下单兑换商品的功能
#Pre-c#OS:iOS
#Device:iPhone7 Plus
#Post-conditions:N/A
#Modify History:created by Sam [2018/11/08]
#*********************************************************************************************
    def test_jingxi_basket2exchange_tc023(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_用户从购物车下单兑换商品的功能----step1进入惊喜页面')
        print('step2点击购物车图标进入购物车页面；step3点击编辑按钮进入编辑页面；step4改变所选商品的规格：颜色')
        print('step5改变所选商品的数量;step6改变收货地址;step7立即下单检查订单是否已提交')
        print('step8查看订单检查商品状态是否为未发货')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='惊喜').click()
        sleep(5)
        #点击购物车图标
        #s(xpath='//XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther').click()
        s.tap(371,41)
        sleep(6)
        #refresh
        #sleep(2)
        chk0=s(xpath='//XCUIElementTypeStaticText[contains(@name,"去添加点什么吧")]')
        sleep(1)
        if chk0.exists:
            print('购物车里没有商品，请先去惊喜页面添加')
            sleep(1)
        else:
            print('购物车里有商品')
            sleep(1)
            #检查购物车页面ui
            chk=fun_cartui_check(self)
            if chk == True:
                print('购物车页面UI检查成功')
                sleep(2)
                #285,43
                #s(xpath='//XCUIElementTypeOther[@name="编辑"]')[4].click()
                s.tap(371,41)
                sleep(6)
                try:
                    #改变商品数量
                    s.tap(372,314)
                    sleep(3)
                    #完成
                    #s(xpath='//XCUIElementTypeOther[@name="完成"]')[4].click()
                    s.tap(371,41)
                    sleep(2)
                    s(id='立即购买').click()
                    sleep(3)
                    #改变收货地址
                    ###s(xpath='//XCUIElementTypeOther[contains(@name,"赵子龙")]').click()
                    s.tap(374,160)
                    sleep(2)
                    #第二个地址
                    s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
                    sleep(2)
                    s(id='立即下单').click()
                    sleep(1)
                    s(id='确定').click()
                    sleep(3)
                    chk=s(xpath='//*[contains(@name,"订单已提交")]')
                    sleep(1)
                    if (not chk.exists):
                        print('订单已提交检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftOrder_R_stg_tc023.png'
                        c.screenshot(sf1)
                        sleep(2)
                    else:
                        print('订单已提交检查通过')
                        sleep(2)
                        #查看订单
                        s(id='查看订单').click()
                        sleep(6)
                        #检查商品状态
                        chk1=s(xpath='//XCUIElementTypeOther[contains(@name,"cake")]')
                        chk2=s(xpath='//XCUIElementTypeOther[contains(@name,"已付款")]')
                        sleep(1)
                        if chk1.exists and chk2.exists:
                            print('订单里商品状态检查通过')
                            sleep(1)
                        else:
                            print('订单里商品状态检查失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf1='../../test_report/ios/'+now+'_errorGiftStatus_R_stg_tc023.png'
                            c.screenshot(sf1)
                        sleep(2)
                except Exception as e:
                    print('发生异常：'+str(e))
                    sleep(2)
                    pass
            else:
                print('购物车页面UI检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorCartUI_R_stg_tc023.png'
                c.screenshot(sf1)
                sleep(2)
        s.tap(34,41)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_用户从购物车下单兑换商品的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_livecastshare_tc024
#Purpose:检查发现页面资讯tab下的直播的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/12]
#*******************************************************
    def test_faxian_livecastshare_tc024(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的直播的分享功能----step1进入发现页面资讯tab')
        print('step2检查直播是否存在；step3进入直播详细页面点右下角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的直播的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='资讯').click()
        sleep(4)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            s(id='自动化专题').click()
            sleep(7)
            s.swipe(50,600,50,100,0.5)
        sleep(2)
        u=s(id='大叔自动化直播')
        if u.exists:
            print('直播存在，检查通过')
            sleep(2)
            s(id='大叔自动化直播').click()
            sleep(6)
            #share
            s(xpath='//XCUIElementTypeButton[@name="icon share black"]').click()
            sleep(2)
            #微信
            wh=s(id='微信')
            if wh.exists:
                print('分享到微信按钮存在，检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
                sleep(8)
                s(id='王小龙').click()
                sleep(3)
                words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                sleep(2)
                if words.exists:
                    words.click()
                    sleep(1)
                    now0=time.strftime('%Y%m%d_%H%M%S')
                    s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('我用Python_直播微信好友:'+now0)
                    sleep(1)
                #发送
                s(id='发送').click()
                sleep(1)
                s(id='返回蔚来').click()
                sleep(0.5)
                #检查toast
                save1=s(id='分享成功')
                if save1.exists:
                    print('分享微信成功')
                else:
                    print('分享微信失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorsharewechat_R_stg_tc024.png'
                    c.screenshot(sf1)
                sleep(1)
            else:
                print('分享到微信按钮不存在，请检查原因')
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share black"]').click()
            sleep(2)
            #朋友圈
            pyq=s(id='微信朋友圈')
            if pyq.exists:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton').click()
                sleep(8)
                word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y%m%d_%H%M%S')
                word2.set_text('我用Python_直播朋友圈:'+now2)
                sleep(1)
                s(id='表情').click()
                sleep(1)
                s(id='完成').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                sleep(1)
                #私密, 仅自己可见
                s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                sleep(1)
                s(id='完成').click()
                sleep(2)
                #发表
                s(id='发表').click()
                sleep(1)
                #检查toast
                save2=s(id='分享成功')
                if save2.exists:
                    print('分享微信朋友圈成功')
                else:
                    print('分享微信朋友圈失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R_stg_tc024.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share black"]').click()
            sleep(2)
            #微博
            wb=s(id='新浪微博')
            if wb.exists:
                print('分享到新浪微博按钮存在，检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton').click()
                sleep(6)
                #ar=s(id='确认')
                ad=s(id='确定')
                if ad.exists:
                    s(id='确定').click()
                sleep(2)
                s(id='发送到分组').click()
                sleep(3)
                #仅自己可见
                #s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                s(id='仅自己可见').click()
                sleep(2)
                #发送
                s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                sleep(1)
                #检查toast
                save3=s(id='分享成功')
                if save3.exists:
                    print('分享微博成功')
                else:
                    print('分享微博失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errorsharewebo_R_stg_tc024.png'
                    c.screenshot(sf3)
                sleep(2)
            else:
                print('分享到微博按钮不存在，请检查原因')
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share black"]').click()
            sleep(2)
            #我的朋友
            mf=s(id='我的朋友')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(2)
                s(id='我的朋友').click()
                sleep(2)
                s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeButton').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                sleep(1)
                #发送
                #检查toast
                save4=s(id='分享成功')
                if save4.exists:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios'+now+'_errorsharemyfriend_R_stg_tc024.png'
                    c.screenshot(sf4)
                sleep(2)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(2)
            s(xpath='//XCUIElementTypeButton[@name="all page back black icon"]').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的直播的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_checkin_tc025
#Purpose:我的页面点击签到及检查当日签到积分是否能正常获得的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_checkin_tc025(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查我的页面右上角点击签到是否存在；')
        print('step2检查点击签到功能是否正常；step3到积分明细页面检查当日签到的积分是否已经获得')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        
        #点击签到accessibility_id('点击签到')
        chk=s(xpath='//XCUIElementTypeStaticText[@name="点击签到"]')
        if chk.exists:
            s(xpath='//XCUIElementTypeStaticText[@name="点击签到"]').click()
            sleep(1)
        else:
            print('今日已经签到过，请明日再来')
        sleep(2)
        #检查积分
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeButton[2]').click()
        sleep(2)
        cb=s(xpath='//XCUIElementTypeStaticText[@name="每日签到"]')
        #print(cb))
        nowtm=time.strftime('%Y.%m.%d')
        tm=s(xpath='//XCUIElementTypeStaticText[contains(@name, nowtm)]')
        sleep(1)
        if cb.exists and tm.exists:
            print('每日签到获取积分功能检查通过')
        else:
            print('每日签到获取积分功能检查失败，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errorCheckinScore_R.png'
            c.screenshot(sf2)
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_activity_tc026
#Purpose:我的页面活动详细页面UI检查
#OS:iOS
#Device:iPhone7 Plus
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/12]
#*******************************************************
    def test_wode_activity_tc026(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面我的活动里取消报名的功能---')
        print('step1进入我的->我的活动页面;step2点击已报名的活动；step3对活动详细页面进行UI元素检查')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——活动详细页面UI检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,600,50,100,0.5)
        sleep(2)
        #我的活动
        s(id='我的活动').click()
        sleep(3)
        ch=s(id='小龙自动化3（请勿报名）')
        if ch.exists:
            print('活动存在，检查通过')
            sleep(1)
            s(id='小龙自动化3（请勿报名）').click()
            sleep(8)
            #UI checking
            c1=fun_activityui_check(self)
            sleep(1)
            if c1 == True:
                print('活动详细页面上各个被检查元素都检查完毕')
            sleep(1)
            #返回
            ##s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('活动不存在，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errorNoJoinActivity_R_stg_tc026.png'
            c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——活动详细页面UI检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_onlinesupport_tc027
#Purpose:我的页面在线支持功能检查
#OS:iOS
#Device:iPhone7 Plus
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/14]
#*******************************************************
    def test_wode_onlinesupport_tc027(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面在线支持功能检查---')
        print('step1进入我的->在线支持页面;step2点击蔚来专员图标；step3聊天输入文本并检查发送文本是否存在')
        print('step4聊天输入表情；step5击蔚来专员电话按钮检查弹出呼叫是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——在线支持页面功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,650,50,100,1.0)
        sleep(2)
        #在线支持
        s(id='在线支持').click()
        sleep(3)
        #364,704
        #蔚来专员图标
        #s.tap(364,704)
        s(xpath='(//XCUIElementTypeOther[@name="在线支持"])[1]/XCUIElementTypeImage').click()
        sleep(3)
        edit=s(id='chat_input_textView')
        edit.click()
        sleep(0.5)
        edit.clear_text()
        sleep(0.5)
        now0=time.strftime('%H%M%S')
        edit.set_text('在线咨询'+now0)
        sleep(1)
        s(id='Send').click()
        sleep(2)
        ch=s(id='在线咨询'+now0)
        if ch.exists:
            print('聊天文本存在，检查通过')
            sleep(1)
        else:
            print('聊天文本不存在，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errNoChatText_R_stg_tc027.png'
            c.screenshot(sf2)
            sleep(2)
        #发送表情
        edit.click()
        sleep(0.5)
        edit.clear_text()
        sleep(0.5)
        s(id='chatting biaoqing btn normal').click()
        sleep(1)
        s.tap(39,554)
        sleep(1)
        s(id='发送').click()
        sleep(2)
        print('聊天发送表情完毕')
        sleep(1)
        #call
        s(xpath='//XCUIElementTypeNavigationBar[@name="蔚来专员"]/XCUIElementTypeButton[2]').click()
        sleep(1)
        tt=s(id='呼叫')
        if tt.exists:
            print('蔚来专员电话呼叫正常')
            sleep(1)
        else:
            print('蔚来专员电话呼叫不正常，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errCallSupport_R_stg_tc027.png'
            c.screenshot(sf1)
        sleep(2)
        s(id='取消').click()
        sleep(2)
        #返回
        s(id='chat back icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——在线支持页面功能检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_nicknameheadicon_tc028
#Purpose:朋友页面修改群聊昵称和头像功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_nicknameheadicon_tc028(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_修改群聊昵称和头像功能---step1检查朋友页面群聊是否存在；')
        print('step2进入群聊修改群组名称；step3检查群组名称是否修改成功；step4检查修改群组头像功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorNoMultichat_R.png'
                c.screenshot(sf3)
            sleep(2)
        except Exception as e:
            print('发生异常：'+str(e))
            sleep(1)
            pass
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_修改群聊名称和头像功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_searchwatch_tc029
#Purpose:朋友页面搜索好友并打开个人主页进行关注
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_searchwatch_tc029(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_朋友页面搜索好友并打开个人主页进行关注---')
        print('step1朋友页面点+号，检查添加朋友按钮是否存在；step2输入好友名称进行搜索；')
        print('step3点击搜索出的朋友打开他的个人主页；step4检查关注功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
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
            #print(ff))
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
                        now=time.strftime('%Y%m%d_%H%M%S')
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
            now=time.strftime('%Y%m%d_%H%M%S')
            sf3='../../test_report/ios/'+now+'_errorNoAddFriend_R.png'
            c.screenshot(sf3)
            sleep(2)
        s(id='all page back grey icon').click()  
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----结束:'+now)

#*******************************************************
#TC Name:test_wode_resetsecupwd_tc030
#Purpose:我的页面设置里重置服务安全密码的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_resetsecupwd_tc030(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点设置；')
        print('step2点击服务安全密码；step3检查重置服务安全密码的功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里重置服务安全密码的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe(150,600,150,100,0.5)
        sleep(2)
        s(id='设置').click()
        sleep(2)
        s(id='安全管理').click()
        sleep(2)
        #设置服务安全密码
        s(id='设置服务安全密码').click()
        sleep(3)
        code=s(className='XCUIElementTypeTextField')
        code.click()
        code.set_text('867129')
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
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errorResetSecupwd_R.png'
            c.screenshot(sf2)
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里重置服务安全密码的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_addeditaddress_tc031
#Purpose:我的页面里地址管理页面新增和编辑一个收货地址的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_wode_addeditaddress_tc031(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点击头像')
        print('step2点击编辑个人信息；step3点击我的地址进入地址管理页面;step4检查添加新地址的功能是否正常')
        print('step5检查编辑地址的功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_新增和编辑一个收货地址的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s(xpath='//XCUIElementTypeStaticText[@name="SamSTG"]').click()
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
            #old=name.get().value
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
                now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_新增和编辑一个收货地址的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershowpic_tc032
#Purpose:发现页面体验tab活动的晒图功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_expershowpic_tc032(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的晒图功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查晒图功能是否正常;step4检查晒图的文字是否正确')
        print('step5检查晒图的9张图片数量是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——体验tab活动的晒图功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(3)
        """
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        sleep(2)
        for i in range(2):
            s.swipe(150,550,150,100,0.5)
            sleep(2)
        sleep(1)
        """
        s(id='NIO DAY 选座活动之最后一版').click()
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
            now0=time.strftime('%Y%m%d_%H%M%S')
            word.set_text('人生苦短体验晒图:'+now0)
            sleep(1)
            s(id='发布').click()
            sleep(9)
            #s.swipe(150,500,150,200,0.5)
            #sleep(2)
            #check numbers of pictures and published text here
            title=s(xpath='//XCUIElementTypeTextView[contains(@value,"人生苦短体验晒图:")]')
            sleep(2)
            if title.exists:
                print('体验晒图的文字检查通过')
            else:
                print('体验晒图的文字检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorShowpicText_R.png'
                c.screenshot(sf1)
            sleep(2)
            number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
            if number.exists:
                print('体验晒图的上传9张图片检查通过')
            else:
                print('体验晒图的上传9张图片检查失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorPic9_R.png'
                c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(3)
        else:
            print('晒图按钮不存在/找不到，请检查原因')
            sleep(2)
        #s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
        s.tap(32,42)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——体验tab活动的晒图功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnowatfriend_tc033
#Purpose:检查发现页面的发布此刻并@好友的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_publishnowatfriend_tc033(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻并@好友的功能----step1检查发现首页右上角+号是否存在；')
        print('step2检查发布此刻按钮是否存在；step3发布并@好友功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片；')
        print('step5检查发布文字是否正确;step6退出当前账号并已@的好友账号登录app;step7检查朋友页面里是否收到@通知')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                now0=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorText_R.png'
                    c.screenshot(sf1)
                sleep(2)
                number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
                if number.exists:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_error#friend_R.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('发此刻按钮不存在，请检查原因')
                sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_发布此刻并@好友----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcshare_tc034
#Purpose:检查发现页面此刻tab下的ugc的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_ugcshare_tc034(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
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
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"SamSTG")]').click()
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
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
                words=s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]')
                sleep(1)
                if words.exists:
                    words.click()
                    sleep(1)
                    now0=time.strftime('%Y%m%d_%H%M%S')
                    sleep(0.5)
                    words.set_text('我用Python_UGC微信好友:'+now0)
                    sleep(1)
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
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorsharewechat_R_stg_tc034.png'
                    c.screenshot(sf1)
                sleep(1)
            else:
                print('分享到微信按钮不存在，请检查原因')
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
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
                now2=time.strftime('%Y%m%d_%H%M%S')
                word2.set_text('我用Python_UGC朋友圈:'+now2)
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
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R_stg_tc034.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
                sleep(1)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #微博
            wb=s(id='微博')
            if wb.exists:
                print('分享到微博按钮存在，检查通过')
                sleep(2)
                s(id='微博').click()
                sleep(5)
                if s(id='确定').exists:
                    s(id='确定').click()
                sleep(2)
                #发送
                s(id='发送到分组').click()
                sleep(2)
                s(id='仅自己可见').click()
                sleep(2)
                s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                sleep(0.35)
                #检查toast
                save3=s(id='分享成功')
                if save3.exists:
                    print('分享微博成功')
                else:
                    print('分享微博失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errorsharewebo_R_stg_tc034.png'
                    c.screenshot(sf3)
                sleep(2)
            else:
                print('分享到微博按钮不存在，请检查原因')
            sleep(2)
            #...
            s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
            sleep(2)
            #我的朋友
            mf=s(id='我的朋友')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(2)
                s(id='我的朋友').click()
                sleep(2)
                s(id='朋友').click()
                sleep(2)
                #Sam8201
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                sleep(1)
                #发送
                #检查toast
                save4=s(id='分享成功')
                if save4.exists:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios'+now+'_errorsharemyfriend_R_stg_tc034.png'
                    c.screenshot(sf4)
                sleep(2)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_此刻tab下的ugc的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcdel_tc035
#Purpose:检查发现页面此刻tab下的ugc的删除功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_ugcdel_tc035(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的...按钮；step4检查删除按钮是否存在')
        print('step5检查删除ugc功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_此刻tab下的ugc的删除功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='此刻').click()
        sleep(3)
        u=s(className='XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            my=s(xpath='//XCUIElementTypeStaticText[@name="SamSTG"]')
            sleep(2)
            #print(my))
            if my.exists:
                s(id='SamSTG').click()
                sleep(2)
                #...
                s(xpath='//XCUIElementTypeButton[@name="icon share gray background new"]').click()
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
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorDelUgc_R_stg_tc035.png'
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_此刻tab下的ugc的删除功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_im_tc036
#Purpose:检查朋友页面IM聊天信息复制、删除、撤回、转发
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_pengyou_im_tc036(self):
        print('TC_检查手机号码登录APP，检查点:朋友_IM聊天信息复制、删除、撤回、转发功能----step1朋友页面找到一个朋友发起聊天')
        print('step2发送一条消息；step3检查复制消息功能；step4检查删除消息功能')
        print('step5检查转发消息功能;step6检查撤回消息功能')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----开始:'+now)
        sleep(1)
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
        sleep(2)
        s(id='friends go friendlist').click()
        sleep(3)
        u=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam2")]')
        if u.exists:
            u.click()
            sleep(3)
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
                #s(id='im closed 3').click()
                #sleep(2)
            else:
                print('转发消息按钮不存在，请检查原因')
            sleep(2)
            #新发一条im
            s(id='chat_input_textView').click()
            sleep(1)
            s(id='chat_input_textView').set_text('测试撤回im')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----结束:'+now)
    
#*******************************************************
#TC Name:test_faxian_infopgcshare_tc037
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/29]
#*******************************************************
    def test_faxian_infopgcshare_tc037(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的pgc的分享功能----step1进入发现页面资讯tab')
        print('step2PGC的UI检查；step3进入pgc文章页面点右下角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #此刻
        s(id='资讯').click()
        sleep(4)
        for i in range(18):
            s.swipe(150,660,150,50,0.5)
            sleep(1)
        s.swipe(150,200,150,300,0.5)
        sleep(2)
        #检查发现页面资讯tab下的pgc的的各个元素是否存在
        c1=fun_pgcui_check(self)
        if c1 == True:
            print('发现页面资讯tab下的pgc的各个被检查元素都检查完毕')
            sleep(1)
        u=s(id='小龙投票stg')
        ch0=s(id='小龙投票stg').displayed
        if u.exists and ch0 == True:
            print('PGC:小龙投票stg存在，检查通过')
            sleep(2)
            s(id='小龙投票stg').click()
            sleep(5)
            #左上角按钮
            sh=s(xpath='//XCUIElementTypeOther[@name="小龙投票stg"]/XCUIElementTypeOther[2]')
            if sh.exists:
                print('分享按钮存在，检查通过')
                sleep(2)
                s.tap(382,42)
                sleep(2)
                #微信
                wh=s(id='微信')
                if wh.exists:
                    print('分享到微信按钮存在，检查通过')
                    sleep(2)
                    s(id='微信').click()
                    sleep(7)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        sleep(0.5)
                        #s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短PGC微信好友:'+now0)
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短PGC微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.6)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                    else:
                        print('分享微信好友失败，请检查原因')
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorPGCsharewechat_R_stg_tc037.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382,42)
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
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    #word2.set_text('人生苦短PGC朋友圈:'+now2)
                    word2.set_text('人生苦短PGC朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorPGCsharewechatpyq_R_stg_tc037.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382,42)
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(9)
                    #发送
                    s(id='发送到分组').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorPGCsharewebo_R_stg_tc037.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382,42)
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(1)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(id='Sam0698Stg').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorPGCsharemyfriend_R_stg_tc037.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在，请检查原因')
                sleep(2)
            s.tap(32,42)
            sleep(2)
        else:
            print('PGC:小龙投票stg不存在/未找到，无法执行分享操作')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_experjoin_tc038
#Purpose:发现页面体验tab活动的报名功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_faxian_experjoin_tc038(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的报名功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查报名功能是否正常;step4进入我的->我的活动页面')
        print('step5点击查看行程单;step6检查活动订单里活动的时间是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——体验tab活动的报名功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(4)
        #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton[2]').click()
        #sleep(2)
        for i in range(2):
            s.swipe(150,600,100,80,0.5)
            sleep(2)
        #小龙自动化3（请勿报名）
        s(id='小龙自动化3（请勿报名）').click()
        sleep(4)
        #报名
        joins=s(xpath='//XCUIElementTypeLink[@name="报名"]')
        sleep(2)
        if joins.exists:
            print('报名按钮存在,检查通过')
            sleep(2)
            joins.click()
            sleep(4)
            #场次
            #s(xpath='//XCUIElementTypeStaticText[@name="10.24 / 00:00"]').click()
            #sleep(1)
            #s(xpath='//XCUIElementTypeStaticText[@name="粉丝票"]').click()
            #sleep(2)
            #+限购1张
            #s(xpath='//XCUIElementTypeButton[@name="+"]').click()
            #sleep(1)
            #s.swipe(150,550,150,50,0.5)
            #sleep(2)
            #姓
            name=s(className='XCUIElementTypeTextField')
            name.click()
            name.set_text('王镇声')
            sleep(1)
            s(id='完成').click()
            sleep(1)
            """
            s.tap(382,268)
            sleep(1)
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(1)
            #mobile
            mb=s(className='XCUIElementTypeTextField')[2]
            mb.click()
            sleep(1)
            mb.set_text('18930018807')
            sleep(1)
            s(id='完成').click()
            sleep(2)
            #证件类型
            s(id='证件类型').click()
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
            """
            #购买
            s(id='购买').click()
            sleep(1)
            #确认
            s(id='确认').click()
            sleep(6)
            #checking
            ch=s(xpath='//XCUIElementTypeStaticText[contains(@name,"预约成功")]')
            if not ch.exists:
                print('报名失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorJoin_R_stg_tc038.png'
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
                #s(id='all page back grey icon').click()
                #sleep(2)
                #我的
                s(id='我的').click()
                sleep(3)
                s.swipe(50,650,50,100,1.0)
                sleep(1)
                s(id='我的活动').click()
                sleep(3)
                #活动降序排列检查
                ch3=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeStaticText[1]').get().value
                if '小龙自动化3' in ch3:
                    print('活动降序排列检查通过')
                    sleep(1)
                else:
                    print('活动降序排列检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errorMyActivityOrder_R_stg_tc038.png'
                    c.screenshot(sf3)
                sleep(2)
                ch2=s(xpath='//XCUIElementTypeStaticText[contains(@value,"3月29日")]')
                if ch2.exists:
                    print('活动订单里活动时间检查通过')
                    sleep(1)
                else:
                    print('活动订单里活动时间检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorMyActivity_R.png'
                    c.screenshot(sf2)
                    sleep(2)
        else:
            print('报名按钮不存在，请检查原因')
        sleep(2)
        #s(id='all page back grey icon').click()
        s.tap(32,42)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现——体验tab活动的报名功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_canceljoin_tc039
#Purpose:我的页面我的活动里取消报名的功能
#OS:iOS
#Device:iPhone7 Plus
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_wode_canceljoin_tc039(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面我的活动里取消报名的功能---step1进入我的->我的活动页面')
        print('step2点击查看行程单；step3检查取消报名按钮是否存在;step4检查取消报名功能是否正常')
        print('step5检查活动订单里是否暂无活动预约')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——我的活动里取消报名的功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,650,50,100,1.0)
        sleep(1)
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
            """
            ch1=s(id='取消成功')
            if ch1.exists:
            """
            print('取消报名成功')
            sleep(8)
            s(id='all page back grey icon').click()
            sleep(2)
            s.swipe(50,650,50,100,1.0)
            sleep(1)
            #我的活动
            s(id='我的活动').click()
            sleep(3)
            #暂无活动预约
            ch2=s(xpath='//XCUIElementTypeStaticText[@name="小龙自动化3（请勿报名）"]')
            if not ch2.exists:
                print('我的预约活动已取消报名，检查通过')
                sleep(2)
            else:
                print('我的预约活动取消报名失败，请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf0='../../test_report/ios/'+now+'_errorActivityList_R_stg_tc039.png'
                c.screenshot(sf0)
                sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('取消报名按钮不存在，请检查原因')
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errorNoCancelJoin_R_stg_tc039.png'
            c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——我的活动里取消报名的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershare_tc040
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_faxian_expershare_tc040(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面体验tab下的活动的分享功能----step1进入发现页面体验tab')
        print('step2找到活动进入；step3检查并点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
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
                    words.click()
                    sleep(1)
                    now0=time.strftime('%Y%m%d_%H%M%S')
                    words.set_text('测试PGC微信好友:'+now0)
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
                    now=time.strftime('%Y%m%d_%H%M%S')
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
                now2=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
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
                    now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_giftshare_tc041
#Purpose:检查惊喜页面的商品的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_jingxi_giftshare_tc041(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面的商品的分享功能----step1进入惊喜页面')
        print('step2选择一款商品点击进入商品详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(6)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        sleep(2)
        u=s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]')
        if u.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(3)
            u.click()
            sleep(6)
            #分享图标
            share=s(xpath='//XCUIElementTypeOther[@name="横幅"]/XCUIElementTypeOther[3]')
            sleep(2)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s.tap(377,40)
                sleep(2)
                #微信
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('我用Python_Gift微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.5)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc041.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(377,40)
                sleep(2)
                #朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('我用Python_Gift微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc041.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(377,40)
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    if s(id='确定').exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(3)
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(0.35)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc041.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(377,40)
                sleep(2)
                #我的朋友
                mf=s(id='NIO好友')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(1)
                    s(id='NIO好友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
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
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面的商品的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_visitor_tc042
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:android
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/10]
#*******************************************************
    def test_jingxi_visitor_tc042(self):
        print('TC_访客模式点击我的页面各个菜单，检查点:惊喜_惊喜页面的商品详细页面的访客模式检查----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择一款商品点击进入商品详细页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('惊喜_惊喜页面的商品详细页面的访客模式检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #惊喜
        s(id='惊喜').click()
        sleep(6)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        sleep(2)
        u=s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]')
        if u.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]').click()
            sleep(6)
            f=fun_getjingxiloginmenu(self)
            sleep(2)
            #check the menu by turn
            for j in range(0,2):
                s(xpath=f[0][j]).click()
                sleep(2)
                print('检查的元素名称：'+f[1][j])
                sleep(1)
                bp_is_loginshow(self)
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(2)
            #机器人图标
            s.tap(34, 701)
            sleep(2)
            bp_is_loginshow(self)
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            #购物车图标
            s.tap(76, 701)
            sleep(2)
            bp_is_loginshow(self)
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            #s(xpath='//XCUIElementTypeOther[@name="横幅"]/XCUIElementTypeOther[1]').click()
            s.tap(29, 40)
            sleep(2)
            s(id='我的').click()
            sleep(3)
            bp_normalloginmp(self)
            sleep(2)
        else:
            print('需要兑换的商品不存在/未找到，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面的商品详细页面的访客模式检查----结束:'+now)

#************************************************************************************************************
#TC Name:test_jingxi_cartcheck_tc043
#Purpose:检查用户模式选择多款商品加入购物车后购物车图标角标的变化检查
#OS:android
#Device:iPhone7 Plus
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
        sleep(1)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('惊喜_选择多款商品加入购物车后购物车图标角标的变化检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(6)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        sleep(2)
        u1=s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]')
        if u1.exists:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            u1.click()
            sleep(6)
            add2b=s(id='加入购物车')
            sleep(2)
            if add2b.exists:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                add2b.click()
                sleep(3)
                add2b.click()
                sleep(3)
                #购物车角标
                ch1=s(xpath='//XCUIElementTypeStaticText[@name="1"]')
                if ch1.exists:
                    print('购物车图标角标数字为1检查成功')
                    sleep(2)
                    #点击购物车图标
                    #s(xpath='//XCUIElementTypeStaticText[@name="1"]').click()
                    s.tap(84,694)
                    sleep(4)
                    ch1a=s(xpath='//XCUIElementTypeOther[contains(@name,"已选(1)")]')
                    if ch1a.exists:
                        print('购物车详细页面左下角显示已选(1)检查通过')
                    else:
                        print('购物车详细页面左下角显示已选(1)检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1a='../../test_report/ios/'+now+'_errorCartGift1a_R.png'
                        c.screenshot(sf1a)
                    sleep(2)
                    s.tap(37, 42)
                    sleep(2)
                    s.tap(34, 58)
                    sleep(2)
                    s.tap(34, 58)
                    sleep(2)
                    #driver.swipe(50,500,50,300,1000)
                    #sleep(3)
                    u2=s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]')
                    if u2.exists:
                        print('需要兑换的商品2存在，检查通过')
                        sleep(2)
                        u2.click()
                        sleep(8)
                        add2b=s(id='加入购物车')
                        sleep(2)
                        add2b.click()
                        sleep(3)
                        add2b.click()
                        sleep(3)
                        #购物车角标
                        ch1=s(xpath='//XCUIElementTypeStaticText[@name="2"]')
                        if ch1.exists:
                            print('购物车图标角标数字为2检查成功')
                            sleep(2)
                            #点击购物车图标
                            #s(xpath='//XCUIElementTypeStaticText[@name="2"]').click()
                            s.tap(84,694)
                            sleep(4)
                            ch2a=s(xpath='//XCUIElementTypeOther[contains(@name,"已选(2)")]')
                            if ch2a.exists:
                                print('购物车详细页面左下角显示已选(2)检查通过')
                            else:
                                print('购物车详细页面左下角显示已选(2)检查失败，请检查原因')
                                sleep(1)
                                now=time.strftime('%Y%m%d_%H%M%S')
                                sf2a='../../test_report/ios/'+now+'_errorCartGift2a_R.png'
                                c.screenshot(sf2a)
                            sleep(2)
                            s.tap(37, 42)
                            sleep(2)
                            s.tap(34, 58)
                            sleep(2)
                            s.tap(34, 58)
                            sleep(2)
                        else:
                            print('购物车图标角标数字为2检查失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf2='../../test_report/android/'+now+'_errorCartGift2_R.png'
                            c.screenshot(sf2)
                        sleep(2)
                    else:
                        print('需要兑换的商品2不存在/未找到，请重新挑选')
                        sleep(2)
                else:
                    print('购物车图标角标数字为1检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/android/'+now+'_errorCartGift1_R.png'
                    c.screenshot(sf1)
                    sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
                s.tap(34, 58)
                sleep(2)
        else:
            print('需要兑换的商品1不存在/未找到，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_选择多款商品加入购物车后购物车图标角标的变化检查----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_clearcart_tc044
#Purpose:检查用户模式惊喜选择多款商品加入购物车后清空购物车的功能检查
#OS:android
#Device:iPhone7 Plus
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
        sleep(1)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('惊喜_选择多款商品加入购物车后清空购物车的功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(6)
        for i in range(7):
            s.swipe(50,580,50,90,0.5)
            sleep(1)
        sleep(2)
        u1=s(xpath='//XCUIElementTypeOther[@name="cake cake 2"]')
        if u1.exists:
            print('需要兑换的商品1存在，检查通过')
            sleep(2)
            u1.click()
            sleep(6)
            add2b=s(id='加入购物车')
            sleep(2)
            if add2b.exists:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                add2b.click()
                sleep(3)
                add2b.click()
                sleep(3)
                s.tap(34, 58)
                sleep(2)
                s.tap(34, 58)
                sleep(2)
                u2=s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]')
                if u2.exists:
                    print('需要兑换的商品2存在，检查通过')
                    sleep(2)
                    u2.click()
                    sleep(6)
                    add2b=s(id='加入购物车')
                    sleep(2)
                    add2b.click()
                    sleep(3)
                    add2b.click()
                    sleep(3)
                    #点击购物车图标
                    s(xpath='//XCUIElementTypeStaticText[@name="2"]').click()
                    sleep(4)
                    ch2a=s(xpath='//XCUIElementTypeOther[@name="编辑"]')
                    if ch2a.exists:
                        print('编辑按钮存在，检查通过')
                        sleep(2)
                        #s(xpath='//XCUIElementTypeOther[@name="编辑"]')[4].click()
                        s.tap(371, 41)
                        sleep(2)
                        #s(xpath='//XCUIElementTypeOther[contains(@name,"全选")]').click()
                        s.tap(35, 694)
                        sleep(2)
                        #删除所选
                        s(id='删除所选').click()
                        sleep(1)
                        s(id='确定').click()
                        sleep(3)
                        chk0=s(xpath='//XCUIElementTypeStaticText[@name=" 去添加点什么吧 "]')
                        sleep(2)
                        if chk0.exists:
                            print('购物车已清空')
                            sleep(1)
                        else:
                            print('购物车未被清空，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf3='../../test_report/ios/'+now+'_errorCartNoEdit_R.png'
                            c.screenshot(sf3)
                            sleep(2)
                            s.tap(37, 42)
                            sleep(2)
                    else:
                        print('编辑按钮不存在，检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2a='../../test_report/ios/'+now+'_errorCartNoEdit_R.png'
                        c.screenshot(sf2a)
                    sleep(2)
                    s.tap(37, 42)
                    sleep(2)
                else:
                    print('需要兑换的商品2不存在/未找到，请重新挑选')
                    sleep(2)
            else:
                print('加入购物车按钮不存在，请检查原因')
                sleep(2)
                s.tap(34, 41)
                sleep(2)
        else:
            print('需要兑换的商品1不存在/未找到，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_选择多款商品加入购物车后清空购物车的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_activityshow_tc046
#Purpose:检查用户模式点击我的页面各个菜单的预期动作
#OS:android
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/15]
#*******************************************************
    def test_wode_activityshow_tc046(self):
        print('TC_用户模式点击我的我的活动菜单，检查点:我的_我的活动晒图功能检查----')
        print('step1进入我的活动页面；step2检查是否有晒图按钮；step3检查晒图功能是否正常')
        print('step4检查晒图的文字是否正确;step5检查晒图的9张图片数量是否正确')
        sleep(1)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的活动晒图功检查----开始:'+now)
        sleep(2)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,600,50,300,1.0)
        sleep(2)
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
            now0=time.strftime('%Y%m%d_%H%M%S')
            word.set_text('我Python晒图_'+now0)
            t0='我Python晒图_'+now0
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
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorPublishText_R_tc046.png'
                c.screenshot(sf1)
            sleep(2)
            number=s(xpath='//XCUIElementTypeStaticText[@name="9"]')
            if number.exists:
                print('晒图的上传9张图片检查通过')
            else:
                print('晒图的上传9张图片检查失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorPublishPicture9_R_tc046.png'
                c.screenshot(sf2)
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
        else:
            print('晒图按钮不存在，请检查原因')
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的活动晒图功检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_es8ordershare_tc047
#Purpose:检查我的ES8订单的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_wode_es8ordershare_tc047(self):
        print('TC_检查手机号码登录APP，检查点:我的_我的ES8订单的分享功能----step1进入我的页面')
        print('step2进入我的es8订单点击进入订单详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的ES8订单的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(4)
        s(id='我的车辆订单').click()
        sleep(6)
        #订单排序检查
        ordername=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]').get().value
        if 'ES8六座版' in ordername:
            print('我的车辆订单降序排列检查通过')
            sleep(1)
        else:
            print('我的车辆订单降序排列检查失败,请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf0='../../test_report/ios/'+now+'_errorCarorderList_R_stg_tc047.png'
            c.screenshot(sf0)
        sleep(1)
        car=s(id='ES8基准版')
        if car.exists:
            s(id='ES8基准版').click()
            sleep(4)
            #分享图标
            share=s(id='navigationbar btn share')
            sleep(2)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微信好友
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短我的ES8订单微信好友:'+now0)
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
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_stg_tc047.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微信朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(9)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短我的ES8订单微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_stg_tc047.png'
                        c.screenshot(sf2)
                    sleep(2)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                sleep(2)
                """
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微博no such menu now
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(8)
                    s(id='发送到分组').click()
                    sleep(2)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_stg_tc047.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                """
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #NIO好友
                mf=s(xpath='//XCUIElementTypeStaticText[@name="NIO好友"]')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="NIO好友"]').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_stg_tc047.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            #s.tap(24, 58)
            s(id='navigationbar btn back black1').click()   
            sleep(2)
        else:
            print('暂无订单，无法执行该脚本')
            sleep(2)
            s(id='navigationbar btn back black1').click()   
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的ES8订单的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_joinnio_tc048
#Purpose:检查我的页面加入蔚来功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_wode_joinnio_tc048(self):
        print('TC_检查手机号码登录APP，检查点:我的_我的_加入蔚来----step1进入我的页面')
        print('step2进入加入蔚来页面；step3点击蔚来总部；step4点击软件开发')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_加入蔚来----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,550,50,100,1.0)
        sleep(2)
        s(id='加入蔚来').click()
        sleep(6)
        #蔚来总部
        s.tap(208,268)
        #s(xpath='//XCUIElementTypeOther[@name="NIO"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]').click()
        sleep(4)
        #软件开发
        s.tap(208,242)
        #s(xpath='//XCUIElementTypeOther[@name="NIO"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]').click()
        sleep(4)
        #允许
        allow=s(id='允许')
        if allow.exists:
            s(id='允许').click()
            sleep(2)
        #好
        allow2=s(id='好')
        if allow2.exists:
            s(id='好').click()
            sleep(2)
        #s.swipe(50,550,50,200,1.0)
        sleep(2)
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"工程师")]')
        if ch1.exists:
            print('产品开发职位显示正常')
            sleep(1)
        else:
            print('产品开发职位显示不正常，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errDevJobs_R_stg_tc048.png'
            c.screenshot(sf1)
        sleep(2)
        #s(id='返回').click()
        #sleep(2)
        s(id='返回“蔚来Test”').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_加入蔚来----结束:'+now)

#*******************************************************
#TC Name:test_aiche_cityplan_tc049
#Purpose:检查爱车页面里查询上海市城市服务规划
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_cityplan_tc049(self):
        print('TC_检查手机号码登录APP，检查点:爱车_查询上海市城市服务规划----step1进入爱车页面')
        print('step2点击城市服务查询页面；step3选择山西省->太原市;step4检查太原市城市服务规划是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_查询太原市城市服务规划----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        city=s(id='城市服务查询')
        ch0=s(id='城市服务查询').displayed
        if city.exists and ch0 == True:
            print('城市服务查询按钮找到')
            sleep(2)
            s(id='城市服务查询').click()
            #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[4]').click()
            sleep(6)
            s(id='上海市').click()
            sleep(2)
            s(id='山西省').click()
            sleep(2)
            s(id='太原市').click()
            sleep(4)
            #代客上牌
            ch1=s(id='NIO城市服务规划')
            ch2=s(id='太原市')
            ch3=s(id='代客上牌')
            if ch1.exists and ch2.exists and ch3.exists:
                print('太原市城市服务规划显示正常')
                sleep(1)
            else:
                print('太原市城市服务规划显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errSHcityplan_R_stg_tc049.png'
                c.screenshot(sf1)
            sleep(2)
            s(id='nav back btn').click()
            sleep(2)
        else:
            print('城市服务查询按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_查询太原市城市服务规划----结束:'+now)

#*******************************************************
#TC Name:test_aiche_rechargemap_tc050
#Purpose:检查爱车页面里查询充电地图及查看充电桩信息
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_rechargemap_tc050(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图及查看充电桩信息----step1进入爱车页面')
        print('step2点击充电地图；step3点击一个充电桩;step4检查充电桩信息是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图及查看充电桩信息----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[5]').click()
            sleep(4)
            #page=driver.page_source
            sleep(2)
            #8号充电桩
            #driver.find_element_by_id('cn.com.weilaihui3:id/charging_pile_drag_view').click()
            s.tap(287,272)
            sleep(4)
            ch1=s(id='上海曹安景林苑充电站')
            if ch1.exists:
                print('充电桩信息显示正常')
                sleep(1)
            else:
                print('充电桩信息显示不正常，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errPileStatus_R_tc050.png'
                c.screenshot(sf1)
            sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图及查看充电桩信息----结束:'+now)

#*******************************************************
#TC Name:test_aiche_milecalculator_tc051
#Purpose:检查爱车页面里ES8里程计算器
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_milecalculator_tc051(self):
        print('TC_检查手机号码登录APP，检查点:爱车_ES8里程计算器----step1进入爱车页面')
        print('step2点击ES8里程计算器；step3改变行驶速度;step4改变车外温度;step5打开空调;step6改变轮毂尺寸检查里程计算是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8里程计算器----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe_up()
            sleep(1)
        s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='ES8里程计算器')
        if cmap.exists:
            print('ES8里程计算器按钮找到')
            sleep(2)
            s(id='ES8里程计算器').click()
            sleep(4)
            #page=driver.page_source
            #sleep(2)
            s.swipe(50,530,50,503,1.0)
            sleep(2)
            #改变行驶速度
            #>
            s.tap(324, 373)
            sleep(1)
            res1=s(id='393')
            if res1.exists:
                print('改变行驶速度后里程计算正确')
                sleep(1)
            else:
                print('改变行驶速度后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errMileV_R_tc051.png'
                c.screenshot(sf1)
            sleep(2)
            #改变车外温度>
            s.tap(175, 476)
            sleep(1)
            s.tap(175, 476)
            sleep(1)
            res2=s(id='387')
            if res2.exists:
                print('改变车外温度后里程计算正确')
                sleep(1)
            else:
                print('改变车外温度后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errMileTemp_R_tc051.png'
                c.screenshot(sf2)
            sleep(2)
            #打开空调
            s(id='OFF').click()
            sleep(1)
            res3=s(id='309')
            if res3.exists:
                print('打开空调后里程计算正确')
                sleep(1)
            else:
                print('打开空调后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errMileAir_R_tc051.png'
                c.screenshot(sf3)
            sleep(2)
            #改变轮毂尺寸
            s(id='21英寸').click()
            sleep(1)
            res4=s(id='301')
            if res4.exists:
                print('改变轮毂尺寸后里程计算正确')
                sleep(1)
            else:
                print('改变轮毂尺寸后里程计算不正确，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errMileDem_R_tc051.png'
                c.screenshot(sf4)
            sleep(2)
            s(id='nav back btn').click()
            sleep(2)
        else:
            print('ES8里程计算器按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8里程计算器----结束:'+now)

#*******************************************************
#TC Name:test_aiche_es8content_tc052
#Purpose:检查爱车页面ES8配置表浏览及分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/10/25]
#*******************************************************
    def test_aiche_es8content_tc052(self):
        print('TC_检查手机号码登录APP，检查点:爱车_ES8配置表浏览及分享功能----step1进入爱车页面')
        print('step2进入ES8配置表；step3点右上角的分享按钮（先检查是否存在)')
        print('step4检查个性化、选装包、附件tab页能否正常切换')
        print('step5检查分享微信好友功能是否正常;step6检查分享微信朋友圈功能是否正常')
        print('step7检查分享微博好友功能是否正常;step8检查分享NIO好友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8配置表浏览及分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='详细配置表')
        ch0=s(id='详细配置表').displayed
        if cmap.exists and ch0 == True:
            print('详细配置表按钮找到')
            sleep(2)
            s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[6]').click()
            #s(id='详细配置表').click()
            sleep(6)
            #
            #s(xpath='//XCUIElementTypeStaticText[@name="个性化"]').click()
            s(id='个性化').click()
            sleep(3)
            s(id='选装包').click()
            sleep(3)
            s(id='附件').click()
            sleep(3)
            #分享图标
            share=s(id='nav share btn')
            sleep(2)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信好友
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短我的ES8订单微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.5)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc052.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短我的ES8订单微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc052.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(8)
                    s(id='发送到分组').click()
                    sleep(2)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc052.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到微博按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #NIO好友
                mf=s(id='NIO好友')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(1)
                    s(id='NIO好友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(0.3)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc052.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            s(id='nav back btn').click()   
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8配置表浏览及分享功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_giftexchange_noaddress_tc055
#Purpose:检查惊喜页面用户无收货地址时购买商品的功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/04]
#*********************************************************************************************
    def test_jingxi_giftexchange_noaddress_tc055(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面用户添加商品到购物车的功能----step1进入个人信息页面删除所有的地址信息')
        print('step2进入惊喜页面翻页找到所需兑换的商品；step3把商品加入购物车；step4点击购物车图标进入购物车页面')
        print('step5立即下单;step6添加新的收货地址后保存再下单;step7检查我的精品订单里的商品状态')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面用户无收货地址时购买商品的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_deleteaddress(self)
        sleep(1)
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        for i in range(5):
            s.swipe_up()
            sleep(1)
        #s.swipe(50,300,50,450,1.0)
        sleep(2)
        u1=s(xpath='//XCUIElementTypeOther[@name="充气懒人沙发(自动化专用) (自动化专用) 1"]')
        if u1.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="充气懒人沙发(自动化专用) (自动化专用) 1"]').click()
            sleep(9)
            #加入购物车
            add2b=s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]')
            sleep(2)
            if add2b.exists:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[@name="加入购物车"]').click()
                sleep(3)
                #点击购物车图标
                ###s(xpath='//XCUIElementTypeStaticText[@name="1"])').click()
                s.tap(76, 632)
                sleep(6)
                s(id='立即购买').click()
                sleep(4)
                #添加新地址
                name=s(xpath='//*[contains(@name,"请输入收件人姓名")]')
                name.click()
                r=random.randint(10,99)
                sleep(1)
                name.set_text('测试'+str(r))
                sleep(1)
                pnum=s(xpath='//*[contains(@name,"请输入收件人手机号")]')
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
                sleep(2)
                s(id='立即购买').click()
                sleep(3)
                s(id='立即下单').click()
                sleep(1)
                s(id='确定').click()
                sleep(3)
                chk=s(xpath='//*[contains(@name,"订单已提交")]')
                sleep(1)
                if not chk.exists:
                    print('订单已提交检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorGiftOrder_R_stg_tc023.png'
                    c.screenshot(sf1)
                    sleep(2)
                else:
                    print('订单已提交检查通过')
                    sleep(2)
                    #查看订单
                    s(id='查看订单').click()
                    sleep(6)
                    #检查商品状态
                    chk1=s(xpath='//XCUIElementTypeOther[contains(@name,"充气懒人沙发(自动化专用) (自动化专用) 1")]')
                    chk2=s(xpath='//XCUIElementTypeOther[contains(@name,"已付款")]')
                    sleep(1)
                    if chk1.exists and chk2.exists:
                        print('订单里商品状态检查通过')
                        sleep(1)
                    else:
                        print('订单里商品状态检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftStatus_R_stg_tc055.png'
                        c.screenshot(sf1)
                    sleep(2)
            s.tap(34, 40)
            sleep(2)
        else:
            print('需要兑换的商品不存在，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_惊喜页面用户无收货地址时购买商品的功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_lightenchina4carowner_tc056
#Purpose:检查车主从爱车页面进入点亮中国首页的校验功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/04]
#*********************************************************************************************
    def test_aiche_lightenchina4carowner_tc056(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主从爱车页面进入点亮中国首页的校验----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面检查点亮中国入口文案')
        print('step4点击点亮中国入口检查页面跳转是否正常')
        print('step5点设置按钮进入车辆信息页面关闭参与点亮中国开关;step6返回爱车页面检查点亮中国入口是否显示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_车主从爱车页面进入点亮中国首页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp_carowner(self)
        sleep(1)
        #爱车
        s(id='爱车').click()
        sleep(2)
        #服务安全密码
        pin=s(id='请输入服务安全密码')
        if pin.exists:
            s(id='1').click()
            sleep(0.3)
            s(id='1').click()
            sleep(0.3)
            #s(id='2').click()
            s.tap(206, 539)
            sleep(0.3)
            #s(id='2').click()
            s.tap(206, 539)
            sleep(0.3)
            #s(id='3').click()
            s.tap(345, 539)
            sleep(0.3)
            #s(id='3').click()
            s.tap(345, 539)
            sleep(0.3)
        sleep(2)
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,400,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        #ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"个地标, 查看点亮中国进度")]')
        sleep(2)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"个城市被点亮")]')
            sleep(1)
            if ch2.exists:
                print('点亮中国页面跳转正常')
                sleep(1)
            else:
                print('点亮中国页面跳转不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorLightenChinaPage_R_stg_tc056.png'
                c.screenshot(sf2)
            sleep(2)
            s.tap(32, 42)
            sleep(2)
        else:
            print('点亮中国入口文案检查通过失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errorLightenChinaTextOn_R_stg_tc056.png'
            c.screenshot(sf1)
        sleep(2)
        s.swipe_up()
        sleep(2)
        #设置
        s(id='vehicle setting icon').click()
        sleep(4)
        s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
        #s.tap(330, 616)
        sleep(1)
        s(id='我知道了').click()
        sleep(2)
        print('参与点亮中国开关已关闭')
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,450,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        #ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"个地标, 查看点亮中国进度")]')
        sleep(2)
        if not ch1.exists:
            print('点亮中国入口不显示检查通过')
            sleep(1)
        else:
            print('点亮中国入口不显示检查通过失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf3='../../test_report/ios/'+now+'_errorLightenChinaTextOff_R_stg_tc056.png'
            c.screenshot(sf3)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_车主从爱车页面进入点亮中国首页的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_mylighted4carowner_tc057
#Purpose:检查车主在点亮中国首页中点击我已点亮的校验测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_aiche_mylighted4carowner_tc057(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面点击进入点亮中国首页')
        print('step4点击我已点亮')
        print('step5点击导航按钮确认查看推送toast是否正确;step6点击第一个地标进入检查页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击我已点亮的校验测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(2)
        #服务安全密码
        pin=s(id='请输入服务安全密码')
        if pin.exists:
            s(id='1').click()
            sleep(0.2)
            s(id='1').click()
            sleep(0.2)
            s.tap(206, 539)
            sleep(0.2)
            s.tap(206, 539)
            sleep(0.2)
            s.tap(345, 539)
            sleep(0.2)
            s.tap(345, 539)
            sleep(0.2)
        sleep(2)
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,400,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        sleep(2)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            #我已点亮
            s(xpath='//XCUIElementTypeLink[contains(@name,"我已点亮")]').click()
            sleep(5)
            #refresh
            s.swipe_up()
            sleep(2)
            #导航按钮
            #s(xpath='//XCUIElementTypeOther[4]/XCUIElementTypeLink[1]/XCUIElementTypeLink[3]').click()
            s.tap(349, 205)
            sleep(1)
            #发送
            s(id='发送').click()
            sleep(0.2)
            ch1=s(id='地址已推送至你的爱车')
            if ch1.exists:
                print('地址推送toast显示正常')
                sleep(1)
            else:
                print('地址推送toast显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorMyLightedPushAddress_R_stg_tc057.png'
                c.screenshot(sf2)
            sleep(2)
            #1st address
            addr1=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeLink[1]/XCUIElementTypeLink[1]')
            ch2=addr1.get_attribute('label')
            sleep(1)
            addr1.click()
            sleep(3)
            addr1a=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText')
            ch2a=addr1a.get_attribute('label')
            sleep(1)
            if ch2a in ch2:
                print('地标详细页面显示正常')
                sleep(1)
            else:
                print('地标详细页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_error1stAddressDetail_R_stg_tc057.png'
                c.screenshot(sf3)
            sleep(2)
            #返回
            #(32,42)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(3)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(5)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(2)
        else:
            print('点亮中国入口不显示，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc057.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击我已点亮的校验测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_myexplored4carowner_tc058
#Purpose:检查车主在点亮中国首页中点击我已探索的校验测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_aiche_myexplored4carowner_tc058(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面点击进入点亮中国首页')
        print('step4点击我已探索')
        print('step5点击导航按钮确认查看推送toast是否正确;step6点击第一个地标进入检查页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击我已探索的校验测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,400,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        sleep(2)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            #我已探索
            s(xpath='//XCUIElementTypeLink[contains(@name,"我已探索")]').click()
            sleep(5)
            #refresh
            s.swipe_up()
            sleep(2)
            #导航按钮
            #s(xpath='//XCUIElementTypeLink[1]/XCUIElementTypeLink[3]').click()
            s.tap(349, 205)
            sleep(1)
            #发送
            s(id='发送').click()
            #sleep(0.2)
            ch1=s(id='地址已推送至你的爱车')
            if ch1.exists:
                print('地址推送toast显示正常')
                sleep(1)
            else:
                print('地址推送toast显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorMyExploredPushAddress_R_stg_tc058.png'
                c.screenshot(sf2)
            sleep(2)
            #1st address
            addr1=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeLink[1]/XCUIElementTypeLink[1]')
            ch2=addr1.get_attribute('label')
            #print(ch2)
            addr1.click()
            sleep(5)
            addr1a=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText')
            ch2a=addr1a.get_attribute('label')
            #print(ch2a)
            if ch2a in ch2:
                print('地标详细页面显示正常')
                sleep(1)
            else:
                print('地标详细页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_error1stAddressDetail_R_stg_tc058.png'
                c.screenshot(sf3)
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(2)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(4)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(2)
        else:
            print('点亮中国入口不显示，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc058.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击我已探索的校验测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_myvisitedcity4carowner_tc059
#Purpose:检查车主在点亮中国首页中点击到过的城市的校验测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_aiche_myvisitedcity4carowner_tc059(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面点击进入点亮中国首页')
        print('step4点击到过的城市')
        print('step5点击第一个到过的城市进入检查城市地图页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击到过的城市的校验测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,400,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        sleep(2)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            #到过的城市
            s(xpath='//XCUIElementTypeLink[contains(@name,"到过的城市")]').click()
            sleep(5)
            #refresh
            s.swipe_up()
            sleep(2)
            #2nd address:上海市
            addr1=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeLink[2]')
            #ch2=addr1.get_attribute('label')
            addr1.click()
            sleep(5)
            addr1a=s(id='上海博物馆')
            if addr1a.exists:
                print('到过的城市的详细地图页面显示正常')
                sleep(1)
            else:
                print('到过的城市的详细地图页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_error1stCityMap_R_stg_tc059.png'
                c.screenshot(sf3)
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(4)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(4)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(2)
        else:
            print('点亮中国入口不显示，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc059.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国首页中点击到过的城市的校验测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_explorenearbymore4carowner_tc060
#Purpose:检查车主在点亮中国首页中点击到过的城市的校验测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_aiche_explorenearbymore4carowner_tc060(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面点击进入点亮中国首页')
        print('step4点击到过的城市')
        print('step5点击第一个到过的城市进入检查城市地图页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国入口中点击探索附近的查看更多按钮的校验测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        #s.swipe(50,400,50,50,1.0)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        sleep(2)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            for i in range(1):
                s.swipe_up()
                sleep(2)
            s.swipe(5,550,5,300,1.0)
            sleep(2)
            #查看更多
            s(id='查看更多').click()
            sleep(8)
            addr1a=s(id='嘉定图书馆')
            if addr1a.exists:
                print('查看更多的详细地图页面显示正常')
                sleep(2)
                #site=s(id='嘉定图书馆')
                #sleep(2)
                #缩放
                fun_zoom(self)
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_siteZoom_R_stg_tc060.png'
                c.screenshot(sf1)
                sleep(2)
                fun_pinch(self)
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_sitePinch_R_stg_tc060.png'
                c.screenshot(sf2)
                sleep(2)
            else:
                print('查看更多的详细地图页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorMoreMap_R_stg_tc060.png'
                c.screenshot(sf3)
            sleep(2)
            #返回
            #(32,42)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(4)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(4)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(2)
        else:
            print('点亮中国入口不显示，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc060.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_点亮中国入口中点击探索附近的查看更多按钮的校验测试的校验测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_lightenchina4carowner_tc061
#Purpose:检查车主从发现页面资讯tab进入点亮中国首页的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_lightenchina4carowner_tc061(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主从发现页面资讯tab进入点亮中国首页的校验----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3点击发现页面的资讯tab')
        print('step4翻页找到点亮中国跳转的文章点击进入;step5检查我已点亮、我已探索、到过的城市3个按钮')
        print('step6检查此地标无人探索，快来点亮地标吧、我与n位车主探索过此地标文案和导航按钮')
        print('step7点击导航按钮确认查看推送toast是否正确;step8点击点亮中国说明按钮检查跳转页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_从发现页面资讯tab进入点亮中国首页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s(id='发现').click()
        sleep(4)
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #3个检查点
            ch1=s(xpath='//XCUIElementTypeLink[contains(@name,"我已点亮")]')
            ch2=s(xpath='//XCUIElementTypeLink[contains(@name,"我已探索")]')
            ch3=s(xpath='//XCUIElementTypeLink[contains(@name,"到过的城市")]')
            sleep(2)
            if ch1.exists and ch2.exists and ch3.exists:
                print('我已点亮、我已探索、到过的城市3个按钮找到')
                sleep(1)
            else:
                print('我已点亮、我已探索、到过的城市3个按钮未找到，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorNo3Buttons_R_stg_tc061.png'
                c.screenshot(sf3)
            sleep(2)
            #探索附近
            #s.swipe(250,700,250,200,1.0)
            s.swipe_up()
            sleep(2)
            #3个检查点
            chk1=s(xpath='//XCUIElementTypeStaticText[@name="此地标无人探索，快来点亮地标吧"]')
            chk2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"位车主探索过此地标")]')
            chk3=s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[7]/XCUIElementTypeLink[3]')
            sleep(1)
            #print(chk1))
            #print(chk2))
            #print(chk3))
            if chk1.exists and chk2.exists and chk3.exists:
                print('此地标无人探索，快来点亮地标吧、我与n位车主探索过此地标文案和导航按钮检查通过')
                sleep(1)
            else:
                print('此地标无人探索，快来点亮地标吧、我与n位车主探索过此地标文案和导航按钮检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorNearby_R_stg_tc061.png'
                c.screenshot(sf3)
            sleep(2)
            #导航按钮
            #安亭老街
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[7]/XCUIElementTypeLink[3]').click()
            s.tap(349, 124)
            sleep(1)
            #发送
            s(id='发送').click()
            #sleep(0.2)
            ch0=s(id='地址已推送至你的爱车')
            if ch0.exists:
                print('地址推送toast显示正常')
                sleep(1)
            else:
                print('地址推送toast显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorNearbyPushAddress_R_stg_tc061.png'
                c.screenshot(sf2)
            sleep(2)
            #问号
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[1]').click()
            sleep(5)
            ch2=s(xpath='//XCUIElementTypeStaticText[@name="点亮中国说明"]')
            if ch2.exists:
                print('点亮中国说明页面显示正常')
                sleep(1)
            else:
                print('点亮中国说明页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorQuestionPage_R_stg_tc061.png'
                c.screenshot(sf2)
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(3)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(3)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc061.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_从发现页面资讯tab进入点亮中国首页的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_mapswitch4carowner_tc062
#Purpose:检查车主从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_mapswitch4carowner_tc062(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3点击发现页面的资讯tab')
        print('step4翻页找到点亮中国跳转的文章点击进入;step5点击地图查看省/市列表')
        print('step6点击安徽省再点击合肥市,已点亮、待点亮、全部按钮切换;step7点击右上角全部地标')
        print('step8点击导航按钮确认查看推送toast是否正确;step9已点亮、待点亮、全部按钮切换')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        pin=s(id='请输入服务安全密码')
        if pin.exists:
            s(id='1').click()
            sleep(0.2)
            s(id='1').click()
            sleep(0.2)
            s.tap(206, 539)
            sleep(0.2)
            s.tap(206, 539)
            sleep(0.2)
            s.tap(345, 539)
            sleep(0.2)
            s.tap(345, 539)
            sleep(0.2)
        sleep(2)
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            #s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s(id='发现').click()
        sleep(4)
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(4)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(13)
            #地图
            #108,220
            s.tap(108, 220)
            sleep(5)
            #refresh
            s.swipe_up()
            sleep(2)
            #安徽省
            s(xpath='//XCUIElementTypeLink[contains(@name,"安徽省")]').click()
            sleep(2)
            #refresh
            s.swipe_up()
            sleep(2)
            s(xpath='//XCUIElementTypeLink[contains(@name,"合肥市")]').click()
            sleep(6)
            s(id='已点亮').click()
            sleep(2)
            s(id='待点亮').click()
            sleep(2)
            s(id='全部').click()
            sleep(2)
            #全部地标
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink').click()
            sleep(6)
            #refresh
            #s.swipe_up()
            #sleep(2)
            #导航按钮
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[1]/XCUIElementTypeLink[3]').click()
            sleep(1)
            #发送
            s(id='发送').click()
            #sleep(0.2)
            ch0=s(id='地址已推送至你的爱车')
            if ch0.exists:
                print('地址推送toast显示正常')
                sleep(1)
            else:
                print('地址推送toast显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorAllPushAddress_R_stg_tc062.png'
                c.screenshot(sf2)
            sleep(2)
            s(id='已点亮').click()
            sleep(2)
            s(id='待点亮').click()
            sleep(2)
            s(id='全部').click()
            sleep(2)
            #返回
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(3)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(3)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(3)
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(3)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc062.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_lightenchina4noncarowner_tc063
#Purpose:检查非车主从发现页面资讯tab进入点亮中国首页的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:非车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_lightenchina4noncarowner_tc063(self):
        print('TC_检查手机号码登录APP，检查点:爱车_非车主从发现页面资讯tab进入点亮中国首页的校验----')
        print('step1非车主用户点击发现页面的资讯tab')
        print('step2翻页找到点亮中国跳转的文章点击进入;step3检查我已点亮、我已探索、到过的城市3个按钮')
        print('step4检查探索附近、此地标无人探索，快来点亮地标吧、快来成为第n位探索者吧文案文案')
        print('step5检查最地标、蔚来探索榜显示是否正常')
        print('step6点击点亮中国说明按钮检查跳转页面是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主从发现页面资讯tab进入点亮中国首页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp(self)
        sleep(1)
        s(id='发现').click()
        sleep(3)
        s(id='资讯').click()
        sleep(3)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_value('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        #ch0=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').displayed
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #3个检查点
            ch1=s(xpath='//XCUIElementTypeLink[contains(@name,"我已点亮")]')
            ch2=s(xpath='//XCUIElementTypeLink[contains(@name,"我已探索")]')
            ch3=s(xpath='//XCUIElementTypeLink[contains(@name,"到过的城市")]')
            sleep(2)
            if (not ch1.exists) and (not ch2.exists) and (not ch3.exists):
                print('非车主:我已点亮、我已探索、到过的城市3个按钮不显示,检查通过')
                sleep(1)
            else:
                print('非车主:我已点亮、我已探索、到过的城市3个按钮显示，检查不通过,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_error3ButtonsShow_R_stg_tc063.png'
                c.screenshot(sf1)
            sleep(2)
            #探索附近
            s.swipe(5,500,5,150,1.0)
            sleep(2)
            #2个检查点
            chk1=s(xpath='//XCUIElementTypeStaticText[@name="此地标无人探索，快来点亮地标吧"]')
            chk2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"位探索者吧")]')
            chk3=s(xpath='//XCUIElementTypeStaticText[@name="探索附近"]')
            sleep(1)
            if chk1.exists and chk2.exists and chk3.exists:
                print('探索附近、此地标无人探索，快来点亮地标吧、快来成为第n位探索者吧文案检查通过')
                sleep(1)
            else:
                print('探索附近、此地标无人探索，快来点亮地标吧、快来成为第n位探索者吧文案检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorNearby_R_stg_tc063.png'
                c.screenshot(sf2)
            sleep(2)
            s.swipe(5,500,5,100,1.0)
            sleep(2)
            s.swipe(5,500,5,150,1.0)
            sleep(2)
            #最地标
            #2个检查点
            chk1=s(xpath='//XCUIElementTypeStaticText[@name="最地标"]')
            chk2=s(xpath='//XCUIElementTypeStaticText[@name="蔚来探索榜"]')
            sleep(1)
            if chk1.exists and chk2.exists:
                print('最地标、蔚来探索榜显示正常')
                sleep(1)
            else:
                print('最地标、蔚来探索榜显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorList_R_stg_tc063.png'
                c.screenshot(sf3)
            sleep(2)
            #问号
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[1]').click()
            sleep(5)
            ch2=s(xpath='//XCUIElementTypeStaticText[@name="点亮中国说明"]')
            if ch2.exists:
                print('点亮中国说明页面显示正常')
                sleep(1)
            else:
                print('点亮中国说明页面显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorQuestionPage_R_stg_tc061.png'
                c.screenshot(sf4)
            sleep(2)
            #返回
            #(32,42)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(5)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
            #x
            #s(id='evaluate close').click()
            #sleep(2)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf5='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc063.png'
            c.screenshot(sf5)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主从发现页面资讯tab进入点亮中国首页的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_lighted4noncarowner_tc064
#Purpose:检查非车主从发现页面资讯tab进入点亮中国首页的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:非车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_lighted4noncarowner_tc064(self):
        print('TC_检查手机号码登录APP，检查点:爱车_非车主点击已点亮的地标详情页的校验----')
        print('step1非车主用户点击发现页面的资讯tab')
        print('step2翻页找到点亮中国跳转的文章点击进入;step3点击已点亮的地标进入地标详细页面')
        print('step4对页面UI元素检查')
        print('step5检查我的探索和导航按钮不显示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主点击已点亮的地标详情页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        #ch0=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').displayed
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            s.swipe(5,500,5,200,1.0)
            #s.swipe_up()
            sleep(2)
            lighted=s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[4]/XCUIElementTypeLink[1]')
            sleep(1)
            lighted.click()
            sleep(6)
            #ui_check here
            s.swipe(5,500,5,300,1.0)
            sleep(2)
            c1=fun_lightedui_check(self)
            sleep(1)
            if c1 == True:
                print('非车主点击已点亮的地标详情页上各个被检查元素都检查完毕')
            sleep(1)
            #导航按钮
            ch1=s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[1]/XCUIElementTypeLink[3]')
            ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"我的探索")]')
            if (not ch1.exists) and (not ch2.exists):
                print('我的探索和导航按钮不显示,检查通过')
                sleep(1)
            else:
                print('我的探索和导航按钮显示，检查不通过,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorShouldnotShow_R_stg_tc064.png'
                c.screenshot(sf4)
            sleep(2)
            #返回
            #(32,42)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(5)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
            #x
            #s(id='evaluate close').click()
            #sleep(2)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf5='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc064.png'
            c.screenshot(sf5)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主点击已点亮的地标详情页的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_notlighted4noncarowner_tc065
#Purpose:检查非车主从发现页面资讯tab进入点亮中国首页的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:非车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_notlighted4noncarowner_tc065(self):
        print('TC_检查手机号码登录APP，检查点:爱车_非车主点击未点亮的地标详情页的校验----')
        print('step1非车主用户点击发现页面的资讯tab')
        print('step2翻页找到点亮中国跳转的文章点击进入;step3点击未点亮的地标进入地标详细页面')
        print('step4对页面UI元素检查')
        print('step5检查全部探索、我的探索和导航按钮不显示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主点击未点亮的地标详情页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(4)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        #ch0=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').displayed
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            s.swipe(5,600,5,200,1.0)
            sleep(2)
            #未点亮
            notlighted=s(xpath='//XCUIElementTypeStaticText[@name="此地标无人探索，快来点亮地标吧"]')
            notlighted.click()
            sleep(6)
            #ui_check here
            #s.swipe_up()
            #sleep(2)
            c1=fun_notlightedui_check(self)
            sleep(1)
            if c1 == True:
                print('非车主点击未点亮的地标详情页上各个被检查元素都检查完毕')
            sleep(1)
            #导航按钮
            ch1=s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[1]/XCUIElementTypeLink[3]')
            ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"我的探索")]')
            ch3=s(xpath='//XCUIElementTypeStaticText[contains(@name,"全部探索")]')
            if (not ch1.exists) and (not ch2.exists) and (not ch3.exists):
                print('全部探索、我的探索和导航按钮不显示,检查通过')
                sleep(1)
            else:
                print('全部探索、我的探索和导航按钮显示，检查不通过,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorShouldnotShow_R_stg_tc065.png'
                c.screenshot(sf4)
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(5)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
            #x
            #s(id='evaluate close').click()
            #sleep(2)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf5='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc065.png'
            c.screenshot(sf5)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主点击未点亮的地标详情页的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_mapswitch4noncarowner_tc066
#Purpose:检查非车主从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:非车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/11]
#*********************************************************************************************
    def test_faxian_mapswitch4noncarowner_tc066(self):
        print('TC_检查手机号码登录APP，检查点:发现_非车主地图-省/市列表页-地标互切的校验----')
        print('step1点击发现页面的资讯tab')
        print('step2翻页找到点亮中国跳转的文章点击进入;step3点击地图查看省/市列表')
        print('step4点击安徽省再点击合肥市,已点亮、待点亮、全部按钮切换;step5点击右上角全部地标')
        print('step6已点亮、待点亮、全部按钮切换')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        #ch0=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').displayed
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #地图
            #108,220
            s.tap(108, 220)
            sleep(5)
            #refresh
            s.swipe_up()
            sleep(2)
            #安徽省
            s(xpath='//XCUIElementTypeLink[contains(@name,"安徽省")]').click()
            sleep(2)
            #refresh
            s.swipe_up()
            sleep(2)
            s(xpath='//XCUIElementTypeLink[contains(@name,"合肥市")]').click()
            sleep(6)
            s(id='已点亮').click()
            sleep(3)
            s(id='待点亮').click()
            sleep(3)
            s(id='全部').click()
            sleep(3)
            #全部地标
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink').click()
            sleep(6)
            #refresh
            s.swipe_up()
            sleep(2)
            s(id='已点亮').click()
            sleep(2)
            s(id='待点亮').click()
            sleep(2)
            s(id='全部').click()
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(6)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32,42)
            sleep(3)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc066.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主从发现页面资讯tab进入点亮中国首页地图省/市列表页地标互切的校验----结束:'+now)

#*********************************************************************************************
#TC Name:test_aiche_moreandicon4carowner_tc067
#Purpose:检查车主在点亮中国首页中探索附近的查看更多按钮、最地标的更多按钮、蔚来探索榜中非神秘用户的头像的校验测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_aiche_moreandicon4carowner_tc067(self):
        print('TC_检查手机号码登录APP，检查点:爱车_车主在点亮中国首页点击我已点亮的校验测试----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面打开参与点亮中国开关；step3返回爱车页面点击进入点亮中国首页')
        print('step4点击探索附近的查看更多按钮的校验')
        print('step5点击最地标的更多按钮的校验,对最地标页面进行UI元素检查')
        print('step6点击蔚来探索榜中非神秘用户的头像的校验')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_车主在点亮中国首页中探索附近的查看更多按钮、最地标的更多按钮、蔚来探索榜中非神秘用户的头像的校验测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            print('参与点亮中国开关已打开')
            sleep(1)
        else:
            #s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            s.tap(350, 616)
            sleep(1)
            s(id='确定').click()
            sleep(2)
            print('参与点亮中国开关已手动打开')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(1)
        s.swipe_up()
        sleep(2)
        #已探索
        ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]')
        sleep(1)
        if ch1.exists:
            print('点亮中国入口文案检查通过')
            sleep(1)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"已探索")]').click()
            sleep(9)
            for i in range(1):
                s.swipe_up()
                sleep(1)
            #s.swipe(5,530,5,40,1.0)
            sleep(2)
            #查看更多
            s(xpath='//XCUIElementTypeLink[@name="查看更多"]').click()
            sleep(5)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(4)
            """
            for i in range(1):
                s.swipe_up()
                sleep(1)
            s.swipe(5,500,5,200,1.0)
            sleep(4)
            """
            #最地标:更多
            s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeLink[11]').click()
            #s(xpath='//XCUIElementTypeLink[contains(@name,"更多")]').click()
            sleep(6)
            print('最地标的更多按钮存在')
            sleep(2)
            c1=fun_mostsiteui_check(self)
            sleep(1)
            if c1 == True:
                print('最地标页面上各个被检查元素都检查完毕')
            sleep(2)
            #返回
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(4)
            for i in range(1):
                s.swipe_up()
                sleep(1)
            #s.swipe(5,500,5,300,1.0)
            sleep(2)
            #非神秘用户的头像3rd carowner
            s(xpath='//XCUIElementTypeStaticText[@name="ADAS_ACC"]').click()
            sleep(7)
            #checking
            ch2=s(xpath='//XCUIElementTypeStaticText[@name="关注"]')
            if ch2.exists:
                print('非神秘用户的个人信息页面显示正常')
                sleep(1)
            else:
                print('非神秘用户的个人信息页面显示不正常，检查不通过,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorPersonalInfo_R_stg_tc067.png'
                c.screenshot(sf4)
            sleep(2)
            s(id='full screen back icon').click()
            sleep(3)
            #返回
            s.tap(32, 42)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            sleep(2)
        else:
            print('点亮中国入口不显示，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc059.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_车主在点亮中国首页中探索附近的查看更多按钮、最地标的更多按钮、蔚来探索榜中非神秘用户的头像的校验测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_faxian_lightenchina4unauthcarowner_tc068
#Purpose:检查未授权的车主从发现页面资讯tab进入点亮中国首页的校验
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:车主用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/05]
#*********************************************************************************************
    def test_faxian_lightenchina4unauthcarowner_tc068(self):
        print('TC_检查手机号码登录APP，检查点:爱车_未授权的车主车主从发现页面资讯tab进入点亮中国首页的校验----step1车主用户进入爱车页面')
        print('step2点设置按钮进入车辆信息页面关闭参与点亮中国开关；step3点击发现页面的资讯tab')
        print('step4翻页找到点亮中国跳转的文章点击进入;step5检查解锁点亮中国，记录你与蔚来的故事文案、解锁按钮')
        print('step6点击解锁按钮,点击允许按钮')
        print('step7检查我已点亮、我已探索、到过的城市3个按钮是否显示,解锁按钮是否消失;step8点击爱车页面设置按纽')
        print('step9检查参与点亮中国开关是否已打开')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_未授权的车主车主从发现页面资讯tab进入点亮中国首页的校验----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(4)
        #服务安全密码
        #设置
        s(id='vehicle setting icon').click()
        sleep(5)
        swi=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
        c_swi=swi.get().value
        if c_swi == '1':
            #s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]').click()
            s.tap(350, 616)
            sleep(1)
            s(id='我知道了').click()
            sleep(2)
            print('参与点亮中国开关已手动关闭')
            sleep(1)
        else:
            print('参与点亮中国开关已关闭')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='发现').click()
        sleep(4)
        s(id='资讯').click()
        sleep(4)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('点亮中国跳转')
        sleep(2)
        #search
        s(id='Search').click()  
        sleep(4)
        """
        for i in range(19):
            s.swipe_up()
            sleep(1)
        sleep(2)
        """
        #点亮中国跳转
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        #ch0=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').displayed
        sleep(1)
        if ch.exists:
            print('资讯tab点亮中国跳转已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #2个检查点
            ch1=s(xpath='//XCUIElementTypeStaticText[@name="解锁点亮中国，记录你与蔚来的故事"]')
            ch2=s(xpath='//XCUIElementTypeLink[@name="解锁"]')
            sleep(2)
            if ch1.exists and ch2.exists:
                print('解锁点亮中国，记录你与蔚来的故事文案、解锁按钮找到')
                sleep(1)
            else:
                print('解锁点亮中国，记录你与蔚来的故事文案、解锁按钮未找到，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errorNoButtons_R_stg_tc068.png'
                c.screenshot(sf3)
            sleep(2)
            s(xpath='//XCUIElementTypeLink[@name="解锁"]').click()
            sleep(2)
            s(id='允许').click()
            sleep(3)
            #4个检查点
            c1=s(xpath='//XCUIElementTypeLink[contains(@name,"我已点亮")]')
            c2=s(xpath='//XCUIElementTypeLink[contains(@name,"我已探索")]')
            c3=s(xpath='//XCUIElementTypeLink[contains(@name,"到过的城市")]')
            c4=s(xpath='//XCUIElementTypeLink[@name="解锁"]')
            sleep(2)
            if c1.exists and c2.exists and c3.exists and (not c4.exists):
                print('我已点亮、我已探索、到过的城市3个按钮显示,解锁按钮消失,检查通过')
                sleep(1)
            else:
                print('我已点亮、我已探索、到过的城市3个按钮未显示,解锁按钮未消失，检查不通过,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorAuthied_stg_tc068.png'
                c.screenshot(sf1)
            sleep(2)
            #(32,42)
            #s(xpath='//XCUIElementTypeOther[@name="点亮中国"]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(3)
            s(id='evaluate close').click()
            sleep(3)
            #爱车
            s(id='爱车').click()
            sleep(4)
            #设置
            s(id='vehicle setting icon').click()
            sleep(5)
            swi2=s(xpath='//XCUIElementTypeSwitch[@name="参与点亮中国"]')
            c_swi2=swi2.get().value
            if c_swi2 == '1':
                print('参与点亮中国开关已打开,验证通过')
                sleep(1)
            else:
                print('参与点亮中国开关未打开,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errorSetting_stg_tc068.png'
                c.screenshot(sf2)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('资讯tab点亮中国跳转未找到，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNoLightenChina_stg_tc061.png'
            c.screenshot(sf4)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_未授权的车主车主从发现页面资讯tab进入点亮中国首页的校验----结束:'+now)

#*******************************************************
#TC Name:test_faxian_experjoincancel_tc069
#Purpose:发现页面体验tab活动的报名及立即取消报名功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/30]
#*******************************************************
    def test_faxian_experjoincancel_tc069(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——发现_体验tab活动的报名并立即取消报名---')
        print('step1发现页面里点击体验tab')
        print('step2翻页找到一个报名活动；step3检查报名功能是否正常')
        print('step4完成报名后在活动订单详细页面里点击取消报名')
        print('step5取消成功后到我的——>我的活动里检查该报名活动是否存在')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_体验tab活动的报名并立即取消报名功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(4)
        """
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]').click()
        sleep(2)
        #s.swipe(50,550,50,150,1.0)
        #sleep(2)
        s(id='蔚来中心丨上海太古汇店1112121312').click()
        sleep(2)
        """
        for i in range(2):
            s.swipe(150,600,150,80,0.5)
            sleep(1)
        sleep(2)
        #小龙自动化2
        s(id='小龙自动化3（请勿报名）').click()
        sleep(4)
        #报名
        joins=s(xpath='//XCUIElementTypeLink[@name="报名"]')
        sleep(2)
        if joins.exists:
            print('报名按钮存在,检查通过')
            sleep(2)
            s(xpath='//XCUIElementTypeLink[@name="报名"]').click()
            sleep(4)
            #场次
            #s(xpath='//XCUIElementTypeStaticText[contains(@name,"02/04")]').click()
            #sleep(1)
            #s(xpath='//XCUIElementTypeStaticText[contains(@name,"稍等哈活动")]').click()
            #sleep(2)
            #+限购1张
            #s(xpath='//XCUIElementTypeButton[@name="+"]').click()
            #sleep(1)
            #s.swipe(350,550,350,150,1.0)
            #sleep(2)
            #姓名
            name=s(className='XCUIElementTypeTextField')
            name.click()
            name.set_text('王振声')
            sleep(1)
            s(id='完成').click()
            sleep(1)
            """
            s.tap(382, 268)
            ##s(xpath='//XCUIElementTypeOther[@name="性别"]').click()
            sleep(1)
            #确定
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #mobile
            mb=driver.find_elements_by_class_name('XCUIElementTypeTextField')[1]
            mb.click()
            sleep(1)
            mb.set_text('18930018883')
            sleep(1)
            s(id='完成').click()
            sleep(1)
            #证件类别
            s(id='证件类别').click()
            sleep(1)
            #确定
            s(xpath='//XCUIElementTypeButton[contains(@name,"确定")]').click()
            sleep(2)
            #证件号码
            em=driver.find_elements_by_class_name('XCUIElementTypeTextField')[2]
            em.click()
            sleep(1)
            em.set_text('340103197301142518')
            sleep(1)
            s(id='完成').click()
            sleep(2)
            """
            #购买
            s(id='购买').click()
            sleep(1)
            #确认
            s(id='确认').click()
            sleep(6)
            #checking
            ch=s(xpath='//XCUIElementTypeStaticText[contains(@name,"预约成功")]')
            if not ch.exists:
                print('报名失败，请检查原因')
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorJoin_R_stg_tc069.png'
                c.screenshot(sf1)
                sleep(1)
            else:
                print('报名成功')
                sleep(1)
                s(id='完成').click()
                sleep(8)
                #活动清单详细页面
                for i in range(3):
                    s.swipe(250,350,250,100,0.5)
                sleep(1)
                ch0=s(xpath='//XCUIElementTypeStaticText[@name="取消报名"]')
                if ch0.exists:
                    print('取消报名按钮存在')
                    sleep(1)
                    s(xpath='//XCUIElementTypeStaticText[@name="取消报名"]').click()
                    sleep(1)
                    s(id='确认').click()
                    sleep(2)
                    ch1=s(id='取消成功')
                    if ch1.exists:
                        print('取消报名成功')
                        sleep(4)
                        s(id='完成').click()
                        sleep(3)
                        #32,42
                        #s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[1]').click()
                        s.tap(32, 42)
                        sleep(2)
                        s(id='我的').click()
                        sleep(2)
                        s.swipe(50,600,50,200,1.0)
                        sleep(2)
                        #我的活动
                        s(id='我的活动').click()
                        sleep(3)
                        #暂无活动预约
                        ch3=s(xpath='//XCUIElementTypeStaticText[@name="小龙自动化3（请勿报名）"]')
                        if not ch3.exists:
                            print('我的预约活动已取消报名，检查通过')
                            sleep(1)
                        else:
                            print('我的预约活动取消报名失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf0='../../test_report/ios/'+now+'_errorActivityList_R_stg_tc069.png'
                            c.screenshot(sf0)
                            sleep(2)
                        s(id='all page back grey icon').click()
                        sleep(2)
                    else:
                        print('取消报名失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorCancel_R_stg_tc069.png'
                        c.screenshot(sf3)
                        sleep(2) 
                else:
                    print('取消报名按钮不存在，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorNoCancel_R_stg_tc069.png'
                    c.screenshot(sf2)
                    sleep(2)
                    s(xpath='//XCUIElementTypeButton[@name="all page back black icon"]').click()
                    sleep(2)
        else:
            print('报名按钮不存在，请检查原因')
            sleep(2)
            s.tap(32, 42)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_体验tab活动的报名并立即取消报名----结束:'+now)

#*******************************************************
#TC Name:test_faxian_infospecialshare_tc070
#Purpose:检查发现页面资讯tab下的专题的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/17]
#*******************************************************
    def test_faxian_infospecialshare_tc070(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的专题的分享功能----step1进入发现页面资讯tab')
        print('step2进入专题文章页面,点右上角的分享按钮；step3检查分享微信好友功能是否正常')
        print('step4检查分享朋友圈功能是否正常;step5检查分享新浪微博功能是否正常;step6检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的专题的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(4)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('专题存在，检查通过')
            sleep(2)
            s(id='自动化专题').click()
            sleep(6)
            #左上角按钮
            sh=s(xpath='(//XCUIElementTypeOther[@name="自动化专题"])[1]/XCUIElementTypeOther[2]')
            if sh.exists:
                print('分享按钮存在，检查通过')
                sleep(2)
                s.tap(382, 42)
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
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短专题微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.2)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorSpecialsharewechat_R_stg_tc070.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382, 42)
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
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短专题朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                        sleep(1)
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorSpecialsharewechatpyq_R_stg_tc070.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382, 42)
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    ad=s(id='确定')
                    if ad.exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(3)
                    #仅自己可见
                    #s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    s(id='仅自己可见').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    #sleep(0.3379)
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorSpecialsharewebo_R_stg_tc070.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                s.tap(382, 42)
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(2)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(3)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                        sleep(1)
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorSpecialsharemyfriend_R_stg_tc070.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在，请检查原因')
                sleep(2)
            #s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在，无法执行分享操作')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的专题的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_infoarticleshare_tc071
#Purpose:检查发现页面资讯tab下的文章的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/17]
#*******************************************************
    def test_faxian_infoarticleshare_tc071(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的专题的分享功能----step1进入发现页面资讯tab')
        print('step2进入专题文章的文章页面,点右上角的分享按钮；step3检查分享微信好友功能是否正常')
        print('step4检查分享朋友圈功能是否正常;step5检查分享新浪微博功能是否正常;step6检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的文章的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(3)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('专题存在，检查通过')
            sleep(2)
            s(id='自动化专题').click()
            sleep(3)
            s.swipe(50,600,50,100,0.5)
            sleep(2)
            ch1a=s(id='自动化文章')
            ch1=s(id='自动化文章').displayed
            sleep(1)
            if ch1a.exists and ch1 == True:
                print('自动化文章存在，检查通过')
                sleep(2)
                s(id='自动化文章').click()
                sleep(3)
                #左上角按钮
                sh=s(xpath='(//XCUIElementTypeOther[@name="自动化文章"])[1]/XCUIElementTypeOther[2]')
                if sh.exists:
                    print('分享按钮存在，检查通过')
                    sleep(2)
                    s.tap(382, 42)
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
                        words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                        sleep(2)
                        if words.exists:
                            words.click()
                            sleep(1)
                            now0=time.strftime('%Y%m%d_%H%M%S')
                            s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短自动化文章微信好友:'+now0)
                            sleep(1)
                        #发送
                        s(id='发送').click()
                        sleep(2)
                        s(id='返回蔚来').click()
                        sleep(0.2)
                        #检查toast
                        save1=s(id='分享成功')
                        if save1.exists:
                            print('分享微信好友成功')
                            sleep(1)
                        else:
                            print('分享微信好友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf1='../../test_report/ios/'+now+'_errorArticlesharewechat_R_stg_tc071.png'
                            c.screenshot(sf1)
                        sleep(2)
                    else:
                        print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
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
                        now2=time.strftime('%Y%m%d_%H%M%S')
                        word2.set_text('人生苦短自动化文章朋友圈:'+now2)
                        sleep(1)
                        s(id='表情').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                        sleep(1)
                        #私密, 仅自己可见
                        s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        #发表
                        s(id='发表').click()
                        sleep(1)
                        #检查toast
                        save2=s(id='分享成功')
                        if save2.exists:
                            print('分享朋友圈成功')
                            sleep(1)
                        else:
                            print('分享朋友圈失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf2='../../test_report/ios/'+now+'_errorArticlesharewechatpyq_R_stg_tc071.png'
                            c.screenshot(sf2)
                        sleep(1)
                    else:
                        print('分享到朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
                    sleep(2)
                    #微博
                    wb=s(id='微博')
                    if wb.exists:
                        print('分享到微博按钮存在，检查通过')
                        sleep(2)
                        s(id='微博').click()
                        sleep(8)
                        s(id='发送到分组').click()
                        sleep(3)
                        #仅自己可见
                        #s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                        s(id='仅自己可见').click()
                        sleep(2)
                        #发送
                        s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                        sleep(1)
                        #检查toast
                        save3=s(id='分享成功')
                        if save3.exists:
                            print('分享微博成功')
                            sleep(1)
                        else:
                            print('分享微博失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf3='../../test_report/ios/'+now+'_errorArticlesharewebo_R_stg_tc071.png'
                            c.screenshot(sf3)
                        sleep(1)
                    else:
                        print('分享到新浪微博按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
                    sleep(2)
                    #我的朋友
                    mf=s(id='我的朋友')
                    if mf.exists:
                        print('分享到我的朋友按钮存在，检查通过')
                        sleep(2)
                        s(id='我的朋友').click()
                        sleep(2)
                        s(id='朋友').click()
                        sleep(2)
                        s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                        sleep(1)
                        #检查toast
                        save4=s(id='分享成功')
                        if save4.exists:
                            print('分享我的朋友成功')
                            sleep(1)
                        else:
                            print('分享我的朋友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf4='../../test_report/ios/'+now+'_errorArticlesharemyfriend_R_stg_tc071.png'
                            c.screenshot(sf4)
                        sleep(1)
                    else:
                        print('分享到我的朋友按钮不存在，请检查原因')
                        sleep(2)
                else:
                    print('分享按钮不存在，请检查原因')
                    sleep(2)
                #s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[1]').click()
                s.tap(32, 42)
                sleep(2)
            else:
                print('自动化文章不存在，无法执行分享操作')
                sleep(2)
            s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的文章的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_infolinkshare_tc072
#Purpose:检查发现页面资讯tab下的链接文章的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/17]
#*******************************************************
    def test_faxian_infolinkshare_tc072(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的专题的分享功能----step1进入发现页面资讯tab')
        print('step2进入专题文章的链接文章页面,点右上角的分享按钮；step3检查分享微信好友功能是否正常')
        print('step4检查分享朋友圈功能是否正常;step5检查分享新浪微博功能是否正常;step6检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的链接文章的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(3)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').displayed
        if ch.exists and ch0 == True:
            print('专题存在，检查通过')
            sleep(2)
            s(id='自动化专题').click()
            sleep(3)
            s.swipe(50,600,50,100,0.5)
            sleep(2)
            ch1a=s(id='自动化链接')
            ch1=s(id='自动化链接').displayed
            sleep(1)
            if ch1a.exists and ch1 == True:
                print('链接文章存在，检查通过')
                sleep(2)
                s(id='自动化链接').click()
                sleep(4)
                #左上角按钮
                sh=s(xpath='//XCUIElementTypeOther[@name="蔚来"]/XCUIElementTypeOther[2]')
                if sh.exists:
                    print('分享按钮存在，检查通过')
                    sleep(2)
                    s.tap(382, 42)
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
                        words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                        sleep(2)
                        if words.exists:
                            words.click()
                            sleep(1)
                            now0=time.strftime('%Y%m%d_%H%M%S')
                            s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短链接文章微信好友:'+now0)
                            sleep(1)
                        #发送
                        s(id='发送').click()
                        sleep(2)
                        s(id='返回蔚来').click()
                        sleep(0.2)
                        #检查toast
                        save1=s(id='分享成功')
                        if save1.exists:
                            print('分享微信好友成功')
                            sleep(1)
                        else:
                            print('分享微信好友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf1='../../test_report/ios/'+now+'_errorLinksharewechat_R_stg_tc072.png'
                            c.screenshot(sf1)
                        sleep(2)
                    else:
                        print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
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
                        now2=time.strftime('%Y%m%d_%H%M%S')
                        word2.set_text('人生苦短链接文章朋友圈:'+now2)
                        sleep(1)
                        s(id='表情').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                        sleep(1)
                        #私密, 仅自己可见
                        s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        #发表
                        s(id='发表').click()
                        sleep(1)
                        #检查toast
                        save2=s(id='分享成功')
                        if save2.exists:
                            print('分享朋友圈成功')
                            sleep(1)
                        else:
                            print('分享朋友圈失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf2='../../test_report/ios/'+now+'_errorLinksharewechatpyq_R_stg_tc072.png'
                            c.screenshot(sf2)
                        sleep(1)
                    else:
                        print('分享到朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382,42)
                    sleep(2)
                    #微博
                    wb=s(id='微博')
                    if wb.exists:
                        print('分享到微博按钮存在，检查通过')
                        sleep(2)
                        s(id='微博').click()
                        sleep(8)
                        s(id='发送到分组').click()
                        sleep(3)
                        #仅自己可见
                        s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                        sleep(2)
                        #发送
                        s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                        sleep(1)
                        #检查toast
                        save3=s(id='分享成功')
                        if save3.exists:
                            print('分享微博成功')
                            sleep(1)
                        else:
                            print('分享微博失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf3='../../test_report/ios/'+now+'_errorLinksharewebo_R_stg_tc072.png'
                            c.screenshot(sf3)
                        sleep(1)
                    else:
                        print('分享到新浪微博按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
                    sleep(2)
                    #我的朋友
                    mf=s(id='我的朋友')
                    if mf.exists:
                        print('分享到我的朋友按钮存在，检查通过')
                        sleep(2)
                        s(id='我的朋友').click()
                        sleep(2)
                        s(id='朋友').click()
                        sleep(3)
                        s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                        sleep(1)
                        #检查toast
                        save4=s(id='分享成功')
                        if save4.exists:
                            print('分享我的朋友成功')
                            sleep(1)
                        else:
                            print('分享我的朋友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf4='../../test_report/ios/'+now+'_errorLinksharemyfriend_R_stg_tc072.png'
                            c.screenshot(sf4)
                        sleep(1)
                    else:
                        print('分享到我的朋友按钮不存在，请检查原因')
                        sleep(2)
                else:
                    print('分享按钮不存在，请检查原因')
                    sleep(2)
                #s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[1]').click()
                s.tap(32, 42)
                sleep(2)
            else:
                print('链接文章不存在，无法执行分享操作')
                sleep(2)
            s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的链接文章的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_infovoteshare_tc073
#Purpose:检查发现页面资讯tab下的投票的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/17]
#*******************************************************
    def test_faxian_infovoteshare_tc073(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的专题的分享功能----step1进入发现页面资讯tab')
        print('step2进入专题文章的投票页面,点右上角的分享按钮；step3检查分享微信好友功能是否正常')
        print('step4检查分享朋友圈功能是否正常;step5检查分享新浪微博功能是否正常;step6检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的投票的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        s(id='资讯').click()
        sleep(3)
        for i in range(10):
            s.swipe(50,580,50,90,0.5)
            sleep(0.5)
        sleep(2)
        ch=s(id='自动化专题')
        ch0=s(id='自动化专题').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('专题存在，检查通过')
            sleep(2)
            s(id='自动化专题').click()
            sleep(3)
            s.swipe(50,600,50,100,0.5)
            sleep(2)
            ch1a=s(id='自动化投票')
            ch1=s(id='自动化投票').displayed
            sleep(1)
            if ch1a.exists and ch1 == True:
                print('自动化投票存在，检查通过')
                sleep(2)
                s(id='自动化投票').click()
                sleep(3)
                #左上角按钮
                sh=s(xpath='(//XCUIElementTypeOther[@name="自动化投票"])[1]/XCUIElementTypeOther[2]')
                if sh.exists:
                    print('分享按钮存在，检查通过')
                    sleep(2)
                    s.tap(382, 42)
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
                        words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                        sleep(2)
                        if words.exists:
                            words.click()
                            sleep(1)
                            now0=time.strftime('%Y%m%d_%H%M%S')
                            s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短投票微信好友:'+now0)
                            sleep(1)
                        #发送
                        s(id='发送').click()
                        sleep(2)
                        s(id='返回蔚来').click()
                        sleep(0.2)
                        #检查toast
                        save1=s(id='分享成功')
                        if save1.exists:
                            print('分享微信好友成功')
                            sleep(1)
                        else:
                            print('分享微信好友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf1='../../test_report/ios/'+now+'_errorVotesharewechat_R_stg_tc073.png'
                            c.screenshot(sf1)
                        sleep(2)
                    else:
                        print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
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
                        now2=time.strftime('%Y%m%d_%H%M%S')
                        word2.set_text('人生苦短投票朋友圈:'+now2)
                        sleep(1)
                        s(id='表情').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                        sleep(1)
                        #私密, 仅自己可见
                        s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                        sleep(1)
                        s(id='完成').click()
                        sleep(2)
                        #发表
                        s(id='发表').click()
                        sleep(1)
                        #检查toast
                        save2=s(id='分享成功')
                        if save2.exists:
                            print('分享朋友圈成功')
                            sleep(1)
                        else:
                            print('分享朋友圈失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf2='../../test_report/ios/'+now+'_errorVotesharewechatpyq_R_stg_tc073.png'
                            c.screenshot(sf2)
                        sleep(1)
                    else:
                        print('分享到朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
                    sleep(2)
                    #微博
                    wb=s(id='微博')
                    if wb.exists:
                        print('分享到微博按钮存在，检查通过')
                        sleep(2)
                        s(id='微博').click()
                        sleep(8)
                        s(id='发送到分组').click()
                        sleep(2)
                        #仅自己可见
                        s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                        sleep(2)
                        #发送
                        s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                        sleep(1)
                        #检查toast
                        save3=s(id='分享成功')
                        if save3.exists:
                            print('分享微博成功')
                            sleep(1)
                        else:
                            print('分享微博失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf3='../../test_report/ios/'+now+'_errorVotesharewebo_R_stg_tc073.png'
                            c.screenshot(sf3)
                        sleep(1)
                    else:
                        print('分享到新浪微博按钮不存在，请检查原因')
                    sleep(2)
                    #share
                    s.tap(382, 42)
                    sleep(2)
                    #我的朋友
                    mf=s(id='我的朋友')
                    if mf.exists:
                        print('分享到我的朋友按钮存在，检查通过')
                        sleep(2)
                        s(id='我的朋友').click()
                        sleep(2)
                        s(id='朋友').click()
                        sleep(2)
                        s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                        sleep(1)
                        #检查toast
                        save4=s(id='分享成功')
                        if save4.exists:
                            print('分享我的朋友成功')
                            sleep(1)
                        else:
                            print('分享我的朋友失败，请检查原因')
                            sleep(1)
                            now=time.strftime('%Y%m%d_%H%M%S')
                            sf4='../../test_report/ios/'+now+'_errorVotesharemyfriend_R_stg_tc073.png'
                            c.screenshot(sf4)
                        sleep(1)
                    else:
                        print('分享到我的朋友按钮不存在，请检查原因')
                        sleep(2)
                else:
                    print('分享按钮不存在，请检查原因')
                    sleep(2)
                #s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[1]').click()
                s.tap(32, 42)
                sleep(2)
            else:
                print('投票不存在，无法执行分享操作')
                sleep(2)
            s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_资讯tab下的投票的分享功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_notenoughscore_tc074
#Purpose:检查惊喜页面用户积分不足购买一件纯积分商品的功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/18]
#*********************************************************************************************
    def test_jingxi_notenoughscore_tc074(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_用户积分不足购买一件纯积分商品的测试----step1进入惊喜页面')
        print('step2翻页找到所需兑换的纯积分商品；step3点击商品进入商品页面检查是否出现积分不足提示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_用户积分不足购买一件纯积分商品的测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp_notenoughscore(self)
        sleep(1)
        #惊喜
        s(id='惊喜').click()
        sleep(5)
        for i in range(5):
            s.swipe_up()
            sleep(1)
        #s.swipe(50,300,50,450,1.0)
        sleep(3)
        u1=s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]')
        #ch0=s(xpath='//XCUIElementTypeOther[@name="自动化专用纯积分 自动化专用别动 10000"]').displayed
        sleep(1)
        if u1.exists:
            print('纯积分商品找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]').click()
            sleep(9)
            #加入购物车
            nomore=s(xpath='//XCUIElementTypeStaticText[@name="积分不足"]')
            if nomore.exists:
                print('积分不足检查通过')
                sleep(2)
            else:
                print('积分不足检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorNotenoughscore_R_stg_tc074.png'
                c.screenshot(sf4)
            sleep(1)
            s.tap(34, 40)
            sleep(2)
        else:
            print('纯积分商品不存在/未找到，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_用户积分不足购买一件纯积分商品的测试----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_notenoughscore4scorecash_tc075
#Purpose:检查惊喜页面用户积分不足购买一件积分+现金商品的功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/18]
#*********************************************************************************************
    def test_jingxi_notenoughscore4scorecash_tc075(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_用户积分不足购买一件纯积分商品的测试----step1进入惊喜页面')
        print('step2翻页找到所需兑换的积分+现金商品；step3点击商品进入商品页面检查是否出现积分不足提示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_用户积分不足购买一件积分+现金商品的测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #惊喜
        s(id='惊喜').click()
        sleep(8)
        for i in range(3):
            s.swipe_up()
            sleep(1)
        #s.swipe(50,300,50,450,1.0)
        sleep(3)
        u1=s(xpath='//XCUIElementTypeOther[@name="自动化专用别动积分+现金 自动化专用别动 15000"]')
        ch0=s(xpath='//XCUIElementTypeOther[@name="自动化专用别动积分+现金 自动化专用别动 15000"]').displayed
        sleep(1)
        if u1.exists and ch0 == True:
            print('积分+现金商品找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="自动化专用别动积分+现金 自动化专用别动 15000"]').click()
            sleep(9)
            s(id='立即购买').click()
            sleep(1)
            s(id='立即购买').click()
            sleep(1)
            s(id='立即下单').click()
            sleep(1)
            s(id='确定').click()
            sleep(3)
            #选择支付方式
            #not finished
            #加入购物车
            nomore=s(xpath='//XCUIElementTypeStaticText[@name="积分不足"]')
            if nomore.exists:
                print('积分不足检查通过')
                sleep(2)
            else:
                print('积分不足检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorNotenoughscore_R_stg_tc074.png'
                c.screenshot(sf4)
            sleep(1)
            s.tap(34, 40)
            sleep(2)
        else:
            print('积分+现金商品不存在/未找到，请重新挑选')
            sleep(2)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_用户积分不足购买一件积分+现金商品的测试----结束:'+now)

#*******************************************************
#TC Name:test_wode_errfeedback_tc076
#Purpose:我的页面设置里错误反馈的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/21]
#*******************************************************
    def test_wode_errfeedback_tc076(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_设置里错误反馈的功能---')
        print('step1我的页面里点设置')
        print('step2点击错误反馈；step3输入错误反馈内容,点提交,检查是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里错误反馈的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe(50,600,50,100,1.0)
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #错误反馈
        s(id='错误反馈').click()
        sleep(2)
        code=s(className='XCUIElementTypeTextView')
        code.click()
        now2=time.strftime('%Y%m%d_%H%M%S')
        code.set_text('app经常闪退:'+now2)
        sleep(1)
        s(id='提交').click()
        sleep(9)
        s(id='all page back grey icon').click()
        sleep(2)
        print('错误反馈功能检查通过')
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里错误反馈的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_unbundlingwechat_tc077
#Purpose:我的页面设置里解除微信绑定的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/21]
#*******************************************************
    def test_wode_unbundlingwechat_tc077(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_设置里解除微信绑定的功能---')
        print('step1我的页面里点设置')
        print('step2点击账号绑定；step3检查微信绑定状态,如果已绑定,点解除绑定开关,检查是否解绑是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里解除微信绑定的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe_up()
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #账号绑定
        s(id='账号绑定').click()
        sleep(3)
        swi_wechat=s(xpath='//XCUIElementTypeSwitch[@name="微信"]')
        swi=swi_wechat.get().value
        if swi == '1':
            s(xpath='//XCUIElementTypeSwitch[@name="微信"]').click()
            sleep(1)
            s(id='确定').click()
            sleep(1)
            #检查toast
            save1=s(id='解绑成功')
            if save1.exists:
                print('微信解绑成功')
                sleep(1)
            else:
                print('微信解绑失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorUnbundliingWechat_R_stg_tc077.png'
                c.screenshot(sf1)
            sleep(1)
        else:
            print('微信已经解除绑定,无需执行此操作!')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里解除微信绑定的功能----结束:'+now)
        
#*******************************************************
#TC Name:test_wode_bindingwechat_tc078
#Purpose:我的页面设置里绑定微信的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/21]
#*******************************************************
    def test_wode_bindingwechat_tc078(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_设置里绑定微信的功能---')
        print('step1我的页面里点设置')
        print('step2点击账号绑定；step3检查微信绑定状态,如果未绑定,点绑定开关,检查是否绑定是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里绑定微信的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe_up()
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #账号绑定
        s(id='账号绑定').click()
        sleep(3)
        swi_wechat=s(xpath='//XCUIElementTypeSwitch[@name="微信"]')
        swi=swi_wechat.get().value
        if swi != '1':
            s(xpath='//XCUIElementTypeSwitch[@name="微信"]').click()
            sleep(1)
            #检查toast
            save1=s(id='绑定成功')
            if save1.exists:
                print('绑定微信成功')
                sleep(1)
            else:
                print('绑定微信失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorBindiingWechat_R_stg_tc078.png'
                c.screenshot(sf1)
            sleep(1)
        else:
            print('微信已经绑定,无需执行此操作!')
        sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里绑定微信的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_unbundlingwebo_tc079
#Purpose:我的页面设置里解除微博绑定的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/21]
#*******************************************************
    def test_wode_unbundlingwebo_tc079(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_设置里解除微博绑定的功能---')
        print('step1我的页面里点设置')
        print('step2点击账号绑定；step3检查微博绑定状态,如果已绑定,点解除绑定开关,检查是否解绑是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里解除微博绑定的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe_up()
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #账号绑定
        s(id='账号绑定').click()
        sleep(3)
        swi_webo=s(xpath='//XCUIElementTypeSwitch[@name="微博"]')
        swi=swi_webo.get().value
        if swi == '1':
            s(xpath='//XCUIElementTypeSwitch[@name="微博"]').click()
            sleep(1)
            s(id='确定').click()
            sleep(1)
            #检查toast
            save1=s(id='解绑成功')
            if save1.exists:
                print('微博解绑成功')
                sleep(1)
            else:
                print('微博解绑失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorUnbundliingWebo_R_stg_tc079.png'
                c.screenshot(sf1)
            sleep(1)
        else:
            print('微博已经解除绑定,无需执行此操作!')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里解除微博绑定的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_bindingwebo_tc080
#Purpose:我的页面设置里绑定微博的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/21]
#*******************************************************
    def test_wode_bindingwebo_tc080(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_设置里绑定微博的功能---')
        print('step1我的页面里点设置')
        print('step2点击账号绑定；step3检查微博绑定状态,如果未绑定,点绑定开关,检查是否绑定是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里绑定微博的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s.swipe_up()
        sleep(2)
        s(id='设置').click()
        sleep(2)
        #账号绑定
        s(id='账号绑定').click()
        sleep(3)
        swi_webo=s(xpath='//XCUIElementTypeSwitch[@name="微博"]')
        swi=swi_webo.get().value
        if swi != '1':
            s(xpath='//XCUIElementTypeSwitch[@name="微博"]').click()
            sleep(2)
            """
            re=s(id='重新加载')
            if re.exists:
                s(id='重新加载').click()
                sleep(1)
            """
            #检查toast
            save1=s(id='绑定成功')
            if save1.exists:
                print('绑定微博成功')
                sleep(1)
            else:
                print('绑定微博失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorBindiingWebo_R_stg_tc080.png'
                c.screenshot(sf1)
            sleep(1)
        else:
            print('微信已经绑定,无需执行此操作!')
            sleep(1)
        s(id='all page back grey icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_设置里绑定微博的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_publishdel_tc081
#Purpose:我的发布页面删除发布内容的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************
    def test_wode_publishdel_tc081(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号我的_发布页面删除发布内容的功能---')
        print('step1我的页面里点发布')
        print('step2点击第一条发布内容；step3点击右上角按钮,检查是否有删除按钮')
        print('step4点击删除按钮,检查是否删除成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_发布页面删除发布内容的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(2)
        s(id='发布').click()
        sleep(2)
        #s(xpath='//XCUIElementTypeTextView[contains(@value,"我用Python")]').click()
        s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextView').click()
        sleep(3)
        s(id='icon share gray background new').click()
        sleep(1)
        erase=s(id='删除')
        if erase.exists:
            print('删除按钮存在')
            sleep(1)
            s(id='删除').click()
            sleep(1)
            s(id='确认').click()
            sleep(1)
            #检查toast
            save1=s(id='删除成功')
            if save1.exists:
                print('删除我的发布成功')
                sleep(1)
                #fresh
                s.swipe(50,100,50,600,0.5)
                sleep(2)
            else:
                print('删除我的发布失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorPublishDel_R_stg_tc081.png'
                c.screenshot(sf1)
            sleep(1)
        else:
            print('删除按钮不存在!')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('我的_发布页面删除发布内容功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_delchatfromchats_tc082
#Purpose:检查朋友页面全部对话列表里删除聊天的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************
    def test_pengyou_delchatfromchats_tc082(self):
        print('TC_检查手机号码登录APP，检查点:朋友_从全部对话列表里删除聊天的功能----step1进入朋友页面')
        print('step2检查需要删除的聊天是否存在;step3进入需要删除的聊天页面点右上角的按钮')
        print('step4检查删除并退出按钮是否存在;step5检查该聊天是否被删除成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从全部对话列表里删除聊天的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(4)
        myf=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')
        sleep(1)
        if myf.exists:
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
            sleep(2)
            #和分享按钮合并
            s(id='im btn more').click()
            sleep(2)
            #删除并退出
            butt=s(id='删除并退出')
            if butt.exists:
                print('删除并退出按钮存在，检查通过')
                sleep(2)
                s(id='删除并退出').click()
                sleep(1)
                s(id='确定').click()
                sleep(1)
                #检查toast
                save1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')
                if (not save1.exists):
                    print('从全部对话列表里删除聊天成功')
                else:
                    print('从全部对话列表里删除聊天失败，请检查原因')
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorDelchatfromchats_R_stg_tc082.png'
                    c.screenshot(sf1)
                sleep(2)
            else:
                print('删除并退出按钮不存在，请检查原因')
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
        else:
            print('没有需要删除的聊天,请先发起聊天!')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从全部对话列表里删除聊天的功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_zeroscore_tc083
#Purpose:检查惊喜页面零积分用户购买一件纯积分商品的功能测试
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*********************************************************************************************
    def test_jingxi_zeroscore_tc083(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_零积分用户购买一件纯积分商品的测试----step1进入惊喜页面')
        print('step2翻页找到所需兑换的纯积分商品；step3点击商品进入商品页面检查是否出现积分不足提示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_零积分用户购买一件纯积分商品的测试----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp_zeroscore(self)
        sleep(1)
        #惊喜
        s(id='惊喜').click()
        sleep(5)
        for i in range(5):
            s.swipe_up()
            sleep(1)
        #s.swipe(50,300,50,450,1.0)
        sleep(2)
        u1=s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]')
        #ch0=s(xpath='//XCUIElementTypeOther[@name="自动化专用纯积分 自动化专用别动 10000"]').displayed
        sleep(1)
        if u1.exists:
            print('纯积分商品找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther[@name="自动化_供应商发货商品1 自动化_供应商发货商品1 10000"]').click()
            sleep(9)
            #加入购物车
            nomore=s(xpath='//XCUIElementTypeStaticText[@name="积分不足"]')
            if nomore.exists:
                print('积分不足检查通过')
                sleep(1)
            else:
                print('积分不足检查失败，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf4='../../test_report/ios/'+now+'_errorNotenoughscore_R_stg_tc083.png'
                c.screenshot(sf4)
            sleep(1)
            s.tap(34, 40)
            sleep(2)
        else:
            print('纯积分商品不存在/未找到，请重新挑选')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_惊喜_零积分用户购买一件纯积分商品的测试----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_delchatfromfriendslist_tc084
#Purpose:检查朋友页面从朋友列表里删除聊天的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************
    def test_pengyou_delchatfromfriendslist_tc084(self):
        print('TC_检查手机号码登录APP，检查点:朋友_从朋友列表里删除聊天的功能----step1进入朋友页面')
        print('step2点击朋友列表按钮;step3检查需要删除聊天的朋友是否存在;step4点击朋友进入朋友页面,再点击聊天按钮')
        print('step5输入聊天的文字;step6返回后点击右上角的按钮')
        print('step7检查删除并退出按钮是否存在;step8检查该聊天是否被删除成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从朋友列表里删除聊天的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(3)
        #朋友列表按钮
        s(id='friends go friendlist').click()
        sleep(5)
        myf=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')
        sleep(1)
        if myf.exists:
            print('找到需要删除聊天的朋友')
            sleep(2)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
            sleep(3)
            s(id='聊天').click()
            sleep(4)
            inp=s(id='chat_input_textView')
            inp.click()
            sleep(0.5)
            now0=time.strftime('%Y%m%d_%H%M%S')
            inp.set_text('人生苦短聊天:'+now0)
            sleep(1)
            s(id='Send').click()
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(2)
            s(id='full screen back icon').click()
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
            sleep(3)
            #...
            s(id='im btn more').click()
            sleep(2)
            #删除并退出
            butt=s(id='删除并退出')
            if butt.exists:
                print('删除并退出按钮存在，检查通过')
                sleep(2)
                s(id='删除并退出').click()
                sleep(1)
                s(id='确定').click()
                sleep(1)
                #检查
                save1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]')
                if (not save1.exists):
                    print('从朋友列表里删除聊天成功')
                else:
                    print('从朋友列表里删除聊天失败，请检查原因')
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorDelchatfromFriendsList_R_stg_tc084.png'
                    c.screenshot(sf1)
                sleep(2)
            else:
                print('删除并退出按钮不存在，请检查原因')
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
        else:
            print('没有找到需要删除聊天的朋友,请检查原因!')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从朋友列表里删除聊天的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_experjoinzeroscore_tc085
#Purpose:发现页面体验tab活动的积分不足用户报名的检查
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************
    def test_faxian_experjoinzeroscore_tc085(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的积分不足用户报名的检查---')
        print('step1发现页面里点击体验tab')
        print('step2找到一个同城活动里的报名活动；step3进入活动报名页面检查积分不足是否显示')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_检查积分不足用户在体验tab报名活动是否显示积分不足----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp_zeroscore(self)
        sleep(1)
        s(id='发现').click()
        sleep(4)
        #体验
        s(id='体验').click()
        sleep(6)
        """
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]').click()
        sleep(2)
        #s.swipe(50,550,50,150,1.0)
        #sleep(2)
        s(id='蔚来中心丨上海太古汇店1112121312').click()
        sleep(2)
        """
        for i in range(2):
            s.swipe(150,600,150,80,0.5)
            sleep(1)
        sleep(2)
        #小龙自动化2
        s(id='小龙自动化3（请勿报名）').click()
        sleep(6)
        #积分不足
        nomore=s(xpath='//XCUIElementTypeStaticText[@name="积分不足"]')
        if nomore.exists:
            print('积分不足检查通过')
            sleep(2)
        else:
            print('积分不足检查失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf4='../../test_report/ios/'+now+'_errorNotenoughscore_R_stg_tc085.png'
            c.screenshot(sf4)
        sleep(2)
        s.tap(34, 42)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_检查积分不足用户在体验tab报名活动是否显示积分不足----结束:'+now)

#*******************************************************************************************************************************
#TC Name:test_aiche_es6share_tc086
#Purpose:检查爱车页面ES6页面分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************************************************************************************
    def test_aiche_es6share_tc086(self):
        print('TC_检查手机号码登录APP，检查点:爱车_ES6页面分享功能----step1进入爱车页面')
        print('step2进入ES6页面；step3点右上角的分享按钮（先检查是否存在)')
        print('step4检查分享微信好友功能是否正常;step5检查分享微信朋友圈功能是否正常')
        print('step6检查分享微博好友功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES6页面分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(3):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        es6=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeImage')
        if es6.exists:
            print('NIO es6找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeImage').click()
            #s(id='详细配置表').click()
            sleep(9)
            #分享图标
            share=s(xpath='//XCUIElementTypeButton[@name="nav share btn"]')
            sleep(1)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信好友
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短爱车ES6微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.5)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc086.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短爱车ES6页面微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc086.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    if s(id='确定').exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(2)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(0.35)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc086.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到微博按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #NIO好友
                mf=s(id='NIO好友')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(1)
                    s(id='NIO好友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc086.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            s(id='nav back btn').click()   
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES6页面分享功能----结束:'+now)

#*********************************************************************************************************************
#TC Name:test_wode_es6ordershare_tc087
#Purpose:检查我的ES6订单的分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*********************************************************************************************************************
    def test_wode_es6ordershare_tc087(self):
        print('TC_检查手机号码登录APP，检查点:我的_我的ES6订单的分享功能----step1进入我的页面')
        print('step2进入我的es6订单点击进入订单详细页面；step3点右上角的分享按钮（先检查是否存在；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的ES6订单的分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(4)
        s(id='我的车辆订单').click()
        sleep(9)
        s.swipe(50,580,50,80,1.0)
        sleep(2)
        car=s(id='ES6基准版')
        if car.exists:
            s(id='ES6基准版').click()
            sleep(4)
            #分享图标
            share=s(id='navigationbar btn share')
            sleep(1)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微信好友
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短我的ES6订单微信好友:'+now0)
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
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_stg_tc087.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微信朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短我的ES6订单微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_stg_tc087.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                sleep(2)
                """
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #微博no such menu now
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(8)
                    s(id='发送到分组').click()
                    sleep(2)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_stg_tc087.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                """
                #share
                s(id='navigationbar btn share').click()
                sleep(2)
                #NIO好友
                mf=s(xpath='//XCUIElementTypeStaticText[@name="NIO好友"]')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="NIO好友"]').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(1)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_stg_tc087.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            #s.tap(35, 42)
            s(id='navigationbar btn back black1').click()   
            sleep(2)
        else:
            print('暂无订单，无法执行该脚本')
            sleep(2)
            #s(id='navigationbar btn back black1').click()
            s.tap(35, 42)
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_我的ES6订单的分享功能----结束:'+now)

#*******************************************************************************************************************************
#TC Name:test_aiche_es8share_tc088
#Purpose:检查爱车页面ES8页面分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/12/24]
#*******************************************************************************************************************************
    def test_aiche_es8share_tc088(self):
        print('TC_检查手机号码登录APP，检查点:爱车_ES8页面分享功能----step1进入爱车页面')
        print('step2进入ES8页面；step3点右上角的分享按钮（先检查是否存在)')
        print('step4检查分享微信好友功能是否正常;step5检查分享微信朋友圈功能是否正常')
        print('step6检查分享微博好友功能是否正常;step7检查分享NIO好友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8页面分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(3):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        sleep(2)
        es8=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[11]/XCUIElementTypeImage')
        if es8.exists:
            print('NIO es8找到')
            sleep(2)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[11]/XCUIElementTypeImage').click()
            #s(id='详细配置表').click()
            sleep(9)
            #分享图标
            share=s(xpath='//XCUIElementTypeButton[@name="nav share btn"]')
            sleep(1)
            if share.exists:
                print('分享按钮存在,检查通过')
                sleep(3)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信好友
                wh=s(id='微信好友')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    s(id='微信好友').click()
                    sleep(6)
                    s(id='王小龙').click()
                    sleep(3)
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('人生苦短爱车ES8微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.5)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorGiftsharewechat_R_tc088.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微信朋友圈
                pyq=s(id='微信朋友圈')
                if pyq.exists:
                    print('分享到微信朋友圈按钮存在，检查通过')
                    sleep(1)
                    s(id='微信朋友圈').click()
                    sleep(8)
                    word2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('人生苦短爱车ES8页面微信朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享微信朋友圈成功')
                        sleep(1)
                    else:
                        print('分享微信朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorGiftsharewechatpyq_R_tc088.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到微信朋友圈按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    if s(id='确定').exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(2)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorGiftsharewebo_R_tc088.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到微博按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
                #share
                s(id='nav share btn').click()
                sleep(2)
                #NIO好友
                mf=s(id='NIO好友')
                if mf.exists:
                    print('分享到NIO好友按钮存在，检查通过')
                    sleep(1)
                    s(id='NIO好友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享NIO好友成功')
                        sleep(1)
                    else:
                        print('分享NIO好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorGiftsharemyfriend_R_tc088.png'
                        c.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到NIO好友按钮不存在，请检查原因')
                    sleep(2)
                    s(id='letter btn close').click()
                sleep(2)
            else:
                print('分享按钮不存在/未找到，请检查原因')
                sleep(2)
            s(id='nav back btn').click()   
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_ES8页面分享功能----结束:'+now)

#*******************************************************************************************************************************
#TC Name:test_faxian_cityswitch_tc089
#Purpose:检查发现页面体验tab切换城市的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/07]
#*******************************************************
    def test_faxian_cityswitch_tc089(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab切换城市的功能---step1发现页面里点击体验tab')
        print('step2切换地点找到南京市点击进入；step3检查该城市的绑定活动是否显示正常;step4翻页点击更多同城活动点击进入')
        print('step5检查该城市的同城活动列表是否显示正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_体验tab切换城市的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #体验
        s(id='体验').click()
        sleep(3)
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]').click()
        sleep(2)
        s.swipe(50,650,50,50,1.0)
        sleep(3)
        #南京市
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeOther[1]/XCUIElementTypeImage').click()
        sleep(3)
        #报名
        activ=s(xpath='//XCUIElementTypeStaticText[@name="南京普通活动"]')
        if activ.exists:
            print('城市切换成功,检查通过')
            sleep(1)
            for i in range(1):
                s.swipe_up()
                sleep(1)
            sleep(2)
            #s(xpath='//XCUIElementTypeButton[contains(@name,"更多同城活动")]').click()
            s.tap(207, 632)
            sleep(3)
            #checking
            ch=s(xpath='//XCUIElementTypeStaticText[contains(@name,"普通活动")]')
            if (not ch.exists):
                print('城市切换后的同城活动显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errorSameCityAct_R_stg_tc089.png'
                c.screenshot(sf1)
                sleep(1)
            else:
                print('城市切换后的同城活动显示正常,检查通过')
                sleep(1)
            s(xpath='//XCUIElementTypeButton[@name="all page back black icon"]').click()
            sleep(2)
        else:
            print('城市切换失败，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errorSameCityAct_R_stg_tc089.png'
            c.screenshot(sf1)
            sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_体验tab切换城市的功能能----结束:'+now)

#*******************************************************
#TC Name:test_aiche_rechargemapswipe_tc090
#Purpose:检查爱车页面里爱车_充电地图滑动和定位操作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/07]
#*******************************************************
    def test_aiche_rechargemapswipe_tc090(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图及查看充电桩信息----step1进入爱车页面')
        print('step2点击充电地图；step3充电地图放大;step4充电地图缩小')
        print('step5充电地图向下滑动;step6充电地图向右滑动;step7点击定位按钮')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图滑动和定位操作----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            p=s(xpath='//XCUIElementTypeStaticText[@name="1"]')[2]
            #zoom
            p.pinch(1.3,1.1)
            sleep(2)
            print('充电地图放大')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_chargemapZoom_R_tc090.png'
            c.screenshot(sf1)
            sleep(2)
            s(id='PE locate icon').click()
            sleep(3)
            p1=s(xpath='//XCUIElementTypeStaticText[@name="1"]')[2]
            #pinch
            p1.pinch(0.7, -1.1)
            sleep(2)
            print('充电地图缩小')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_chargemapPinch_R_tc090.png'
            c.screenshot(sf1)
            sleep(2)
            #down
            s.swipe(50,400,50,100,1.0)
            sleep(2)
            print('充电地图向下滑动')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_chargemapSwipeDown_R_tc090.png'
            c.screenshot(sf1)
            sleep(2)
            s.swipe(300,300,50,300,1.0)
            sleep(2)
            print('充电地图向右滑动')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_chargemapSwipeRight_R_tc090.png'
            c.screenshot(sf1)
            sleep(2)
            #定位
            s(id='PE locate icon').click()
            sleep(3)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_chargemapLocate_R_tc090.png'
            c.screenshot(sf1)
            sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图滑动和定位操作----结束:'+now)

#*******************************************************
#TC Name:test_aiche_rechargemapfeedback_tc091
#Purpose:检查爱车页面里充电地图提交反馈的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/07]
#*******************************************************
    def test_aiche_rechargemapfeedback_tc091(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图提交反馈的功能----')
        print('step1进入爱车页面;step2点击充电地图；step3点击一个充电桩;step4点击我要反馈')
        print('step5体验点击五星,选择2个标签,输入文字,点击+号后选择3张照片,再点击提交反馈,检查反馈是否成功')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图提交反馈的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #8号充电桩
            #driver.find_element_by_id('cn.com.weilaihui3:id/charging_pile_drag_view').click()
            s.tap(287,272)
            sleep(5)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"上海曹安景林苑充电站")]').click()
            sleep(6)
            #我要反馈
            s(id='我要反馈').click()
            sleep(2)
            #5-star
            #s(className='Image', id='star_evaluate_normal')[4].click()
            s.tap(231,94)
            sleep(1)
            s(id='充电很快').click()
            sleep(2)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"车位充足")]').click()
            sleep(1)
            fb=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextView[1]')
            fb.click()
            sleep(0.5)
            now0=time.strftime('%Y%m%d_%H%M%S')
            fb.set_text('充电地图反馈:'+now0)
            sleep(0.5)
            s(id='Toolbar Done Button').click()
            sleep(1)
            #+
            s.tap(74, 384)
            sleep(1)
            #好
            allow=s(id='好')
            if allow.exists:
                s(id='好').click()
                sleep(1)
            for i in range(3):
                s(predicate='name=="compose guide check box defaul"')[i].click()
                sleep(1)
            sleep(1)
            s(id='完成(3/9)').click()
            sleep(3)
            #s.swipe_up()
            #sleep(2)
            s(id='提交反馈').click()
            sleep(3)
            ch1=s(id='反馈提交成功')
            if ch1.exists:
                print('反馈提交成功')
                sleep(1)
            else:
                print('反馈提交不成功，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errChargemapFeedback_R_tc091.png'
                c.screenshot(sf1)
            sleep(6)
            #s(id='all page back grey icon').click()
            #sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图提交反馈的功能----结束:'+now)

#*******************************************************
#TC Name:test_aiche_rechargemapownercommentslike_tc092
#Purpose:检查爱车页面里充电地图车主评价点赞/取消点赞的功
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/07]
#*******************************************************
    def test_aiche_rechargemapownercommentslike_tc092(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图车主评价点赞/取消点赞的功能----')
        print('step1进入爱车页面;step2点击充电地图；step3点击一个充电桩;step4上滑页面,对一个车主评价点赞')
        print('step5取消点赞;step6点击其他反馈,检查显示是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图车主评价点赞/取消点赞的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #8号充电桩
            #driver.find_element_by_id('cn.com.weilaihui3:id/charging_pile_drag_view').click()
            s.tap(287,273)
            sleep(5)
            #s.swipe(150,550,150,50,1.0)
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"上海曹安景林苑充电站")]').click()
            sleep(6)
            #点赞
            s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(1)
            print('点赞成功')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_ChargemapCommentsLike_R_tc092.png'
            c.screenshot(sf1)
            sleep(2)
            s(xpath='//XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton').click()
            sleep(1)
            print('取消点赞成功')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_ChargemapCommentsCancelLike_R_tc092.png'
            c.screenshot(sf2)
            sleep(2)
            #其他反馈
            s(xpath='//XCUIElementTypeButton[contains(@name,"其他反馈")]').click()
            sleep(2)
            ch=s(xpath='//XCUIElementTypeStaticText[contains(@name,"充电地图反馈:2019")]')
            if ch.exists:
                print('其他反馈显示正常,检查通过')
                sleep(1)
            else:
                print('其他反馈显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_errChargemapOtherFeedback_R_tc092.png'
                c.screenshot(sf3)
            sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图车主评价点赞/取消点赞的功能----结束:'+now)

#*************************************************************************************************************
#TC Name:test_aiche_rechargemappilot_tc093
#Purpose:检查爱车页面里充电地图充电桩导航的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/08]
#*************************************************************************************************************
    def test_aiche_rechargemappilot_tc093(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图充电桩导航的功能----')
        print('step1进入爱车页面;step2点击充电地图；step3点击一个充电桩;step4点击导航按钮')
        print('step5选择苹果地图;step6返回蔚来app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电桩导航的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #8号充电桩
            #driver.find_element_by_id('cn.com.weilaihui3:id/charging_pile_drag_view').click()
            s.tap(287,273)
            sleep(5)
            #导航
            pi=s(xpath='//XCUIElementTypeButton[@name="locationNav"]')
            if (not pi.exists):
                print('导航按钮未找到,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errNoPilot_R_tc093.png'
                c.screenshot(sf2)
                sleep(2)
            else:
                print('导航按钮找到,检查通过')
                sleep(1)
                s(xpath='//XCUIElementTypeButton[@name="locationNav"]').click()
                sleep(1)
                #高德地图
                s(xpath='//XCUIElementTypeStaticText[@name="苹果地图"]').click()
                sleep(4)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_ChargemapPilotApple_R_tc093.png'
                c.screenshot(sf3)
                sleep(2)
                #s(id='蔚来Test').click()
                s.tap(36,10)
                sleep(2)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电桩导航的功能----结束:'+now)

#*************************************************************************************************************
#TC Name:test_aiche_rechargemaprechargehistory_tc094
#Purpose:检查爱车页面里充电地图充电历史
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/08]
#*************************************************************************************************************
    def test_aiche_rechargemaprechargehistory_tc094(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图充电历史检查----')
        print('step1进入爱车页面;step2点击充电地图；step3点击充电历史按钮')
        print('step4点击换电tab')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电历史检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        #s.tap(188,613)
        #sleep(2)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #充电历史
            pi=s(xpath='//XCUIElementTypeButton[@name="peMapHistory"]')
            if (not pi.exists):
                print('充电历史未找到,请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errNoPilot_R_tc093.png'
                c.screenshot(sf2)
                sleep(2)
            else:
                print('充电历史按钮找到,检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeButton[@name="peMapHistory"]').click()
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf3='../../test_report/ios/'+now+'_rechargeHistory_R_tc094.png'
                c.screenshot(sf3)
                sleep(2)
                s(id='换电').click()
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_changeBatteryHistory_R_tc094.png'
                c.screenshot(sf2)
                sleep(2)
                s(id='all page back grey icon').click()
                sleep(3)
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电历史检查----结束:'+now)

#*************************************************************************************************************
#TC Name:test_aiche_rechargemaprechargepole_tc095
#Purpose:检查爱车页面里充电地图充电桩
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/08]
#*************************************************************************************************************
    def test_aiche_rechargemaprechargepole_tc095(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图充电桩群里查看充电桩信息----')
        print('step1进入爱车页面;step2点击充电地图；step3缩小地图,再放大地图')
        print('step4点击7号充电桩群一次;step5点击3号充电桩,检查充电桩信息是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电桩群里查看充电桩信息----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #7号充电桩
            pi=s(xpath='//XCUIElementTypeStaticText[@name="1"]')
            if (not pi.exists):
                print('1号充电桩群未找到,请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errNoPole_R_tc095.png'
                c.screenshot(sf2)
                sleep(2)
            else:
                print('1号充电桩群找到,检查通过')
                sleep(2)
                #zoom
                p0=s(xpath='//XCUIElementTypeStaticText[@name="1"]')[1]
                sleep(1)
                p0.pinch(1.4, 1.1)
                sleep(2)
                #s(xpath='//XCUIElementTypeStaticText[@name="1"]').click()
                p=s(xpath='//XCUIElementTypeStaticText[@name="1"]')[1]
                sleep(1)
                #pinch
                p.pinch(0.9,-1.1)
                sleep(2)
                #3号充电桩
                p1=s(xpath='//XCUIElementTypeStaticText[@name="3"]')[1]
                sleep(1)
                x1=p1.bounds.x+20
                y1=p1.bounds.y+20
                s.tap(x1,y1)
                sleep(5)
                px=s(xpath='//XCUIElementTypeStaticText[contains(@name,"20190123annie")]')
                if (not px.exists):
                    print('3号充电桩未找到,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_rechargepole_R_tc095.png'
                    c.screenshot(sf3)
                    sleep(2)
                else:
                    print('3号充电桩找到,检查通过')
                    sleep(1)
                    """
                    s(id='routPlanBack').click()
                    sleep(2)
                    s(id='PE locate icon').click()
                    sleep(3)
                    """
            s(id='routPlanBack').click()
            sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图充电桩群里查看充电桩信息----结束:'+now)

#*************************************************************************************************************
#TC Name:test_aiche_rechargemapsearchroute_tc096
#Purpose:检查爱车页面里搜索及路径规划
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/09]
#*************************************************************************************************************
    def test_aiche_rechargemapsearchroute_tc096(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图搜索及路径规划----')
        print('step1进入爱车页面;step2点击充电地图；step3搜索栏输入北京,再点击结果里的北京南站')
        print('step4点击充电线路;step5上拉路径卡片,检查路径卡片详细行程显示是否正确')
        print('step6点击详细功率,检查详细功率页面显示是否正确并关闭')
        print('step7点击详细费率,检查收费规则页面显示是否正确并关闭')
        print('step8点击下一站,检查下一站充电站页面显示是否正确')
        sleep(0.5)
        print('step9点击上一站,检查上一站充电站页面显示是否正确')
        print('step10点击完整路线进行切换')
        print('step11点击路径输入框旁+号,输入南京,再点击结果里的南京南站')
        print('step12点击路径输入框旁+号,输入合肥,再点击结果里的合肥南站')
        print('step13点击路径输入框旁+号,输入郑州,再点击结果里的郑州站')
        sleep(0.5)
        print('step14点击互换起终点,再上拉路径卡片,下拉路径卡片')
        print('step15点击过滤按钮,只选择直流快充')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图搜索及路径规划----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #搜索
            s(id='搜索').click()
            sleep(1)
            pi=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
            pi.click()
            pi.set_text('北京')
            sleep(0.5)
            s(id='Toolbar Done Button').click()
            sleep(1)
            #s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
            s(id='北京南站').click()
            sleep(2)
            s(id='PERoutPlan').click()
            sleep(8)
            #上拉卡片
            s.swipe(50,650,50,100,1.0)
            sleep(2)
            ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"服务区充电站")]')
            if (not ch1.exists):
                print('路径卡片详细行程显示不正常,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errRouteCard_R_tc096.png'
                c.screenshot(sf1)
                sleep(2)
            else:
                print('路径卡片详细行程显示正常,检查通过')
                sleep(2)
                s(id='routPlanLineRightArrow')[0].click()
                sleep(4)
                #上拉
                ##s.swipe(50,550,50,200,1.0)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"服务区充电站")]').click()
                sleep(3)
                #详细功率
                ##s(xpath='//XCUIElementTypeImage[@name="pe_icon_right_arrow"]').click()
                ##s(id='最快120度每小时').click()
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"度每小时")]').click()
                sleep(1)
                ch2=s(xpath='//XCUIElementTypeStaticText[@name="详细功率"]')
                if (not ch2.exists):
                    print('详细功率页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errPowerDetailPage_R_tc096.png'
                    c.screenshot(sf2)
                    sleep(2)
                else:
                    print('详细功率页面显示正常,检查通过')
                sleep(1)
                #关闭详细功率
                s(id='PE cancelClose').click()
                sleep(2)
                #详细费率
                #s(xpath='//XCUIElementTypeImage[@name="pe_icon_right_arrow"]')[1].click()
                s(id='0.70 - 1.77元/度').click()
                sleep(1)
                ch3=s(xpath='//XCUIElementTypeStaticText[@name="00:00-24:00,收费0.70 - 1.77元/度"]')
                if (not ch3.exists):
                    print('收费规则页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errPayRulePage_R_tc096.png'
                    c.screenshot(sf3)
                    sleep(2)
                else:
                    print('收费规则页面显示正常,检查通过')
                sleep(1)
                s(id='PE cancelClose').click()
                sleep(1)
                ##s.swipe(50,200,50,650,1.0)
                s(id='routPlanBack').click()
                sleep(2)
                #下一站
                s(id='PERoutPlanNext').click()
                sleep(4)
                chnext=s(xpath='//XCUIElementTypeStaticText[contains(@name,"服务区充电站")]')
                if (not chnext.exists):
                    print('下一站充电站页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errNextPolePage_R_tc096.png'
                    c.screenshot(sf3)
                    sleep(2)
                else:
                    print('下一站充电站页面显示正常,检查通过')
                sleep(1)
                #上一站
                s(id='PERoutPlanLast').click()
                sleep(4)
                chlast=s(xpath='//XCUIElementTypeStaticText[contains(@name,"服务区充电站")]')
                if (not chlast.exists):
                    print('上一站充电站页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios/'+now+'_errLastPolePage_R_tc096.png'
                    c.screenshot(sf4)
                    sleep(2)
                else:
                    print('上一站充电站页面显示正常,检查通过')
                sleep(1)
                #完整路线
                s(id='完整路线').click()
                sleep(2)
                print('切换完整路线成功')
                sleep(2)
                #+
                s(id='pedoAddPoiIcon').click()
                sleep(2)
                p1=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField[2]')
                p1.click()
                p1.set_text('南京')
                sleep(0.5)
                s(id='Toolbar Done Button').click()
                sleep(1)
                s(id='南京南站').click()
                sleep(4)
                #+
                s(id='pedoAddPoiIcon').click()
                sleep(2)
                p2=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField[3]')
                p2.click()
                p2.set_text('合肥')
                sleep(0.5)
                s(id='Toolbar Done Button').click()
                sleep(1)
                s(id='合肥南站').click()
                sleep(6)
                #+
                s(id='pedoAddPoiIcon').click()
                sleep(2)
                p3=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField[4]')
                p3.click()
                p3.set_text('郑州')
                sleep(0.5)
                s(id='Toolbar Done Button').click()
                sleep(1)
                s(id='郑州站').click()
                sleep(6)
                #互换起终点
                s(id='PEAddressChange').click()
                sleep(9)
                print('互换起终点成功')
                sleep(2)
                #上拉卡片
                s.swipe(50,650,50,200,1.0)
                sleep(2)
                """
                now=time.strftime('%Y%m%d_%H%M%S')
                sf='../../test_report/ios/'+now+'_AddrChanged_R_tc096.png'
                c.screenshot(sf)
                sleep(2)
                """
                #下拉卡片
                s.swipe(50,300,50,650,1.0)
                sleep(2)
                #过滤
                s.tap(376,214)
                #s(id='peMapFilter').click()
                sleep(2)
                s(id='换电站').click()
                sleep(1)
                s(id='交流慢充').click()
                sleep(1)
                s(id='完成').click()
                sleep(5)
                print('过滤充电类型完成')
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图搜索及路径规划----结束:'+now)

#*************************************************************************************************************
#TC Name:test_aiche_rechargemaprouteplan_tc097
#Purpose:检查爱车页面里路径规划页面
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/09]
#*************************************************************************************************************
    def test_aiche_rechargemaprouteplan_tc097(self):
        print('TC_检查手机号码登录APP，检查点:爱车_充电地图搜索及路径规划----')
        print('step1进入爱车页面;step2点击充电地图；step3搜索栏输入北京,再点击结果里的北京南站')
        print('step4点击充电线路;step5上拉路径卡片,检查路径卡片详细行程显示是否正确')
        print('step6下拉路径卡片,点击过滤按钮,全部选择')
        print('step7返回在搜索栏输入安阳服务区,再点击结果里的安阳服务区')
        sleep(0.5)
        print('step8点击换电站,上拉卡片,检查换电站详情页面显示是否正常')
        print('step9点击立即联系,检查联系电话显示是否正常,再取消')
        print('step10点击导航按钮,检查导航地图弹出页面显示是否正常,再取消')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图路径规划页面功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #爱车
        s(id='爱车').click()
        sleep(5)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
            sleep(1)
        for i in range(1):
            s.swipe(50,650,50,90,1.0)
            sleep(1)
        #s.swipe(50,400,50,100,1.0)
        sleep(2)
        cmap=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        if cmap.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            s(id='充电地图').click()
            sleep(4)
            #搜索
            s(id='搜索').click()
            sleep(1)
            pi=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
            pi.click()
            pi.set_text('北京')
            sleep(0.5)
            s(id='Toolbar Done Button').click()
            sleep(1)
            #s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
            s(id='北京南站').click()
            sleep(2)
            s(id='PERoutPlan').click()
            sleep(8)
            #上拉卡片
            s.swipe(50,650,50,100,1.0)
            sleep(2)
            ch1=s(xpath='//XCUIElementTypeStaticText[contains(@name,"服务区充电站")]')
            if (not ch1.exists):
                print('路径卡片详细行程显示不正常,请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errRouteCard_R_tc097.png'
                c.screenshot(sf1)
                sleep(2)
            else:
                print('路径卡片详细行程显示正常,检查通过')
                sleep(1)
                #下拉
                s.swipe(50,200,50,600,1.0)
                sleep(3)
                #过滤
                s.tap(376,174)
                #s(id='peMapFilterSelect').click()
                sleep(2)
                """
                s(id='换电站').click()
                sleep(1)
                s(id='交流慢充').click()
                sleep(1)
                """
                s(id='完成').click()
                sleep(6)
                print('过滤充电类型完成')
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
                #搜索
                s(id='搜索').click()
                sleep(1)
                pi=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
                pi.click()
                pi.set_text('安阳服务区')
                sleep(0.5)
                s(id='Toolbar Done Button').click()
                sleep(1)
                s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
                sleep(2)
                """
                p=s(xpath='//XCUIElementTypeStaticText[@name="4"]')[1]
                sleep(2)
                #zoom
                p.pinch(1.9,1.3)
                sleep(3)
                """
                #换电站
                s.tap(296,245)
                sleep(3)
                #上拉
                s.swipe(50,650,50,100,1.0)
                sleep(3)
                ch3=s(xpath='//XCUIElementTypeStaticText[contains(@name,"安阳服务区")]')
                if (not ch3.exists):
                    print('换电站详情页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errCallService_R_tc097.png'
                    c.screenshot(sf3)
                    sleep(2)
                else:
                    print('换电站详情页面显示正常,检查通过')
                sleep(2)
                #立即联系
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"立即联系")]').click()
                sleep(2)
                ch2=s(xpath='//XCUIElementTypeStaticText[contains(@name,"021-67099903")]')
                if (not ch2.exists):
                    print('联系电话显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errCallService_R_tc097.png'
                    c.screenshot(sf2)
                    sleep(2)
                else:
                    print('联系电话显示正常,检查通过')
                    sleep(1)
                s(id='取消').click()
                sleep(2)
                #导航
                s(id='locationNav').click()
                sleep(2)
                ch4=s(xpath='//XCUIElementTypeStaticText[contains(@name,"苹果地图")]')
                if (not ch4.exists):
                    print('导航地图弹出页面显示不正常,请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios/'+now+'_errPilotMenu_R_tc097.png'
                    c.screenshot(sf4)
                    sleep(2)
                else:
                    print('导航地图弹出页面显示正常,检查通过')
                    sleep(1)
                    s(id='取消').click()
                    sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
                s(id='routPlanBack').click()
                sleep(2)
        else:
            print('充电地图按钮未找到/不存在，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_充电地图路径规划页面功能检查----结束:'+now)

#*************************************************************************************************************
#TC Name:test_faxian_articlecollect_tc098
#Purpose:检查发现页面里文章收藏功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/24]
#*************************************************************************************************************
    def test_faxian_articlecollect_tc098(self):
        print('TC_检查手机号码登录APP，检查点:发现_文章收藏功能检查----')
        print('step1进入发现->资讯页面;step2翻页找到需要收藏的文章点击进入文章详细页面')
        print('step3点击收藏按钮,如果收藏数-1则再点击收藏按钮一次;step4进入我的—>我的收藏页面')
        print('step5检查收藏的文章是否显示正常/存在')
        sleep(0.5)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_文章收藏功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #资讯
        s(id='资讯').click()
        sleep(4)
        for i in range(8):
            s.swipe(50,580,50,100,1.0)
            sleep(1)
        #s.swipe(50,600,50,100,1.0)
        sleep(2)
        cmap=s(id="test prod comment can't show")
        ch0=s(id="test prod comment can't show").displayed
        if cmap.exists and ch0 == True:
            print('需要收藏的文章找到')
            sleep(2)
            s(id="test prod comment can't show").click()
            sleep(4)
            c_num=s(xpath='//XCUIElementTypeOther[@name="test prod comment can\'t show"]/XCUIElementTypeOther[46]/XCUIElementTypeStaticText')
            chnum=c_num.get().value
            c_num_ini=int(chnum)
            #收藏按钮
            coll=s(xpath='//XCUIElementTypeOther[@name="test prod comment can\'t show"]/XCUIElementTypeOther[45]')
            coll.click()
            sleep(0.5)
            c_num2=s(xpath='//XCUIElementTypeOther[@name="test prod comment can\'t show"]/XCUIElementTypeOther[46]/XCUIElementTypeStaticText')
            chnum2=c_num2.get().value
            if chnum2 == str(c_num_ini+1):
                print('收藏数+1')
                sleep(1)
            else:
                print('收藏数-1,已收藏过')
                sleep(1)
                coll.click()
            sleep(0.5)
            s.tap(32,42)
            sleep(2)
            s(id='我的').click()
            sleep(3)
            s(id='我的收藏').click()
            sleep(3)
            ch1=s(xpath='//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')
            chtxt=ch1.get().value
            if chtxt != "test prod comment can't show":
                print('收藏的文章显示不正常,请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errMyCollect_R_tc098.png'
                c.screenshot(sf1)
                sleep(2)
            else:
                print('收藏的文章显示正常,检查通过')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(2)
        else:
            print('需要收藏的文章未找到，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_文章收藏功能检查----结束:'+now)

#*************************************************************************************************************
#TC Name:test_wode_swipedelcollect_tc099
#Purpose:检查我的收藏页面里滑动收藏栏删除收藏的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/24]
#*************************************************************************************************************
    def test_wode_swipedelcollect_tc099(self):
        print('TC_检查手机号码登录APP，检查点:我的_滑动收藏栏删除收藏的功能检查----')
        print('step1进入我的->我的收藏页面;step2检查需要删除的已收藏文章是否存在')
        print('step3左滑文章;step4检查删除按钮是否出现,然后点击删除')
        print('step5检查删除的收藏文章是否存在')
        sleep(0.5)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_滑动收藏栏删除收藏的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #资讯
        s(id='我的').click()
        sleep(2)
        s(id='我的收藏').click()
        sleep(3)
        cmap=s(id="test prod comment can't show")
        if cmap.exists:
            print('需要删除的已收藏文章找到')
            sleep(2)
            #左滑动
            s.swipe(388,192,250,192,1.0)
            sleep(2)
            ch1=s(xpath='//XCUIElementTypeButton[@name="删除"]')
            if (not ch1.exists):
                print('删除按钮显示不正常,请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errNoDel_R_tc099.png'
                c.screenshot(sf1)
                sleep(2)
            else:
                print('删除按钮显示正常,检查通过')
                sleep(2)
                s(xpath='//XCUIElementTypeButton[@name="删除"]').click()
                sleep(2)
                ch2=s(id="test prod comment can't show")
                if (not ch2.exists):
                    print('删除已收藏文章成功,检查通过')
                    sleep(2)
                else:
                    print('删除已收藏文章失败,请检查原因')
                    sleep(2)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errDeleted_R_tc099.png'
                    c.screenshot(sf2)
                    sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('需要删除的已收藏文章未找到，请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_滑动收藏栏删除收藏的功能----结束:'+now)

#*************************************************************************************************************
#TC Name:test_wode_clickdelcollect_tc100
#Purpose:检查我的收藏页面里滑动收藏栏删除收藏的功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/01/24]
#*************************************************************************************************************
    def test_wode_clickdelcollect_tc100(self):
        print('TC_检查手机号码登录APP，检查点:我的_点击收藏按钮删除收藏的功能----')
        print('step1进入我的->我的收藏页面;step2检查需要删除的已收藏文章是否存在')
        print('step3点击文章进入文章详细页面;step4点击收藏按钮')
        print('step5检查删除的收藏文章是否存在')
        sleep(0.5)
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_点击收藏按钮删除收藏的功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #资讯
        s(id='我的').click()
        sleep(2)
        s(id='我的收藏').click()
        sleep(3)
        cmap=s(id="test prod comment can't show")
        if cmap.exists:
            print('需要删除的已收藏文章找到')
            sleep(2)
            s(id="test prod comment can't show").click()
            sleep(4)
            s(xpath='//XCUIElementTypeOther[@name="test prod comment can\'t show"]/XCUIElementTypeOther[46]').click()
            sleep(1)
            #返回
            s.tap(32,42)
            sleep(3)
            ch2=s(id="test prod comment can't show")
            if (not ch2.exists):
                print('删除已收藏文章成功,检查通过')
                sleep(2)
            else:
                print('删除已收藏文章失败,请检查原因')
                sleep(2)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errDeleted_R_tc100.png'
                c.screenshot(sf2)
                sleep(2)
        else:
            print('需要删除的已收藏文章未找到，请检查原因')
            sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_点击收藏按钮删除收藏的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_takenote_tc101
#Purpose:检查发现页面的写笔记功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/01]
#*******************************************************
    def test_faxian_takenote_tc101(self):
        print('TC_检查手机号码登录APP，检查点:发现_写笔记功能----step1检查发现首页右上角+号是否存在')
        print('step2检查写笔记按钮是否存在；step3设置封面,添加标题,@好友,#参与话题；step4添加图片,检查里是否可以一次最大上传9张图片')
        print('step5检查发布的笔记标题是否正确;step6检查点赞功能是否正常;step7检查评论功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_写笔记功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #写笔记
            c2=s(id='写笔记')
            if c2.exists:
                s(id='写笔记').click()
                sleep(3)
                #+设置封面
                #s.tap(207,246)
                s(id='PUGCViewAddCoverImage').click()
                sleep(1)
                s(id='从手机相册选择').click()
                sleep(3)
                s(xpath='//XCUIElementTypeCell[@name="最近添加"]').click()
                sleep(2)
                s(xpath='//XCUIElementTypeCell[contains(@name,"照片, 竖排")]')[0].click()
                sleep(2)
                s(id='选取').click()
                sleep(2)
                #添加标题
                add=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTextView')
                sleep(1)
                add.click()
                sleep(1)
                now0=time.strftime('%Y%m%d_%H%M%S')
                add.set_text('写笔记:'+now0+'\n')
                sleep(1)
                t0='写笔记:'+now0
                sleep(1)
                #编辑正文
                art=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther[3]/XCUIElementTypeTextView')
                #now1=time.strftime('%Y%m%d_%H%M%S')
                art.set_text('人生苦短,我用Python;人到中年不如狗')
                sleep(1)
                #@好友
                s(id='PUGCViewAtSome btn').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                sleep(1)
                ##参与话题
                s(id='PUGCViewTopic btn').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"#情景试驾#")]').click()
                sleep(1)
                #添加图片
                s(id='PUGCViewAddImage').click()
                sleep(2)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                sleep(1)
                for i in range(9):
                    s(predicate='name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                s(id='完成(9/9)').click()
                sleep(3)
                s(id='发布').click()
                sleep(2)
                s(id='确定').click()
                sleep(2.5)
                #check toast
                title=s(id='发布成功')
                if title.exists:
                    print('发布笔记成功')
                    sleep(1)
                else:
                    print('发布笔记失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errSendNote_R_stg_tc101.png'
                    c.screenshot(sf1)
                sleep(2)
                #此刻页面
                tt=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]')
                ch0=tt.get().value
                sleep(1)
                if t0 in ch0:
                    print('已发布的笔记的标题检查通过')
                    sleep(1)
                else:
                    print('已发布的笔记的标题检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorNoteTitle_R_stg_tc101.png'
                    c.screenshot(sf2)
                sleep(2)
                #点赞
                s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]').click()
                sleep(1)
                praise=s(xpath='//XCUIElementTypeStaticText[@name="1"]')
                if praise.exists:
                    print('点赞功能检查通过')
                    sleep(1)
                else:
                    print('点赞功能检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf3='../../test_report/ios/'+now+'_errorPraise_R_stg_tc101.png'
                    c.screenshot(sf3)
                sleep(2)
                #评论
                s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[3]').click()
                sleep(1)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"我也来说~")]').click()
                sleep(2)
                combtn=s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextView')
                combtn.click()
                sleep(1)
                now01=time.strftime('%Y%m%d_%H%M%S')
                combtn.set_text('自己评论自己:'+now01)
                sleep(1)
                t01='自己评论自己:'+now0
                s(xpath='//XCUIElementTypeButton[@name="Send"]').click()
                sleep(3)
                #check published text here
                title=s(xpath='//XCUIElementTypeTextView[contains(@value,t01)]')
                #print(title))
                if title.exists:
                    print('评论的文字检查通过')
                    sleep(1)
                else:
                    print('评论的文字检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errorComment_R_stg_tc101.png'
                    c.screenshot(sf1)
                sleep(2)
                s(xpath='//XCUIElementTypeButton[@name="all page back grey icon"]').click()
                sleep(2)
            else:
                print('写笔记按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_写笔记功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_takenotesave_tc102
#Purpose:检查发现页面的写笔记中返回保留再发布功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/02]
#*******************************************************
    def test_faxian_takenotesave_tc102(self):
        print('TC_检查手机号码登录APP，检查点:发现_写笔记中返回保留再发布功能----step1检查发现首页右上角+号是否存在')
        print('step2检查写笔记按钮是否存在；step3设置封面,添加标题,@好友,#参与话题；step4添加图片,检查里是否可以一次最大上传9张图片')
        print('step5点返回按钮,点击保留;step6点发现页面右上角+号,再点写笔记;step7点击发布,检查发布的笔记标题是否正确')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_写笔记中返回保留再发布功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #写笔记
            c2=s(id='写笔记')
            if c2.exists:
                s(id='写笔记').click()
                sleep(3)
                #+设置封面
                #s.tap(207,246)
                s(id='PUGCViewAddCoverImage').click()
                sleep(1)
                s(id='从手机相册选择').click()
                sleep(3)
                s(xpath='//XCUIElementTypeCell[@name="最近添加"]').click()
                sleep(2)
                s(xpath='//XCUIElementTypeCell[contains(@name,"照片, 竖排")]')[0].click()
                sleep(2)
                s(id='选取').click()
                sleep(2)
                #添加标题
                add=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeTextView')
                sleep(1)
                add.click()
                sleep(1)
                now0=time.strftime('%Y%m%d_%H%M%S')
                add.set_text('写笔记:'+now0+'\n')
                sleep(1)
                t0='写笔记:'+now0
                sleep(1)
                #编辑正文
                art=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther[3]/XCUIElementTypeTextView')
                #now1=time.strftime('%Y%m%d_%H%M%S')
                art.set_text('人生苦短,我用Python;人到中年不如狗')
                sleep(1)
                #@好友
                s(id='PUGCViewAtSome btn').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                sleep(1)
                ##参与话题
                s(id='PUGCViewTopic btn').click()
                sleep(2)
                s(xpath='//XCUIElementTypeStaticText[contains(@name,"#情景试驾#")]').click()
                sleep(1)
                #添加图片
                s(id='PUGCViewAddImage').click()
                sleep(2)
                #好
                allow=s(id='好')
                if allow.exists:
                    s(id='好').click()
                sleep(1)
                for i in range(9):
                    s(predicate='name=="compose guide check box defaul"')[i].click()
                    sleep(1)
                sleep(1)
                s(id='完成(9/9)').click()
                sleep(3)
                #返回
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='保留').click()
                sleep(2)
                s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
                sleep(2)
                s(id='写笔记').click()
                sleep(2)
                s(id='发布').click()
                sleep(2)
                s(id='确定').click()
                sleep(2.5)
                #check toast
                title=s(id='发布成功')
                if title.exists:
                    print('发布笔记成功')
                    sleep(1)
                else:
                    print('发布笔记失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf1='../../test_report/ios/'+now+'_errSendNote_R_stg_tc102.png'
                    c.screenshot(sf1)
                sleep(2)
                #此刻页面
                tt=s(xpath='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]')
                ch0=tt.get().value
                sleep(1)
                if t0 in ch0:
                    print('已发布的笔记的标题检查通过')
                    sleep(1)
                else:
                    print('已发布的笔记的标题检查失败，请检查原因')
                    sleep(1)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf2='../../test_report/ios/'+now+'_errorNoteTitle_R_stg_tc102.png'
                    c.screenshot(sf2)
                sleep(2)
            else:
                print('写笔记按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_写笔记中返回保留再发布功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tryes6share_tc103
#Purpose:检查发现页面的邀请试驾es6分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/02]
#*******************************************************
    def test_faxian_tryes6share_tc103(self):
        print('TC_检查手机号码登录APP，检查点:发现_写笔记中返回保留再发布功能----step1检查发现首页右上角+号是否存在')
        print('step2检查邀请试驾按钮是否存在；step3点击邀请试驾；step4点击es6立即邀请')
        print('step5检查分享微信功能是否正常;step6检查分享朋友圈功能是否正常')
        print('step7检查分享微博功能是否正常;step8检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_邀请试驾es6分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #邀请试驾
            c2=s(id='邀请试驾')
            if c2.exists:
                s(id='邀请试驾').click()
                sleep(3)
                #es6
                sh=s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage')
                sh.click()
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
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        sleep(0.5)
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('邀请试驾es6分享微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.2)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorsharewechat_R_stg_tc103.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
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
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('邀请试驾es6分享朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                        sleep(1)
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R_stg_tc103.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    ad=s(id='确定')
                    if ad.exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(3)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorsharewebo_R_stg_tc103.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(2)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(3)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                        sleep(1)
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorsharemyfriend_R_stg_tc103.png'
                        c.screenshot(sf4)
                    sleep(2)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('邀请试驾按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_邀请试驾es6分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tryes8share_tc104
#Purpose:检查发现页面的邀请试驾es6分享功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/02]
#*******************************************************
    def test_faxian_tryes8share_tc104(self):
        print('TC_检查手机号码登录APP，检查点:发现_写笔记中返回保留再发布功能----step1检查发现首页右上角+号是否存在')
        print('step2检查邀请试驾按钮是否存在；step3点击邀请试驾；step4点击es8立即邀请')
        print('step5检查分享微信功能是否正常;step6检查分享朋友圈功能是否正常')
        print('step7检查分享微博功能是否正常;step8检查分享我的朋友功能是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_邀请试驾es8分享功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #邀请试驾
            c2=s(id='邀请试驾')
            if c2.exists:
                s(id='邀请试驾').click()
                sleep(3)
                s.swipe(50,600,50,300,1.0)
                sleep(2)
                #es8
                sh=s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeOther[2]/XCUIElementTypeImage')
                sh.click()
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
                    words=s(xpath='//XCUIElementTypeWindow[4]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView')
                    sleep(2)
                    if words.exists:
                        words.click()
                        sleep(1)
                        now0=time.strftime('%Y%m%d_%H%M%S')
                        sleep(0.5)
                        s(xpath='//XCUIElementTypeWindow[3]/XCUIElementTypeImage[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextView').set_text('邀请试驾es8分享微信好友:'+now0)
                        sleep(1)
                    #发送
                    s(id='发送').click()
                    sleep(2)
                    s(id='返回蔚来').click()
                    sleep(0.2)
                    #检查toast
                    save1=s(id='分享成功')
                    if save1.exists:
                        print('分享微信好友成功')
                        sleep(1)
                    else:
                        print('分享微信好友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf1='../../test_report/ios/'+now+'_errorsharewechat_R_stg_tc104.png'
                        c.screenshot(sf1)
                    sleep(2)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
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
                    now2=time.strftime('%Y%m%d_%H%M%S')
                    word2.set_text('邀请试驾es8分享朋友圈:'+now2)
                    sleep(1)
                    s(id='表情').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    s(xpath='//XCUIElementTypeStaticText[@name="公开"]').click()
                    sleep(1)
                    #私密, 仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="私密"]').click()
                    sleep(1)
                    s(id='完成').click()
                    sleep(2)
                    #发表
                    s(id='发表').click()
                    sleep(1)
                    #检查toast
                    save2=s(id='分享成功')
                    if save2.exists:
                        print('分享朋友圈成功')
                        sleep(1)
                    else:
                        print('分享朋友圈失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf2='../../test_report/ios/'+now+'_errorsharewechatpyq_R_stg_tc104.png'
                        c.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
                sleep(2)
                #微博
                wb=s(id='微博')
                if wb.exists:
                    print('分享到微博按钮存在，检查通过')
                    sleep(2)
                    s(id='微博').click()
                    sleep(6)
                    ad=s(id='确定')
                    if ad.exists:
                        s(id='确定').click()
                    sleep(2)
                    s(id='发送到分组').click()
                    sleep(3)
                    #仅自己可见
                    s(xpath='//XCUIElementTypeStaticText[@name="仅自己可见"]').click()
                    sleep(2)
                    #发送
                    s(xpath='//XCUIElementTypeButton[@name="转发到微博"]').click()
                    sleep(1)
                    #检查toast
                    save3=s(id='分享成功')
                    if save3.exists:
                        print('分享微博成功')
                        sleep(1)
                    else:
                        print('分享微博失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf3='../../test_report/ios/'+now+'_errorsharewebo_R_stg_tc104.png'
                        c.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                sh.click()
                sleep(2)
                #我的朋友
                mf=s(id='我的朋友')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(2)
                    s(id='我的朋友').click()
                    sleep(2)
                    s(id='朋友').click()
                    sleep(3)
                    s(xpath='//XCUIElementTypeStaticText[contains(@name,"Sam8")]').click()
                    sleep(1)
                    #检查toast
                    save4=s(id='分享成功')
                    if save4.exists:
                        print('分享我的朋友成功')
                        sleep(1)
                    else:
                        print('分享我的朋友失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y%m%d_%H%M%S')
                        sf4='../../test_report/ios/'+now+'_errorsharemyfriend_R_stg_tc104.png'
                        c.screenshot(sf4)
                    sleep(2)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('邀请试驾按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_邀请试驾es8分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tryes6noncarowner_tc105
#Purpose:检查发现页面的非车主邀请试驾es6功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/02]
#*******************************************************
    def test_faxian_tryes6noncarowner_tc105(self):
        print('TC_检查非车主手机号码登录APP，检查点:发现_写笔记中返回保留再发布功能----')
        print('step1检查发现首页右上角+号是否存在')
        print('step2检查邀请试驾按钮是否存在；step3点击邀请试驾；step4点击es6立即邀请')
        print('step5检查提示框是否出现')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主邀请试驾es6功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        bp_normalloginmp_notenoughscore(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #邀请试驾
            c2=s(id='邀请试驾')
            if c2.exists:
                s(id='邀请试驾').click()
                sleep(3)
                #es6
                sh=s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage')
                sh.click()
                sleep(2)
                #alert
                wh=s(id='知道了')
                if wh.exists:
                    print('提示出现，检查通过')
                    sleep(2)
                    s(id='知道了').click()
                    sleep(2)
                else:
                    print('提示未出现，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios/'+now+'_errNoAlert_R_stg_tc105.png'
                    c.screenshot(sf4)
                    sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('邀请试驾按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_非车主邀请试驾es6功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tryes8noncarowner_tc106
#Purpose:检查发现页面的非车主邀请试驾es8功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/02]
#*******************************************************
    def test_faxian_tryes8noncarowner_tc106(self):
        print('TC_检查非车主手机号码登录APP，检查点:发现_写笔记中返回保留再发布功能----')
        print('step1检查发现首页右上角+号是否存在')
        print('step2检查邀请试驾按钮是否存在；step3点击邀请试驾；step4点击es8立即邀请')
        print('step5检查提示框是否出现')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_非车主邀请试驾es8功能----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #发现
        #s(id='发现').click()
        #sleep(2)
        c1=bp_is_plusexist(self)
        if c1 == True:
            s(xpath='//XCUIElementTypeButton[@name="addPopMenu"]').click()
            sleep(2)
            #邀请试驾
            c2=s(id='邀请试驾')
            if c2.exists:
                s(id='邀请试驾').click()
                sleep(3)
                s.swipe(50,600,50,300,1.0)
                sleep(2)
                #es8
                sh=s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]/XCUIElementTypeImage')
                sh.click()
                sleep(2)
                #alert
                wh=s(id='知道了')
                if wh.exists:
                    print('提示出现，检查通过')
                    sleep(2)
                    s(id='知道了').click()
                    sleep(2)
                else:
                    print('提示未出现，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y%m%d_%H%M%S')
                    sf4='../../test_report/ios/'+now+'_errNoAlert_R_stg_tc106.png'
                    c.screenshot(sf4)
                    sleep(2)
                s(id='all page back grey icon').click()
                sleep(2)
            else:
                print('邀请试驾按钮不存在，请检查原因')
                sleep(2)
            s.close()
            now=time.strftime('%Y%m%d_%H%M%S')
            print('TC_发现_非车主邀请试驾es8功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_giftorderdetail_tc107
#Purpose:检查我的精品订单页面点击精品订单后弹出页面的各项功能
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/15]
#*******************************************************
    def test_wode_giftorderdetail_tc107(self):
        print('TC_检查用户模式打开APP，检查点:我的_精品订单详情页面元素检查和蔚来专员页面功能检查----')
        print('step1检查我的精品订单页面点击某条订单后显示的精品订单详情页面各个元素是否存在')
        print('step2点击蔚来专员按钮；step3检查聊天发送文本和表情是否正常')
        print('step4检查呼叫蔚来专员电话是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_精品订单详情页面元素检查和蔚来专员页面功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        #我的精品订单
        s(id='我的精品订单').click()
        sleep(3)
        s(xpath='//XCUIElementTypeOther[contains(@name,"cake")]')[0].click()
        sleep(3)
        #检查精品订单详情页面的各个元素是否存在
        c1=fun_mygiftorderdetailui_check(self)
        sleep(2)
        if c1 == True:
            print('精品订单详情页面上各个被检查元素都检查完毕')
            sleep(1)
            #蔚来专员
            s.tap(368, 41)
            sleep(3)
            edit=s(id='chat_input_textView')
            edit.click()
            sleep(0.5)
            edit.clear_text()
            sleep(0.5)
            now0=time.strftime('%H%M%S')
            edit.set_text('在线咨询'+now0)
            sleep(1)
            s(id='Send').click()
            sleep(2)
            ch=s(id='在线咨询'+now0)
            if h.exists:
                print('聊天文本存在，检查通过')
                sleep(1)
            else:
                print('聊天文本不存在，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf2='../../test_report/ios/'+now+'_errNoChatText_R_stg_tc107.png'
                c.screenshot(sf2)
                sleep(2)
            #发送表情
            edit.click()
            sleep(0.5)
            edit.clear_text()
            sleep(0.5)
            s(id='chatting biaoqing btn normal').click()
            sleep(1)
            s.tap(39, 554)
            sleep(1)
            s(id='发送').click()
            sleep(2)
            print('聊天发送表情完毕')
            sleep(1)
            #call
            s(xpath='//XCUIElementTypeNavigationBar[@name="蔚来专员"]/XCUIElementTypeButton[2]').click()
            sleep(1)
            tt=s(id='呼叫')
            if tt.exists:
                print('蔚来专员电话呼叫正常')
                sleep(1)
            else:
                print('蔚来专员电话呼叫不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errCallSupport_R_stg_tc107.png'
                c.screenshot(sf1)
            sleep(2)
            s(id='取消').click()
            sleep(2)
            #返回
            s(id='chat back icon').click()
            sleep(2)
            #<
            s.tap(37, 42)
            sleep(2)
        s.tap(37, 42)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的_精品订单详情页面元素检查和蔚来专员页面功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_onlinesupport_tc108
#Purpose:我的页面在线支持功能检查
#OS:iOS
#Device:iPhone7 Plus
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/14]
#*******************************************************
    def test_wode_onlinesupport_tc108(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面在线支持功能检查---')
        print('step1进入我的->在线支持页面;step2点击蔚来专员图标；step3聊天输入文本并检查发送文本是否存在')
        print('step4聊天输入表情；step5击蔚来专员电话按钮检查弹出呼叫是否正常')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——在线支持页面功能检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #我的
        s(id='我的').click()
        sleep(3)
        s.swipe(50,650,50,100,1.0)
        sleep(2)
        #在线支持
        s(id='在线支持').click()
        sleep(3)
        #364,704
        #蔚来专员图标
        #s.tap(364, 704)
        s(xpath='(//XCUIElementTypeOther[@name="在线支持"])[1]/XCUIElementTypeImage').click()
        sleep(3)
        edit=s(id='chat_input_textView')
        edit.click()
        sleep(0.5)
        edit.clear_text()
        sleep(0.5)
        now0=time.strftime('%H%M%S')
        edit.set_text('在线咨询'+now0)
        sleep(1)
        s(id='Send').click()
        sleep(2)
        ch=s(id='在线咨询'+now0)
        if ch.exists:
            print('聊天文本存在，检查通过')
            sleep(1)
        else:
            print('聊天文本不存在，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf2='../../test_report/ios/'+now+'_errNoChatText_R_stg_tc108.png'
            c.screenshot(sf2)
            sleep(2)
        #发送表情
        edit.click()
        sleep(0.5)
        edit.clear_text()
        sleep(0.5)
        s(id='chatting biaoqing btn normal').click()
        sleep(1)
        s.tap(39, 554)
        sleep(1)
        s(id='发送').click()
        sleep(2)
        print('聊天发送表情完毕')
        sleep(1)
        #call
        s(xpath='//XCUIElementTypeNavigationBar[@name="蔚来专员"]/XCUIElementTypeButton[2]').click()
        sleep(1)
        tt=s(id='呼叫')
        if tt.exists:
            print('蔚来专员电话呼叫正常')
            sleep(1)
        else:
            print('蔚来专员电话呼叫不正常，请检查原因')
            sleep(1)
            now=time.strftime('%Y%m%d_%H%M%S')
            sf1='../../test_report/ios/'+now+'_errCallSupport_R_stg_tc108.png'
            c.screenshot(sf1)
        sleep(2)
        s(id='取消').click()
        sleep(2)
        #返回
        s(id='chat back icon').click()
        sleep(2)
        s(id='all page back grey icon').click()
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_我的——在线支持页面功能检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_searchfromlist_tc109
#Purpose:从朋友列表页面搜索好友并进入朋友聊天页面
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/15]
#*******************************************************
    def test_pengyou_searchfromlist_tc109(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友_朋友列表页面搜索好友并进入朋友聊天页面')
        print('step1朋友页面点朋友按钮进入朋友列表页面；step2搜索栏输入好友名称进行搜索')
        print('step3点击搜索出的第一个朋友进入朋友聊天页面检查聊天框是否存在')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从朋友列表页面搜索好友并进入朋友聊天页面----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        #朋友
        s(id='朋友').click()
        sleep(6)
        s(xpath='//XCUIElementTypeNavigationBar[@name="朋友"]/XCUIElementTypeButton').click()
        sleep(2)
        #点搜索栏
        edit=s(className='XCUIElementTypeTextField')
        edit.click()
        sleep(0.5)
        edit.set_value('Sam')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        ff=driver.find_elements_by_class_name('XCUIElementTypeCell')
        sleep(1)
        if ff.exists:
            print('搜索好友功能检查通过')
            sleep(2)
            #1st friend
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
            sleep(4)
            tt=s(id='chat_input_textView')
            if tt.exists:
                print('朋友聊天框显示正常')
                sleep(1)
            else:
                print('朋友聊天框显示不正常，请检查原因')
                sleep(1)
                now=time.strftime('%Y%m%d_%H%M%S')
                sf1='../../test_report/ios/'+now+'_errChatInput_R_stg_tc109.png'
                c.screenshot(sf1)
            sleep(2)
            s(id='all page back grey icon').click()
            sleep(2)
        else:
            print('搜索好友功能检查失败，请检查原因')
            sleep(1)
        s(id='all page back grey icon').click()  
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_朋友_从朋友列表页面搜索好友并进入朋友聊天页面----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorlikecomment_tc110
#Purpose:检查访客模式点击发现页面文章的点赞和评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorlikecomment_tc110(self):
        print('TC_访客模式，检查点:点击发现页面任一文章的点赞和评论按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现页面')
        print('step4点击任一文章的点赞按钮跳转页面是否弹出用户登陆页面;step5点击任一文章的评论按钮后再点击评论输入栏是否弹出用户登陆页面')
        print('step6用原来账号和验证码重新登录app再点击文章进入文章详细页面')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击任一文章的点赞和评论按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(4)
        #点赞
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]').click()
        sleep(1)
        f1=bp_is_loginshow(self)
        if f1 == True:
            print('点击点赞按钮弹出用户登陆页面检查正常')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
        sleep(4)
        #评论
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[3]').click()
        sleep(2)
        #评论栏
        s(xpath='//XCUIElementTypeStaticText[contains(@name,"我也来说~")]').click()
        sleep(1)
        f2=bp_is_loginshow(self)
        if f2 == True:
            print('点击评论输入栏弹出用户登陆页面检查正常')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
            s(id='all page back grey icon').click()
            #s.tap(31, 42)
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s(id='发现').click()
        sleep(2)
        #1st article
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
        sleep(1)
        print('文章详细页面已正常显示')
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击页面文章的点赞和评论按钮的预期动作检查----结束:'+now)

#**************************************************************************************************************************
#TC Name:test_faxian_visitorshareniofriend_tc111
#Purpose:检查访客模式点击发现页面文章的分享NIO好友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#**************************************************************************************************************************
    def test_faxian_visitorshareniofriend_tc111(self):
        print('TC_访客模式，检查点:点击发现页面任一文章的分享NIO好友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现页面')
        print('step4点击任一文章进入文章详细页面,点击分享按钮,再点击分享我的朋友按钮跳转页面是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app再点击文章进入文章详细页面')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击任一文章的分享NIO好友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(4)
        #1st article
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
        sleep(2)
        #share
        #s(id='icon share gray background new').click()
        s.tap(374, 42)
        sleep(2)
        #我的朋友
        s(id='我的朋友').click()
        sleep(1)
        f1=bp_is_loginshow(self)
        if f1 == True:
            print('点击分享我的朋友按钮弹出用户登陆页面检查正常')
            sleep(1)
            s(id='all page back grey icon').click()
            sleep(1)
            s(id='all page back grey icon').click()
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s(id='发现').click()
        sleep(2)
        #1st article
        s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[1]').click()
        sleep(1)
        print('文章详细页面已正常显示')
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击任一文章的分享NIO好友按钮的预期动作检查----结束:'+now)

#*******************************************************************************************************************************
#TC Name:test_faxian_visitorexpjoin_tc112
#Purpose:检查访客模式点击发现的体验页面的活动报名按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*******************************************************************************************************************************
    def test_faxian_visitorexpjoin_tc112(self):
        print('TC_访客模式，检查点:发现_点击体验页面的活动报名按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->体验页面')
        print('step4找到报名活动点击进入,点击报名按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击体验页面的活动报名按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        #体验
        s(id='体验').click()
        sleep(4)
        for i in range(2):
            s.swipe(50,650,50,100,1.0)
            sleep(1)
        sleep(2)
        #小龙自动化3
        s(id='小龙自动化3（请勿报名）').click()
        sleep(4)
        #报名
        joins=s(xpath='//XCUIElementTypeLink[@name="报名"]')
        sleep(1)
        if joins.exists:
            print('报名按钮存在,检查通过')
            sleep(2)
            s(xpath='//XCUIElementTypeLink[@name="报名"]').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击活动报名按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s.tap(32, 42)
            sleep(2)
            s(id='我的').click()
            sleep(2)
            bp_normalloginmp(self)
            sleep(1)
        else:
            print('报名按钮不存在,请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击体验页面的活动报名按钮的预期动作检查----结束:'+now)

#*******************************************************************************************************************************
#TC Name:test_faxian_visitorexpshowpic_tc113
#Purpose:检查访客模式点击发现的体验页面的活动晒图按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*******************************************************************************************************************************
    def test_faxian_visitorexpshowpic_tc113(self):
        print('TC_访客模式，检查点:发现_点击体验页面的活动晒图按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->体验页面')
        print('step4找到晒图活动点击进入,点击晒图按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击体验页面的活动晒图按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        #体验
        s(id='体验').click()
        sleep(3)
        s(id='NIO DAY 选座活动之最后一版').click()
        sleep(4)
        #晒图
        show=s(xpath='//XCUIElementTypeLink[@name="晒图"]')
        sleep(1)
        if show.exists:
            print('晒图按钮存在,检查通过')
            sleep(1)
            s(xpath='//*[@name="晒图"]').click()
            sleep(2)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击活动报名按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s.tap(32, 42)
            sleep(2)
            s(id='我的').click()
            sleep(2)
            bp_normalloginmp(self)
            sleep(1)
        else:
            print('晒图按钮不存在,请检查原因')
            sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击体验页面的活动晒图按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorseminarlikecomment_tc114
#Purpose:检查访客模式点击发现页面专题的点赞和评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorseminarlikecomment_tc114(self):
        print('TC_访客模式，检查点:点击发现页面专题的点赞和评论按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4找到某专题:专题测试221点击进入,再点击某内容进入,再点赞按钮跳转页面是否弹出用户登陆页面')
        print('step5点击评论按钮是否弹出用户登陆页面;step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击专题的点赞和评论按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(2)
        s(id='资讯').click()
        sleep(3)
        for i in range(6):
            s.swipe(50,650,50,100,1.0)
            sleep(1)
        sleep(2)
        #专题测试221
        ch=s(id='专题测试221')
        ch0=s(id='专题测试221').displayed
        if ch.exists and ch0 == True:
            print('专题存在/已找到')
            sleep(2)
            s(id='专题测试221').click()
            sleep(8)
            #1st content
            s(xpath='//XCUIElementTypeOther[@name="专题测试221"]/XCUIElementTypeLink[1]').click()
            sleep(4)
            #点赞
            s(xpath='//XCUIElementTypeOther[@name="2019新年礼物安排上了，请签收"]/XCUIElementTypeOther[27]').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击点赞按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            sleep(4)
            #评论
            s(xpath='//XCUIElementTypeOther[@name="2019新年礼物安排上了，请签收"]/XCUIElementTypeOther[25]').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击评论输入栏弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s.tap(32, 42)
                sleep(1)
                s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在/未找到,请检查原因')
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击专题的点赞和评论按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorseminarshareniofriend_tc115
#Purpose:检查访客模式点击发现页面专题的点赞和评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorseminarshareniofriend_tc115(self):
        print('TC_访客模式，检查点:点击发现页面专题和专题内容的分享我的朋友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4找到某专题:专题测试221点击分享,再点击我的朋友,检查是否弹出用户登陆页面')
        print('step5点击某专题内容进入,再点击分享按钮,再点击我的朋友,检查是否弹出用户登陆页面')
        print('step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击专题和专题内容的分享我的朋友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(2)
        s(id='资讯').click()
        sleep(3)
        for i in range(6):
            s.swipe(50,650,50,100,1.0)
            sleep(1)
        sleep(2)
        #专题测试221
        ch=s(id='专题测试221')
        ch0=s(id='专题测试221').displayed
        if ch.exists and ch0 == True:
            print('专题存在/已找到')
            sleep(2)
            s(id='专题测试221').click()
            sleep(8)
            #share
            s.tap(382, 42)
            sleep(2)
            s(id='我的朋友').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击专题的分享我的朋友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
            sleep(2)
            #1st content专题内容
            s(xpath='//XCUIElementTypeOther[@name="专题测试221"]/XCUIElementTypeLink[1]').click()
            sleep(4)
            #分享
            s(xpath='//XCUIElementTypeOther[@name="2019新年礼物安排上了，请签收"]/XCUIElementTypeOther[2]').click()
            #382,42
            sleep(2)
            s(id='我的朋友').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击专题内容的分享我的朋友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s.tap(32, 42)
                sleep(1)
                s.tap(32, 42)
            sleep(2)
        else:
            print('专题不存在/未找到,请检查原因')
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(2)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击专题和专题内容的分享我的朋友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorugclikecomment_tc116
#Purpose:检查访客模式点击发现页面UGC的点赞和评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorugclikecomment_tc116(self):
        print('TC_访客模式，检查点:点击发现页面UGC的点赞和评论按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->此刻页面')
        print('step4点击UGC进入,点击点赞按钮跳转页面检查是否弹出用户登陆页面;step5点击评论按钮,再点击评论输入栏检查是否弹出用户登陆页面')
        print('step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击UGC的点赞和评论按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='此刻').click()
        sleep(3)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            #SamSTG
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"SamSTG")]').click()
            sleep(3)
            #点赞
            s(xpath='//XCUIElementTypeImage[@name="icon_dislike_new"]').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击点赞按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            sleep(3)
            #评论
            s(xpath='//XCUIElementTypeImage[@name="icon_comment_new"]').click()
            sleep(3)
            #评论栏
            s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击评论输入栏弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                #s.tap(31, 42)
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击页面UGC的点赞和评论按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorugcshareniofriend_tc117
#Purpose:检查访客模式点击发现页面UGC的分享我的朋友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorugcshareniofriend_tc117(self):
        print('TC_访客模式，检查点:点击发现页面UGC的分享我的朋友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->此刻页面')
        print('step4点击UGC进入,点击分享按钮,再点击我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击UGC的分享我的朋友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='此刻').click()
        sleep(3)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            #SamSTG
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"SamSTG")]').click()
            sleep(3)
            #分享
            s(id='icon share gray background new').click()
            sleep(2)
            s(id='我的朋友').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享我的朋友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                #s.tap(31, 42)
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击UGC的分享我的朋友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorugcreport_tc118
#Purpose:检查访客模式点击发现页面UGC的举报按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorugcreport_tc118(self):
        print('TC_访客模式，检查点:点击发现页面UGC的举报按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->此刻页面')
        print('step4点击UGC进入,点击分享按钮,再点击举报钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击UGC的举报按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='此刻').click()
        sleep(3)
        u=driver.find_elements_by_class_name('XCUIElementTypeCell')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(2)
            #SamSTG
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"SamSTG")]').click()
            sleep(3)
            #分享
            s(id='icon share gray background new').click()
            sleep(2)
            s(id='举报').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击举报按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                #s.tap(31, 42)
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击UGC的举报按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorvotelikecomment_tc119
#Purpose:检查访客模式点击发现页面投票的点赞和评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitorvotelikecomment_tc119(self):
        print('TC_访客模式，检查点:点击发现页面投票的点赞和评论按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4搜索找到小龙投票stg,点击进入投票页面,点击点赞按钮跳转页面检查是否弹出用户登陆页面')
        print('step5点击评论按钮检查是否弹出用户登陆页面;step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击投票页面的点赞和评论按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='资讯').click()
        sleep(3)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('小龙投票stg')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        #小龙投票stg
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('资讯tab小龙投票stg已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #点赞
            s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[54]').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击点赞按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
            sleep(6)
            #评论
            s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[52]').click()
            ###s(xpath='(//XCUIElementTypeOther[@name="自动化投票"])[1]/XCUIElementTypeOther[19]/XCUIElementTypeStaticText').click()
            #s.tap(341, 703)
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击评论按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
            #s(xpath='(//XCUIElementTypeOther[@name="小龙投票stg"])[1]/XCUIElementTypeOther[1]').click()
            s.tap(32, 42)
            sleep(1)
            s.tap(32, 42)
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击投票页面的点赞和评论按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorvoteshareniofriend_tc120
#Purpose:检查访客模式点击发现页面投票的分享我的朋友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_faxian_visitorvoteshareniofriend_tc120(self):
        print('TC_访客模式，检查点:点击发现页面投票的分享我的朋友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4搜索找到小龙投票stg,点击进入投票页面,再点击分享按钮->我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击投票的分享我的朋友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='资讯').click()
        sleep(3)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(0.5)
        sear.set_text('小龙投票stg')
        sleep(0.5)
        #search
        s(id='Search').click()  
        sleep(2)
        #小龙投票stg
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('资讯小龙投票stg已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #分享
            s(xpath='//XCUIElementTypeOther[@name="小龙投票stg"]/XCUIElementTypeOther[2]').click()
            #(382,42)
            sleep(2)
            s(id='我的朋友').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享我的朋友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s.tap(32, 42)
                sleep(1)
        #x
        s(id='evaluate close').click()
        #37,42
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击投票的分享我的朋友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorlivecastcomment_tc121
#Purpose:检查访客模式点击发现页面直播的评论按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_faxian_visitorlivecastcomment_tc121(self):
        print('TC_访客模式，检查点:点击发现页面直播的评论按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4搜索找到stg倒计时直播,点击进入直播页面')
        print('step5点击评论输入栏检查是否弹出用户登陆页面;step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击直播的评论按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='资讯').click()
        sleep(3)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(1)
        sear.set_text('stg倒计时直播')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        #stg倒计时直播
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('stg倒计时直播存在/已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #评论
            s(xpath='//XCUIElementTypeStaticText[contains(@name,"你的观点")]').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击评论输入栏弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
        s.tap(37, 42)
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击直播的评论按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitorlivecastshareniofriend_tc122
#Purpose:检查访客模式点击发现页面直播的分享我的朋友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_faxian_visitorlivecastshareniofriend_tc122(self):
        print('TC_访客模式，检查点:点击发现页面直播的分享我的朋友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击发现->资讯页面')
        print('step4搜索找到stg倒计时直播,点击进入直播页面,再点击分享按钮->我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击直播的分享我的朋友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(3)
        s(id='资讯').click()
        sleep(3)
        s(id='main global search icon').click()
        sleep(2)
        #search
        sear=s(className='XCUIElementTypeTextField')
        sear.click()
        sleep(0.5)
        sear.set_text('stg倒计时直播')
        sleep(1)
        #search
        s(id='Search').click()  
        sleep(3)
        #stg倒计时直播
        ch=s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]')
        sleep(1)
        if ch.exists:
            print('stg倒计时直播存在/已找到')
            sleep(1)
            s(xpath='//XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell[2]').click()
            sleep(9)
            #分享
            s(id='icon share black').click()
            #(382,42)
            sleep(2)
            #我的朋友
            s(xpath='//XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeButton').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享我的朋友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
        #x
        s(id='evaluate close').click()
        #37,42
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击直播的分享我的朋友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_faxian_visitornowheadiconfollow_tc123
#Purpose:检查访客模式点击发现页面此刻的用户头像和关注按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/18]
#*********************************************************************************************************************************
    def test_faxian_visitornowheadiconfollow_tc123(self):
        print('TC_访客模式，检查点:点击发现页面此刻的用户头像和关注按钮按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号')
        print('step3点击发现->此刻页面;step4点击用户头像检查是否弹出用户登陆页面')
        print('step5点击关注按钮检查是否弹出用户登陆页面;step6用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击此刻的用户头像和关注按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #发现
        s(id='发现').click()
        sleep(2)
        s(id='此刻').click()
        sleep(3)
        #用户头像
        s.tap(54, 124)
        sleep(1)
        f1=bp_is_loginshow(self)
        if f1 == True:
            print('点击用户头像钮弹出用户登陆页面检查正常')
            sleep(1)
            s(id='all page back grey icon').click()
        sleep(2)
        #关注
        s(xpath='//XCUIElementTypeButton[@name="关注"]').click()
        sleep(1)
        f2=bp_is_loginshow(self)
        if f2 == True:
            print('点击关注按钮弹出用户登陆页面检查正常')
            sleep(1)
            s(id='all page back grey icon').click()
        sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_发现_访客模式点击此刻的用户头像和关注按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_aiche_visitorcontentshareniofriend_tc124
#Purpose:检查访客模式点击爱车页面详细配置表的分享NIO好友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_aiche_visitorcontentshareniofriend_tc124(self):
        print('TC_访客模式，检查点:点击爱车页面详细配置表的分享NIO好友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击爱车页面')
        print('step4翻页点击详细配置表进入详细配置表页面,再点击分享按钮->我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击详细配置表的分享NIO好友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #爱车
        s(id='爱车').click()
        sleep(3)
        s.swipe(50,650,50,90,1.0)
        sleep(1)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
        sleep(1)
        s.swipe(50,300,50,100,1.0)
        sleep(1)
        s.swipe(50,650,50,90,1.0)
        sleep(3)
        ch=s(xpath='//XCUIElementTypeStaticText[@name="详细配置表"]')
        ch0=s(xpath='//XCUIElementTypeStaticText[@name="详细配置表"]').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('详细配置表按钮找到')
            sleep(2)
            s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[6]').click()
            #s(id='详细配置表').click()
            sleep(6)
            #分享
            #share
            s(id='nav share btn').click()
            sleep(2)
            #NIO好友
            s(id='NIO好友').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享NIO好友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='nav back btn').click()
                #38,42
                sleep(2)
        else:
            print('详细配置表按钮未找到,请检查原因')
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击详细配置表的分享NIO好友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_aiche_visitormilecalculatorshareniofriend_tc125
#Purpose:检查访客模式点击爱车页面里程计算器的分享NIO好友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_aiche_visitormilecalculatorshareniofriend_tc125(self):
        print('TC_访客模式，检查点:点击爱车页面里程计算器的分享NIO好友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击爱车页面')
        print('step4翻页点击里程计算器进入里程计算器页面,再点击分享按钮->我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击里程计算器的分享NIO好友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #爱车
        s(id='爱车').click()
        sleep(3)
        s.swipe(50,650,50,90,1.0)
        sleep(1)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
        sleep(1)
        s.swipe(50,300,50,100,1.0)
        sleep(1)
        s.swipe(50,650,50,90,1.0)
        sleep(3)
        ch=s(xpath='//XCUIElementTypeStaticText[@name="里程计算器"]')
        ch0=s(xpath='//XCUIElementTypeStaticText[@name="里程计算器"]').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('里程计算器按钮找到')
            sleep(2)
            #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[2]').click()
            s(id='里程计算器').click()
            sleep(6)
            #分享
            #share
            s(id='nav share btn').click()
            sleep(2)
            #NIO好友
            s(id='NIO好友').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享NIO好友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='nav back btn').click()
                #38,42
                sleep(2)
        else:
            print('里程计算器按钮未找到,请检查原因')
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击里程计算器的分享NIO好友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_aiche_visitorcityserviceshareniofriend_tc126
#Purpose:检查访客模式点击爱车页面城市服务查询的分享NIO好友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_aiche_visitorcityserviceshareniofriend_tc126(self):
        print('TC_访客模式，检查点:点击爱车页面城市服务查询的分享NIO好友按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击爱车页面')
        print('step4翻页点击城市服务查询进入城市服务查询页面,再点击分享按钮->我的朋友按钮检查是否弹出用户登陆页面')
        print('step5用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击城市服务查询页面的分享NIO好友按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #爱车
        s(id='爱车').click()
        sleep(3)
        s.swipe(50,650,50,90,1.0)
        sleep(1)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
        sleep(1)
        s.swipe(50,300,50,100,1.0)
        sleep(1)
        s.swipe(50,650,50,90,1.0)
        sleep(3)
        ch=s(id='城市服务查询')
        ch0=s(id='城市服务查询').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('城市服务查询按钮找到')
            sleep(2)
            #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[2]').click()
            s(id='城市服务查询').click()
            sleep(6)
            #分享
            #share
            s(id='nav share btn').click()
            sleep(2)
            #NIO好友
            s(id='NIO好友').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击分享NIO好友按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
                sleep(1)
                s(id='nav back btn').click()
                #38,42
                sleep(2)
        else:
            print('城市服务查询按钮未找到,请检查原因')
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击城市服务查询页面的分享NIO好友按钮的预期动作检查----结束:'+now)

#*********************************************************************************************************************************
#TC Name:test_aiche_visitorrechargemap_tc127
#Purpose:检查访客模式点击爱车页面充电地图的分享NIO好友按钮的预期动作
#OS:iOS
#Device:iPhone7 Plus
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2019/02/19]
#*********************************************************************************************************************************
    def test_aiche_visitorrechargemap_tc127(self):
        print('TC_访客模式，检查点:点击爱车页面充电地图的3个按钮是否跳转到用户登录页面')
        print('step1检查用户是否已经登录;step2如果用户已经登录则退出原来账号；step3点击爱车页面')
        print('step4翻页点击城市服务查询进入充电地图页面,再点击充电历史按钮检查是否弹出用户登陆页面')
        print('step5点击上报充电桩按钮检查是否弹出用户登陆页面;step6点击扫码加电按钮检查是否弹出用户登陆页面')
        print('step7用原来账号和验证码重新登录app')
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击充电地图页面的充电历史/上报充电桩/扫码加电按钮的预期动作检查----开始:'+now)
        sleep(1)
        s=c.session('com.do1.WeiLaiApp.inhouse')
        bp_is_loggedin(self)
        sleep(1)
        #爱车
        s(id='爱车').click()
        sleep(3)
        s.swipe(50,650,50,90,1.0)
        sleep(1)
        for i in range(2):
            s.swipe(50,600,50,90,1.0)
        sleep(1)
        s.swipe(50,300,50,100,1.0)
        sleep(1)
        s.swipe(50,650,50,90,1.0)
        sleep(3)
        ch=s(id='充电地图')
        ch0=s(id='充电地图').displayed
        sleep(1)
        if ch.exists and ch0 == True:
            print('充电地图按钮找到')
            sleep(2)
            #s(xpath='//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeButton[2]').click()
            s(id='充电地图').click()
            sleep(6)
            #充电历史
            s(id='peMapHistory').click()
            sleep(1)
            f1=bp_is_loginshow(self)
            if f1 == True:
                print('点击充电历史按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
            sleep(1)
            #上报充电桩
            s(id='peMapReportSpot').click()
            sleep(1)
            f2=bp_is_loginshow(self)
            if f2 == True:
                print('点击上报充电桩按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
            sleep(1)
            #扫码加电
            s(id='PEScanBack').click()
            sleep(1)
            f3=bp_is_loginshow(self)
            if f3 == True:
                print('点击扫码加电按钮弹出用户登陆页面检查正常')
                sleep(1)
                s(id='all page back grey icon').click()
            sleep(1)
            s(id='routPlanBack').click()
            #30,56
            sleep(2)
        else:
            print('充电地图按钮未找到,请检查原因')
            sleep(2)
        s(id='我的').click()
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        s.close()
        now=time.strftime('%Y%m%d_%H%M%S')
        print('TC_爱车_访客模式点击充电地图页面的充电历史/上报充电桩/扫码加电按钮的预期动作检查----结束:'+now)
        
if __name__ == '__main__':unittest.main()
