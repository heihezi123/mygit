#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()
driver.get("https://www.zentao.net/user-login.html")

loc1 = ("xpath","//*[text()='忘记密码']")
r1 = EC.presence_of_element_located(loc1)(driver)
print(r1) #返回元素对象

loc2 =("xpath","//*[text()='忘记密码']")
#loc2 =("xpath",".//*[@id='login-form']/form/table/tbody/tr[4]/td/a") #路径写错了
r2 = EC.text_to_be_present_in_element(loc2,"忘记密码")(driver)
print(r2)

driver.quit()
