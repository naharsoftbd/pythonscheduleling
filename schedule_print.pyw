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

url = 'http://192.168.4.28:8000/api/v1/printers'
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 2)
myobj = []
for printer in printers:
  currentprinter = win32print.GetDefaultPrinter();
  if currentprinter == printer['pPrinterName']:
    status = 1
  else:
    status = 0
  myobj.append({'printer_name': printer['pPrinterName'],'status':status,'client_ip':ipaddress})


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
x = requests.post(url, json = {'printers':myobj},headers=headers)


while True:
  url = "http://192.168.4.28:8000/api/v1/printers"
  response = requests.get(url)
  defaultprinter = response.json()['defaultprinter'][0]['printer_name']
  win32print.SetDefaultPrinter(defaultprinter)
  currentprinter = win32print.GetDefaultPrinter();
  if response.json()['filename']:
    filename = response.json()['filename'][0]['printing_file']
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % currentprinter, ".", 0)
  print(currentprinter)  
  time.sleep(1)
  
