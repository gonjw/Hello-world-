import requests
import json
#接口header
headers={
"Content-Type": "application/json;charset=utf-8",
"ncov-access-token": "5ebca86899bf9d003d587e77",
}
data={
"address": {
"province": "420000",#省份代码（湖北省）
"city": "420100",#市区代码（武汉市）
"county": "420115",#县级代码（江夏区）
"autoFetch": True,
"lng": "114.31301",#填写当前地区经度
"lat": "30.34653"#填写当前地区纬度
},
"self_suspected": False,
"self_confirmed": False,
"family_suspected": False,
"family_confirmed": False,
"fever": False,
"description":"",
"infected": False,
"at_home": True,
"contacted_beijing":False,
"passed_beijing":False,
"contacted": False,
}
#获取当前日报id
def get_DailyCode():
    link='https://www.ioteams.com/ncov/api/users/dailyReport'
    req=requests.post(link,headers=headers,data=json.dumps(data))
    response=req.json()
    id=response['data']['data']['_id']
    print(id)
    return id
#打卡
def report_health():
    id=get_DailyCode()
    url = 'https://www.ioteams.com/ncov/api/users/dailyReports/{}'
    req=requests.put(url.format(id),headers=json.dumps(headers),data=json.dumps(data))
if __name__ == '__main__':
    report_health()

