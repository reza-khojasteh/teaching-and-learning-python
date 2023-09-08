sample_string = "Hello World"

# len() is a built-in function that returns the length of the string
print(len(sample_string))
# Prints 11

# __len__() is a magic method that returns the length of the string
print(sample_string.__len__())
# Prints 11

print(sample_string[0])
# Prints H

print(sample_string[10])
# Prints d

# print(sample_string[11])
# IndexError: string index out of range

print(sample_string[-1])
# Prints d

print(sample_string[-2])
# Prints l

print(sample_string[-11])
# Prints H

# print(sample_string[-12])
# IndexError: string index out of range

print(sample_string[0:2])
# Prints He

print(sample_string[0:11])
# Prints Hello World

print(sample_string[0:12])
# Prints Hello World

print(sample_string[0:100])
# Prints Hello World

print(sample_string[0:])
# Prints Hello World

print(sample_string[-11:-1])
# Prints Hello Worl

print(sample_string[-11:0])
# Prints nothing

print(sample_string[-11:11])
# Prints Hello World

print(sample_string[-11:12])
# Prints Hello World

print(sample_string[-11:100])
# Prints Hello World

print(sample_string[-100:100])
# Prints Hello World

print(sample_string[:len(sample_string)])
# Prints Hello World

print(sample_string[:])
# Prints Hello World

print(sample_string[0:11:1])
# Prints Hello World

print(sample_string[0:11:2])
# Prints HloWrd

print(sample_string[0:11:3])
# Prints HlWl

print(sample_string[-11:11:1])
# Prints Hello World

print(sample_string[:11:1])
# Prints Hello World

print(sample_string[0::1])
# Prints Hello World

print(sample_string[::1])
# Prints Hello World

print(sample_string[::])
# Prints Hello World

print(sample_string[0:11:-1])
# Prints nothing

print(sample_string[11:0:-1])
# Prints dlroW olle

print(sample_string[11:-1:-1])
# Prints nothing

print(sample_string[11::-1])
# Prints dlroW olleH

print(sample_string[::-1])
# Prints dlroW olleH