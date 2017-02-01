import requests
import json
from manager.redis import redis
def reqPOST(URL,body = {}):
	#여기서 Authorization Bearer 뒤에 값은 유저 액세스 토큰이다.
	headers = {
		'content-Type': 'application/json',
		'Authorization' : 'Bearer ' + redis.get('access_token')
	}
	response = requests.post(URL,data = json.dumps(body),headers = headers)
	return response.text

def reqGET(URL,params = {}):
	headers = {
		'content-Type': 'application/json',
		'Authorization' : 'Bearer ' + redis.get('access_token')
		
	}	
	response = requests.get(URL,params = params,headers = headers)
	return response.text