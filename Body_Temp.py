# The DS18B20 uses a 1 wire serial interface
# Setting : Raspberry Pi Configuration -> Preferences -> Interfaces -> Enable for the 1-Wire interface.

# Python library: w1thermsensor
#--> 	sudo pip3 install w1thermsensor

# Import Libraries
import time         # to control how often the sensor data is collected
from w1thermsensor import W1ThermSensor # to enable our project to talk to the sensor

sensor = W1ThermSensor()                # create an object to store a connection the sensor. 
                                        # So rather than typing W1ThermSensor() everytime we want to use the sensor, 
                                        # we store the connection in an object called sensor.
# Running a Forever Loop
while True:
    temperature = sensor.get_temperature()   # get the current temperature from the DS18B20 sensor,
                                             # and then store it in a variable called temperature. 
    
    print("The temperature is %s celsius" % temperature) # print the data in the form of a sentence that will tell the us what the temperature is in celsius.
                                                         # using string formatting, where we would like the temperature data to be printed in the sentence, 
                                                         #  we use an %s which will format the temperature data from an float to a string 
    
    if temperature == 37:                    # temperature threshold
        # *** take an action regarding the cloud ***
        break                                # break out of the loop
            
    time.sleep(60)                            # wait for 60 seconds between taking a temperature reading.

    # end of program
