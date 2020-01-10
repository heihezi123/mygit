#coding:utf-8
from selenium  import webdriver
from  pages.login_page import LoginPage ,login_url
import time
import unittest


class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome()
        cls.lognp = LoginPage(cls.driver)


    def setUp(self):
        self.driver.get(login_url)


    def login_case(self,user,psw,expect):
        #self.lognp.login(user,psw)
        self.lognp.input_user(user)
        self.lognp.input_psw(psw)
        self.lognp.click_login_button()
        time.sleep(2)
        result=self.lognp.get_login_name()
        self.assertTrue(result==expect)


    def test_01(self):
        '''输入用户名heihezi_123,密码408797JY,点登陆'''
        print("---------开始测试：test01---------")
        self.lognp.input_user("heihezi_123")
        self.lognp.input_psw("408798JY")
        self.lognp.click_login_button()
        time.sleep(2)
        result=self.lognp.get_login_name()
        self.assertTrue(result=="heihezi_123")
        print("----------结束：pass---------")


    def test_02(self):
        '''输入用户名heihezi_123,点击登陆'''
        print("---------开始测试：test02---------")
        self.lognp.input_user("heihezi_123" )
        self.lognp.click_login_button()
        time.sleep(2)
        result=self.lognp.get_login_err()
        self.assertTrue(result =="登录失败，请检查您的用户名或密码是否填写正确。")
        print("----------结束：pass---------")

    def test_03(self):
        '''输入用户名heihezi_123,点击登陆'''
        print("---------开始测试：test03---------")
        self.lognp.input_user("heihezi_123")
        self.lognp.click_login_button()
        time.sleep(2)
        result = self.lognp.get_login_name()
        self.assertTrue(result == "登录")
        print("----------结束：pass---------")

    def test_04(self):
        '''忘记密码'''
        print("---------开始测试：test04---------")
        #self.lognp.input_user("heihezi_123")
        self.lognp.click_froget_psw()
        self.lognp.is_refresh_exist()
        print("----------结束：pass---------")

    def tearDown(self):
        self.driver.delete_all_cookies()  # 退出登陆
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
         #self.driver.delete_all_cookies() #退出登陆
         #self.driver.refresh()
         cls.driver.quit()



