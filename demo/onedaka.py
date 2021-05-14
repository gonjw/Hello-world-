import requests,json

headers={
"Content-Type": "application/json;charset=utf-8",
"ncov-access-token": '5ebd5cba23cc19003daca144	',#警告：用户token是唯一且不变的，必须要有！！！！谨慎保存请勿泄露
}
data={
"address": {
"province": "420000",#省份代码
"city": "420100",#市区代码
"county": "420115",#县级代码
"autoFetch": True,
"lng": "114.2621",#填写当前地区经度
"lat": "30.295"#填写当前地区纬度
},
"self_suspected": False,
"self_confirmed": False,
"family_suspected": False,
"family_confirmed": False,
"fever": False,
"infected": False,
"description": "",
"at_home": True,
"contacted": False
}
def get_DailyCode():
#创建日报并获取当前日报id
	link='https://www.ioteams.com/ncov/api/users/dailyReport'
	req=requests.post(link,headers=headers,data=json.dumps(data))
	response=req.json()
	id=response['data']['data']['_id']
    print(id)
	return id

def report_health():
	id=get_DailyCode()
	url = 'https://www.ioteams.com/ncov/api/users/dailyReports/{}'
	req=requests.put(url.format(id),headers=headers,data=json.dumps(data))
if __name__ == '__main__':
	report_health()

