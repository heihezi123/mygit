from selenium import webdriver
from pages.login_page import LoginPage

driver = webdriver.Chrome()
a = LoginPage(driver)
a.logine()

driver.get("http://demo.zentao.net/qa/")

js = 'document.getElemntsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="hello word"'

driver.execute_script(js)

#参数化
body = "hello world"
js = 'document.getElemntsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%body


#JS定位  只有by是单数，其他都是复数
document.getElementById("account").value="admin"
document.getElementsByName("password")[0].value="123456"
document.getElementById("keepLoginon").click()

#订票系统，不能直接输入日期的，要先零时去掉readnoly属性后再赋值，刷新后属性又复原了


