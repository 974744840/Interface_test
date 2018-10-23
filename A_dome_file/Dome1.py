import json
import requests


'''设置api地址'''
URL='https://api.github.com'
def build_url(endpotion):
    return '/'.join([URL,endpotion])    #用字符串join方法拼接URL

'''设置获取信息的格式'''
def better_output(json_str):
    '''
    dumps是将dict转化成str格式，loads是将str转化成dict格式
    dump和load也是类似的功能，只是与文件操作结合起来了
    :param json_str:
    :return:
    '''
    return json.dumps(json.loads(json_str),indent=4)

'''发送请求'''
def request_mthod():

    '''发送get请求得到respons相应信息并赋值'''
    respons=requests.get(build_url('users/974744840'))
    '''格式限制输出相应信息'''
    print(better_output(respons.text))
    '''输出状态码'''
    print(respons.status_code)
    '''输出head头里的：content-type信息'''
    print(respons.headers['content-type'])

if __name__=='__main__':
    request_mthod()


