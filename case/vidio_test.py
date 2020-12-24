from page.my import MyPage
from page.popup import Popup
from base.baseView import BaseView
import pytest
import time
from page.homepage import Homepage
from py._xmlgen import html
import logging


class Test_测试(object):
    logging.basicConfig(level=logging.INFO)

    def setup_method(self):
        self.driver = None
        self.driver = BaseView.appium_start()

    def test_shoot_video001(self):
        log = logging.getLogger("test_shoot_video001")
        a = Homepage(self.driver)
        b = Popup(self.driver)
        logging.info("判断首页弹窗")
        if b.waitElement("首页") == True:
            self.driver.keyevent(4)
        a.swipe()
        a.clickMy()

    def test_2(self):
        a = MyPage(self.driver)
        a.test()

    def teardown_method(self):
        self.driver.terminate_app('cn.v6.sixrooms')
        del (self.driver)


if __name__ == '__main__':
    # a = os.system(r'pytest -sv ..\case\\test_vidio.py')
    # print(a)
    report_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    pytest.main(['-sv', r"..\case\\vidio_test.py", "--html",
                 r"C:\Users\dell\PycharmProjects\sixroom\report\report{}.html".format(report_time)])
