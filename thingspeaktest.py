import sys
import RPi.GPIO as GPIO
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
    sleep(1)
    c = a
    a = a + b
    b = c
    if a>5:
        requests.post("https://maker.ifttt.com/trigger/111/with/key/nRm3Yf4BU-Irdwh4MnqoXmsH4SoHxY7wf7EpsgvFV26Irdwh4MnqoXmsH4SoHxY7wf7EpsgvFV26")
print ("Program has ended")