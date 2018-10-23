import json
import requests
import unittest

class Test_login(unittest.TestCase):
    url='https://passport.womai.com/redirect/redirect.do'

    headers={'Accept':'application/json, text/javascript, */*',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection':'keep-alive',
             'Content-Length':'159',
             'Content-Type':'application/x-www-form-urlencoded',
             'Host':'passport.womai.com',
             'Referer':'https://passport.womai.com/redirect/redirect.do?mid=0&returnUrl=http%3A%2F%2Fwww.womai.com%2Findex-31066-0.htm',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0',
             'X-Requested-With':'XMLHttpRequest'
    }

    playde={'loginId':'www974744840',
            'mid':'0',
            'password':'xiaoxinxin123',
            'returnUrl':'http://www.womai.com/index-31066-0.htm',
            'serverPath':'http://www.womai.com/',
            'tempcode':'',
            'validateCode':''
    }
    def test_login(self):
        '''
        发送response请求：
        post里有三个参数：url、headers、data
        :return:
        '''
        response=requests.post(self.url,headers=self.headers,data=self.playde)
        '''这里如果返回的response响应是json字符串的话，response.json()则将成为一个对象'''
        json_data=response.json()
        print(json_data)

        self.assertEqual('2',json_data['msg'])

if __name__=='__main__':
    unittest.main()