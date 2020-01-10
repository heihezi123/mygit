#coding:utf-8
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("")
check=Base(driver)

loc1=("id",'c1xxxx')
r1 = check.isElementExist2(loc1)
print(r1)

loc_all = ("xpath",'.//*[@type="checkbox"]')
r2 = check.isElementExist2(loc1)
print(r2)