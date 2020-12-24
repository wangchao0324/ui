from base.baseView import BaseView
from appium.webdriver.common.touch_action import TouchAction
from page.my import MyPage
from page.homepage import Homepage
from page.httpres import Socket
from page.popup import Popup
import pytest
import time
import logging
from py._xmlgen import html
from page.inroom import InRoom


class Test_弹窗(object):
    logging.basicConfig(level=logging.INFO)
    eventname_319_1 = 'test1'
    eventname_319_2 = 'test2'
    eventname_319_3 = 'test3'
    uid = 91271306
    uuid = '655228ca720f1b21dd915421ff209068'
    ruid = 86823842
    show_321 = 1

    baoming="cn.v6.sixrooms"
    # baoming="cn.v6.xiuchang"


    def setup_method(self):
        self.driver = None
        self.driver = BaseView.appium_start(self.baoming)
        self.home = Homepage(self.driver)
        self.my = MyPage(self.driver)
        self.pop = Popup(self.driver)
        self.room = InRoom(self.driver)

    @pytest.mark.skip()
    def test_php319(self):
        logging.getLogger("test_php319")
        logging.info("开始运行319消息用例")
        Socket().send_update(self.eventname_319_1, 2)
        Socket().send_update(self.eventname_319_3, 0)
        logging.info("重启APP")
        self.teardown_method()

        self.setup_method()
        # pop=Popup(self.driver)
        flag = self.pop.waitElement_pop("首页")
        assert flag == True, "首页弹窗没弹出来"
        self.driver.keyevent(4)
        # home=Homepage(self.driver)
        self.home.swipe()
        self.home.clickMy()
        # my=MyPage(self.driver)
        flag = self.my.loginStatus()
        if flag == True:
            self.my.goToLogin()
            self.home.clickRemen()
            self.pop.waitElement("登录后弹窗")
            self.driver.keyevent(4)
        else:
            self.home.clickRemen()
        Socket().send_update(self.eventname_319_1, 0)
        Socket().send_319_send(self.uid, self.eventname_319_1, self.uuid)
        flag = self.pop.waitElement_pop("319通知")
        assert flag == True, "319通知弹窗没弹出来"

    @pytest.mark.skip()
    def test_php320(self):
        logging.getLogger("test_php320")
        logging.info("开始执行320消息用例")
        Socket().send_update(self.eventname_319_1, 2)
        Socket().send_update(self.eventname_319_3, 0)
        Socket().send_update(self.eventname_319_2, 2)
        logging.info("重启APP")
        self.teardown_method()
        self.setup_method()
        self.pop.waitElement_pop("首页")
        self.driver.keyevent(4)
        self.home.swipe()
        self.home.searchInfoRoom(232740372)
        flag = self.pop.waitElement_pop("视频房")
        assert flag == True, "视频房主动弹窗没弹出来"
        self.driver.keyevent(4)
        flag = self.pop.waitElement_band(self.pop.room_band_first, "视频房倒数第一")
        assert flag == True, "视频房倒数第一创可贴没显示出来"
        flag = self.pop.waitElement_band(self.pop.room_band_second, "视频房倒数第二")
        assert flag == True, "视频房倒数第二创可贴没显示出来"
        Socket().send_update(self.eventname_319_2, 0)
        Socket().send_320_send(self.ruid, self.uuid)
        time.sleep(1)
        flag = self.pop.waitElement_band(self.pop.room_band_first, "视频房倒数第一")
        assert flag == True, "视频房倒数第一创可贴没显示出来"
        flag = self.pop.waitElement_band(self.pop.room_band_second, "视频房倒数第二")
        assert flag == False, "视频房倒数第二创可贴不该显示出来"

    @pytest.mark.skip()
    def test_php322(self):
        logging.getLogger("test_php322")
        logging.info("开始执行322消息用例")
        Socket().send_update(self.eventname_319_1, 0)
        Socket().send_update(self.eventname_319_3, 2)
        logging.info("重启APP")
        self.teardown_method()
        self.setup_method()
        self.pop.waitElement_pop("首页")
        self.driver.keyevent(4)
        self.home.swipe()
        self.home.searchInfoRoom(232740372)
        falg = self.pop.waitElement_pop("房间内322消息")
        assert falg == True, "房间内322消息弹窗没弹出来"
        self.driver.keyevent(4)
        self.room.click_close_room()
        Socket().send_update(self.eventname_319_3, 0)
        Socket().send_322_send(self.uid, self.ruid, self.uuid)
        self.home.infoRoom()
        falg = self.pop.waitElement_pop("房间内322取消")
        assert falg == False, "房间内322消息弹窗不该弹出来"


    def test_php323(self):
        logging.getLogger("test_php323")
        Socket().send_update(self.eventname_319_1, 0)
        Socket().send_update(self.eventname_319_3, 2)
        logging.info("重启app")
        self.teardown_method()
        self.setup_method()
        self.pop.waitElement_pop("首页")
        self.driver.keyevent(4)
        self.home.swipe()
        self.home.clickMy()
        flag = self.my.loginStatus()
        if flag == True:
            self.my.goToLogin()
        self.home.clickRemen()
        self.home.searchInfoRoom(232740372)
        flag = self.pop.waitElement_pop("322视频房")
        assert flag == True, "322视频房弹窗没弹出来"
        self.driver.keyevent(4)
        Socket().send_update(self.eventname_319_3, 2)
        Socket().send_321_send(self.show_321, self.eventname_319_3, self.uid, self.ruid, self.uuid)
        flag = self.pop.waitElement_pop("321视频房通知型")
        assert flag == True, "321视频房通知型弹窗没弹出来"

    @pytest.mark.skip()
    def test_initialApi(self):
        logging.getLogger("test_initialApi")
        logging.info("开始运行initialApi用例")
        Socket().send_update(self.eventname_319_1, 2)
        Socket().send_update(self.eventname_319_3, 0)
        logging.info("重启APP")
        self.teardown_method()

        self.setup_method()
        flag = self.pop.waitElement_pop("首页")
        assert flag == True, "首页弹窗没弹出来"
        self.driver.keyevent(4)
        flag = self.pop.waitElement_band(self.pop.home_band, '首页')
        assert flag == True, "首页创可贴没显示出来"
        self.pop.touch_home_band()
        flag = self.pop.waitElement_pop("首页")
        assert flag == True, "点击首页创可贴无反应"
        self.driver.keyevent(4)
        self.home.swipe()
        self.home.clickMy()
        flag = self.my.loginStatus()
        if flag == True:
            self.my.goToLogin()
        self.home.clickRemen()
        self.home.searchInfoRoom(232740372)
        flag = self.pop.waitElement_pop("视频房")
        assert flag == True, "视频房主动弹窗没弹出来"
        self.driver.keyevent(4)
        flag = self.pop.waitElement_band(self.pop.room_band_first, "视频房倒数第一")
        assert flag == True, "视频房倒数第一创可贴没显示出来"
        flag = self.pop.waitElement_band(self.pop.room_band_bottom_center, "视频房正下方")
        assert flag == True, "视频房正下方创可贴没显示出来"
        flag = self.pop.waitElement_band(self.pop.room_band_right_top, "视频房右上方")
        assert flag == True, "视频房右上方创可贴没显示出来"
        flag = self.pop.waitElement_band(self.pop.room_band_left_top, "视频房左上角")
        assert flag == True, "视频房左上角创可贴没显示出来"
        self.room.click_close_room()
        self.room.click_back()
        logging.info("查找进入房间")
        self.home.searchRoom(786023)
        self.home.searchGo()
        self.home.searchGoroom()
        self.home.infoRoom()
        flag = self.pop.waitElement_pop("电台房")
        assert flag == True, "电台房主动弹窗没弹出来"
        self.driver.keyevent(4)
        flag = self.pop.waitElement_band(self.pop.room_band_first, "电台房倒数第一")
        assert flag == True, "电台房倒数第一创可贴没显示出来"
        self.room.click_close_room()
        self.room.click_back()
        logging.info("查找进入房间")
        self.home.searchRoom(714626)
        self.home.searchGo()
        self.home.searchGoroom()
        self.home.infoRoom()
        self.room.infoXiangQin()
        flag = self.pop.waitElement_pop("相亲房")
        assert flag == True, "相亲房主动弹窗没弹出来"
        self.driver.keyevent(4)
        flag = self.pop.waitElement_band(self.pop.room_band_first, "相亲房倒数第一个创可贴")
        assert flag == True, "相亲房倒数第一创可贴没显示出来"

    def teardown_method(self):
        time.sleep(1)
        self.driver.terminate_app(self.baoming)
        self.driver.quit()


if __name__ == '__main__':
    report_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    pytest.main(['-sv', r"..\case\\popUp_test.py", "--html",
                 r"C:\Users\dell\PycharmProjects\sixroom\report\report{}.html".format(report_time)])
