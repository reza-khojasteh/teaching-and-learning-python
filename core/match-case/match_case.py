"""
Prints a message based on the value of mycolor using pattern matching.

Parameters:
mycolor (str): The color to check.

match mycolor.lower():
Checks the lowercase value of mycolor against the cases.

case 'blue': 
Prints 'Blue' if mycolor is 'blue'.

case 'green':
Prints 'Green' if mycolor is 'green'.

case 'yellow': 
Prints 'Yellow' if mycolor is 'yellow'.

case _:  
Prints 'Any other color!' if mycolor does not match any other case.

This construct was added in Python 3.10.
"""

mycolor = "Yellow"

match mycolor.lower():
    case "blue":
        print("Blue")
    case "green":
        print("Green")
    case "yellow":
        print("Yellow")
    case _:
        print("Any other color!")
