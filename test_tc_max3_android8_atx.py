#coding=utf-8
#test purpose: verify the main features on XiaoMi
#os: Android
#device: Mi Max3
#version:android 8.1
#author: Sam Wang
#update date: created by Sam [2018-09-21]

import unittest
import time
import os
import random
from time import sleep

from common_max3_android8_atx import fun_myfansui_check
from common_max3_android8_atx import fun_mywatchui_check
from common_max3_android8_atx import fun_mypublishui_check
from common_max3_android8_atx import bp_is_loggedin
from common_max3_android8_atx import fun_getinfo
from common_max3_android8_atx import bp_normalloginmp
from common_max3_android8_atx import bp_is_loginshow
from common_max3_android8_atx import fun_getloginmenu
from common_max3_android8_atx import bp_is_plusexist
from common_max3_android8_atx import bp_is_publishnowexist
from common_max3_android8_atx import bp_is_openmultichatexist
from common_max3_android8_atx import fun_findui_check
from common_max3_android8_atx import fun_personalinfoui_check
from common_max3_android8_atx import fun_scoredetailui_check
from common_max3_android8_atx import fun_giftui_check
from common_max3_android8_atx import fun_articleui_check
from common_max3_android8_atx import fun_cartui_check
from common_max3_android8_atx import fun_pgcui_check
from common_max3_android8_atx import fun_articledetailui_check
from common_max3_android8_atx import fun_giftorderui_check
from common_max3_android8_atx import fun_giftorderdetailui_check

import uiautomator2 as u2
d=u2.connect('6036a61d')

class Weilai_test(unittest.TestCase):

    def setUp(self):
        d.app_start('cn.com.weilaihui3')
        sleep(3)
    
    def tearDown(self):
        d.press('back')
        d.press('back')
        d.press('back')
        d.press('back')
        sleep(1)

#*******************************************************
#TC Name:test_wode_fans_tc001
#Purpose:检查我的页面点击粉丝后弹出页面的各项功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/21]
#*******************************************************
    def test_wode_fans_tc001(self):
        print('TC_检查用户模式打开APP，检查点:我的_粉丝功能----step1检查我的页面点击粉丝后页面各个元素是否存在')
        print('step2取消互相关注/关注；step3检查被取消互相关注/关注的粉丝关系是否变成+关注/互相关注')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消互相关注/+关注功能----开始:'+now)
        sleep(4)
        d(text='我的').click()
        sleep(3)
        d(text='粉丝').click()
        sleep(2)
        #检查粉丝面的各个元素是否存在
        c1=fun_myfansui_check(self)
        if c1 == True:
            print('粉丝页面上各个被检查元素都已经检查完毕')
            sleep(1)
        #取消互相关注/+关注
        d.toast.reset()
        for j in range(2):
            d(resourceId='cn.com.weilaihui3:id/user_friend_relation').click()
            #check the message of toast
            print(d.toast.get_message(1.0,2.0))
            if '取消成功' in d.toast.get_message(1.0,2.0):
                print('取消互相关注的功能检查通过--互相关注-->+关注')
            elif '关注成功' in d.toast.get_message(1.0,2.0):
                print('+关注的功能检查通过--+关注-->互相关注')
            else:
                print('取消互相关注/+关注的功能检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/android/'+now+'_errorChangeFans_R.png'
                d.screenshot(sf2)
                d.toast.reset()
            sleep(3)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_粉丝页面元素检查和取消关注/+关注功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_watch_tc002
#Purpose:检查我的页面点击关注后弹出页面的各项功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_wode_watch_tc002(self):
        print('TC_检查用户模式打开APP，检查点:我的_关注功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2取消关注；step3检查刷新后被取消关注的朋友是否消失')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注功能----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        #关注
        d(text='关注').click()
        sleep(2)
        #检查发布关注面的各个元素是否存在
        c1=fun_mywatchui_check(self)
        if c1 == True:
            print('关注页面上各个被检查元素都已经检查完毕')
            sleep(1)
        #取消关注
        nickname=d(resourceId='cn.com.weilaihui3:id/user_friend_name')[0].info['text']
        #print(nickname)
        d(resourceId='cn.com.weilaihui3:id/user_friend_relation').click()
        sleep(2)
        #refresh
        d.swipe(100,300,100,700,1.0)
        sleep(2)
        #check wether the friend who was been cancelled caring dispeared
        n=d(text='+nickname+')
        if not n.exists:
            print('取消关注的功能检查通过--'+nickname+'已经被取消关注了')
        else:
            print('取消关注的功能检查失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorCancelCare_R.png'
            d.screenshot(sf1)
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_关注页面元素检查和取消关注功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_publish_tc003
#Purpose:检查我的页面点击发布后弹出页面的各项功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_wode_publish_tc003(self):
        print('TC_检查用户模式打开APP，检查点:我的_发布功能----step1检查我的页面点击发布后页面各个元素是否存在')
        print('step2发布功能是否正常；step3检查发布内容里是否可以一次最大上传9张图片；step4检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        #发布
        d(text='发布').click()
        sleep(3)
        #检查发布页面的各个元素是否存在
        c1=fun_mypublishui_check(self)
        if c1 == True:
            print('发布页面上各个被检查元素都正常显示.')
            sleep(1)
        #发布
        d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
        sleep(2)
        d(resourceId='cn.com.weilaihui3:id/image').click()
        sleep(2)
        #允许
        if d(text='允许').exists:
            d(text='允许').click()
            sleep(2)
        for i in range(10,19):
            d(resourceId='cn.com.weilaihui3:id/media_item_cb_check')[i].click()
            sleep(1)
        d(text='确定').click()
        sleep(1)
        word=d(resourceId='cn.com.weilaihui3:id/community_create_evaluation_edit_view')
        word.click()
        sleep(1)
        now0=time.strftime('%Y-%m-%d %H_%M_%S')
        word.send_keys('人生苦短#发布#'+now0)
        sleep(1)
        d(text='发布').click()
        sleep(10)
        #refresh
        d.swipe(100,300,100,700,1.0)
        sleep(2)
        #check numbers of pictures and published text here
        title=d(resourceId='cn.com.weilaihui3:id/ugc_list_content').info['text']
        if '人生苦短#发布#'+now0 in title:
            print('发布内容的文字检查通过')
        else:
            print('发布内容的文字检查失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorPublishText_R.png'
            d.screenshot(sf1)
        sleep(2)
        number=d(resourceId='cn.com.weilaihui3:id/ugc_list_three_img_num').info['text']
        if '9' in number:
            print('发布内容的上传9张图片检查通过')
        else:
            print('发布内容的上传9张图片检查失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorPublishPicture9_R.png'
            d.screenshot(sf2)
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_发布页面元素检查和发布功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_reloginmp_tc004
#Purpose:检查用户用手机号+验证码重新登录app的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_wode_reloginmp_tc004(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用手机号码重新登录，如果已登录先退出账号----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3选择用手机号+验证码登录；step4检查登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('客户重新登录账号----开始:'+now)
        f=fun_getinfo(self)
        sleep(2)
        bp_is_loggedin(self)
        sleep(2)
        #登录页面
        d(text='注册/登录').click()
        sleep(1)
        mobile_no=d(resourceId='cn.com.weilaihui3:id/login_main_login_phone_edit')
        mobile_no.click()
        mobile_no.send_keys(f[0])
        sleep(1)
        code=d(resourceId='cn.com.weilaihui3:id/login_main_login_code_edit')
        code.click()
        #code.send_keys(f[1])
        code.send_keys('112233')
        sleep(1)
        d.set_fastinput_ime(True)
        sleep(1)
        d.press('back')
        sleep(1)
        d(resourceId='cn.com.weilaihui3:id/login_main_login_button').click()
        #d(text='注册/登录').click()
        sleep(8)
        d.swipe(100,300,100,1000,1.0)
        sleep(2)
        if d(textContains='Sam8').exists:
            print('登录成功！')
        else:
            print('登录失败！')
            sleep(1)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorLoginMP_R.png'
            d.screenshot(sf1)
        sleep(1)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_客户重新登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_visitor_tc005
#Purpose:检查访客模式点击我的页面各个菜单的预期动作
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app/未登录
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_wode_visitor_tc005(self):
        print('TC_访客模式点击我的页面各个菜单，检查点:点击我的页面各个菜单是否跳转到用户登录页面----step1检查用户是否已经登录')
        print('step2如果用户已经登录则退出原来账号；step3点击我的页面；step4从excel文件读取要检查的各个菜单名称，')
        print('依次点击检查是否会跳转到用户登录界面;step5点击加入蔚来跳转页面是否正常显示;step6点击设置弹出页面是否正常显示')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_访客模式点击我的页面各个菜单跳转页面----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(1)
        #我的
        d(text='我的').click()
        sleep(4)
        menu_name=fun_getloginmenu(self)
        sleep(1)
        #check the menu by turn
        for j in range(0,11):
            menu=d(text=menu_name[j])
            menu.click()
            sleep(2)
            print('检查的菜单名称：'+menu_name[j])
            bp_is_loginshow(self)
            d.press('back')
            sleep(2)
        #加入蔚来
        d(text='加入蔚来').click()
        sleep(9)
        #所有职位
        tl=d(text='NIO')
        if not tl.exists:
            print('访客模式点击加入蔚来跳转页面不正常，请检查')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf0='../../test_report/android/'+now+'_errorJoinNIO_R.png'
            d.screenshot(sf0)
            sleep(2)
        else:
            print('访客模式点击加入蔚来跳转页面正常显示')
            sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        #设置
        d(resourceId='cn.com.weilaihui3:id/my_palace_setting_layout').click()
        sleep(1)
        out=d(text='退出登录')
        if out.exists:
            print('访客模式点击设置跳转页面不正常，请检查')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorSettings_R.png'
            d.screenshot(sf1)
            sleep(2)
        else:
            print('访客模式点击设置跳转页面正常显示')
        sleep(2)
        d.press('back')
        sleep(2)
        bp_normalloginmp(self)
        sleep(1)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_访客模式点击我的页面各个菜单跳转页面----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnow_tc006
#Purpose:检查发现页面的发布功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_faxian_publishnow_tc006(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻功能----step1检查发现首页右上角+号是否存在；')
        print('step2检查发布此刻按钮是否存在；step3发布功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片；')
        print('step5检查发布文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻----开始:'+now)
        sleep(4)
        #发现
        d(text='发现').click()
        sleep(4)
        c1=bp_is_plusexist(self)
        if c1 == True:
            d(resourceId='cn.com.weilaihui3:id/main_page_more').click()
            sleep(2)
            #发布此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                d(text='发布此刻').click()
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/image').click()
                sleep(2)
                #允许
                allow=d(text='允许')
                if allow.exists:
                    d(text='允许').click()
                    sleep(2)
                for i in range(10,19):
                    d(resourceId='cn.com.weilaihui3:id/media_item_cb_check')[i].click()
                    sleep(1)
                d(text='确定').click()
                sleep(1)
                word=d(resourceId='cn.com.weilaihui3:id/community_create_evaluation_edit_view')
                word.click()
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('人生苦短#发布此刻_'+now0)
                sleep(1)
                d(text='发布').click()
                sleep(9)
                #check numbers of pictures and published text here
                title=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')[0].info['text']
                if '人生苦短#发布此刻_'+now0 in title:
                    print('发布内容的文字检查通过')
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorText_R.png'
                    d.screenshot(sf1)
                sleep(2)
                number=d(resourceId='cn.com.weilaihui3:id/ugc_list_three_img_num').info['text']
                #print(number.info['text'])
                if '9' in number:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorPic9_R.png'
                    d.screenshot(sf2)
                sleep(2)
                d.press('back')
                sleep(1)
                d.press('back')
                sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻----结束:'+now)

#*******************************************************
#TC Name:test_wode_deletepublished_tc007
#Purpose:检查我的页面的删除已发布内容的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/05]
#*******************************************************
    def test_wode_deletepublished_tc007(self):
        print('TC_检查手机号码登录APP，检查点:我的——删除已发布的内容---step1点击我的页面发布;step2检查是否有已发布的内容，')
        print('有的话点击它进入详细页面再点击右上角按钮，执行删除动作;step3检查被删除的发布内容是否删除成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_删除已发布的内容----开始:'+now)
        sleep(4)
        #我的
        d.xpath('//*[@text="我的"]').click()
        sleep(4)
        d.xpath('//*[@text="发布"]').click()
        sleep(2)
        p=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')
        if p.exists:
            ct=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')
            checktext=ct.info['text']
            ct.click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(1)
            #删除
            d(text='删除').click()
            sleep(1)
            #确定
            d(resourceId='cn.com.weilaihui3:id/common_alert_dialog_right_container').click()
            sleep(2)
            ch=d.xpath('//*[@text="'+checktext+'"]')
            if ch.exists:
                print('发布的内容删除失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorDeleted_R.png'
                d.screenshot(sf1)
            else:
                print('发布的内容删除成功')
            sleep(2)
        else:
            print('没有已发布的内容可以删除！')
        sleep(2)
        d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
        sleep(2)
        d.press('back')
        sleep(1)
        d.press('back')
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_删除已发布的内容----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwechat_tc008
#Purpose:检查用户能否用微信账号登录app
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_wode_loginwechat_tc008(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微信登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微信登录；step4检查微信登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(1)
        #登录页面
        d(text='注册/登录').click()
        sleep(1)
        #微信登录
        btn=d(resourceId='cn.com.weilaihui3:id/login_main_wechat_login_button')
        if btn.exists:
            print('微信登录按钮存在')
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/login_main_wechat_login_button').click()
            sleep(9)
            name=d(resourceId='cn.com.weilaihui3:id/my_head_info_user_name').info['text']
            if '王若妍' in name:
                print('微信登录成功！')
            else:
                print('微信登录失败！')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/android/'+now+'_errorLoginWechat_R.png'
                d.screenshot(sf0)
            sleep(2)
        else:
            print('微信登录按钮不存在，请检查原因')
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorNoButton_R.png'
            d.screenshot(sf1)
            sleep(2)
            d.press('back')
            sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微信登录账号----结束:'+now)

#*******************************************************
#TC Name:test_wode_loginwebo_tc009
#Purpose:检查用户能否用微博账号登录app
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_wode_loginwebo_tc009(self):
        print('TC_检查手机号码登录APP，检查点:我的页面里用微博登录，如果已登录先退出账号----step1检查用户是否已经登录；')
        print('step2如果用户已经登录则退出原来账号；step3选择用微博登录；step4检查微博登录的账号是否正确')
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----开始:'+now)
        g=bp_is_loggedin(self)
        sleep(2)
        #登录页面
        d(text='注册/登录').click()
        sleep(1)
        #微博登录
        btn=d(resourceId='cn.com.weilaihui3:id/login_main_weibo_login_button')
        if btn.exists:
            print('微博登录按钮存在')
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/login_main_weibo_login_button').click()
            sleep(5)
            #确定
            d.xpath('//*[@text="确定"]').click()
            sleep(8)
            name=d(resourceId='cn.com.weilaihui3:id/my_head_info_user_name').info['text']
            if 'Sam8' in name:
                print('微博登录成功！')
            else:
                print('微博登录失败！')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf0='../../test_report/android/'+now+'_errorLoginWebo_R.png'
                d.screenshot(sf0)
            sleep(2)
        else:
            print('微博登录按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf1='../../test_report/android/'+now+'_errorNoButton_R.png'
            d.screenshot(sf1)
            sleep(2)
            d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_客户用微博登录账号----结束:'+now)

#*******************************************************
#TC Name:test_faxian_tabcheck_tc010
#Purpose:检查发现页面tab上元素和推荐、此刻子tab页上元素是否存在
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_faxian_tabcheck_tc010(self):
        print('TC_检查用户模式打开APP，检查点:发现_tabUI检查功能----step1检查发现页面tab上各子tab元素是否存在;')
        print('step2检查推荐子tab页上各元素是否存在;step3检查此刻子tab页上各元素是否存在')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----开始:'+now)
        sleep(4)
        #检查粉丝面的各个元素是否存在
        c1=fun_findui_check(self)
        if c1 == True:
            print('发现页面tab上各子tab元素检查通过')
        else:
            print('发现页面tab上各子tab元素检查失败，请检查原因')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_tab上元素和推荐、此刻子tab页上元素检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_personalinfo_tc011
#Purpose:我的个人信息页面上元素UI检查和相关元素的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_wode_personalinfo_tc011(self):
        print('TC_检查手机号码登录APP，检查点:个人信息页面上元素UI检查和相关元素的功能检查----step1进入个人信息页面；')
        print('step2个人信息页面上元素UI检查;step3检查点击头像的功能;step4检查昵称和简称是否可以编辑;step5检查性别是否')
        print('可以改变;step6检查常驻地区页面是否可以进入;step7检查地址管理页面是否可以进入;step8检查用户隐私条款页面')
        print('是否可以进入;step9检查修改的个人信息是否可以保存成功')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        d(resourceId='cn.com.weilaihui3:id/my_head_info_user_name').click()
        sleep(2)
        #编辑个人信息
        d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').click()
        sleep(2)
        #检查发布页面的各个元素是否存在
        c1=fun_personalinfoui_check(self)
        sleep(2)
        if c1 == True:
            print('个人信息页面上各个被检查元素都正常显示.')
            sleep(1)
            #点击头像
            d(resourceId='cn.com.weilaihui3:id/login_update_user_message_header_image').click()
            sleep(2)
            #拍照
            ph=d(resourceId='cn.com.weilaihui3:id/choose_up_button')
            if ph.exists:
                print('拍照按钮存在')
                d(resourceId='cn.com.weilaihui3:id/choose_up_button').click()
                sleep(1)
                #允许
                allow=d(text='允许')
                if allow.exists:
                    d(text='允许').click()
                    sleep(1)
                #允许
                allow2=d(text='允许')
                if allow2.exists:
                    d(text='允许').click()
                    sleep(1)
                phbtn=d(resourceId='com.android.camera:id/v9_shutter_button_internal')
                if phbtn.exists:
                    print('手机相机已正常弹出')
                else:
                    print('手机相机没有正常弹出，请检查原因')
                sleep(1)
                d.press('back')
                sleep(2)
            else:
                print('拍照按钮不存在，请检查')
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/login_update_user_message_header_image').click()
            sleep(2)
            #从手机相册选择
            pic=d(resourceId='cn.com.weilaihui3:id/choose_bellow_button')
            if pic.exists:
                print('从手机相册选择按钮存在')
                d(resourceId='cn.com.weilaihui3:id/choose_bellow_button').click()
                sleep(1)
                picbtn=d(text='相册')
                if picbtn.exists:
                    print('手机相册可以正常调用')
                else:
                    print('手机相册不可以正常调用，请检查原因')
                sleep(2)
                d.press('back')
                sleep(2)
            else:
                print('从手机相册选择按钮不存在，请检查')
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/login_update_user_message_header_image').click()
            sleep(2)
            #取消
            can=d(resourceId='cn.com.weilaihui3:id/cancle_button')
            if can.exists:
                print('取消按钮存在')
                d(resourceId='cn.com.weilaihui3:id/cancle_button').click()
                sleep(2)
            else:
                print('取消按钮不存在，请检查')
            sleep(2)
            #昵称
            nick=d(resourceId='cn.com.weilaihui3:id/login_update_user_message_nickname_edit')
            nick.click()
            sleep(1)
            d.set_fastinput_ime(True)
            sleep(1)
            d.press('back')
            sleep(1)
            #focused=true;
            c1=nick.info['focused']
            if c1 == True:
                print('昵称可以被编辑')
            else:
                print('昵称不可以被编辑，请检查原因')
            sleep(2)
            #简介
            intro=d(resourceId='cn.com.weilaihui3:id/login_update_update_intro')
            intro.click()
            sleep(1)
            d.set_fastinput_ime(True)
            sleep(1)
            d.press('back')
            sleep(1)
            c2=intro.info['focused']
            if c2 == True:
                print('简介可以被编辑')
            else:
                print('简介不可以被编辑，请检查原因')
            sleep(1)
            #clear昵称
            d(resourceId='cn.com.weilaihui3:id/login_update_user_message_delete_button').click()
            sleep(1)
            nick=d(resourceId='cn.com.weilaihui3:id/login_update_user_message_nickname_edit').info['text']
            if '昵称' == nick:
                print('清除昵称功能检查通过')
            else:
                print('清除昵称功能检查失败，请检查原因')
            sleep(2)
            #clear简介
            d(resourceId='cn.com.weilaihui3:id/login_update_remark_delete_button').click()
            sleep(1)
            intro=d(resourceId='cn.com.weilaihui3:id/login_update_update_intro').info['text']
            if '暂无个人简介' == intro:
                print('清除简介功能检查通过')
            else:
                print('清除简介功能检查失败，请检查原因')
            sleep(2)
            d.press('back')
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/common_alert_dialog_right_text').click()
            sleep(1)
            #编辑个人信息
            d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').click()
            sleep(2)
            #性别
            man=d(resourceId='cn.com.weilaihui3:id/login_update_user_info_gender_male_rb')
            woman=d(resourceId='cn.com.weilaihui3:id/login_update_user_info_gender_female_rb')
            #checked=true
            c_man=man.info['checked']
            c_woman=woman.info['checked']
            if c_man == True:
                woman.click()
                sleep(1)
                c_woman=woman.info['checked']
                if c_woman == True:
                    print('用户性别可以从男改变成女')
                else:
                    print('用户性别无法从男改变成女')
            else:
                man.click()
                sleep(1)
                c_man=man.info['checked']
                if c_man == True:
                    print('用户性别可以从女改变成男')
                else:
                    print('用户性别无法从女改变成男')
            sleep(2)
            #地区
            d(resourceId='cn.com.weilaihui3:id/login_update_update_region').click()
            sleep(3)
            ct=d(text='天津市')
            if ct.exists:
                print('常驻地区页面可以进入')
            else:
                print('常驻地区页面不可以进入，请检查原因')
            sleep(2)
            d.press('back')
            sleep(2)    
            #我的地址
            d(resourceId='cn.com.weilaihui3:id/login_update_user_message_address_layout').click()
            sleep(3)
            addr=d(text='设为默认地址')
            if addr.exists:
                print('地址管理页面可以进入')
            else:
                print('地址管理页面没有默认地址，请添加收货地址')
            sleep(2)
            d.press('back')
            sleep(2)
            #用户隐私条款
            d(resourceId='cn.com.weilaihui3:id/login_update_privacy_text').click()
            sleep(5)
            #ttt=d.xpath('//android.view.View[contains(@text,"上海蔚来汽车有限公司及其关联企业")]')
            ttt=d(text='隐私条款')
            if ttt.exists:
                print('用户隐私条款页面可以进入')
                d.press('back')
                sleep(2)
            else:
                print('用户隐私条款页面不可以进入，请检查原因')
                sleep(2)
            d.toast.reset()
            #保存
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_text').click()
            sleep(3)
            #print('toast='+d.toast.get_message(1.0,5.0))
            if '保存成功' in d.toast.get_message(1.0,5.0):
                print('----修改的个人信息可以保存成功')
            else:
                print('----修改的个人信息没有保存成功，请检查')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf='../../test_report/android/'+now+'_errorSaveInfo_R.png'
                d.screenshot(sf)
            sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——个人信息页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_wode_scores_tc016
#Purpose:我的积分明细页面上元素UI检查和相关元素的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_wode_scores_tc016(self):
        print('TC_检查手机号码登录APP，检查点:积分明细页面上元素UI检查和相关元素的功能检查----step1进入积分明细页面；')
        print('step2页面上元素UI检查;step3检查点击积分规则按钮的功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        d(resourceId='cn.com.weilaihui3:id/my_head_info_user_integral_layout').click()
        sleep(3)
        #检查积分明细页面的各个元素是否存在
        c1=fun_scoredetailui_check(self)
        sleep(2)
        if c1 == True:
            print('积分明细页面上各个被检查元素已检查完毕')
            sleep(1)
            #点击？号
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(3)
            #拍照
            t=d(text='积分规则')
            if t.exists:
                print('积分规则页面存在')
            else:
                print('积分规则页面不存在，请检查')
            sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——积分明细页面上元素UI检查和相关元素的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_products_tc013
#Purpose:惊喜页面上元素UI检查和相关元素的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_jingxi_products_tc013(self):
        print('TC_检查手机号码登录APP，检查点:惊喜页面上元素UI检查----step1惊喜页面上任意礼品的元素UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----开始:'+now)
        sleep(4)
        #惊喜
        d.xpath('//*[@text="惊喜"]').click()
        sleep(6)
        #惊喜页面的各个元素是否存在
        c1=fun_giftui_check(self)
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜——惊喜页面上元素UI检查----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_remarkfriend_tc018
#Purpose:朋友页面对好友设置备注并检查备注是否生效
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_pengyou_remarkfriend_tc018(self):
        print('TC_检查手机号码登录APP，检查点:对好友设置备注并检查备注是否生效----step1从朋友页面进入朋友列表页面')
        print('step2选择一个朋友进入朋友详细信息页面；step3检查点击设置备注按钮的功能;step4检查备注是否生效')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----开始:'+now)
        sleep(4)
        #朋友
        d.xpath('//*[@text="朋友"]').click()
        sleep(6)
        d(resourceId='cn.com.weilaihui3:id/friend_button').click()
        sleep(2)
        f=d(resourceId='cn.com.weilaihui3:id/tv_name')
        if f.exists:
            old=d(resourceId='cn.com.weilaihui3:id/tv_name')[0].info['text']
            d(resourceId='cn.com.weilaihui3:id/tv_name')[0].click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            combtn=d(text='设置备注')
            sleep(1)
            if combtn.exists:
                d(text='设置备注').click()
                sleep(1)
                edit=d(resourceId='cn.com.weilaihui3:id/user_remark_edit_view')
                edit.click()
                sleep(1)
                d.set_fastinput_ime(True)
                sleep(1)
                d.press('back')
                sleep(1)
                edit.clear()
                edit.send_keys(old+'的备注')
                sleep(1)
                d(text='保存').click()
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
                sleep(2)
                new=d(resourceId='cn.com.weilaihui3:id/tv_name')[0].info['text']
                if old+'的备注' in new:
                    print('好友的备注设置已经生效')
                else:
                    print('好友的备注设置没有生效，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorRemark_R.png'
                    d.screenshot(sf1)
                sleep(2)
            else:
                print('设置备注的按钮不存在，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/android/'+now+'_errorNoRemark_R.png'
                d.screenshot(sf2)
            sleep(2)
        else:
            print('没有好友可以设置备注，请先添加好友')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/android/'+now+'_errorNoFriend_R.png'
            d.screenshot(sf3)
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友——对好友设置备注并检查备注是否生效的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_article_tc019
#Purpose:发现页面推荐tab里文章元素UI检查和相关元素的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/14]
#*******************************************************
    def test_faxian_article_tc019(self):
        print('TC_检查手机号码登录APP，检查点:发现页面推荐tab里文章元素UI检查和评论的功能检查----step1从发现页面推荐tab页找到一个文章')
        print('step2文章详情页面上元素UI检查;step3检查点击评论按钮的功能;step4检查发表评论成功后文章详情顶部的评论内容')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----开始:'+now)
        sleep(5)
        #发现
        #d.xpath('//*[@text="发现"]').click()
        #sleep(2)
        d.swipe(50,1700,50,300,1.0)
        sleep(2)
        d.swipe(50,1700,50,300,1.0)
        sleep(2)
        #检查文章的各个元素是否存在
        c1=fun_articleui_check(self)
        sleep(2)
        if c1 == True:
            print('推荐tab里文章各个被检查元素都正常显示.')
            sleep(1)
            #点击评论
            cbtn=d(resourceId='cn.com.weilaihui3:id/ugc_list_bottom_comment_text')
            if cbtn.exists:
                d(resourceId='cn.com.weilaihui3:id/ugc_list_bottom_comment_text').click()
                sleep(2)
                d.swipe(50,1200,50,1500,1.0)
                sleep(2)
                c2=fun_articledetailui_check(self)
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/post_detail_txt_write_comment').click()
                sleep(2)
                combtn=d(resourceId='cn.com.weilaihui3:id/common_reply_edit_text')
                combtn.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                combtn.send_keys('I like this article：'+now0)
                sleep(1)
                d.press('back')
                sleep(1)
                d(text='发送').click()
                sleep(3)
                #check published text here
                title=d(resourceId='cn.com.weilaihui3:id/post_detail_comment_content').info['text']
                #print(title.info['text'])
                if 'I like this article：'+now0 in title:
                    print('评论的文字检查通过')
                else:
                    print('评论的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorComment_R_tc019.png'
                    d.screenshot(sf1)
                sleep(2)
            else:
                print('评论按钮没找到，请重新翻页查找')
                sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——推荐tab里文章元素UI检查和评论的功能检查----结束:'+now)

#*******************************************************
#TC Name:test_faxian_openmultichat_tc020
#Purpose:发现页面发起群聊功能的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_faxian_openmultichat_tc020(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查发现首页右上角+号是否存在；')
        print('step2检查点击+号后发起群聊按钮是否存在；step3发起群聊并发送内容功能是否正常；step4检查发布内容里文字是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----开始:'+now)
        sleep(4)
        #发现
        #d(text='发现').click()
        #sleep(2)
        #+
        c1=bp_is_plusexist(self)
        if c1 == True:
            d(resourceId='cn.com.weilaihui3:id/main_page_more').click()
            sleep(2)
            #发起群聊
            c2=bp_is_openmultichatexist(self)
            if c2 == True:
                d(text='发起群聊').click()
                sleep(3)
                cb=d(resourceId='cn.com.weilaihui3:id/cb')
                #print(len(cb))
                for i in range(cb.count):
                    d(className='android.widget.CheckBox')[i].click()
                    sleep(1)
                d(text='确定').click()
                sleep(3)
                msg=d(resourceId='cn.com.weilaihui3:id/rc_edit_text')
                msg.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                msg.send_keys('人生苦短群聊:'+now0)
                sleep(1)
                d.press('back')
                sleep(1)
                #发送
                d(text='发送').click()
                sleep(1)
                d(resourceId='cn.com.weilaihui3:id/toolbar_back_icon').click()
                sleep(1)
                #朋友
                d(text='朋友').click()
                sleep(2)
                #检查群聊的发送内容是否正确
                t=d(resourceId='cn.com.weilaihui3:id/rc_conversation_content')[0].info['text']
                #print(t.info['text'])
                if '人生苦短群聊:'+now0 in t:
                    print('群聊的发送内容正确')
                else:
                    print('群聊的发送内容不正确，请检查')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorMultiChatText_R.png'
                    d.screenshot(sf2)
                sleep(2)
                d.press('back')
                sleep(2)
                d.press('back')
                sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('发现_发起群聊功能----结束:'+now)

#*******************************************************************
#TC Name:test_pengyou_dismissmultichat_tc021
#Purpose:朋友页面群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************************
    def test_pengyou_dismissmultichat_tc021(self):
        print('TC_检查手机号码登录APP，检查点:朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊功能')
        print('step1进入已发起的群聊，检查踢人出群聊的功能是否正常;step2检查邀请朋友加入群聊的功能是否正常')
        print('step3检查解散并退出群聊的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群聊----开始:'+now)
        sleep(4)
        #朋友
        #d(text='朋友').click()
        d.xpath('//android.widget.TextView[@text="朋友"]').click()
        sleep(6)
        #群聊
        mul=d.xpath('//android.widget.TextView[contains(@text,"群聊")]')
        if mul.exists:
            d.xpath('//android.widget.TextView[contains(@text,"群聊")]').click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/toolbar_opt_icon').click()
            sleep(2)
            #-
            n=d(resourceId='cn.com.weilaihui3:id/iv_avatar')
            minus=len(n)-1
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/iv_avatar')[minus].click()
            sleep(2)
            name1=d(resourceId='cn.com.weilaihui3:id/tv_name')[0].info['text']
            d(className='android.widget.CheckBox')[0].click()
            sleep(1)
            d(text='确定').click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
            sleep(2)
            #检查是否已被移出群组
            n_msg=d(resourceId='cn.com.weilaihui3:id/rc_msg')
            t1=d(resourceId='cn.com.weilaihui3:id/rc_msg')[(n_msg.count)-1]
            #print(t1.info['text'])
            #print(name1)
            #'你将'+name1+'移出群组'
            if '移出群组' in t1.info['text']:
                print('踢人出群聊的功能检查通过')
            else:
                print('踢人出群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorKickoff_R.png'
                d.screenshot(sf1)
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/toolbar_opt_icon').click()
            sleep(2)
            #+
            n=d(resourceId='cn.com.weilaihui3:id/iv_avatar')
            plus=len(n)-2
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/iv_avatar')[plus].click()
            sleep(2)
            name2=d(resourceId='cn.com.weilaihui3:id/tv_name')[0].info['text']
            d(className='android.widget.CheckBox')[0].click()
            sleep(1)
            d(text='确定').click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
            sleep(2)
            #检查是否已被邀请加入群组
            n_msg=d(resourceId='cn.com.weilaihui3:id/rc_msg')
            t2=d(resourceId='cn.com.weilaihui3:id/rc_msg')[len(n_msg)-1]
            sleep(1)
            #print(t2.info['text'])
            #print(name2)
            #'你邀请'+name2+'加入群组'
            if '加入群组' in t2.info['text']:
                print('邀请朋友加入群聊的功能检查通过')
            else:
                print('邀请朋友加入群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/android/'+now+'_errorJoin_R.png'
                d.screenshot(sf2)
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/toolbar_opt_icon').click()
            sleep(2)
            #解散并退出
            d(text='解散并退出').click()
            sleep(1)
            d(text='确定').click()
            sleep(2)
            #检查解散的群聊是否还存在
            title1=d(resourceId='cn.com.weilaihui3:id/rc_conversation_title')[0].info['text']
            if '群聊' not in title1:
                print('解散并退出群聊的功能检查通过')
            else:
                print('解散并退出群聊的功能检查没有通过，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf3='../../test_report/android/'+now+'_errorDismissMultiChat_R.png'
                d.screenshot(sf3)
            sleep(2)
        else:
            print('没有群聊可以操作，请先发起群聊')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf4='../../test_report/android/'+now+'_errorNoMultiChat_R.png'
            d.screenshot(sf4)
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('朋友_群聊发起人踢人出群聊、邀请朋友加入群聊和解散并退出群----结束:'+now)

#*******************************************************
#TC Name:test_jingxi_add2basket_tc022
#Purpose:检查惊喜页面用户添加商品到购物车的功能测试
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_jingxi_add2basket_tc022(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_惊喜页面用户添加商品到购物车的功能----step1进入惊喜页面')
        print('step2翻页找到所需兑换的商品；step3把商品加入购物车；step4点击购物车图标进入购物车页面')
        print('step5购物车页面UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(4)
        #此刻
        d.xpath('//*[@text="惊喜"]').click()
        sleep(6)
        for i in range(3):
            d.swipe(50,1800,50,300,1.0)
            sleep(2)
        sleep(1)
        u=d.xpath('//*[@text="ES8创始版1:18车模"]')
        if u.exists:
            print('需要兑换的商品存在，检查通过')
            sleep(2)
            d.xpath('//android.widget.TextView[@text="ES8创始版1:18车模"]').click()
            sleep(9)
            page=d.info
            sleep(2)
            #加入购物车
            add2b=d(text='加入购物车')
            sleep(2)
            if add2b.exists:
                print('加入购物车按钮存在，检查通过')
                sleep(2)
                add2b[0].click()
                sleep(2)
                #点击购物车图标
                d.xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[2]').click()
                sleep(13)
                #检查购物车页面ui
                chk=fun_cartui_check(self)
                if chk == True:
                    print('购物车页面UI检查成功')
                else:
                    print('购物车页面UI检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorCartUI_R_tc022.png'
                    d.screenshot(sf1)
                sleep(2)
                d.press('back')
                sleep(2)
            else:
                print('加入购物车按钮不存在/未找到，请检查原因')
                sleep(2)
            d.press('back')
            sleep(2)
        else:
            print('需要兑换的商品不存在，请重新挑选')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----结束:'+now)

#*********************************************************************************************
#TC Name:test_jingxi_basket2exchange_tc023
#Purpose:检查惊喜页面从购物车下单兑换商品的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*********************************************************************************************
    def test_jingxi_basket2exchange_tc023(self):
        print('TC_检查手机号码登录APP，检查点:惊喜_用户从购物车下单兑换商品的功能----step1进入惊喜页面')
        print('step2点击购物车图标进入购物车页面；step3点击编辑按钮进入编辑页面；step4改变所选商品的规格：颜色')
        print('step5改变所选商品的数量;step6改变收货地址;step7立即下单检查订单是否已提交')
        print('step8查看订单检查商品状态是否为未发货')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_惊喜页面用户添加商品到购物车的功能----开始:'+now)
        sleep(4)
        #此刻
        d.xpath('//*[@text="惊喜"]').click()
        sleep(9)
        #点击购物车图标
        d.xpath('//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        sleep(6)
        #refresh5
        d.swipe(50,700,50,1300,1.0)
        sleep(2)
        chk0=d.xpath('//*[contains(@text,"去添加点什么吧")]')
        sleep(2)
        if chk0.exists:
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
                d.xpath('//*[@text="编辑"]').click()
                sleep(6)
                try:
                    #改变商品规格：颜色已选择: 天蓝
                    d.xpath('//android.widget.TextView[@text="已选择: 天蓝"]').click()
                    sleep(3)
                    d.xpath('//android.widget.TextView[@text="云白"]').click()
                    #driver.find_element_by_android_uiautomator('new UiSelector().info['text']("云白")').click()
                    sleep(1)
                    #改变商品数量
                    d.xpath('//android.widget.TextView[@text="＋"]').click()
                    sleep(3)
                    d.xpath('//android.widget.TextView[@text="确定"]').click()
                    sleep(3)
                    d.xpath('//*[@text="完成"]').click()
                    sleep(2)
                    d.xpath('//*[@text="立即购买"]').click()
                    sleep(3)
                    #改变收货地址android.view.ViewGroup[1]/
                    d.xpath('//android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
                    sleep(2)
                    #第二个地址android.view.ViewGroup[1]/
                    d.xpath('//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
                    sleep(2)
                    d.xpath('//*[@text="立即下单"]').click()
                    sleep(1)
                    d(resourceId='android:id/button1').click()
                    sleep(3)
                    chk=d.xpath('//*[@text="订单已提交"]')
                    sleep(1)
                    if chk.exists:
                        print('订单已提交检查失败，请检查原因')
                        sleep(1)
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/android/'+now+'_errorGiftOrder_R.png'
                        d.screenshot(sf1)
                        sleep(2)
                    else:
                        print('订单已提交检查通过')
                        sleep(2)
                        #查看订单
                        d(text='查看订单').click()
                        sleep(6)
                        #检查商品状态
                        chk1=d.xpath('//*[@text="ES8创始版1:18车模"]')
                        chk2=d.xpath('//*[@text="待发货"]')
                        sleep(1)
                        if chk1.exists and chk2.exists:
                            print('订单里商品状态检查通过')
                        else:
                            print('订单里商品状态检查失败，请检查原因')
                            now=time.strftime('%Y-%m-%d %H_%M_%S')
                            sf1='../../test_report/android/'+now+'_errorGiftStatus_R.png'
                            d.screenshot(sf1)
                        sleep(2)
                except Exception as e:
                    print('发生异常：'+str(e))
                    sleep(2)
            else:
                print('购物车页面UI检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorCartUI_R.png'
                d.screenshot(sf1)
                sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_惊喜_用户从购物车下单兑换商品的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_checkin_tc025
#Purpose:我的页面点击签到的功能检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/20]
#*******************************************************
    def test_wode_checkin_tc025(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1检查我的页面右上角点击签到是否存在；')
        print('step2检查点击签到功能是否正常；step3到积分明细页面检查当日签到的积分是否已经获得')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        #点击签到
        chk=d(resourceId='cn.com.weilaihui3:id/my_head_info_user_check_tip')
        cli=chk.info['clickable']
        if cli == True:
            d(resourceId='cn.com.weilaihui3:id/my_head_info_user_check_tip').click()
            sleep(2)
        else:
            print('今日已经签到过，请明日再来')
        sleep(2)
        #检查积分
        d(resourceId='cn.com.weilaihui3:id/my_head_top_user_integral_tip').click()
        sleep(2)
        cb=d(text='每日签到')
        #print(len(cb))
        tm=d(resourceId='cn.com.weilaihui3:id/integral_detail_item_time').info['text']
        nowtm=time.strftime('%Y.%m.%d')
        if cb.exists and (nowtm in tm):
            print('每日签到获取积分功能检查通过')
        else:
            print('每日签到获取积分功能检查失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorCheckinScore_R.png'
            d.screenshot(sf2)
        sleep(1)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_点击签到及检查当日签到积分是否能正常获得的功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_nicknameheadicon_tc028
#Purpose:朋友页面修改群聊昵称和头像功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/21]
#*******************************************************
    def test_pengyou_nicknameheadicon_tc028(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_修改群聊昵称和头像功能---step1检查朋友页面群聊是否存在；')
        print('step2进入群聊修改群组名称；step3检查群组名称是否修改成功；step4检查修改群组头像功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----开始:'+now)
        sleep(4)
        #朋友
        d.xpath('//*[@text="朋友"]').click()
        sleep(6)
        t=d(resourceId='cn.com.weilaihui3:id/rc_conversation_title')[0].info['text']
        sleep(1)
        if '群聊' in t:
            d(resourceId='cn.com.weilaihui3:id/rc_conversation_title')[0].click()
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/toolbar_opt_icon').click()
            sleep(2)
            #修改群组名称
            d(resourceId='cn.com.weilaihui3:id/group_name').click()
            sleep(1)
            edit=d(resourceId='cn.com.weilaihui3:id/view_edit_text_et')
            edit.click()
            sleep(1)
            edit.clear()
            sleep(1)
            edit.send_keys('群聊new')
            sleep(1)
            d.press('back')
            sleep(1)
            d.xpath('//android.widget.TextView[@text="确定"]').click()
            sleep(3)
            nk=d(resourceId='cn.com.weilaihui3:id/group_name').info['text']
            if '群聊new' == nk:
                print('群组的名称已经修改成功')
            else:
                print('群组的名称没有修改成功，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorName_R.png'
                d.screenshot(sf1)
            sleep(2)
            #修改头像
            d(resourceId='cn.com.weilaihui3:id/group_header').click()
            sleep(1)
            #拍照
            d(resourceId='cn.com.weilaihui3:id/choose_up_button').click()
            sleep(2)
            #允许
            allow=d(text='允许')
            if allow.exists:
                d(text='允许').click()
                sleep(1)
            #允许
            allow2=d(text='允许')
            if allow2.exists:
                d(text='允许').click()
                sleep(1)
            #前后置切换
            face=d.xpath('//*[@content-desc="打开美颜面板"]')
            if face.exists:
                d(resourceId='com.android.camera:id/v9_camera_picker').click()
                sleep(2)
            d(resourceId='com.android.camera:id/v9_shutter_button_internal').click()
            sleep(3)
            #d.xpath('//android.widget.ImageView[@content-desc="Done"]').click()
            d(resourceId='com.android.camera:id/inten_done_apply').click()
            sleep(15)
            #修改头像
            d(resourceId='cn.com.weilaihui3:id/group_header').click()
            sleep(1)
            #从手机相册选择
            d(resourceId='cn.com.weilaihui3:id/choose_bellow_button').click()
            sleep(2)
            d.xpath('//*[@text="相册"]').click()
            sleep(2)
            d.xpath('//*[@text="Pictures"]').click()
            sleep(2)
            d(resourceId='com.miui.gallery:id/pick_num_indicator')[1].click()
            sleep(15)
            d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/toolbar_back_icon').click()
            sleep(1)
        else:
            print('没有群聊可以操作，请先发起群聊')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/android/'+now+'_errorNoMultichat_R.png'
            d.screenshot(sf3)
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_修改群聊名称和头像功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_searchwatch_tc029
#Purpose:朋友页面搜索好友并打开个人主页进行关注
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/21]
#*******************************************************
    def test_pengyou_searchwatch_tc029(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号朋友页面_朋友页面搜索好友并打开个人主页进行关注---')
        print('step1朋友页面点+号，检查添加朋友按钮是否存在；step2输入好友名称进行搜索；')
        print('step3点击搜索出的朋友打开他的个人主页；step4检查关注功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----开始:'+now)
        sleep(4)
        #朋友
        d.xpath('//*[@text="朋友"]').click()
        sleep(6)
        d(resourceId='cn.com.weilaihui3:id/friend_button').click()
        sleep(2)
        #点+号
        d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
        sleep(1)
        add=d.xpath('//android.widget.TextView[@text="添加朋友"]')
        if add.exists:
            d.xpath('//android.widget.TextView[@text="添加朋友"]').click()
            sleep(2)
            edit=d(resourceId='cn.com.weilaihui3:id/user_search_friend_condition_edit')
            edit.click()
            sleep(1)
            edit.send_keys('张三')
            sleep(1)
            #手动点search
            #driver.tap([(1000,1932)],500)
            d.set_fastinput_ime(False)
            d.send_action('search')
            sleep(2)
            ff=d(resourceId='cn.com.weilaihui3:id/user_friend_name')
            if ff.exists:
                print('搜索好友功能检查通过')
                sleep(1)
                d(resourceId='cn.com.weilaihui3:id/user_friend_name')[1].click()
                sleep(4)
                #关注
                t=d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').info['text']
                if '关注' == t:
                    d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').click()
                    sleep(2)
                    t=d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').info['text']
                    if '已关注' in t:
                        print('好友已经关注成功')
                    else:
                        print('好友没有关注成功，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/android/'+now+'_errorWatch_R.png'
                        d.screenshot(sf1)
                    sleep(2)
                    d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
                    sleep(2)
                    d.press('back')
                    sleep(2)
                    d(resourceId='cn.com.weilaihui3:id/navigation_back_icon').click()
                    sleep(2)
                else:
                    print('该好友你以前已经关注过了，无需再操作')
                    sleep(1)
                    d.press('back')
                    sleep(2)
                    d.press('back')
                    sleep(2)
            else:
                print('搜索好友功能检查失败，请检查原因')
                sleep(1)
                d.press('back')
                sleep(2)
                d.press('back')
                sleep(2)
        else:
            print('没有添加朋友按钮，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf3='../../test_report/android/'+now+'_errorNoAddFriend_R.png'
            d.screenshot(sf3)
            sleep(2)
            d.press('back')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_搜索好友并打开个人主页进行关注----结束:'+now)

#*******************************************************
#TC Name:test_wode_instuninstversioncheck_tc015
#Purpose:安装和卸载app及版本检测功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/21]
#*******************************************************
    def test_wode_instuninstversioncheck_tc015(self):
        print('TC_检查手机号码登录APP，检查点:兼容性测试：安装和卸载app功能----step1卸载app')
        print('step2检查app是否存在；step3安装app；step4检查app是不是最新版本')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app及版本检测功能----开始:'+now)
        sleep(4)
        #home
        driver.press_keycode('3')
        sleep(2)
        #卸载app
        driver.remove_app('cn.com.weilaihui3')
        sleep(3)
        #check if app is uninstalled
        c=driver.is_app_installed('cn.com.weilaihui3')
        sleep(1)
        if c == True:
            print('卸载蔚来app失败，请检查原因')
        else:
            print('卸载蔚来app成功')
            sleep(2)
            #install app
            d=os.path.abspath(os.path.join(os.getcwd(), '../..'))
            #print(d)
            driver.install_app(d+'/test_data/app/android_package/weilai_test.apk')
            sleep(1)
            #继续安装
            inst=d.xpath('//*[@text="继续安装"]')
            if inst.exists:
                d.xpath('//*[@text="继续安装"]').click()
                sleep(5)
            sleep(3)
            driver.launch_app()
            #允许
            sleep(6)
            allow=d.xpath('//*[@text="允许"]')
            if allow.exists:
                d.xpath('//*[@text="允许"]').click()
                sleep(2)
            #我的
            d.xpath('//*[@text="我的"]').click()
            sleep(4)
            #设置
            d(resourceId='cn.com.weilaihui3:id/my_palace_setting_layout').click()
            sleep(2)
            d.xpath('//android.widget.TextView[@text="检测更新"]').click()
            sleep(1)
            n1=d.xpath('//*[contains(@text,"已是最新版本")]')
            #n2=d.xpath('//*[@text="蔚来：已是最新版本"]')
            if n1.exists:
                print('app版本检测功能检查通过')
            else:
                print('app版本检测功能检查失败，请检查原因')
            sleep(1)
            d.press('back')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_兼容性测试：安装和卸载app及版本检测功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_resetsecupwd_tc030
#Purpose:我的页面设置里重置服务安全密码的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/22]
#*******************************************************
    def test_wode_resetsecupwd_tc030(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点设置；')
        print('step2点击服务安全密码；step3检查重置服务安全密码的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----开始:'+now)
        sleep(4)
        #我的
        d.xpath('//*[@text="我的"]').click()
        sleep(4)
        d.swipe(50,1000,50,300,1.0)
        sleep(2)
        #设置      
        d(resourceId='cn.com.weilaihui3:id/my_palace_setting_layout').click()
        sleep(2)
        #服务安全密码
        d(resourceId='cn.com.weilaihui3:id/layout_pin').click()
        sleep(4)
        code=d(resourceId='cn.com.weilaihui3:id/inputVcodeEdt')
        code.click()
        sleep(0.5)
        code.send_keys('112233')
        sleep(1)
        d.press('back')
        sleep(1)
        #下一步
        d(resourceId='cn.com.weilaihui3:id/nextStepBtn').click()
        sleep(1)
        #证件类型
        d(resourceId='cn.com.weilaihui3:id/inputIdCodeType').click()
        sleep(1)
        d.xpath('//android.widget.TextView[@text="身份证"]').click()
        sleep(1)
        idnum=d(resourceId='cn.com.weilaihui3:id/inputIdCodeEdt')
        idnum.click()
        idnum.send_keys('340103197301142518')
        sleep(1)
        d.press('back')
        sleep(1)
        #下一步
        d(resourceId='cn.com.weilaihui3:id/nextStepBtn').click()
        sleep(2)
        p=[]
        p_real=[]
        for i in range(6):
            r=random.randint(7,16)
            p.append(str(r))
            p_real.append(str(r-7))
        print('重置的密码是：'+str(p_real))
        sleep(1)
        for j in range(6):
            d.press(eval(p[j]))
        sleep(1)
        for j in range(6):
            d.press(eval(p[j]))
        d.toast.reset()
        sleep(3)
        #检查toast
        print('toast='+str(d.toast.get_message(2.0,5.0)))
        if '重置成功请重新输入' in d.toast.get_message(2.0,5.0):
            print('服务安全密码重置成功')
        else:
            print('服务安全密码重置失败，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorResetSecupwd_R.png'
            d.screenshot(sf2)
        sleep(1)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('我的_设置里重置服务安全密码的功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_addeditaddress_tc031
#Purpose:我的页面里地址管理页面新增和编辑一个收货地址的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/22]
#*******************************************************
    def test_wode_addeditaddress_tc031(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现首页_发起群聊功能---step1我的页面里点击头像')
        print('step2点击编辑个人信息；step3点击我的地址进入地址管理页面;step4检查添加新地址的功能是否正常')
        print('step5检查编辑地址的功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----开始:'+now)
        sleep(4)
        #我的
        d.xpath('//*[@text="我的"]').click()
        sleep(4)
        d(resourceId='cn.com.weilaihui3:id/my_head_info_user_name').click()
        sleep(2)
        #编辑个人信息
        d.xpath('//*[@text="编辑个人信息"]').click()
        sleep(2)
        #我的地址
        d(resourceId='cn.com.weilaihui3:id/login_update_user_message_address_layout').click()
        sleep(2)
        #添加新地址
        add=d.xpath('//android.widget.Button[@text="添加新地址"]')
        if add.exists:
            print('添加新地址按钮存在,检查通过')
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/multi_address_new_address').click()
            sleep(1)
            name=d(resourceId='cn.com.weilaihui3:id/address_item_edit__recipients_content')
            name.click()
            sleep(0.5)
            r=random.randint(10,99)
            sleep(1)
            name.send_keys('测试'+str(r))
            sleep(1)
            d.press('back')
            sleep(1)
            pnum=d(resourceId='cn.com.weilaihui3:id/address_item_edit_phone_num')
            pnum.click()
            sleep(1)
            r2=random.randint(10,99)
            sleep(1)
            pnum.send_keys('138160328'+str(r2))
            sleep(1)
            d.press('back')
            sleep(1)
            #选择所在地区
            d(resourceId='cn.com.weilaihui3:id/address_item_region_content_edit').click()
            sleep(2)
            #确定
            d(resourceId='cn.com.weilaihui3:id/btnSubmit').click()
            sleep(1)
            #街道/楼牌号等
            addr=d(resourceId='cn.com.weilaihui3:id/address_item_edit_details')
            addr.click()
            sleep(1)
            r3=random.randint(100,999)
            sleep(1)
            addr.send_keys('中山北路'+str(r3)+'号')
            sleep(1)
            d.press('back')
            sleep(1)
            d.toast.reset()
            #保存
            d(resourceId='cn.com.weilaihui3:id/address_toolbar_right').click()
            sleep(1)
            #检查toast
            print('toast='+d.toast.get_message(1.0,5.0))
            if '更新地址成功' in d.toast.get_message(1.0,5.0):
                print('新增地址成功')
            else:
                print('新增地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/android/'+now+'_errorAddnewaddr_R.png'
                d.screenshot(sf2)
            sleep(2)
        else:
            print('添加新地址按钮不存在，请检查原因')
        sleep(2)
        #编辑
        edi=d.xpath('//android.widget.TextView[@text="编辑"]')
        if len(edi) != 0:
            print('编辑按钮存在,检查通过')
            sleep(1)
            d.xpath('//android.widget.TextView[@text="编辑"]').click()
            sleep(1)
            name=d(resourceId='cn.com.weilaihui3:id/address_item_edit__recipients_content')
            name.click()
            sleep(1)
            old=name.info['text']
            r4=random.randint(10,99)
            sleep(1)
            name.send_keys(old+str(r4))
            sleep(1)
            d.press('back')
            sleep(1)
            d.toast.reset()
            #保存
            d(resourceId='cn.com.weilaihui3:id/address_toolbar_right').click()
            sleep(1)
            #检查toast
            print('toast='+d.toast.get_message(1.0,5.0))
            if '更新地址成功' in d.toast.get_message(1.0,5.0):
                print('编辑地址成功')
            else:
                print('编辑地址失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorEditaddr_R.png'
                d.screenshot(sf1)
            sleep(2)
        else:
            print('编辑按钮不存在，请检查原因')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_新增和编辑一个收货地址的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershowpic_tc032
#Purpose:发现页面体验tab活动的晒图功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/23]
#*******************************************************
    def test_faxian_expershowpic_tc032(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的晒图功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查晒图功能是否正常;step4检查晒图的文字是否正确')
        print('step5检查晒图的9张图片数量是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----开始:'+now)
        sleep(4)
        #体验
        d.xpath('//*[@text="体验"]').click()
        sleep(5)
        d(resourceId='cn.com.weilaihui3:id/loi_cur_store_tip').click()
        sleep(2)
        d.swipe(50,1500,50,300,1.0)
        sleep(2)
        d.xpath('//android.widget.TextView[@text="蔚来上海二号店"]').click()
        sleep(2)
        #还未开始
        d(resourceId='cn.com.weilaihui3:id/activity_list_item_title').click()
        sleep(5)
        page=d.info
        sleep(1)
        #晒图
        show=d.xpath('//android.webkit.WebView[1]/android.view.View[1]/android.view.View[12]/android.view.View[2]')
        sleep(2)
        if show.exists:
            print('晒图按钮存在,检查通过')
            sleep(1)
            show.click()
            sleep(2)
            #+
            d(resourceId='cn.com.weilaihui3:id/image').click()
            sleep(2)
            #允许
            allow=d.xpath('//*[@text="允许"]')
            if allow.exists:
                d.xpath('//*[@text="允许"]').click()
                sleep(2)
            for i in range(9):
                d(resourceId='cn.com.weilaihui3:id/media_item_cb_check')[i].click()
                sleep(1)
            d.xpath('//*[@text="确定"]').click()
            sleep(1)
            word=d(resourceId='cn.com.weilaihui3:id/community_create_evaluation_edit_view')
            word.click()
            sleep(0.5)
            now0=time.strftime('%Y-%m-%d %H_%M_%S')
            word.send_keys('人生苦短体验晒图:'+now0)
            sleep(1)
            d.press('back')
            sleep(1)
            d.xpath('//*[@text="发布"]').click()
            sleep(6)
            #check numbers of pictures and published text here
            title=d(resourceId='cn.com.weilaihui3:id/comment_list_item_content')[0].info['text']
            #print(title.info['text'])
            if '人生苦短体验晒图:'+now0 in title:
                print('体验晒图的文字检查通过')
            else:
                print('体验晒图的文字检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorShowpicText_R.png'
                d.screenshot(sf1)
            sleep(1)
            number=d(resourceId='cn.com.weilaihui3:id/comment_view_text_num').info['text']
            #print(number.info['text'])
            if '9' == number:
                print('体验晒图的上传9张图片检查通过')
            else:
                print('体验晒图的上传9张图片检查失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf2='../../test_report/android/'+now+'_errorPic9_R.png'
                d.screenshot(sf2)
            sleep(2)
            d.press('back')
            sleep(2)
        else:
            print('晒图按钮不存在，请检查原因')
        sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的晒图功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_publishnowatfriend_tc033
#Purpose:检查发现页面的发布此刻并@好友的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/24]
#*******************************************************
    def test_faxian_publishnowatfriend_tc033(self):
        print('TC_检查手机号码登录APP，检查点:发现_发布此刻并@好友的功能----step1检查发现首页右上角+号是否存在；')
        print('step2检查发布此刻按钮是否存在；step3发布并@好友功能是否正常；step4检查发布内容里是否可以一次最大上传9张图片；')
        print('step5检查发布文字是否正确;step6退出当前账号并已@的好友账号登录app;step7检查朋友页面里是否收到@通知')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----开始:'+now)
        sleep(4)
        #发现
        d.xpath('//*[@text="发现"]').click()
        sleep(4)
        c1=bp_is_plusexist(self)
        if c1 == True:
            d(resourceId='cn.com.weilaihui3:id/main_page_more').click()
            sleep(2)
            #发布此刻
            c2=bp_is_publishnowexist(self)
            if c2 == True:
                print('发布此刻按钮存在，检查通过')
                sleep(1)
                d(text='发布此刻').click()
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/image').click()
                sleep(2)
                #允许
                allow=d.xpath('//*[@text="允许"]')
                if allow.exists:
                    d.xpath('//*[@text="允许"]').click()
                    sleep(2)
                for i in range(10,19):
                    d(resourceId='cn.com.weilaihui3:id/media_item_cb_check')[i].click()
                    sleep(1)
                d(text='确定').click()
                sleep(1)
                word=d(resourceId='cn.com.weilaihui3:id/community_create_evaluation_edit_view')
                word.click()
                sleep(0.5)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('人生苦短我用Python'+now0)
                sleep(1)
                d.press('back')
                sleep(1)
                #@
                d(resourceId='cn.com.weilaihui3:id/community_input_at').click()
                sleep(1)
                d.xpath('//*[@text="Sam8202"]').click()
                sleep(1)
                d.xpath('//*[@text="发布"]').click()
                sleep(9)
                #check numbers of pictures and published text here
                title=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')[0].info['text']
                if '人生苦短我用Python'+now0 in title:
                    print('发布内容的文字检查通过')
                else:
                    print('发布内容的文字检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorText_R.png'
                    d.screenshot(sf1)
                sleep(1)
                number=d(resourceId='cn.com.weilaihui3:id/ugc_list_three_img_num').info['text']
                if '9' in number:
                    print('发布内容的上传9张图片检查通过')
                else:
                    print('发布内容的上传9张图片检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorPic9_R.png'
                    d.screenshot(sf2)
                sleep(1)
                #logout
                #我的
                d.xpath('//*[@text="我的"]').click()
                sleep(3)
                d.swipe(50,700,50,300,1.0)
                sleep(2)
                #设置
                d(resourceId='cn.com.weilaihui3:id/my_palace_setting_layout').click()
                sleep(1)
                d(text='退出登录').click()
                sleep(1)
                d(text='确定').click()
                sleep(2)
                #relogin as 'Sam8201'
                d(text='注册/登录').click()
                sleep(2)
                #登录页面
                mobile_no=d(resourceId='cn.com.weilaihui3:id/login_main_login_phone_edit')
                mobile_no.click()
                sleep(1)
                mobile_no.send_keys('98762648202')
                sleep(1)
                code=d(resourceId='cn.com.weilaihui3:id/login_main_login_code_edit')
                code.click()
                sleep(1)
                code.send_keys('112233')
                sleep(1)
                d.press('back')
                sleep(1)
                d.xpath('//android.widget.Button[@text="注册/登录"]').click()
                sleep(8)
                #朋友
                d(text='朋友').click()
                sleep(6)
                #检查好友'Sam8202'是否收到@通知
                fb=d.xpath('//*[contains(@text,"@了你")]')
                if fb.exists:
                    print('好友收到@通知检查通过')
                else:
                    print('好友收到@通知检查失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_error#friend_R.png'
                    d.screenshot(sf2)
                sleep(2)
                bp_is_loggedin(self)
                sleep(2)
                #relogin as '8293'
                bp_normalloginmp(self)
                sleep(2)
            else:
                print('发布此刻按钮不存在，请检查原因')
                sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发布此刻并@好友----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcshare_tc034
#Purpose:检查发现页面此刻tab下的ugc的分享功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/08/24]
#*******************************************************
    def test_faxian_ugcshare_tc034(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面此刻tab下的ugc的分享功能----开始:'+now)
        sleep(4)
        #此刻
        d(text='此刻').click()
        sleep(4)
        u=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')
        if u.exists:
            print('UGC存在，检查通过')
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/ugc_list_content').click()
            sleep(2)
            #...
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            #微信好友
            wh=d.xpath('//*[@text="微信好友"]')
            if wh.exists:
                print('分享到微信好友按钮存在，检查通过')
                sleep(1)
                d.xpath('//*[@text="微信好友"]').click()
                sleep(5)
                d.xpath('//android.widget.TextView[@text="王小龙"]').click()
                sleep(1)
                word=d(resourceId='com.tencent.mm:id/aps')
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('人生苦短UGC微信好友:'+now0)
                sleep(1)
                d.press('back')
                sleep(1)
                #分享
                d.xpath('//android.widget.Button[@text="分享"]').click()
                sleep(1)
                d.xpath('//android.widget.Button[@text="返回蔚来"]').click()
                d.toast.reset()
                sleep(1)
                #检查toast
                #print('toast='+d.toast.get_message(1.0,5.0))
                if '分享成功' in d.toast.get_message(1.0,5.0):
                    print('分享微信好友成功')
                else:
                    print('分享微信好友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorsharewechat_R.png'
                    d.screenshot(sf1)
                sleep(1)
            else:
                print('分享到微信好友按钮不存在，请检查原因')
            sleep(2)
            #...
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            #朋友圈
            pyq=d.xpath('//*[@text="朋友圈"]')
            if pyq.exists:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(1)
                d.xpath('//*[@text="朋友圈"]').click()
                sleep(8)
                word2=d(resourceId='com.tencent.mm:id/dp0')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.send_keys('人生苦短UGC朋友圈:'+now2)
                sleep(1)
                d.press('back')
                sleep(1)
                d.toast.reset()
                #发表
                #d.xpath('//*[@text="发表"]').click()
                d(resourceId='com.tencent.mm:id/iv').click()
                sleep(1)
                #检查toast
                if '分享成功' in d.toast.get_message(1.0,5.0):
                    print('分享朋友圈成功')
                else:
                    print('分享朋友圈失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorsharewechatpyq_R.png'
                    d.screenshot(sf2)
                sleep(1)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
            sleep(2)
            #...
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            #新浪微博
            wb=d.xpath('//*[@text="新浪微博"]')
            if wb.exists:
                print('分享到新浪微博按钮存在，检查通过')
                sleep(1)
                d.xpath('//*[@text="新浪微博"]').click()
                sleep(9)
                d.toast.reset()
                #发送
                d(resourceId='com.sina.weibo:id/titleSave').click()
                sleep(1)
                #检查toast
                if '分享成功' in d.toast.get_message(1.0,5.0):
                    print('分享新浪微博成功')
                else:
                    print('分享新浪微博失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/android/'+now+'_errorsharewebo_R.png'
                    d.screenshot(sf3)
                sleep(1)
            else:
                print('分享到新浪微博按钮不存在，请检查原因')
                sleep(1)
            #...
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            #我的朋友
            mf=d.xpath('//*[@text="我的朋友"]')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(1)
                d.xpath('//*[@text="我的朋友"]').click()
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/share_top_item').click()
                sleep(2)
                d.toast.reset()
                #Sam8230
                d.xpath('//android.widget.TextView[@text="Sam8230"]').click()
                sleep(1)
                #发送
                #检查toast
                if '分享成功' in d.toast.get_message(1.0,5.0):
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/android/'+now+'_errorsharemyfriend_R.png'
                    d.screenshot(sf4)
                sleep(1)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
                sleep(1)
            d.press('back')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面此刻tab下的ugc的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_ugcdel_tc035
#Purpose:检查发现页面此刻tab下的ugc的删除功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_faxian_ugcdel_tc035(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面此刻tab下的ugc的分享功能----step1进入发现页面此刻tab')
        print('step2检查ugc是否存在；step3进入ugc页面点右上角的...按钮；step4检查删除按钮是否存在')
        print('step5检查删除ugc功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面此刻tab下的ugc的删除功能----开始:'+now)
        sleep(4)
        #此刻
        d(text='此刻').click()
        sleep(4)
        u=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')
        if u.exists:
            t0=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')[0].info['text']
            sleep(1)
            print('UGC存在，检查通过')
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/ugc_list_content').click()
            sleep(2)
            #...
            d(resourceId='cn.com.weilaihui3:id/navigation_opt_icon').click()
            sleep(2)
            #删除
            db=d(text='删除')
            if db.exists:
                print('删除按钮存在，检查通过')
                sleep(2)
                d(text='删除').click()
                sleep(1)
                #确定
                d(resourceId='cn.com.weilaihui3:id/common_alert_dialog_right_text').click()
                sleep(3)
                t1=d(resourceId='cn.com.weilaihui3:id/ugc_list_content')[0].info['text']
                if t1 != t0:
                    print('删除ugc成功')
                else:
                    print('删除ugc失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorDelUgc_R.png'
                    d.screenshot(sf1)
                sleep(2)
            else:
                print('删除按钮不存在，请检查原因')
                sleep(2)
            #print(t0)
            #print(t1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面此刻tab下的ugc的删除功能----结束:'+now)

#*******************************************************
#TC Name:test_pengyou_im_tc036
#Purpose:检查朋友页面IM聊天信息复制、删除、撤回、转发
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_pengyou_im_tc036(self):
        print('TC_检查手机号码登录APP，检查点:朋友_IM聊天信息复制、删除、撤回、转发功能----step1朋友页面找到一个朋友发起聊天')
        print('step2发送一条消息；step3检查复制消息功能；step4检查删除消息功能')
        print('step5检查转发消息功能;step6检查撤回消息功能')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----开始:'+now)
        sleep(4)
        #朋友
        d(text='朋友').click()
        sleep(5)
        d(resourceId='cn.com.weilaihui3:id/friend_button').click()
        sleep(6)
        u=d(resourceId='cn.com.weilaihui3:id/tv_name')
        if u.exists:
            d(resourceId='cn.com.weilaihui3:id/tv_name')[0].click()
            sleep(3)
            #聊天
            d(resourceId='cn.com.weilaihui3:id/user_info_submit_btn').click()
            sleep(2)
            #发送文本信息
            word=d(resourceId='cn.com.weilaihui3:id/rc_edit_text')
            word.click()
            sleep(1)
            word.send_keys('测试im')
            sleep(1)
            d.press('back')
            sleep(1)
            #发送
            d(resourceId='cn.com.weilaihui3:id/rc_send_toggle').click()
            sleep(2)
            #长按im
            d1=d.xpath('//android.widget.TextView[@text="测试im"]')
            #TouchAction(driver).long_press(d1,duration=1000).release().perform()
            d1.long_click()
            sleep(1)
            #复制消息
            cp=d.xpath('//android.widget.TextView[@text="复制消息"]')
            if cp.exists:
                print('复制消息按钮存在，检查通过')
                sleep(2)
                d.xpath('//android.widget.TextView[@text="复制消息"]').click()
                sleep(1)
                word.click()
                sleep(1)
                #TouchAction(driver).long_press(word,duration=1000).release().perform()
                word.long_click()
                #sleep(1)
                #TouchAction(driver).tap(x=115,y=1033).release().perform()
                d.click(115,1033)
                sleep(1)
                #发送
                d(resourceId='cn.com.weilaihui3:id/rc_send_toggle').click()
                sleep(1)
                #检查
                c=d.xpath('//*[@text="测试im"]')
                #print(len(c))
                if c.count != 1:
                    print('复制消息成功')
                else:
                    print('复制消息失败，请检查原因')
                sleep(2)
            else:
                print('复制消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d2=d.xpath('//android.widget.TextView[@text="测试im"]')
            #TouchAction(driver).long_press(d2,duration=1000).release().perform()
            d2.long_click()
            sleep(1)
            #删除消息
            de=d.xpath('//android.widget.TextView[@text="删除消息"]')
            if de.exists:
                print('删除消息按钮存在，检查通过')
                sleep(2)
                d.xpath('//android.widget.TextView[@text="删除消息"]').click()
                sleep(1)
                #检查
                c2=d.xpath('//*[@text="测试im"]')
                if c2.count == 1:
                    print('删除消息成功')
                else:
                    print('删除消息失败，请检查原因')
                sleep(2)
            else:
                print('删除消息按钮不存在，请检查原因')
                sleep(2)
            #长按im
            d3=d.xpath('//android.widget.TextView[@text="测试im"]')
            #TouchAction(driver).long_press(d3,duration=1000).release().perform()
            d3.long_click()
            sleep(1)
            #转发消息
            de=d.xpath('//android.widget.TextView[@text="转发消息"]')
            if de.exists:
                print('转发消息按钮存在，检查通过')
                sleep(2)
                d.xpath('//android.widget.TextView[@text="转发消息"]').click()
                sleep(1)
                fri=d(resourceId='cn.com.weilaihui3:id/share_name')
                if fri.exists:
                    #1nd friend
                    d(resourceId='cn.com.weilaihui3:id/share_name')[0].click()
                else:
                    print('没有其他朋友可以转发消息')
                    d.press('back')
                sleep(3)
            else:
                print('转发消息按钮不存在，请检查原因')
                sleep(2)
            #新发一条im
            word.click()
            sleep(1)
            word.send_keys('测试撤回im')
            sleep(1)
            d.press('back')
            sleep(1)
            #发送
            d(resourceId='cn.com.weilaihui3:id/rc_send_toggle').click()
            sleep(2)
            #长按im
            d4=d.xpath('//android.widget.TextView[@text="测试撤回im"]')
            #TouchAction(driver).long_press(d4,duration=1000).release().perform()
            d4.long_click()
            sleep(1)
            #撤回消息
            wd=d.xpath('//android.widget.TextView[@text="撤回消息"]')
            if wd.exists:
                print('撤回消息按钮存在，检查通过')
                sleep(2)
                d.xpath('//android.widget.TextView[@text="撤回消息"]').click()
                sleep(1)
                #检查
                w=d.xpath('//*[@text="你撤回了一条消息"]')
                if w.exists:
                    print('撤回消息成功')
                else:
                    print('撤回消息失败，请检查原因')
                sleep(2)
            else:
                print('撤回消息按钮不存在，请检查原因')
                sleep(2)
            d.press('back')
            sleep(2)
            d.press('back')
            sleep(2)
        else:
            print('朋友不存在，无法执行聊天相关操作')
            sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_朋友_IM聊天信息复制、删除、撤回、转发功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_infopgcshare_tc037
#Purpose:检查发现页面资讯tab下的pgc的分享功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_faxian_infopgcshare_tc037(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面资讯tab下的pgc的分享功能----step1进入发现页面资讯tab')
        print('step2PGC的UI检查；step3进入pgc文章页面点右下角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----开始:'+now)
        sleep(4)
        #此刻
        d.xpath('//*[@text="资讯"]').click()
        sleep(4)
        d.swipe(50,1700,50,300,1.0)
        sleep(2)
        #检查发现页面资讯tab下的pgc的的各个元素是否存在
        c=fun_pgcui_check(self)
        if c == True:
            print('发现页面资讯tab下的pgc的各个被检查元素都检查完毕')
            sleep(2)
        u=d(resourceId='cn.com.weilaihui3:id/content_style_title')
        if u.exists:
            print('PGC存在，检查通过')
            sleep(2)
            d(resourceId='cn.com.weilaihui3:id/content_style_title').click()
            sleep(4)
            #右下角按钮
            sh=d(resourceId='cn.com.weilaihui3:id/img_share')
            if sh.exists:
                print('分享按钮存在，检查通过')
                sleep(2)
                d(resourceId='cn.com.weilaihui3:id/img_share').click()
                sleep(2)
                #微信好友
                wh=d.xpath('//*[@text="微信好友"]')
                if wh.exists:
                    print('分享到微信好友按钮存在，检查通过')
                    sleep(2)
                    d.xpath('//*[@text="微信好友"]').click()
                    sleep(5)
                    d.xpath('//android.widget.TextView[@text="王小龙"]').click()
                    sleep(1)
                    word=d(resourceId='com.tencent.mm:id/aps')
                    word.click()
                    sleep(1)
                    now0=time.strftime('%Y-%m-%d %H_%M_%S')
                    word.send_keys('人生苦短PGC微信好友:'+now0)
                    sleep(1)
                    d.press('back')
                    sleep(1)
                    #分享
                    d.xpath('//android.widget.Button[@text="分享"]').click()
                    sleep(2)
                    d.toast.reset()
                    d.xpath('//android.widget.Button[@text="返回蔚来"]').click()
                    sleep(1)
                    #检查toast
                    if '分享成功' in d.toast.get_message(1.0,5.0):
                        print('分享微信好友成功')
                    else:
                        print('分享微信好友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf1='../../test_report/android/'+now+'_errorPGCsharewechat_R.png'
                        d.screenshot(sf1)
                    sleep(1)
                else:
                    print('分享到微信好友按钮不存在，请检查原因')
                    sleep(1)
                #share
                d(resourceId='cn.com.weilaihui3:id/img_share').click()
                sleep(2)
                #朋友圈
                pyq=d.xpath('//*[@text="朋友圈"]')
                if pyq.exists:
                    print('分享到朋友圈按钮存在，检查通过')
                    sleep(1)
                    d.xpath('//*[@text="朋友圈"]').click()
                    sleep(8)
                    word2=d(resourceId='com.tencent.mm:id/dp0')
                    word2.click()
                    sleep(1)
                    now2=time.strftime('%Y-%m-%d %H_%M_%S')
                    word2.send_keys('人生苦短PGC朋友圈:'+now2)
                    sleep(1)
                    d.press('back')
                    sleep(1)
                    d.toast.reset()
                    #发表
                    d(resourceId='com.tencent.mm:id/iv').click()
                    sleep(1)
                    #检查toast
                    if '分享成功' in d.toast.get_message(1.0,5.0):
                        print('分享朋友圈成功')
                    else:
                        print('分享朋友圈失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf2='../../test_report/android/'+now+'_errorPGCsharewechatpyq_R.png'
                        d.screenshot(sf2)
                    sleep(1)
                else:
                    print('分享到朋友圈按钮不存在，请检查原因')
                sleep(2)
                #share
                d(resourceId='cn.com.weilaihui3:id/img_share').click()
                sleep(2)
                #新浪微博
                wb=d.xpath('//*[@text="新浪微博"]')
                if wb.exists:
                    print('分享到新浪微博按钮存在，检查通过')
                    sleep(2)
                    d.xpath('//*[@text="新浪微博"]').click()
                    sleep(9)
                    d.toast.reset()
                    #发送
                    d(resourceId='com.sina.weibo:id/titleSave').click()
                    sleep(1)
                    #检查toast
                    if '分享成功' in d.toast.get_message(1.0,5.0):
                        print('分享新浪微博成功')
                    else:
                        print('分享新浪微博失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf3='../../test_report/android/'+now+'_errorPGCsharewebo_R.png'
                        d.screenshot(sf3)
                    sleep(1)
                else:
                    print('分享到新浪微博按钮不存在，请检查原因')
                sleep(2)
                #share
                d(resourceId='cn.com.weilaihui3:id/img_share').click()
                sleep(2)
                #我的朋友
                mf=d.xpath('//*[@text="我的朋友"]')
                if mf.exists:
                    print('分享到我的朋友按钮存在，检查通过')
                    sleep(1)
                    d.xpath('//*[@text="我的朋友"]').click()
                    sleep(2)
                    d(resourceId='cn.com.weilaihui3:id/share_top_item').click()
                    sleep(2)
                    d.toast.reset()
                    #Sam8263
                    d(resourceId='cn.com.weilaihui3:id/tv_name').click()
                    sleep(1)
                    #检查toast
                    if '分享成功' in d.toast.get_message(1.0,5.0):
                        print('分享我的朋友成功')
                    else:
                        print('分享我的朋友失败，请检查原因')
                        now=time.strftime('%Y-%m-%d %H_%M_%S')
                        sf4='../../test_report/android/'+now+'_errorPGCsharemyfriend_R.png'
                        d.screenshot(sf4)
                    sleep(1)
                else:
                    print('分享到我的朋友按钮不存在，请检查原因')
                    sleep(2)
                d.press('back')
                sleep(2)
            else:
                print('分享按钮不存在，请检查原因')
                sleep(2)
            d.press('back')
            sleep(2)
        else:
            print('PGC不存在，无法执行分享操作')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面资讯tab下的PGC的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_experjoin_tc038
#Purpose:发现页面体验tab活动的报名功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_faxian_experjoin_tc038(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——体验tab活动的报名功能---step1发现页面里点击体验tab')
        print('step2切换地点找到一个同城活动；step3检查报名功能是否正常;step4进入我的->我的活动页面')
        print('step5点击查看行程单;step6检查活动订单里活动的时间是否正确')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的报名功能----开始:'+now)
        sleep(4)
        #体验
        d(text='体验').click()
        sleep(6)
        d(resourceId='cn.com.weilaihui3:id/loi_cur_store_tip').click()
        sleep(2)
        for i in range(2):
            d.swipe(50,1500,50,300,1.0)
            sleep(2)
        sleep(1)
        d.xpath('//android.widget.TextView[@text="蔚来上海二号店"]').click()
        sleep(2)
        d.xpath('//*[@text="更多活动"]').click()
        sleep(2)
        d.swipe(50,2000,50,300,1.0)
        sleep(2)
        #自动化测试活动
        d.xpath('//*[@text="自动化测试活动"]').click()
        sleep(4)
        page=d.info
        sleep(2)
        #报名
        joins=d.xpath('//android.webkit.WebView[1]/android.view.View[1]/android.view.View[20]/android.view.View[2]')
        sleep(2)
        if joins.exists:
            print('报名按钮存在,检查通过')
            sleep(2)
            joins.click()
            sleep(6)
            #driver.tap([(786,1936)],200)
            #场次
            #d.xpath('//*[@text="10.24 / 00:00"]').click()
            #sleep(1)
            #d.xpath('//*[contains(@text,"车主票")]').click()
            #sleep(2)
            #+限购1张
            #d.xpath('//*[@text="+"]').click()
            #sleep(1)
            d.swipe(50,1800,50,200,1.0)
            sleep(2)
            #姓名
            name=d(className='android.widget.EditText')[0]
            name.click()
            name.send_keys('测试员')
            sleep(0.5)
            d.set_fastinput_ime(True)
            sleep(1)
            #mobile
            mb=d(className='android.widget.EditText')[1]
            mb.click()
            sleep(1)
            mb.send_keys('18930018801')
            sleep(0.5)
            d.set_fastinput_ime(True)
            sleep(1)
            d.press('back')
            sleep(2)
            #性别
            d.xpath('//android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View[1]').click()
            sleep(1)
            #完成
            d(resourceId='cn.com.weilaihui3:id/data_selector_ok').click()
            sleep(2)
            #血型
            d.xpath('//android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View[1]').click()
            sleep(1)
            #完成
            d(resourceId='cn.com.weilaihui3:id/data_selector_ok').click()
            sleep(2)
            #证件类型
            d.xpath('//android.view.View[2]/android.view.View[6]/android.view.View[2]/android.view.View[1]').click()
            sleep(1)
            #完成
            d(resourceId='cn.com.weilaihui3:id/data_selector_ok').click()
            sleep(1)
            #证件号码
            em=d(className='android.widget.EditText')[2]
            em.click()
            sleep(1)
            em.send_keys('340103197301142518')
            sleep(0.5)
            d.set_fastinput_ime(True)
            sleep(1)
            d.press('back')
            sleep(1)
            #d(className='android.widget.CheckBox').click()
            #sleep(1)
            #购买
            d.xpath('//*[@text="购买"]').click()
            sleep(1)
            #确认
            d.xpath('//*[@text="确认"]').click()
            sleep(3)
            #checking
            ch=d.xpath('//*[@text="预约成功"]')
            if (not ch.exists):
                print('报名失败，请检查原因')
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorJoin_R_tc038.png'
                d.screenshot(sf1)
                sleep(2)
            else:
                print('报名成功')
                sleep(1)
                d.xpath('//*[@text="完成"]').click()
                sleep(4)
                d.press('back')
                sleep(2)
                d.press('back')
                sleep(2)
        else:
            print('报名按钮不存在，请检查原因')
        sleep(2)
        #我的
        d(text='我的').click()
        sleep(4)
        d(resourceId='cn.com.weilaihui3:id/my_palace_appointment_tv').click()
        sleep(2)
        ch2=d.xpath('//android.widget.TextView[contains(@text,"10月24日")]')
        if ch2.exists:
            print('活动订单里活动时间检查通过')
            sleep(2)
        else:
            print('活动订单里活动时间检查失败，请检查原因')
            sleep(2)
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorMyActivity_R_tc038.png'
            d.screenshot(sf2)
            sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现——体验tab活动的报名功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_canceljoin_tc039
#Purpose:我的页面我的活动里取消报名的功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_wode_canceljoin_tc039(self):
        print('TC_检查手机号码登录APP，检查点:已登录账号发现——我的页面我的活动里取消报名的功能---step1进入我的->我的活动页面')
        print('step2点击查看行程单；step3检查取消报名按钮是否存在;step4检查取消报名功能是否正常')
        print('step5检查活动订单里是否暂无活动预约')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——我的活动里取消报名的功能----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        #我的活动
        d(resourceId='cn.com.weilaihui3:id/my_palace_appointment_tv').click()
        sleep(3)
        ch=d.xpath('//*[@text="取消报名"]')
        if ch.exists:
            print('取消报名按钮存在，检查通过')
            sleep(1)
            d(resourceId='cn.com.weilaihui3:id/appointment_button_tv').click()
            sleep(1)
            #是
            d(text='是').click()
            sleep(3)
            #checking
            ch1=d.xpath('//*[@text="取消成功"]')
            if ch1.exists:
                print('取消报名成功')
                sleep(2)
                d.xpath('//*[@text="完成"]').click()
                sleep(2)
                d.press('back')
                sleep(2)
                d.press('back')
                sleep(2)
                #我的活动
                d(resourceId='cn.com.weilaihui3:id/my_palace_appointment_tv').click()
                sleep(4)
                #暂无活动预约
                ch2=d.xpath('//*[@text="自动化测试活动"]')
                if (not ch2.exists):
                    print('我的预约活动已取消报名，检查通过')
                    sleep(2)
                else:
                    print('我的预约活动取消报名失败，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf0='../../test_report/android/'+now+'_errorActivityList_R_tc039.png'
                    d.screenshot(sf0)
                    sleep(2)
                d.press('back')
                sleep(2)
            else:
                print('取消报名失败，请检查原因')
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorCancel_R_tc039.png'
                d.screenshot(sf1)
                sleep(2)
        else:
            print('取消报名按钮不存在，请检查原因')
            now=time.strftime('%Y-%m-%d %H_%M_%S')
            sf2='../../test_report/android/'+now+'_errorNoCancelJoin_R_tc039.png'
            d.screenshot(sf2)
            sleep(2)
            d.press('back')
            sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的——我的活动里取消报名的功能----结束:'+now)

#*******************************************************
#TC Name:test_faxian_expershare_tc040
#Purpose:检查发现页面体验tab下的活动的分享功能
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_faxian_expershare_tc040(self):
        print('TC_检查手机号码登录APP，检查点:发现_发现页面体验tab下的活动的分享功能----step1进入发现页面体验tab')
        print('step2找到活动进入；step3检查并点右上角的分享按钮；step4检查分享微信好友功能是否正常')
        print('step5检查分享朋友圈功能是否正常;step6检查分享新浪微博功能是否正常;step7检查分享我的朋友功能是否正常')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----开始:'+now)
        sleep(4)
        #体验
        d(text='体验').click()
        sleep(4)
        d(resourceId='cn.com.weilaihui3:id/loi_cur_store_tip').click()
        sleep(2)
        d.swipe(50,1700,50,300,1.0)
        sleep(2)
        d.xpath('//android.widget.TextView[@text="蔚来上海二号店"]').click()
        sleep(2)
        #徐家汇活动之还未开始
        d(resourceId='cn.com.weilaihui3:id/activity_list_item_title').click()
        sleep(6)
        #分享图标
        share=d.xpath('//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]')
        sleep(2)
        if share.exists:
            print('分享按钮存在,检查通过')
            sleep(2)
            #...
            share[0].click()
            sleep(2)
            #微信好友
            wh=d.xpath('//*[@text="微信好友"]')
            if wh.exists:
                print('分享到微信好友按钮存在，检查通过')
                sleep(1)
                d.xpath('//*[@text="微信好友"]').click()
                sleep(9)
                d.xpath('//android.widget.TextView[@text="王小龙"]').click()
                sleep(1)
                word=d(resourceId='com.tencent.mm:id/aps')
                word.click()
                sleep(1)
                now0=time.strftime('%Y-%m-%d %H_%M_%S')
                word.send_keys('人生苦短UGC微信好友:'+now0)
                sleep(1)
                #分享
                d.xpath('//android.widget.Button[@text="分享"]').click()
                sleep(1)
                d.xpath('//android.widget.Button[@text="返回蔚来"]').click()
                sleep(1)
                #检查toast
                save1=d.xpath('//*[contains(@text,"分享成功")]')
                if save1.exists:
                    print('分享微信好友成功')
                else:
                    print('分享微信好友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf1='../../test_report/android/'+now+'_errorsharewechat_R.png'
                    d.screenshot(sf1)
                sleep(2)
            else:
                print('分享到微信好友按钮不存在，请检查原因')
            sleep(2)
            #...
            share[0].click()
            sleep(2)
            #朋友圈
            pyq=d.xpath('//*[@text="朋友圈"]')
            if pyq.exists:
                print('分享到朋友圈按钮存在，检查通过')
                sleep(2)
                d.xpath('//*[@text="朋友圈"]').click()
                sleep(8)
                word2=d(resourceId='com.tencent.mm:id/dp0')
                word2.click()
                sleep(1)
                now2=time.strftime('%Y-%m-%d %H_%M_%S')
                word2.send_keys('测试UGC朋友圈:'+now2)
                sleep(1)
                #发表
                #d.xpath('//android.widget.TextView[@text="发表"]').click()
                d(resourceId='com.tencent.mm:id/iv').click()
                sleep(1)
                #检查toast
                save2=d.xpath('//*[contains(@text,"分享成功")]')
                if save2.exists:
                    print('分享朋友圈成功')
                else:
                    print('分享朋友圈失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorsharewechatpyq_R.png'
                    d.screenshot(sf2)
                sleep(2)
            else:
                print('分享到朋友圈按钮不存在，请检查原因')
            sleep(2)
            #...
            share[0].click()
            sleep(2)
            #新浪微博
            wb=d.xpath('//*[@text="新浪微博"]')
            if wb.exists:
                print('分享到新浪微博按钮存在，检查通过')
                sleep(2)
                d.xpath('//*[@text="新浪微博"]').click()
                sleep(13)
                #发送
                #d(resourceId='com.sina.weibo:id/titleSave').click()
                d.xpath('//android.widget.TextView[@content-desc="发送"]').click()
                sleep(1)
                #检查toast
                save3=d.xpath('//*[contains(@text,"分享成功")]')
                if save3.exists:
                    print('分享新浪微博成功')
                else:
                    print('分享新浪微博失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf3='../../test_report/android/'+now+'_errorsharewebo_R.png'
                    d.screenshot(sf3)
                sleep(2)
            else:
                print('分享到新浪微博按钮不存在，请检查原因')
            sleep(2)
            #...
            share[0].click()
            sleep(2)
            #我的朋友
            mf=d.xpath('//*[@text="我的朋友"]')
            if mf.exists:
                print('分享到我的朋友按钮存在，检查通过')
                sleep(2)
                d.xpath('//*[@text="我的朋友"]').click()
                sleep(5)
                d(resourceId='cn.com.weilaihui3:id/share_top_item').click()
                sleep(3)
                #Sam8198
                d(text='Sam8202').click()
                sleep(1)
                #检查toast
                save4=d.xpath('//*[contains(@text,"分享成功")]')
                if save4.exists:
                    print('分享我的朋友成功')
                else:
                    print('分享我的朋友失败，请检查原因')
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf4='../../test_report/android/'+now+'_errorsharemyfriend_R.png'
                    d.screenshot(sf4)
                sleep(2)
            else:
                print('分享到我的朋友按钮不存在，请检查原因')
            sleep(2)
            d.press('back')
            sleep(2)
        else:
            print('分享按钮不存在/未找到,请检查原因')
            sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_发现_发现页面体验tab下的活动的分享功能----结束:'+now)

#*******************************************************
#TC Name:test_wode_giftorder_tc045
#Purpose:检查我的精品订单UI检查和订单详细页面UI检查
#OS:android
#Device:小米Max3
#Pre-conditions:用户已正常登录app
#Post-conditions:N/A
#Modify History:created by Sam [2018/09/14]
#*******************************************************
    def test_wode_giftorder_tc045(self):
        print('TC_检查用户模式打开APP，检查点:我的_我的精品订单UI检查和订单详细页面UI检查----step1用户模式点击我的，再点击我的精品订单')
        print('step2我的精品订单页面上元素UI检查；step3点击某个订单进入订单详细页面;step4订单详细页面进行元素UI检查')
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的精品订单UI检查和订单详细页面UI检查----开始:'+now)
        sleep(4)
        #我的
        d(text='我的').click()
        sleep(4)
        #我的精品订单
        d(text='我的精品订单').click()
        sleep(3)
        ords=d.xpath('//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]')
        if ords.exists:
            #print('Yes')
            sleep(2)
            #检查我的精品订单的各个元素是否存在
            c1=fun_giftorderui_check(self)
            if c1 == True:
                print('我的精品订单上各个被检查元素都检查完毕')
                sleep(2)
                d.xpath('//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
                sleep(3)
                c2=fun_giftorderdetailui_check(self)
                sleep(5)
                if c2 == True:
                    print('我的精品订单的订单详细页面UI检查完毕')
                    sleep(2)
                else:
                    print('我的精品订单的订单详细页面UI检查失败，请检查原因')
                    sleep(2)
                    now=time.strftime('%Y-%m-%d %H_%M_%S')
                    sf2='../../test_report/android/'+now+'_errorGiftOrderDetailUI_R.png'
                    d.screenshot(sf2)
                    sleep(2)
                d.press('back')
                sleep(2)
            else:
                print('我的精品订单UI检查失败，请检查原因')
                sleep(2)
                now=time.strftime('%Y-%m-%d %H_%M_%S')
                sf1='../../test_report/android/'+now+'_errorGiftOrderUI_R.png'
                d.screenshot(sf1)
                sleep(2)
        else:
            print('没有精品订单，无需做UI检查')
            sleep(2)
        d.press('back')
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        print('TC_我的_我的精品订单UI检查和订单详细页面UI检查----结束:'+now)
