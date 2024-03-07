#!/bin/bash

# EPICS EVEI
# This is a Linux script that reads the data in a coordinates
# log file, and converts it to a CSV format.
# The output is written to a file with the same name as the given
# file, but with a '.csv' file extension.

# To run the script, first run 'chmod +x coords_to_csv.sh' and then
# run './coords_to_csv.sh <logfile>', replacing <logfile> with the
# name of the actual log file.


file_to_read="$1"
file_to_write="${file_to_read%.txt}.csv"

echo "LATITUDE,LONGITUDE" > "$file_to_write"

# 1. Find the relevant lines of the file (Lat/Long and Refresh rate)
# 2. Remove all newlines in the file (Makes it easier to replace text
# 3. Add a newline after printing a set of Lat/Long/Refresh rate (i.e. before the next 'Latitude' print)
# 4. Append a newline to the end of the file
# 5. Remove the first line of the file, which is just an empty line
# 6. Convert the file to a CSV file by inserting commas between the relevant values
# 6. Output to the correct file

grep -E 'Lat|GPS' "$file_to_read" | tr '\r\n' ' ' | sed 's/Lat/\nLat/g' | cat - <(echo "") | tail -n +2  | awk '{print $2 "," $4 "," $8}' - >> "$file_to_write"
