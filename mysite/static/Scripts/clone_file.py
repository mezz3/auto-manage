# curl -i -X POST 'http://localhost:3080/v2/projects/7b438af0-3276-47f7-a213-d0238838f49d/duplicate' -d '{"name": "hello"}'

import requests
import sys
from os.path import exists
import os

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

# clone project
name = temp_name[0]
project_id = dic[name]

url = "http://10.0.15.21/v2/projects/"+project_id+"/duplicate"
data= '{"name": "'+temp_name[0]+'"}'

r = requests.post(url, data=data)