import os
import requests
from time import sleep

ems = os.environ["ET_EMS_LSBEATS_HOST"]
appid = os.environ["APPID"]
hostport = 'http://' + ems + ":8181"

for _ in range(60):
    json_message = {'APPID': int(appid)}
    requests.post(hostport, json=json_message)
    sleep(1)


