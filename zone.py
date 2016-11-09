"""
 NX-API-BOT 
"""
import requests
import json

"""
Modify these please
"""
url='http://172.22.163.35:8080/ins'
switchuser='admin'
switchpassword='nbv_12345'

debug=0

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show zoneset active",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print response
