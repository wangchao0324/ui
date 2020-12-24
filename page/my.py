from appium.webdriver.common.mobileby import By
from base.baseView import BaseView
import logging
from selenium.common.exceptions import NoSuchElementException


class MyPage(BaseView):

    def __init__(self, driver):
        self.driver = driver

    _shoot_video_cut = (By.ID, "cn.v6.sixrooms:id/record_camera")

    _login = (By.ID, 'cn.v6.sixrooms:id/gotoLogin')
    # xx = 'new UiSelector().text("消息")'
    _username_login = (By.ID, 'cn.v6.sixrooms:id/account_login_button')
    _login_username = (By.ID, 'cn.v6.sixrooms:id/et_username')
    _login_password = (By.ID, "cn.v6.sixrooms:id/et_password")
    _login_but = (By.ID, 'cn.v6.sixrooms:id/but_login')

    # 我的页面元素
    _my_grade_star = (By.ID, "cn.v6.sixrooms:id/starNext")
    _my_grade_tre = (By.ID, "cn.v6.sixrooms:id/wealthNext")
    _my_shoot_video = (By.ID, "cn.v6.sixrooms:id/tv_video")

    def loginStatus(self):
        flag = self.judge_element(*self._login)
        if flag == False:
            logging.info("当前以登录")
        else:
            logging.info("当前未登录")
        return flag

    def goToLogin(self, username="houcp", password="1234qwer"):
        logging.info("通过用户名登录")
        try:
            self.find_Element(*self._login)
            self.find_Element(*self._username_login)
            self.send_keys(username, *self._login_username)
            self.send_keys(password, *self._login_password)
            self.find_Element(*self._login_but)
        except NoSuchElementException:
            logging.warning("登录失败")


class Video(BaseView):
    _shoot_video_cut = (By.ID, "cn.v6.sixrooms:id/record_camera")
    _shoot_video_flicker = (By.ID, "cn.v6.sixrooms:id/record_flash_mode")
    _shoot_video_beauty = (By.ID, "cn.v6.sixrooms:id/record_beauty")
    _shoot_video_beauty_test = (By.ID, "cn.v6.sixrooms:id/seek_alpha")
    _shoot_video_shoot = (By.ID, "cn.v6.sixrooms:id/record_take_iv")
    _shoot_video_back = (By.ID, "cn.v6.sixrooms:id/record_cancel")
    _shoot_video_complete = (By.ID, "cn.v6.sixrooms:id/record_complete")
    _shoot_video_title = (By.ID, "com.smallvideo:id/titleEt")
    _shoot_video_publish = (By.ID, "com.smallvideo:id/publishTv")

    def test1(self):
        self.find_Element(*self._shoot_video_cut)
