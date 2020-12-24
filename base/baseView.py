import time
from appium.webdriver.common.mobileby import By
from appium import webdriver
from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import requests
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import logging
from base.config import SetupConfig

class BaseView():

    # log提取、输出
    # CON_LOG='../log/log.conf'
    # logging.config.fileConfig(CON_LOG)
    # logging=logging.getLogger()
    # 封装成一个方法
    def appium_start(bao):
        if bao =="cn.v6.xiuchang":
            desired_caps = SetupConfig.xiuchang
        elif bao == "cn.v6.sixrooms":
            desired_caps = SetupConfig.sixrooms
        elif bao == "linayun":
            pass
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        driver.implicitly_wait(20)
        return driver

    def find_Element(self, *loc):
        try:
            self.driver.find_element(*loc).click()
        except NoSuchElementException:
            logging.error('未找到{}元素'.format(*loc))

    def send_keys(self, vaule, *loc, clear_first=True, click_firsr=True):
        try:
            if click_firsr:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(vaule)
        except NoSuchElementException:
            logging.error(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def judge_element(self, *loc):
        flag = None
        try:
            self.driver.find_element(*loc)
            flag = True
        except:
            flag = False
        finally:
            return flag

    def uiautomotar_click(self, text):
        # self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_android_uiautomator(text).click()
        except NoSuchElementException:
            logging.error('{}页面未找到{}元素'.format(self, text))

    def HttpRequests(self, url, method="get", data=None, headers=None):
        method = method.lower()
        res = None
        if method == 'post':
            if headers != None:
                res = requests.post(url=url, data=data, headers=headers, timeout=10, verify=False)
            else:
                res = requests.post(url=url, data=data, timeout=10, verify=False)

        elif method == 'jsonpost':
            if headers != None:
                res = requests.post(url=url, data=data, headers=headers, timeout=10, verify=False)
            else:
                res = requests.post(url=url, data=data, timeout=10, verify=False)

        elif method == 'get':
            if headers != None:
                res = requests.get(url=url, data=data, headers=headers, timeout=10, verify=False)
            else:
                res = requests.get(url=url, data=data, timeout=10, verify=False)
        elif method == 'paramsget':
            if headers != None:
                res = requests.get(url=url, params=data, headers=headers, timeout=10, verify=False)
            else:
                res = requests.get(url=url, params=data, timeout=10, verify=False)
        else:
            logging.error('没有这个类型的请求')
        return res

    def touch_tap(self, x, y, duration=500):
        time.sleep(1)
        screen_width = self.driver.get_window_size()['width']
        screen_height = self.driver.get_window_size()['height']
        a = (float(x) / 1440) * screen_width
        x1 = int(a)
        b = (float(y) / 2712) * screen_height
        y1 = int(b)
        TouchAction(self.driver).press(x=x1, y=y1).release().perform()
