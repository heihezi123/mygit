import unittest
from common import HTMLTestRunner_cn
casePath = "D:\\12\\web_auto\\case" #用例路径
rule = "test*.py"  #匹配规则
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule) #传入参数
print(discover)

reportPath="D:\\12\\web_auto\\report\\"+"result.html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的名称",description="描述报告是做什么的")

runner.run(discover)
fp.close()