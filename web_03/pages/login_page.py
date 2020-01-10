#coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url ="https://www.zentao.net/user-login.html"
class LoginPage(Base): #继承
    #定位登陆
    loc_user = ("id","account")
    loc_psw= ("css selector","[name='password']")
    loc_button = ("xpath", "//*[@id='submit']")
    loc_keep_login = ("id","keepLoginon")
    loc_forget_psw = ("link text","忘记密码")
    loc_get_user = ("css selector","#siteNav>a")
    loc_login_bug=("id","formError")
    loc_forget_psw_page=("class name","panel-heading")

    def login(self, user="admin", psw="123456", keep_login=False):

        self.sendKeys(self.loc_user, user)
        self.sendKeys(self.loc_psw, psw)
        if keep_login: self.click(self.loc_keep_login)
        self.click(self.loc_button)


    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_psw(self,text=""):
        self.sendKeys(self.loc_psw,text)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_froget_psw(self):
        self.click(self.loc_forget_psw)

    def get_login_name(self):
        user =self.get_text((self.loc_get_user))
        return user

    def get_login_err(self):
        err=self.get_text(self.loc_login_bug)
        return err

    def is_alert_exist(self):
        '''判断alert是不是存在'''
        a=self.is_alert()
        if not a:
            print(a.text)
            a.accept()

    def is_refresh_exist(self):
        '''判断元素是否存在'''
        r = self.isElementExist(self.loc_forget_psw_page)
        return r

    def get_login_result(self,text):
        result =self.is_text_in_element(self.loc_get_user,text)
        return result

    def logine(self, user="heihezi_123",psw="408798JY"):
        '''登陆流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        self.click_login_button()



if __name__=="__main__":
    #driver = webdriver.Chrome()
    #driver.get(login_url)
    #login_page=LoginPage(driver)
    #login_page.input_user("heihezi_123")
    #login_page.input_psw("408798JY")
    #login_page.click_keep_login()
    #login_page.click_froget_psw()
    #time.sleep(2)
    #t =login_page.is_refresh_exist()
    #print(t)

    driver=webdriver.Chrome()
    login_page=LoginPage(driver)
    login_page.logine()
    driver.quit()
