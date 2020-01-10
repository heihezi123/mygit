from selenium import webdriver

driver = webdriver.Firefox()
driver.get("file://c:User/dell/Desktop/div.html")

js = 'document.getElementsByClassName("scroll")[0].scrollTop=1000'
driver.execute_script(js)

#控制横向滚动条的位置
js0='document.getElementsByClassName("scroll")[0].scrollLeft=1000'
driver.execute_script(js0)