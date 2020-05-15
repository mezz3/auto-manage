# curl -X POST "http://10.0.15.21:3080/v2/projects" -d '{"name": "yoktest"}'

import requests
import sys
from os.path import exists
import os

temp_name = sys.argv[1:]

url = "http://10.0.15.21/v2/projects"
data= '{"name": "'+temp_name[0]+'"}'

r = requests.post(url, data=data)