import os
import requests
from time import sleep
import sys
import socket

ems = os.environ["ET_EMS_LSBEATS_HOST"]
appid = os.environ["APPID"]
# TODO: use ET_EMS_HTTPINEVENTS_API
hostport = 'http://' + ems + ":8181"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print "App ID", appid
print "EMS url", hostport

for i in range(240):
    json_message = {'APPID': int(appid), 'NUMBER': i, "SUTIP": IPAddr}
    r = requests.post(hostport, json=json_message)
    print r.content
    print "sent message n", i, "on app", appid
    sys.stdout.flush()
    sleep(0.5)

json_message = {'STOP': True}
r = requests.post(hostport, json=json_message)
print r.content
sys.stdout.flush()

