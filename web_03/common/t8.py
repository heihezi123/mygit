from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from pages.login_page import LoginPage
import time

driver = webdriver.Chrome()
a = LoginPage(driver)
a.logine()

#打开BUG编辑页面
driver.get("https://zentao.com")
time.sleep(3)

#点击上传图片
driver.find_element_by_xpath(".//*[@id='dataform']/table/tbody/tr[6]/tb/div/[2]/div[1]/span[18]/span").click()
time.sleep(3)
#点击浏览
driver.find_element_by_css_selector(".keoinline-block.ke-upload-button").click()


k=PyKeyboard()

s="d:\hello.txt"
for i in s:
    k.tap_key(i)
#k.press_key(k.tab_key)
#k.release_key()
time.sleep(1)

k.tap_key(k.enter_key) #点击回车

time.sleep(3)

import os
os.system(r"C:\Users\Adminstor\Desktop\au.exe") #执行exe文件
os.system(r"C:\Users\Adminstor\Desktop\au.exe D:\r.html ")#参数化1
jpg ="D\1.PNG"
os.system(r"C:\Users\Adminstor\Desktop\au.exe %s"%jpg) #参数化2