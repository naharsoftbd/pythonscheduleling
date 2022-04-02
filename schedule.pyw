import os
import time
import json
import shlex
from urllib.request import urlopen

# some JSON:
url = "https://jsonplaceholder.typicode.com/posts"
#PAYLOAD_CONF =  '{ "name":"John", "age":30, "city":"New York"}'
response = urlopen(url)
paydic = json.dumps(response.read().decode())

while True:
  if os.path.exists("/home/jafar/schedulestore.json"):
   f = open("/home/jafar/schedulestore.json", "r+") 
   f.seek(0)
   # to erase all data 
   f.truncate() 
   os.system('echo '+ paydic + ' >> /home/jafar/schedulestore.json')
  else:
   os.system('echo '+ paydic + ' >> /home/jafar/schedulestore.json')
  
  time.sleep(0.1)
