from selenium import webdriver

driver = webdriver.Chrome()
driver.get("httos://note.youdao.com/")
driver.find_element_by_id("download-btn").click()

#chrome  设置配置参数，运行前加载配置参数就可以了
profile = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups':0,#设置为0禁止弹出窗口
'download.default_directory':'d:\\' } #指定下载路径
profile.add_experimental_option('prefs',prefs)
chromedriver_path = "D:\\path\\chromedeiver.exe"#自己本地电脑路径
driver = webdriver.Chrome(executable_path=chromedriver_path,
chrome_options=profile)
#executable_path 这个是chromedriver的路径，如果设置过环境变量，此参数可以省略