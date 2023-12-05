# data_transfer
Transfers coordinates from coordinate.csv file made from the website to a Raspberry Pi Pico. 

Computer-End(Python) - data_transfer -> computer-end-transfer.py

Pi-End(circuit python) - data_transfer -> data_transfer_pi_end.py 

Pi end code has everything you need to run the geofence, and may be outdated from the main gps_code.py. 

Currently, python code transfers the data in one big string, you can change this so that it transfers one coordinate at a time with a loop

To Test: 
1. Download Thonny and install required libraries
2. Download Visual Studio(or other preferred IDE) for running the computer-end code.
3. Use website to create coordinates.csv file, you can change the name but make sure you change this in the computer end code on line 5.
4. Put coordinates.csv file in the same folder as the computer-end code.
5. Download pySerial library.
6. Through Thonny figure out which port the Raspberry Pi Pico is connected to (found under "Tools" bar).
7. Change first parameter on line 11 of the computer end code to the connected port.
8. Run the pi end code in Thonny first.
9. Close out Thonny once you see "listening..." printed, otherwise the port will be busy and data won't transfer.
10. Next run the computer-end code.
11. Should print "Reply Was: b'(coordinate data here)'" and "Connection Confirmed" as well as any other print statements if successful.

Potential Errors:
If it is printing "Busy Port: Try closing Raspberry Pi IDE(Thonny)", then that means something is interupting the port the Pi is connected to. This would be caused if you kept Thonny open while running the computer end code. You could also have other serial monitors or serial data printers such as the one in the Arduino IDE that is preventing you from transferring data.

"Error: Likely weak signal, try testing outside" comes from the Pi End Code. It is a ValueError, and the most likely culprits are being somewhere where the GPS cant get satelte data, such as too close to a building or inside. It could also indicated a problem with one of the connections, most likely the GPS connection. Make sure there are no cut or disconnected wires and the GPS antenna is firmly connected to the GPS module on the geofence.

Contact jerome1@purdue.edu if any questions
