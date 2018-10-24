import unittest
import time
import HTMLTestRunner
import os

'''获取绝对路径：realpath'''
cur_path=os.path.dirname(os.path.realpath(__file__))

'''add_case方法：加载出在 case 文件下所有符合：test*.py条件的文件'''
def add_case(caseName='case',rule='test*.py'):
    '''将当前目录中的绝对路径和文件拼接成字符串'''
    case_path=os.path.join(cur_path,caseName)

    '''判断是否已经存在：exists这个文件了？？？不存在创建：mkdirif not a:b  意思：如果不是a就执行b '''
    if not os.path.exists(case_path) : os.mkdir(case_path)
    print('test case path:',case_path)

    '''通过unittest模块下的defaultTestLoader类，的discover方法：自动执行目录case下'''
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=rule,
                                                 top_level_dir=None)
    print(discover)
    return discover

'''run_case方法：将上面方法加载出的文件全部执行并省城报告！'''
def run_case(all_case,reportName='report'):
    '''获取现在的时间：strftime'''
    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    '''报告存储的路径'''
    report_path=os.path.join(cur_path,reportName)
    '''判断是否存在，不在创建，如果存在呢？？'''
    if not os.path.exists(report_path):os.mkdir(report_path)
    '''路径+文件名命名=文件全路径'''
    # report_abspath=os.path.join(report_path,now+'_result.html')
    report_abspath = os.path.join(report_path,'result.html')
    print('report path:%s',report_path)
    '''打开报告，往里面写内容'''
    fp=open(report_abspath,'wb')
    '''调用HTMLTestRunner方法，规划格式'''
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'自动化测试报告，测试结果如下',
                                         description=u'用例执行情况')
    runner.run(all_case)
    fp.close()

'''将第一个方法加载出来所有的文件return出来，赋值给all_case。再将all_case传参到run_case方法里进行runner.run()执行'''
if __name__=='__main__':
    all_case=add_case()
    run_case(all_case)