from selenium import webdriver


def js_scroll_end(self):
    '''滚动到底部'''
    js_heig="window.scrollTo(0,document.body.scrollHeight)"
    self.driver.execute_script(js_heig)

def js_focue(self,loctor): #滚动到元素出现的位置
    '''聚焦元素'''
    target = self.findElement(loctor)
    self.driver.execute_script("arguments[0].scrillIntoView();",target)

def js_scroll_top(self):
    '''回到顶部'''
    js = "window.scrollTo(0,0)"
    self.driver.execute_script(js)

js="var q=document.documentElement.scrollTop=200" #滚动控制
self.driver.execute_script(js)