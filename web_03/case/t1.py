import time
class LonginZenTao():
    def __init__(self,driver):
        self.driver = driver

    def login(self, user="admin", psw="12345"):
        self.driver.get=("https://www.zentao.net/user-login.html")
        self.driver.find_element_by_id("account").send_keys(user)  # 正确的密码账号
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()


    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#siteNav>a").text
            print(t)
            return t
        except:
            return ""

    def get_login_bug(self):
        try:
            t = self.driver.find_element_by_id("#siteNav>a").text
            print(t)
        except:
            return""


    def is_alert_exist(self):  # 判断alert是否存在
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()  # 用alert 点alert
            return text
        except:
            return ""


if __name__ =="__mian__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    zentao = LonginZenTao(driver)
    zentao.login()
