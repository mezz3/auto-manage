import os
import sys
from os.path import exists, split

import requests

# get information all file project in gns3
# curl -i -X GET 'http://10.0.15.21/v2/projects'

# delete file project in gns3
# curl -i -X DELETE 'http://localhost:3080/v2/projects/856d9a5f-f0fc-4a14-ab9c-6cd61abde4f6'

temp_name = sys.argv[1:]

# scraping data to get id
url = 'http://10.0.15.21/v2/projects'
web_data = requests.get(url)
text = web_data.json()

dic = {}
for i in text:
    key = i['name']
    if key not in dic.keys():
        dic[key] = i['project_id']
    # print(i['name'])
    # print(i['project_id'])
print(dic)

# delete project
temp_name = sys.argv[1:]
name = temp_name[0]

project_id = dic[name]
print(type(project_id))

url = "http://10.0.15.21/v2/projects/"+project_id
r = requests.delete(url)
