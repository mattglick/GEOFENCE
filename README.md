# data_transfer
Transfers coordinates from coordinate.csv file made from the website to an Arduino. 

Computer-End(Python) - data_transfer -> computer-end-transfer 

Arduino-End(.ino) - data_transfer -> arduino-end-transfer 

Computer-End code should work, but arduino-end code may have to be changed to work for the Raspberry-Pi.  

Currently, python code transfers the data in one big string, you can change this so that it transfers one coordinate at a time with a loop

To Test: 
1. Download Arduino IDE.
2. Download Visual Studio(or other preferred IDE) for running the computer-end code.
3. Use website to create coordinates.csv file(name must match).
4. Put coordinates.csv this file in the same folder as computer-end code.
5. Download pySerial library.
6. Through the Arduino IDE figure out which port arduino is connected to (found under "Tools" bar).
7. Run the Arduino Code first, wait until it is done uploading.
8. Next run the computer-end code.
9. Should print coordinate data between b'(coordinate data here)' if successful.

Contact jerome1@purdue.edu if any questions
