import json
import requests
from common.read_excel import ExcelUtil
from common.write_excel import copy_excel, Write_excel
from common.logger import Logger


logger=Logger(logger='send').getlog()
'''封装requests请求的方法'''
def send_requests(s, testdata):
    '''请求方式和请求URL'''
    method = testdata["method"] #请求类型
    url = testdata["url"]       #请求的URL
    test_nub = testdata['id']   #请求的第几条
    type = testdata["type"]     #数据类型是data还是json

    '''url后面的params参数'''
    try:
        params = eval(testdata["params"])   #eval是将字符串转换为有效格式
    except:
        params=None

    ''' 获取post请求类型的headers、body、type'''
    try:
        headers = eval(testdata["headers"])
    except:
        headers = None

    try:
        body = eval(testdata["body"],)
    except:
        body = None

    if type == "data":
        typebody = testdata['type']
    elif type== "json":
        typebody = testdata['type']
    else:
        typebody=None

    ''' 判断什么类型的请求，进行日志输出'''
    if method == "post":
        logger.info("******************正在执行用例：-----  %s  ----******************" % test_nub)
        logger.info("请求方式：%s, 请求url:%s" % (method, url))
        logger.info("post请求body的数据类型为：%s " % typebody)
        logger.info("post请求的headers：%s" % headers)
        logger.info("post请求的body内容：%s" % body)
    elif method =='get':
        logger.info("******************正在执行用例：-----  %s  ----******************" % test_nub)
        logger.info("请求方式：%s, 请求url:%s" % (method, url))
        logger.info("请求params：%s" % params)


    '''上面的所或许的信息是为了输出日志，下面的信息才是要进行发送请求用的'''
    verify = False      #verify是否验证服务器的TLS证书或字符串
    res = {}   # 接受返回数据
    try:
        r = s.request(method=method,            #r=响应内容
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      # verify=verify
                       )
        # logger.info("页面返回信息：%s" % r.content.decode("utf-8"))    #decode是将内容以utf-8格式解码

        '''这里返回到res的所有数据用来 最后添加到报告的表格里'''
        res['id'] = testdata['id']              #返回测试id
        res['rowNum'] = testdata['rowNum']      #返回第几行

        '''上面两行是将读到表里内容赋给res,下面的将请求返回的各种信息赋给res'''
        res["statuscode"] = str(r.status_code)  #返回状态码，将状态码转成str
        logger.info('返回的状态码：%s'% res["statuscode"])

        res["text"] = r.content.decode("utf-8") #返回的信息，也就是响应的具体内容
        res["times"] = str(r.elapsed.total_seconds())   # 返回请求时间，并转成str
        logger.info('响应时间：%s'%res["times"])

        '''这个if是判断是否是200，如果不是就将响应返回的信息给 error 当错误信息'''
        if res["statuscode"] != "200":          #判断返回的状态码
            res["error"] = res["text"]                    #如果是200返回的error为空
        else:
            res["error"] =  ''         #否则为页面返回信息

        res["msg"] = ""                             #提示信息为空
        '''这里相当于断言判断'''
        if testdata["checkpoint"] in res["text"]:   #将数据表里的要进行断言判断的数据和返回的信息对比，进行判断是否返回正确
            res["result"] = "pass"                  #如果是那么结果是通过：pass
            logger.info("用例测试结果:  %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"                  #如果不在就是失败：fail
            logger.info("用例测试结果:  %s---->%s" % (test_nub, res["result"]))
        return res
    except Exception as msg:                         #异常判断
        res["msg"] = str(msg)
        return res

def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub, 8, result['statuscode'])       # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 9, result['times'])            # 耗时
    wt.write(row_nub, 10, result['error'])           # 状态码非200时的返回信息
    wt.write(row_nub, 12, result['result'])
    wt.write(row_nub, 13, result['msg'])                # 抛异常

# if __name__ == "__main__":
#     data = ExcelUtil("debug_api.xlsx").dict_data()
#     print(data[0])
#     s = requests.session()
#     res = send_requests(s, data[0])
#     copy_excel("debug_api.xlsx", "result.xlsx")
#     wirte_result(res, filename="result.xlsx")