import time
import os
import array
import pylab as pl
import Adafruit_ADS1x15
import csv

ECG_volts=[]

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    data = adc.read_adc(0, gain=GAIN)
    return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places. 
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(40960)-1
  volts = round(volts,places)  
  return volts
  
# Define delay between readings
delay = 0.01
i = 0
while i<200:

  # Read the light sensor data
  ECG_level = ReadChannel(0)
  ECG_volts.append(ConvertVolts(ECG_level,2))
#   file = open('ECG_Radings.csv','a',newline='')
#   wr=csv.writer(file)
#   wr.writerow(ConvertVolts(ECG_level,2))
#   file.close()

  # Print out results
  print( "--------------------------------------------" ) 
  print("ECG_volts : {} ({}V)".format(i,ECG_volts[i]))  
  i=i+1
  # Wait before repeating loop
  time.sleep(delay)
file = open('ECG_Radings.csv','a',newline='')
wr=csv.writer(file)
wr.writerow(ECG_volts)
file.close()

pl.plot(ECG_volts,label="ECG")
pl.legend()
pl.show()