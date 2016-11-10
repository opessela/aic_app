"""
 NX-API-BOT 
"""
import requests
import json

"""
Modify these please
"""
url='http://172.22.163.35:8080/ins'
switchuser='danwms'
switchpassword='AICteam'

debug=0

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.2",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show zoneset active vsan 10",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print response
