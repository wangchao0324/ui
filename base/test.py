from base.config import SetupConfig


class A:
    def __init__(self,bao):

        if bao == "xiuchang":
            self.desired_caps = SetupConfig.xiuchang
        elif bao == "shiliu":
            self.desired_caps = SetupConfig.sixroom

    def a(self):
        print('打印{}'.format(self.desired_caps))


c = A("xiuchang")
# c.a()