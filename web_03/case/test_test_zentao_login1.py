#coding:utf-8
import time
import unittest

from selenium import webdriver

from pages.t2 import LonginZenTao


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   #类方法
       #用例执行之前，只执行一次
         cls.driver = webdriver.Firefox()
         cls.zentao = LonginZenTao(cls.driver)

    def test_01(self):    #测试方法的名称必须要用test开头
         '''用例说明：AAA'''
         self.zentao.login("heihezi_123","408798JY")
         time.sleep(4)
#判断是否登陆成功
         #t =self.driver.find_element_by_css_selector("#userMenu>a").text
         t=self.zentao.get_login_username()  #调用方法
         print("获取的结果：%s"%t)
#断言方法
         self.assertTrue(t == "heihezi_123")


    def test_02(self):  # 错误密码账号
        '''用例说明：AAA'''
        #上面的注释只能写一排
        self.zentao.login("heihezi_123","123456")  #调用登陆函数
        time.sleep(2)
        # 判断是否登陆成功
        #t = self.driver.find_element_by_css_selector("#userMenu>a").text
        t=self.zentao.get_login_username()
        print("登陆失败，获取结果：%s"%t)
        # 断言方法
        self.assertTrue(t == "") #断言失败会自动截图

    def tearDown(self):
        self.zentao.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls): #类方法用CLS
        cls.driver.quit()    #编辑器问题

if __name__=="__main__":
    unittest.main()