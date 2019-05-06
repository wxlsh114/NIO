#coding=utf-8
#test purpose : verify the main features on iPhone
#os: iOS
#device: iPhoneSE
#version:iOS12.2
#author: Sam Wang
#update date: created by Sam [2019-03-04]

import unittest
import time
import sys
import os
import random
from time import sleep

sys.path.append('../../')
from HTMLTestReportEN import HTMLTestRunner
sys.path.append('../../test_case/ios')
import stg_tc_iPhoneSE_ios12

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Weilai_test(unittest.TestCase):


    if __name__ == '__main__':
        testunit=unittest.TestSuite()
        #1st part
        """
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_fans_tc001'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_watch_tc002'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_publish_tc003'))
        """
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_deletepublished_tc007'))
        """
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_publishnow_tc006'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_tabcheck_tc010'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_personalinfo_tc011'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_scores_tc016'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_article_tc019'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_remarkfriend_tc018'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_openmultichat_tc020'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_nicknameheadicon_tc028'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_dismissmultichat_tc021'))
        """
        #testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_checkin_tc025'))
        #testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_onlinesupport_tc108'))
        """
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_giftorderdetail_tc107'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_searchfromlist_tc109'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_searchwatch_tc029'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_resetsecupwd_tc030'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_addeditaddress_tc031'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_errfeedback_tc076'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_expershowpic_tc032'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_ugcshare_tc034'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_ugcdel_tc035'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_articlecollect_tc098'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_swipedelcollect_tc099'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_articlecollect_tc098'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_clickdelcollect_tc100'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_takenote_tc101'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_takenotesave_tc102'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_tryes6share_tc103'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_tryes8share_tc104'))
        #not for now
        """
        #bug:zan=-1
        ###testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infolikecomment_tc129'))
        ###testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infospeciallikecomment_tc131'))
        """
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infovotelikecomment_tc130'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infovideocomment_tc132'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_normal_tc134'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_cancelfollow_tc135'))
        #资讯:自动化专题
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_livecast_tc017'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_livecastshare_tc024'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infospecialshare_tc070'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infoarticleshare_tc071'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infolinkshare_tc072'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infovoteshare_tc073'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_publishdel_tc081'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_delchatfromchats_tc082'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_delchatfromfriendslist_tc084'))
        #惊喜part
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_products_tc013'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_add2basket_tc022'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_basket2exchange_tc023'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_clearcart_tc044'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_cartcheck_tc043'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_giftshare_tc041'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_visitor_tc042'))
        #3rd part
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_es8ordershare_tc047'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_es6share_tc086'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_es6ordershare_tc087'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_es8share_tc088'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_joinnio_tc048'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_cityplan_tc049'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemap_tc050'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_carmall_tc140'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemapswipe_tc090'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemapfeedback_tc091'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemapownercommentslike_tc092'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemappilot_tc093'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemaprechargehistory_tc094'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemaprechargepole_tc095'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemapsearchroute_tc096'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_rechargemaprouteplan_tc097'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_milecalculator_tc051'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_es8content_tc052'))

        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_im_tc036'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_infopgcshare_tc037'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_experjoin_tc038'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_activity_tc026'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_activityshow_tc046'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_canceljoin_tc039'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_experjoincancel_tc069'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_cityswitch_tc089'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_publishnowatfriend_tc033'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_unbundlingwechat_tc077'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_bindingwechat_tc078'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_unbundlingwebo_tc079'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_bindingwebo_tc080'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_loginwechat_tc008'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_loginwebo_tc009'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_loginmp_tc004'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_visitor_tc005'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorlikecomment_tc110'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorshareniofriend_tc111'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorexpjoin_tc112'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorexpshowpic_tc113'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorseminarlikecomment_tc114'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorseminarshareniofriend_tc115'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorugclikecomment_tc116'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorugcshareniofriend_tc117'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorugcreport_tc118'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorvotelikecomment_tc119'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorvoteshareniofriend_tc120'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorlivecastcomment_tc121'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitorlivecastshareniofriend_tc122'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_visitornowheadiconfollow_tc123'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitorcontentshareniofriend_tc124'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitorcityserviceshareniofriend_tc126'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitorrechargemap_tc127'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitormilecalculatorshareniofriend_tc128'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_pengyou_visitor_tc133'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitorenergy_tc136'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitorservice_tc137'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitoronekey_tc138'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_visitoraccessory_tc139'))
        ###testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_wode_instuninstversioncheck_tc015')
        #点亮中国
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_lightenchina4noncarowner_tc063'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_lighted4noncarowner_tc064'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_notlighted4noncarowner_tc065'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_mapswitch4noncarowner_tc066'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_lightenchina4carowner_tc056'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_mylighted4carowner_tc057'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_myexplored4carowner_tc058'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_myvisitedcity4carowner_tc059'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_explorenearbymore4carowner_tc060'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_lightenchina4carowner_tc061'))
        ###testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_mapswitch4carowner_tc062'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_moreandicon4carowner_tc067'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_lightenchina4unauthcarowner_tc068'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_aiche_onekeymaintain4carowner_tc141'))
        #特殊账号
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_notenoughscore_tc074'))
        ###testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_tryes6noncarowner_tc105'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_tryes8noncarowner_tc106'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_canceltryes8noncarowner_tc125'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_jingxi_zeroscore_tc083'))
        testunit.addTest(stg_tc_iPhoneSE_ios12.Weilai_test('test_faxian_experjoinzeroscore_tc085'))
        """
        now=time.strftime('%Y%m%d_%H%M%S')
        filename='../../test_report/ios/'+now+'_stg_ts_iPhoneSE_ios12.html'
        fp=open(filename,'wb')
        runner=HTMLTestRunner(stream=fp,title='iPhoneSE_iOS12.2真机\
                              v3.5.5_build:3135_发现/朋友/惊喜/爱车/我的UI测试报告by Appium',\
                              description='自动化测试脚本集运行状态:')
        runner.run(testunit)
        fp.close()
