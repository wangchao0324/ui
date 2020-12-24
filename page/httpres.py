from base.baseView import BaseView
import re
import logging


class Socket(BaseView):
    baseurl = 'http://v.6.cn/api/doTestPop.php?'

    # uid = 95251880
    # ruid = 66378120
    # eventname_321 = "ceshi_yaping"
    # eventname_322 = 'ceshi_yaping1'
    # eventname_320 = 'ceshi_yaping'
    # eventname_319 = 'test1'
    # # 0代表本次不发送通知形弹窗  ，1则下发
    # show_319 = 1
    # # 0不初始化用——户级弹窗，1只初始化eventname对应的活动，2初始化所有用户
    # isInitEventPop_319 = 2

    def send_socketreq(self, url, socketType):
        req = self.HttpRequests(url)
        res = req.text
        reType = re.compile('act=(.*?)&')
        type = re.findall(reType, url)[0]
        if type == "update":
            if res == "update success":
                logging.info("{}消息状态上线成功".format(socketType))
            else:
                logging.error("{}消息状态上线失败".format(socketType))
        elif type == "send":
            if res == "send success":
                logging.info("{}消息状态下发成功".format(socketType))
            else:
                logging.error("{}消息状态下发失败".format(socketType))
        else:
            logging.error('请求报错：{}'.format(res))

    def send_update(self, eventname_319, status):
        url = self.baseurl + 'act=update&eventname={}&status={}'.format(eventname_319, status)
        res = self.send_socketreq(url, 319)

    def send_319_send(self, uid, eventname, uuid):
        # "http://v.6.cn/api/doTestPop.php?act=send&typeid=319&uid=91271306&eventname=test1&show=1&isInitEventPop=1&uuid=655228ca720f1b21dd915421ff209068&from=0&ctype=2&ver="
        url = self.baseurl + 'act=send&typeid=319&uid={}&eventname={}&show=1&isInitEventPop=1&uuid={}&from=0&ctype=2&ver='.format(
            uid, eventname, uuid)
        res = self.send_socketreq(url, 319)

    def send_320_send(self, ruid, uuid, ifrom=0, ctype=2, ver=None):
        #         http://v.6.cn/api/doTestPop.php?act=send&typeid=320&ruid=86823842&uuid=655228ca720f1b21dd915421ff209068&from=0&ctype=2&ver="
        url = self.baseurl + "act=send&typeid=320&ruid={}&uuid={}&from={}&ctype={}&ver=".format(ruid, uuid, ifrom,
                                                                                                ctype, ver)
        res = self.send_socketreq(url, 320)

    def send_321_send(self, show, eventname, uid, ruid, uuid, ifrom=0, ctype=2, ver=None):
        # http://v.6.cn/api/doTestPop.php?act=send&typeid=321&show=1&eventname=test3&uid=91271306&ruid=86823842&uuid=655228ca720f1b21dd915421ff209068&from=0&ctype=2&ver=
        url = self.baseurl + "act=send&typeid=321&show={}&eventname={}&uid={}&ruid={}&uuid={}&from={}&ctype={}&ver={}".format(
            show, eventname, uid, ruid, uuid, ifrom, ctype, ver)
        res = self.send_socketreq(url, 322)

    def send_322_send(self, uid, ruid, uuid, ifrom=0, ctype=2, ver=None):
        #         http://v.6.cn/api/doTestPop.php?act=send&typeid=322&uid=91271306&ruid=86823842&uuid=655228ca720f1b21dd915421ff209068&from=0&ctype=2&ver=
        url = self.baseurl + "act=send&typeid=322&uid={}&ruid={}&from={}&ctype={}&ver={}".format(uid, ruid, uuid, ctype,
                                                                                                 ver)
        res = self.send_socketreq(url, 322)


if __name__ == '__main__':
    a = Socket()
    a.send_319_send(91271306, 'test1')
