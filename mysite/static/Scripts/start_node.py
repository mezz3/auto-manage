# curl -i -X POST 'http://localhost:3080/v2/projects/7b438af0-3276-47f7-a213-d0238838f49d/duplicate' -d '{"name": "hello"}'

import requests
import sys
from os.path import exists
import os

project_id = sys.argv[1:]

url = "http://10.0.15.21/v2/projects/"+project_id[0]+"/nodes/start"
data = '{}'
r = requests.post(url, data=data)