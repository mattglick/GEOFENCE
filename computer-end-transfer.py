# coordinates.csv file is created from the website at https://epics-evei.github.io/
# coordinates.csv file must be in the same folder in order for python to find it
# code won't work on browser compiler like replit, will work on Visual Studio

import serial # must install pyserial library
import time
import csv

arduinoData = serial.Serial('com5', 115200) # Find which com port the arduino/raspberry pi is connected to

# Writes variable x to the arduino
def arduinoWrite(x):
    time.sleep(1) # Required to give code time to upload, may need to test with increasing/decreasing it
    cmd = str(x)
    cmd = cmd + '\r'
    arduinoData.write(cmd.encode()) # Encodes cmd to transfer to arduino
    time.sleep(0.05)

    data = arduinoData.readline() 
    print(data) # verifies what the arduino is reading

# Turns coordinates.csv file into one string
def get_coordinates():
  filename = open('coordinates.csv', 'r')
  data = list(csv.reader(filename, delimiter = ","))
  filename.close()

  # Puts coordinates into one row array
  new_data = []
  for row in range(len(data)):
    for col in range(len(data[row])):
      new_data.append(data[row][col])

  big_string = ', '.join(new_data) # Turns coordinates.csv file into one long string to make data transfer easier
  # Could transfer coordinates one at a time using a loop if that turns out to be easier
  return(big_string)

first_lat = get_coordinates()
arduinoWrite(first_lat)
