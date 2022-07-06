import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import spidev
import time
import matplotlib.pyplot as plt
from drawnow import *


lopluse = 17
lominus = 27
#temp=[]
temp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
########################################################

######## raspberry pi configuration #############
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(lopluse, GPIO.IN)
GPIO.setup(lominus, GPIO.IN)

#####################################################

################ Analog read function using mcp3204 chip(spi)  ###################
def analogRead(channel):
    
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    data = adc.read_adc(0, gain=GAIN)
    return data

############################################################################

################## Graph plot #######################################
plt.ion()  # tell matplotlib you want interactive mode to plot live data
def graph():
    plt.plot(temp, 'r-')
    plt.title('ECG')
    plt.ylabel(' voltage value')
    plt.axis([0,40,0,30])
    plt.grid(True)
##################################################################

while True:
    if (GPIO.input(lopluse)== GPIO.HIGH | GPIO.input(lominus) == GPIO.HIGH):
        print("!")


    else:
        analogValue = analogRead(0)
        volts = round(((analogValue * 3.3) / 4096.0), 2)
        temp.append(volts)
        temp.pop(0)
        print(analogValue)
        print(volts)
##        print(temp)
        drawnow(graph)
        plt.pause(0.000001)

