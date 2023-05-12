# A simple Python program to calculate the number of conversion_units pr day in a list composed of a few number of 'days:unit' elements...


# A function to return the number of conversion_units(hours or minutes) in a given number of days passed in:
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} day(s) is/are {num_of_days * 24} hours!"
    elif conversion_unit == "minutes":
        return f"{num_of_days} day(s) is/are {num_of_days * 24 * 60} minutes!"
    else:
        return f"unsupported unit: '{conversion_unit}'!"


# A function to calculate the number of units in the number of days (values passed in as a dictionary):
def calculate_units(days_and_unit_dictionary):
    try:
        user_input_number_of_days = int(days_and_unit_dictionary["days"])
        user_input_unit = days_and_unit_dictionary["unit"]

        # we want to do conversion only for positive integers
        if user_input_number_of_days > 0:
            calculated_value = days_to_units(user_input_number_of_days, user_input_unit)
            print(calculated_value)
        elif user_input_number_of_days == 0:
            print("you entered a 0! Please enter a valid positive number!")
        else:
            print(f"You entered a negative number: '{user_input_number_of_days}'! Please enter a valid positive number!")

    except ValueError:
        print(f"Your input: '{days_and_unit_dictionary['days']}', is not a valid number!")


# A loop to accept a list of 'days:unit' elements as the input from user and calculate units per day for each member of that list, until the user enters "exit"
user_input = input("Enter a comma separated list of 'days:unit' elements and I will convert each element's 'days' to its equivalent 'unit's!\n")
while user_input != "exit":
    for key_value_entry in set(user_input.split(", ")):
        try:
            days_and_unit = key_value_entry.split(":")
            days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
            calculate_units(days_and_unit_dictionary)
        
        except IndexError:
            print("Error(s) found in the input format, please double check!")

    user_input = input("Enter a comma separated list of 'days:unit' elements and I will convert each element's 'days' to its equivalent 'unit's!\n")
