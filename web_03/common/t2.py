#coding:utf-8
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
baidu = Base(driver)

loc1 = ("link text","设置")
mouse = baidu.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ("link text","搜索设置")
baidu.click(loc2)

loc3 =("xpath",".//*[@id='nr']/option[3]")
r1 = baidu.findElement(loc3).is_selected()
print(r1)

loc4 = ("id","nr")
select = baidu.findElement(loc4)
Select(select).select_by_index(2)

r2 = baidu.findElement(loc3).is_selected()
print(r2)

#r1=baidu.isSelected(loc3)  #调用方法
#print(r1)
# r2=baidu.isSelected(loc4)
#print(r2)

driver.quit()