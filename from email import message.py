import sys
from time import sleep
import urllib3
import requests

a = 0
b = 1
c = 0
baseURL = 'http://api.thingspeak.com/update?api_key=EGGDD5XE4A35W6MB&field1='
while(a < 1000):
    print (a)
    http = urllib3.PoolManager()
    f = http.request('GET',baseURL +str(a))
    f.read()
    f.close()
    sleep(5)
    c = a
    a = a + b
    b = c
    if a>5:
            report = {}
            report["value1"] = a
            requests.post('https://maker.ifttt.com/trigger/111/with/key/nRm3Yf4BU-Irdwh4MnqoXmsH4SoHxY7wf7EpsgvFV26',data=report)

print ("Program has ended")

