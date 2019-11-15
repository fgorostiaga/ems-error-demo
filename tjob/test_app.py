import os
from websocket import create_connection
import json
import time
import requests
import sys
import socket

if __name__ == "__main__":
    print("Starting the test")
    
    ems = os.environ["ET_EMS_LSBEATS_HOST"]
    tjobid = os.environ["TJOBID"]
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    headers = {'content-type': 'text/plain'}
    stampers = ""
    monMachines = ""

    # get the stampers from file
    with open(os.environ['PWD'] + "/" + "stampers.txt") as f:
      stampers = f.read()
      
    print stampers
    sys.stdout.flush()

    # send stampers to EMS
    url = "http://" + ems + ":8888/stamper/tag0.1"
    response = requests.post(url, headers=headers, data=stampers)
    print(response.content)

    # get the monitoring machines from the file
    with open(os.environ['PWD'] + "/" + "monitoring_machines.txt") as f:
      monMachines = f.read()

    monMachines = monMachines.replace("TJOBID", tjobid)
    monMachines = monMachines.replace("DEPLOYIP", IPAddr)
    monMachines = monMachines.replace("TJOBEMSIP", ems)
    
    print monMachines
    sys.stdout.flush()

    # send the monitoring machines to EMS
    url = "http://" + ems + ":8888/MonitoringMachine/signals0.1"
    response = requests.post(url, headers=headers, data=monMachines)
    print(response.content)
    
    url = "ws://" + ems + ":3232"
    ws = create_connection(url)
    
    print "starting loop"
    sys.stdout.flush()

    start = time.time()
    while time.time() < start + 100:
        try:
            result = ws.recv()
            result = json.loads(result)
            print result
            print str(ws.remote_address)
            if "#stop" in result["channels"]:
                break;
        except Exception, e:
            print "test exception", e
        sys.stdout.flush()
        
    print("Ending the test")
    sys.stdout.flush()

