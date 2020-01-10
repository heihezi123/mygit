#coding:utf-8
from selenium import webdriver
from common.base import Base
import time


class LoginPage(Base): #继承
    #定位登陆
    loc1 = ("id","account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    loc_keep_login = ("id","keepLoginon")
    loc_user = ("class selector","#userMenu>a")


    def login(self,user="admin",psw="123456",keep_login=False):
        self.driver.get(login_url)
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        if keep_login:self.click(self.loc_keep_login)
        self.click(self.loc3)


    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#siteNav>a").text
            print(t)
            return t
        except:
            return ""


    def is_alert_exist(self):  # 判断alert是否存在
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()  # 用alert 点alert
            return text
        except:
            return ""

    def get_login_name(self):
        user = self.get_text(self.loc_user)

if __name__ =="__main__":
    driver = webdriver.Firefox()
    login_url="https://www.zentao.com"
    bug = LoginPage(driver)




