import requests
import json



url='https://api.github.com'
def build_url(endpoint):
    return '/'.join([url,endpoint])
def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)
def json_method():
    response=requests.patch(build_url('user'),auth=('974744840','daxinxin123.'),json={
        'company':'haotest',
        'email':'974744840@qq.com'
    })
    print(better_output(response.text))

if __name__=='__main__':
    json_method()
