#coding:utf-8
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
check = Base(driver)

loc1 = ("id","c1")
r1 =check.isSelected(loc1)
print(r1)
#点击
chel = check.click(loc1)

r2 = check.isSelected(loc1)
print(r2)


#chenkenbox  全部选中
loc_all = ("xpath",'.//*[@type = "checkbox"]')
all = check.findElements(loc_all)
print(all)

for i in all:
    if i.is_selected():
        pass
    else:
        i.cilick()


#函数
def result(all):
    r = []
    for i in all:
        if not i.is_selected():
            i.click()
            r.append(i.is_selected())#判断结果
        else:
            r.append(i.is_selected())

    return r
print(result(all))