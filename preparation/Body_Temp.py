# The DS18B20 uses a 1 wire serial interface
# Setting : Raspberry Pi Configuration -> Preferences -> Interfaces -> Enable for the 1-Wire interface.

# Python library: w1thermsensor
#--> 	sudo pip3 install w1thermsensor

# Import Libraries
import sys
import RPi.GPIO as GPIO
import urllib3
from time import sleep         # to control how often the sensor data is collected
from w1thermsensor import W1ThermSensor # to enable our project to talk to the sensor

sensor = W1ThermSensor()                # create an object to store a connection the sensor. 
                                        # So rather than typing W1ThermSensor() everytime we want to use the sensor, 
                                        # we store the connection in an object called sensor.
baseURL = 'http://api.thingspeak.com/update?api_key=EGGDD5XE4A35W6MB&field1='
                                       # we store the connection in an object called sensor.
# Running a Forever Loop
while True:
    temperature = sensor.get_temperature()   # get the current temperature from the DS18B20 sensor,
    http = urllib3.PoolManager()
    f = http.request('GET',baseURL +str(temperature))
    f.read()
    f.close()                                        # and then store it in a variable called temperature. 
    sleep(15)
    
    #print("The temperature is %s celsius" % temperature) # print the data in the form of a sentence that will tell the us what the temperature is in celsius.
                                                         # using string formatting, where we would like the temperature data to be printed in the sentence, 
                                                         #  we use an %s which will format the temperature data from an float to a string 
    
    if temperature == 37.5:                    # temperature threshold
        # *** take an action regarding the cloud ***
        break                                # break out of the loop
            
   
    # end of program
