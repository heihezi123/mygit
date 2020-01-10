#coding:utf-8
from selenium  import webdriver
from  pages.login_page import LoginPage ,login_url
import time
import unittest
import ddt   #ddT数据框架啊

@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome()
        cls.lognp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        #self.lognp.is_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self,user,psw,expect):
        #self.lognp.login(user,psw)
        self.lognp.input_user(user)
        self.lognp.input_psw(psw)
        self.lognp.click_login_button()
        time.sleep(2)
        result=self.lognp.get_login_name()
        print(" 测试结果：%s"%result)
        self.assertTrue(result==expect)

    @ddt.data({"user": "heihezi_123", "psw": "408798JY", "expect": "heihezi_123"},
              {"user": "heihezi_123", "psw": "", "expect": "登录"},
              {"user": "admin", "psw": "123455", "expect": "登录"})
    def test_01(self,data):
        print("---------开始测试：test01---------")
        print("测试数据:%s" %data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("----------结束：pass---------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__=="__main__":
    unittest.main()



