"""
Prints a greeting using two different string formatting methods.

name (str): The name to use in the greeting.

formatted_1 (str): Uses f-string formatting to insert the name into the greeting string.
Prints:
Hello Reza

greet_format (str): A greeting string with a placeholder.
formatted_2 (str): Uses the .format() method to insert the name into the greeting string. 
Prints:
Hello Reza
"""

# Define the name to use in the greeting
name = "Reza"
# Use f-string formatting to insert the name into the greeting string
formatted_1 = f"Hello {name}"
print(formatted_1)

# OR (the same result...)

greet_format = "Hello {}"
formatted_2 = greet_format.format(name)
print(formatted_2)
