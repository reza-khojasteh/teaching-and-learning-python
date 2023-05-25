"""
Opens the laureates.csv file and reads its contents into a list of dictionaries.

Parameters:
f (file object): The opened laureates.csv file.

Returns: None

Functionality:
reader (csv.DictReader): Reads the rows of the CSV file into dictionaries. 
laureates (list): A list of the dictionaries, one per row.

Loops through the rows, checking if the "surname" is "Einstein". 
If a match is found, it calculates and prints Einstein's age when he received the prize.

year_date (datetime): The year the prize was awarded, parsed from the "year" column.
born_date (datetime): Einstein's birth date, parsed from the "born" column. 
age (int): Einstein's age when he received the prize, calculated by subtracting born_date.year from year_date.year.

Exits the loop after finding the first match.
"""

import csv
from datetime import datetime

# Open the laureates.csv file and read its contents into a list of dictionaries
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)
# Loop through the rows, checking if the "surname" is "Einstein"
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        print((laureate))
        # datetime.strptime() converts a string into a datetime object according to the format specifier you provide.
        year_date = datetime.strptime(laureate["year"], "%Y")
        print((year_date))
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        print((born_date))
        # Calculate and print Einstein's age when he received the prize
        print(
            f"(Roughly) Age at which they received the prize: {year_date.year - born_date.year}"
        )
        break
