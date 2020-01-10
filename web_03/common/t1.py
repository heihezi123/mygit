#coding:utf-8
from selenium import webdriver
from common.base import Base

driver = webdriver.Firefox()
driver.get("http://www.zentao.net/user-login.html")
zentao = Base(driver)
loc1=("id","account")

el1 = zentao.findElement(loc1)

#判断元素
r1 = el1.is_displayed()
print(r1)

loc2 = ("class name","hiding")
el2 = zentao.findElement(loc2)
r2 = el2.is_displayed()
print(r2)

driver.quit()