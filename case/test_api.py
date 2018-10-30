# coding:utf-8
import unittest
import ddt
import os
import requests
from common import base_api
from common import read_excel
from common import write_excel
from common.logger import Logger


logger=Logger(logger='Test_api').getlog()

'''获取demo_api.xlsx路径'''
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "demo_api.xlsx")

'''复制demo_api.xlsx文件到report下'''
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xlsx")

'''调用read类，读取要测试的excel 的内容'''
testdata = read_excel.ExcelUtil(testxlsx).dict_data()

'''创建数据驱动测试类'''
@ddt.ddt
class Test_api(unittest.TestCase):
    '''添加@classmethod 表示该方法是类级别，是类里的所有方法执行前执行setUp，类里的所有方法执行完后执行tearDown'''
    @classmethod
    def setUpClass(cls):
        '''这里的session是如果要登陆需要传参登陆'''
        cls.s = requests.session()
        '''复制case目录下的excel数据到report目录下的result表格'''
        write_excel.copy_excel(testxlsx, reportxlsx)

        '''这里（*testdata）是上面用read方法读到case目录的原始测试的数据，所以下面可以直接调用
            data = *testdata   == 上面读取的所有内容 
        '''
    @ddt.data(*testdata)
    def test_api(self, data):
        '''
        res       是发送请求后返回的respones信息
        base_api  的wierte方法将 返回的状态码等信息写入到report目录下的result表格里
        '''
        res = base_api.send_requests(self.s, data)
        base_api.wirte_result(res, filename=reportxlsx)

        res_text = res["text"]
        logger.info("返回实际结果为->：%s"%res_text)

        '''输出要检查的内容和返回的信息'''
        check = data["checkpoint"]
        logger.info("检查点为->：%s"%check)

        self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()