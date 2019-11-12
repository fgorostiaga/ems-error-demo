import os
import requests
from time import sleep
import sys

ems = os.environ["ET_EMS_LSBEATS_HOST"]
appid = os.environ["APPID"]
hostport = 'http://' + ems + ":8181"

print appid

for i in range(100):
    json_message = {'APPID': int(appid)}
    requests.post(hostport, json=json_message)
    print "sent message n", i, "on app", appid
    sys.stdout.flush()
    sleep(1)


