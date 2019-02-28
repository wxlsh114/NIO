#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhone7
#version:iOS12.1
#author: Sam Wang
#update date: created by Sam [2018-08-10]

import unittest
import time
import os
import sys
import random
from time import sleep

from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

sys.path.append('../../')
from HTMLTestReportEN import HTMLTestRunner
sys.path.append('../../test_case/ios')
import test_tc_iPhone7_ios12

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
        desired_caps['platformVersion'] = '12.1'
        desired_caps['deviceName'] = 'iPhone7'
        desired_caps['app'] = os.path.abspath('../../test_data/app/ios_package/NextevCarInhouseQA.ipa')
        desired_caps['udid'] = '8056ca675ee0f32cf0bdae6bcbaeda80eb41e688'
        desired_caps['noReset'] = True
        #desired_caps['clearSystemFiles'] = True
        desired_caps['xcodeOrgId'] = 'LH69GT89SS'
        #desired_caps['xcodeSigning'] = 'iPhone Developer'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()


if __name__ == '__main__':
    testunit=unittest.TestSuite()
    """
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_fans_tc001'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_watch_tc002'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_publish_tc003'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_deletepublished_tc007'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_publishnow_tc006'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_tabcheck_tc010'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_personalinfo_tc011'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_scores_tc016'))
    """
    #testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_products_tc013'))
    """
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_article_tc019'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_pengyou_remarkfriend_tc018'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_openmultichat_tc020'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_pengyou_nicknameheadicon_tc028'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_pengyou_dismissmultichat_tc021'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_checkin_tc025'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_pengyou_searchwatch_tc029'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_resetsecupwd_tc030'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_addeditaddress_tc031'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_expershowpic_tc032'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_ugcshare_tc034'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_ugcdel_tc035'))

    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_add2basket_tc022'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_basket2exchange_tc023'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_clearcart_tc044'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_cartcheck_tc043'))

    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_activityshow_tc046'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_es8ordershare_tc047'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_joinnio_tc048'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_aiche_cityplan_tc049'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_aiche_rechargemap_tc050'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_aiche_milecalculator_tc051'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_aiche_es8content_tc052'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_pengyou_im_tc036'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_infopgcshare_tc037'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_experjoin_tc038'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_canceljoin_tc039'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_expershare_tc040'))
    """
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_giftshare_tc041'))
    """
    #last one
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_faxian_publishnowatfriend_tc033'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_loginwechat_tc008'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_loginwebo_tc009'))
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_loginmp_tc004'))
    """
    #testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_jingxi_visitor_tc042'))
    """
    testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_visitor_tc005'))
    ###testunit.addTest(test_tc_iPhone7_ios12.Weilai_test('test_wode_instuninstversioncheck_tc015'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='../../test_report/ios/'+now+'_test_ts_iPhone7_ios12.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='蔚来汽车App测试版iOS12.1真机(iPhone7)\
                          [我的/发现/惊喜/爱车页面相关功能]测试报告by Appium',\
                          description='自动化测试脚本集运行状态:')
    runner.run(testunit)
    fp.close()
