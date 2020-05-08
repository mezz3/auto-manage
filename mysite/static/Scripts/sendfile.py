# import json
import paramiko
# from math import floor
# from lxml import etree
from jinja2 import Environment, FileSystemLoader


# upload .unl file to Web EVE-NG
source = r'C:/Users/user/Desktop/ning 23-30.unl'
dest = r'/opt/unetlab/labs/ning 23-30.unl'
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