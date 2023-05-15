"""
Calculates the power of a number using recursion.

Parameters:
value (int): The base number.  
number (int): The exponent.

recursive_power_simulator(value, number)
The main recursive function that calculates value raised to the power of number.

Base case:  
if number == 0:  
Returns 1.  

Base case:
if number == 1:
Returns value.

General case:
Returns value * recursive_power_simulator(value, number - 1). 
"""


# A reccursive function that calculates the power of a number with O(n) time complexity
def recursive_power_simulator(value, number):
    if number == 0:
        return 1
    elif number == 1:
        return value
    else:
        return value * recursive_power_simulator(value, number - 1)


# OR even better, using the following code which gives us O(log(n)) time complexity:
# def recursive_power_simulator(value, number):
#     if number == 0:
#         return 1
#     elif number == 1:
#         return value
#     else:
#         half = number // 2
#         result = recursive_power_simulator(value, half)
#         if number % 2 == 0:
#             return result * result
#         else:
#             return value * result * result


print(recursive_power_simulator(3, 3))
