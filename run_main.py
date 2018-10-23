import unittest
import time
import HTMLTestRunner
import os

cur_path=os.path.dirname(os.path.realpath(__file__))
def add_case(caseName='case',rule='test*.py'):
    case_path=os.path.join(cur_path,caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    print('test case path:%s',case_path)
    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)

    print(discover)
    return discover

def run_case(all_case,reportName='report'):
    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    report_path=os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath=os.path.join(report_path,now+'result.html')
    print('report path:%s',report_path)
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'自动化测试报告，测试结果如下',
                                         description=u'用例执行情况')
    runner.run(all_case)
    fp.close()

if __name__=='__main__':
    all_case=add_case()
    run_case(all_case)