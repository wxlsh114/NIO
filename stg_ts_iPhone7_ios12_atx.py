#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhone7
#version:iOS12.1
#author: Sam Wang
#update date: created by Sam [2018-12-07]

import wda
import unittest
import time
import os
import sys
import random
from time import sleep

sys.path.append('../../')
from HTMLTestReportEN import HTMLTestRunner
sys.path.append('../../test_case/ios')
import stg_tc_iPhone7_ios12_atx

c=wda.Client('http://localhost:8100')

class Weilai_test(unittest.TestCase):


    def setUp(self):
        #s=c.session('com.do1.WeiLaiApp.inhouse')
        sleep(1)

    def tearDown(self):
        # end the session
        sleep(1)


if __name__ == '__main__':
    testunit=unittest.TestSuite()
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_fans_tc001'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_watch_tc002'))
    ##testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_publish_tc003'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_deletepublished_tc007'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_publishnow_tc006'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_tabcheck_tc010'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_personalinfo_tc011'))
    #testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_scores_tc016'))
    ##testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_jingxi_products_tc013'))
    """
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_article_tc019'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_pengyou_remarkfriend_tc018'))
    ##testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_openmultichat_tc020'))
    ##testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_pengyou_nicknameheadicon_tc028'))
    ##testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_pengyou_dismissmultichat_tc021'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_checkin_tc025'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_pengyou_searchwatch_tc029'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_resetsecupwd_tc030'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_addeditaddress_tc031'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_expershowpic_tc032'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_ugcshare_tc034'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_ugcdel_tc035'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_activityshow_tc046'))
    """
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_pengyou_im_tc036'))
    """
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_infopgcshare_tc037'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_experjoin_tc038'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_canceljoin_tc039'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_expershare_tc040'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_jingxi_giftshare_tc041'))
    #last part
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_faxian_publishnowatfriend_tc033'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_loginwechat_tc008'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_loginwebo_tc009'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_loginmp_tc004'))
    testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_visitor_tc005'))
    """
    ###testunit.addTest(stg_tc_iPhone7_ios12_atx.Weilai_test('test_wode_instuninstversioncheck_tc015'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='../../test_report/ios/'+now+'_stg_ts_iPhone7_ios12_atx.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='iPhone7_iOS12.1真机\
                          v3.4.0_build:2906_我的/发现/惊喜/爱车UI测试报告by ATX',\
                          description='自动化测试脚本集运行状态:')
    runner.run(testunit)
    fp.close()
