#订票系统，不能直接输入日期的，要先零时去掉readnoly属性后再赋值，刷新后属性又复原了
#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
time.sleep(3)

js1 = '''document.getElementById("train_date").removeAttribute("readonly");
        document.getElementById("train_date").value="2018-10-25"'''

driver.execute_script(js1)

#或
js1 ='document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js1)

driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").sendkeys("2018-10-25")