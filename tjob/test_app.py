import os
from websocket import create_connection
import json

if __name__ == "__main__":
    print("Starting the test")
    
    url = "ws://" + self.ems + ":3232"
    ws = create_connection(url)
   
    ems = os.environ["ET_EMS_LSBEATS_HOST"]
    tjobid = os.environ["TJOBID"]
    headers = {'content-type': 'text/plain'}
    stampers = ""
    monMachines = ""

    # get the stampers from file
    with open(os.environ['PWD'] + "/" + "stampers.txt") as f:
      stampers = f.read()

    # send stampers to EMS
    url = "http://" + self.ems + ":8888/stamper/tag0.1"
    response = requests.post(url, headers=headers, data=stampers)
    print(response.content)

    # get the monitoring machines from the file
    with open(os.environ['PWD'] + "/" + "monitoring_machines.txt") as f:
      monMachines = f.read()

    monMachines = monMachines.replace("TJOBID", tjobid)

    # send the monitoring machines to EMS
    url = "http://" + self.ems + ":8888/MonitoringMachine/signals0.1"
    response = requests.post(url, headers=self.headers, data=self.monMachines)
    print(response.content)
 

    eventcount = 60    
    while eventcount > 0:
        result = ws.recv()
        result = json.loads(result)
        if "#sendevent" in result.get("channels", {}):
            print result
            eventcount -= 1
        
    print("Ending the test")

