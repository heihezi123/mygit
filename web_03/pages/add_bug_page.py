#coding:utf-8
from selenium import webdriver
from common.base import Base

import time


class AddBugPage(Base): #继承  禅道测试
    #添加BUG
    loc_test = ("link text","测试")
    loc_bug = ("link text","Bug")
    loc_addbug = ("xapth",".//*[@id='createActionMenu']/a")
    loc_truck = ("xapth",".//*[@id='opendBuild_chosen']/u1")
    loc_truck_add = ("xapth", ".//*[@id='opendBuild_chosen']/div/u1/li")
    loc_input_title = ("id","title")
    #需要先切换
    loc_input_body = ("class name","article-content")
    loc_avse = ("css selector","#submit")

    #新增的列表
    loc_new = ("xapth",".//*[@id='bugList']/tbody.tr[1]/td[4]/a")


    def add_bug(self,title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title,title)

        #输入正文
        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)   #需要在类中备注driver浏览器
        body = '''[测试步族]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.driver.clear(self.loc_input_body) #这里有问题，这里是附文本不能用clear
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()   #回到主页面

        self.click(self.loc_avse)

    def is_add_bug_sucess(self,_text):
        self.is_text_in_element(self.loc_new,_text)



if __name__ =="__main__":
    driver = webdriver.Chrome()
    #driver.get("https://www.zentao.net/user-login.html")
    bug = AddBugPage(driver)

    from  pages.login_page import LoginPage
    a=LoginPage(driver)
    a.logine()

    bug.add_bug()
    timestr = time.strftime("%Y_%m_%D_%H_%M_%S")
    title = "测试提交BUG"+ timestr
    bug.add_bug(title)
    result = bug.is_add_bug_sucess(title)
    print(result)



