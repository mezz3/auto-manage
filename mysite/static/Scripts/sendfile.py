# import json
import sys
from os.path import exists
import os

import paramiko
from jinja2 import Environment, FileSystemLoader

name_path = sys.argv[1:]
# if name_path:
#     name = name_path[0]

# print(name_path[0])
# print('test')
# upload .unl file to Web EVE-NG
source = r'C:/Users/user/Desktop/auto-manage/mysite/media/template/file/'+name_path[0]
dest = r'/opt/unetlab/labs/'+name_path[0]
hostname = '192.168.81.128'
port = 22 # default port for SSH
username = 'root'
password = 'eve'

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(source, dest)
finally:
    t.close()
