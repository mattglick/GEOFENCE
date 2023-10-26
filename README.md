# data_transfer
Transfers coordinates from coordinate.csv file made from the website to an Arduino. 

Computer-End(Python) - data_transfer -> computer-end-transfer 

Arduino-End(.ino) - data_transfer -> arduino-end-transfer 

Computer-End code should work, but arduino-end code may have to be changed to work for the Raspberry-Pi.  

Currently, python code transfers the data in one big string, you can change this so that it transfers one coordinate at a time with a loop

To Test: 
1. Download Thonny and install required libraries
2. Download Visual Studio(or other preferred IDE) for running the computer-end code.
3. Use website to create coordinates.csv file(name must match).
4. Put coordinates.csv this file in the same folder as computer-end code.
5. Download pySerial library.
6. Through Thonny figure out which port the Raspberry Pi Pico is connected to (found under "Tools" bar).
7. Change first parameter on line 11 to the connected port.
8. Run the Thonny Code first, wait until it is done uploading.
9. Close out Thonny once you see "listening..." printed, otherwise the port will be busy and data won't transfer.
10. Next run the computer-end code.
11. Should print "Reply Was: b'(coordinate data here)'", as well as any other print statements if successful.

Contact jerome1@purdue.edu if any questions
