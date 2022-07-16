import time
import os
import array
import pylab as pl
import Adafruit_ADS1x15
import requests

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7

def ECg_Readings():

    print('ECG sensors starting...')
    ECG_volts=[]

    def ReadChannel(channel):
        adc = Adafruit_ADS1x15.ADS1115()
        GAIN = 1
        data = adc.read_adc(0, gain=GAIN)
        return data

    # Function to convert data to voltage level,
    # rounded to specified number of decimal places. 
    def ConvertVolts(data,places):
        volts = (data * 4.096) / float(32768)
        volts = round(volts,places)  
        return volts
    # Define delay between readings
    for i in range (0,100):

        # Read the light sensor data
        ECG_level = ReadChannel(0)
        ECG_volts.append(ConvertVolts(ECG_level,2))
        ECG_report = {}
        ECG_report["value1"] = ECG_level                      
        requests.post('https://maker.ifttt.com/trigger/csv/with/key/nRm3Yf4BU-Irdwh4MnqoXmsH4SoHxY7wf7EpsgvFV26',data=ECG_report) 
        time.sleep(0.003)

    #pl.plot(ECG_volts,label="ECG")
    #pl.legend()
    #pl.show()
    return ECG_volts
