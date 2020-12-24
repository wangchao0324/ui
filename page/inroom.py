from appium.webdriver.common.mobileby import By
from base.baseView import BaseView
import logging


class InRoom(BaseView):
    _close_room = (By.ID, "cn.v6.sixrooms:id/iv_close_room")
    _back = (By.ID, "cn.v6.sixrooms:id/iv_back")

    def __init__(self, driver):
        self.driver = driver

    def click_close_room(self):
        logging.info("点击关闭房间按钮")
        self.find_Element(*self._close_room)

    def click_back(self):
        logging.info("点击返回按钮")
        self.find_Element(*self._back)

    def infoXiangQin(self):
        logging.info("通过坐标进入开播的相亲房")
        self.touch_tap(408, 1716)
