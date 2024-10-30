# EPICS EVEI
# 
# This script is used to create plots of data that only uses GPS.
# IT SHOULD BE IGNORED, unless you want to test out the old code.
# 'plot_imu_data.py' plots graphs of data with IMU, so YOU SHOULD
# USE THAT INSTEAD.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import sys
import math as m





# This file converts the input data from the datalog and converts it into an array of Latt, Long, refresh, and in/out
# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# import_file = input("Enter the name of the datalog file: ")

# with open(import_file, "r") as file:
#     for line in file: 
#         if line == "":
#             if "" != "IN" or "OUT":
#                 line.
#                 line = line.strip()
#                 line = line.strip("Latitude:","Longitude:","GPS Refresh Rate:")
import csv

# Function to process the text file and extract necessary information
def process_gps_data(input_file, output_file):
    # Initialize a list to store the relevant rows
    processed_data = []

    # Open the input file and read it line by line
    with open(input_file, 'r') as infile:
        # current_status = None
        current_lat = None
        current_lon = None
        current_refresh_rate = None

        for line in infile:
            stripped_line = line.strip()

            # # Check for 'OUT' or 'IN' status
            if stripped_line == "OUT" or stripped_line == "IN":
                current_status = stripped_line
            
            # Check for Latitude and Longitude line
            elif "Latitude" in stripped_line and "Longitude" in stripped_line:
                parts = stripped_line.split()
                current_lat = parts[1]  # Latitude value
                current_lon = parts[3]  # Longitude value

            # Check for GPS Refresh Rate
            elif "GPS Refresh Rate" in stripped_line:
                current_refresh_rate = stripped_line.split(":")[1].strip()  # Extract the refresh rate

                # Only append if all values (status, lat, lon, refresh rate) are available
                if current_status and current_lat and current_lon and current_refresh_rate:
                    current_lon = "-" + current_lon
                    processed_data.append([current_lat, current_lon, current_status, current_refresh_rate])
                    # Reset the values for the next entry
                    # current_status = None
                    current_lat = None
                    current_lon = None
                    current_status = None
                    current_refresh_rate = None

    # Write the processed data into a CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header
        writer.writerow(['Latitude', 'Longitude', 'Status','GPS Refresh Rate'])
        # Write the processed rows
        writer.writerows(processed_data)

    print(f"Data has been processed and saved to {output_file}")

# Specify the input and output files
input_file = input("Input the TXT file: ")  # Replace with your actual input file
output_file = "stripped_csv_file.csv"

# Call the function to process the data
process_gps_data(input_file, output_file)








def Distance(x1, y1, x2, y2):
	distance = (((y2 - y1) ** 2) + ((x2 - x1) ** 2))
	distance = m.sqrt(distance)
	return distance
#sys.argv[1]
csv_data = pd.read_csv(output_file, skiprows=1)
#keep_default_na = False
csv_data = csv_data.drop_duplicates()
data = csv_data.to_numpy()
print(data)

#for i in range(0, data[:,0].size()):


lat = np.array(data[:,0]) * 100000
long = np.array(data[:,1]) * 100000
status = np.array(data[:,2])
ref_rate = np.array(data[:,3])

distance_arr = []
for i in range(1, lat.size):
    
    
    if status[i] == "OUT":
        status_color = "red"
        distance_arr.append(round(Distance(long[i-1], lat[i-1], long[i], lat[i]), 2))
        plt.plot(long[i-1:i+1],lat[i-1:i+1], "x", color=status_color)
    elif status[i] == "IN":
        status_color = "green"
        distance_arr.append(round(Distance(long[i-1], lat[i-1], long[i], lat[i]), 2))
        plt.plot(long[i-1:i+1],lat[i-1:i+1], "x", color=status_color)
	
	#plt.text(x=np.mean(long[i-1:i+1]), y=np.mean(lat[i-1:i+1]), s=distance_arr[-1])


print(distance_arr)


plt.xlim(np.min(long) - 10, np.max(long) + 10)
plt.ylim(np.min(lat) - 10, np.max(lat) + 10)
#plt.xticks(range(int(min(long)), int(max(long)+1)))
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Longitude vs Latitude")
plt.show()


