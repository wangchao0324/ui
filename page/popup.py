from base.baseView import BaseView
from appium.webdriver.common.mobileby import By
import logging


class Popup(BaseView):
    pop_id = (By.ID, 'cn.v6.sixrooms:id/web_view_h5')
    home_band = (By.ID, 'cn.v6.sixrooms:id/view_hot_banner')
    room_band_first = (By.ID, 'cn.v6.sixrooms:id/first_banner')
    room_band_left_top = (By.ID, 'cn.v6.sixrooms:id/left_top_banner')
    room_band_right_top = (By.ID, 'cn.v6.sixrooms:id/right_top_banner')
    room_band_bottom_center = (By.ID, 'cn.v6.sixrooms:id/bottom_center_banner')
    room_band_second = (By.ID, 'cn.v6.sixrooms:id/second_banner')

    def __init__(self, driver):
        self.driver = driver

    def waitElement_pop(self, place=""):
        logging.info("判断{}弹窗".format(place))
        el = self.judge_element(*self.pop_id)
        if el == False:
            logging.warning("{}弹窗未弹出".format(place))
        else:
            logging.info("{}弹窗以弹出".format(place))
        return el

    def waitElement_band(self, band, place=''):
        logging.info("判断{}创可贴".format(place))
        el = self.judge_element(*band)
        if el == False:
            logging.warning("{}创可贴未出现".format(place))
        else:
            logging.info("{}创可贴以显示".format(place))
        return el

    def touch_home_band(self):
        self.touch_tap(1272, 2221)
