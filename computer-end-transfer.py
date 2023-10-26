import time
import serial
import csv

coordinateFilename = "coordinates"

def initialize():
    ser = 0
    while ser == 0:
        try:
            ser = serial.Serial('COM8', 9600)  # open serial port
        except:
            print("Busy Port: Try closing Raspberry Pi IDE(Thonny)")
            time.sleep(0.3)
            pass
    return ser

# Writes variable x to the arduino
def serialWrite(x, ser):
    time.sleep(1) # Required to give code time to upload, may need to test with increasing/decreasing it
    cmd = str(x)
    cmd = cmd + '\r'
    print(f"Sending Command: [{cmd}]")
    ser.write(cmd.encode()) # Encodes cmd to transfer to pico
    time.sleep(0.05)

    reply = b''

    for _ in range(len(cmd)):
        a = ser.read() # Read the loopback chars and ignore

    coordinateTransferred = False
    while True:
        while True:
            a = ser.read()

            if a== b'\r':
                break

            else:
                reply += a
            time.sleep(0.01)
        if coordinateTransferred == False:
            print(f"\nReply was: {reply}")
            print("\n Connection Confirmed")
            coordinateTransferred = True
        else:
            print(f"{reply}")
        reply = b''

    ser.close()

# Turns coordinates.csv file into one string
def get_coordinates():
  filename = open(f'{coordinateFilename}.csv', 'r')
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

coordinate_data = get_coordinates() # Gets coordinates from coordinates.csv and changes the format
serialWrite(coordinate_data, initialize()) # Transmits data to raspberry pi and returns raspberry pi response
