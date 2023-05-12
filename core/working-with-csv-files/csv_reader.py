"""
Reads data from a CSV file and prints the row for Albert Einstein.

Parameters:
- laureates.csv: The CSV file containing the data.

Returns: None

Functionality: 
- Opens the CSV file "laureates.csv" for reading.
- Creates a DictReader object to read the data into dictionaries.
- Converts the DictReader into a list of dictionaries, one per row.
- Loops through the rows, checking if the "surname" is "Einstein".
- If a match is found, prints that row's dictionary.
- Exits the loop after printing the match.
"""

import csv
import pprint

try:
    # open the file for reading
    with open("laureates.csv", "r") as f:
        # create a DictReader object to read the data into dictionaries
        reader = csv.DictReader(f)
        # convert the DictReader into a list of dictionaries, one per row
        laureates = list(reader)
    # loop through the rows
    for laureate in laureates:
        # check if the "surname" is "Einstein"
        if laureate["surname"] == "Einstein":
            # print the row's dictionary using pprint
            pprint.pprint(laureate)
            break
except FileNotFoundError:
    print("The file 'laureates.csv' does not exist!")
