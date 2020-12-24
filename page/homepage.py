from appium.webdriver.common.mobileby import By
from base.baseView import BaseView
import logging


class Homepage(BaseView):
    _guanzhu = 'new UiSelector().text("关注")'
    _im = 'new UiSelector().text("消息")'
    _dongtai = 'new UiSelector().text("动态")'
    _my = 'new UiSelector().text("我的")'
    _home_fujin = 'new UiSelector().text("附近")'
    _home_remen = 'new UiSelector().text("热门")'
    _search_but = (By.ID, 'cn.v6.sixrooms:id/btn_search')
    _search_room = (By.ID, "cn.v6.sixrooms:id/search_editText_content")
    _search_go = (By.ID, "cn.v6.sixrooms:id/iv_title_serach_cancle")
    _search_choiceRoom = (By.ID, "cn.v6.sixrooms:id/name")
    _infoRoom = (By.ID, "cn.v6.sixrooms:id/tv_living")

    def __init__(self, driver):
        self.driver = driver

    def clickMy(self):
        logging.info("点击'我的按钮'")
        self.uiautomotar_click(self._my)

    def clickGuanzhu(self):
        logging.info("点击'观注按钮'")
        self.uiautomotar_click(self._guanzhu)

    def clickIm(self):
        logging.info("点击'消息按钮'")
        self.uiautomotar_click(self._im)

    def clickRemen(self):
        logging.info("点击'热门按钮'")
        self.uiautomotar_click(self._home_remen)

    def clickDongtai(self):
        logging.info("点击'动态按钮'")
        self.uiautomotar_click(self._dongtai)

    def swipe(self):
        size = self.driver.get_window_size()
        # print(size)
        x1 = size['width'] * 0.75
        x2 = size['width'] * 0.25
        y1 = size['height'] * 0.5
        self.driver.swipe(x1, y1, x2, y1, 400)

    def cliciSearch(self):
        self.find_Element(*self._search_but)

    def searchRoom(self, roomNumber):
        self.send_keys(roomNumber, *self._search_room)

    def searchGo(self):
        self.find_Element(*self._search_go)

    def searchGoroom(self):
        self.find_Element(*self._search_choiceRoom)

    def infoRoom(self):
        self.find_Element(*self._infoRoom)

    def searchInfoRoom(self, roomNumber):
        logging.info("通过查找进入房间")
        self.find_Element(*self._search_but)
        self.send_keys(roomNumber, *self._search_room)
        self.find_Element(*self._search_go)
        self.find_Element(*self._search_choiceRoom)
        self.find_Element(*self._infoRoom)
