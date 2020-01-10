from selenium import webdriver
from selenium .webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import *
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class Base(object):
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self,locator):
        '''定位到元素，返回元素对象，没定位到返回timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele


    def findElement(self, locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc=("id","value1")')
        else:
            print("正在定位元素信息：定位方式->%s,value 值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele


    def findElements(self, locator):
        try:
             eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
             return eles
        except:
             return []



    def sendKeys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()



    def isElementExist(self,locator):
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):  #exist -存在
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n ==1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self,_title):
        '''验证标题'''
        result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
        return result

    def is_title_contains(self,_title):
        '''标题是否包含，返回bool值'''
        result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
        return result

    def is_text_in_element(self,locator,_text):
        '''元素是否包含text，返回bool值'''
        result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
        return  result

    def is_value_in_element(self, locator, _value):
        '''返回bool值,value为空字符串，返回Fasle'''
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
        return result

    def is_alert(self):
        '''检测弹窗'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_titl(self):
        '''获取TITLE'''
        return self.driver.title


    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print(" 获取text失败，返回''")
            return ""

    def move_to_element(self,locator):
        '''鼠标悬停'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def isSelected(self, locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def select_by_index(self,locator,index=0): #不写默认传0
        '''通过索引，index是索引的第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)  #定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def js_scroll_end(self):
        '''滚动到底部'''
        js_heig = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    def js_scroll_end2(self,x=0): #用X参数来控制左右滚动
        '''滚动到底部'''
        js_heig = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js_heig)

    def js_focue(self, loctor):  # 滚动到元素出现的位置
        '''聚焦元素'''
        target = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrillIntoView();", target)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)


if __name__ == "__main__":
    #driver = webdriver.Chrome()
    #driver.get("https://www.zentao.net/user-login.html")
    #zentao = Base(driver)
    #loc1 = (By.ID,"account")
    #zentao.findElement(loc1).send_keys("admin")


    #driver = webdriver.Chrome()
    #driver.get("https://www.zentao.net/user-login.html")
    #zentao = Base(driver)
    #loc1 = (By.ID, "account")
    #loc2 = (By.NAME,"password")
    #loc3 = (By.ID,"submit")
    #zentao.sendKeys(loc1,"heihezi_123")
    #zentao.sendKeys(loc2,"408798JY")
    #zentao.click(loc3)

   # driver = webdriver.Chrome()
    #driver.get("https://www.zentao.net/user-login.html")
    #zentao = Base(driver)
    #loc1 = (By.ID, "account")
    #loc2 = (By.CSS_SELECTOR,"[name='password']")
    #loc3 = (By.XPATH,"//*[@id='submit']")
    #zentao.sendKeys(loc1,"heihezi_123")
    #zentao.sendKeys(loc2,"408798JY")
    #zentao.click(loc3)

    driver = webdriver.Chrome()
    driver.get("https://www.zentao.net/user-login.html")
    zentao = Base(driver)
    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    loc4 = ("id","formError")
    zentao.sendKeys(loc1, "heihezi_123")
    #zentao.sendKeys(loc2, "408798JY")
    zentao.click(loc3)
    time.sleep(2)
    a=zentao.get_text(loc4)
    print(a)
