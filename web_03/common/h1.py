#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()
driver.get("https://www.baidu.com/")

r = EC.title_is("百度一下，你就知道")(driver)
print(r)
assert r == True #或 assert r
r2 = EC.title_contains("百度一下")(driver)
print(r2)
assert r2 ==True
driver.quit()