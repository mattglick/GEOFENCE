# data_transfer
Transfers coordinates from coordinate.csv file made from the website to an Arduino. 

Future changes that must be made
1. Code on arduino/raspberry pi end must be changed to turn imported data into an array stored on the device
2. Arduino code may have to be changed so it will work for raspberry pi, python code should still work for that
3. Currently, python code transfers the data in one big string, you can change this so that it transfers one coordinate at a time with a loop
