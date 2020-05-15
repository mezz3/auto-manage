# curl -X POST "http://10.0.15.21:3080/v2/projects" -d '{"name": "yoktest"}'

# import urllib
import requests
# import urllib.request as urllib
# data = '{"name": "ningtest"}'
# url = 'http://10.0.15.21:3080/v2/projects'
# req = urllib.Request(url, data, {'Content-Type': 'application/json'})
# f = urllib.urlopen(req)
# for x in f:
#     print(x)
# f.close()

# headers = {
#     'Content-type': 'application/json',
# }

# data = '{"name": "yoktest"}'

# response = requests.post('http://10.0.15.21:3080/v2/projects', headers=headers, data=data)


url = "http://10.0.15.21/v2/projects"
data= '{"name": "yoktest2"}'
# headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

r = requests.post(url, data=data)
# data = r.json()
# print(data)