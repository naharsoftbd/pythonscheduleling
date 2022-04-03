import os
import time
import json
import shlex
from urllib.request import urlopen
import requests
import win32print
import win32api
import socket

#get Ip Address
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

ipaddress = getNetworkIp()

url = 'http://127.0.0.1:8000/api/v1/printers'
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 2)
myobj = []
for printer in printers:
  myobj.append({'printer_name': printer['pPrinterName'],'status':0,'client_ip':ipaddress})


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
x = requests.post(url, json = {'printers':myobj},headers=headers)

print(x.json())

r = requests.get('http://127.0.0.1:8000/api/v1/printers')

x=r.json()['printers']

for i in x:
  print(i['printer_name'])

# some JSON:
url = "http://127.0.0.1:8000/api/v1/printers"
#PAYLOAD_CONF =  '{ "name":"John", "age":30, "city":"New York"}'
response = urlopen(url)
paydic = json.dumps(response.read().decode())
resp = json.loads(paydic)
print (resp)

"""
while True:
  if os.path.exists("C:\\schedulestore.json"):
   f = open("C:\\schedulestore.json", "r+") 
   f.seek(0)
   # to erase all data 
   f.truncate() 
   os.system('echo '+ paydic + ' >> C:/schedulestore.json')
  else:
   os.system('echo '+ paydic + ' >> C:/schedulestore.json')
  print ("Local current time :")
  time.sleep(0.1)
  """
