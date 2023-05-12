# A simple Python program to calculate the number of hours in a list composed of a few number of days...
hours_in_a_day = 24


# A function to return the number of hours in a given number of days passed in:
def days_to_hours(num_of_days):
    return f"{num_of_days} day(s) is/are {num_of_days * hours_in_a_day} hours."


# A function to calculate the number of hours in the number of days passed in:
def calculate_hours(num_of_days):
    try:
        user_input_number = int(num_of_days)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_hours(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a '0'! Please enter a valid positive number!")
        else:
            print(f"You entered a negative number: '{num_of_days}'! Please enter a valid positive number!")

    except ValueError:
        print(f"Your input: '{num_of_days}', is not a valid number!")


# A loop to accept a list of days as the input from user and calculate hours per day for each member of that list, until the user enters "exit"
user_input = input("Enter a comma separated list of days and I will convert them to hours!\n")
while user_input != "exit":
    for num_of_days in set(user_input.split(", ")):
        calculate_hours(num_of_days)
    user_input = input("Enter a comma separated list of days and I will convert them to hours!\n")