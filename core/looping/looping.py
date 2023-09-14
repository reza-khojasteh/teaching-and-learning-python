"""
Loops through lists of names and ages using various looping constructs.

NAMES (list): A list of names.
AGES (list): A list of ages corresponding to the names.

# while loop 
Loops while i is less than the length of NAMES, printing each name and age.
Increments i on each iteration.

# for loop
Loops through each name in NAMES, printing the name.

# for loop using zip
Loops through NAMES and AGES simultaneously using zip, printing each name and age.

# for loop using reversed
Loops through NAMES in reverse order, printing each name.

# for loop using range
Loops twice, printing the name at index 0 and 1.

# for loop using enumerate
Loops through NAMES, printing the index and name on each iteration.
"""

NAMES = ["Reza", "Ryan"]
AGES = [47, 2]

# while loop
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

# for loop
for name in NAMES:
    print(name)

# for loop using zip
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# for loop using reversed
for name in reversed(NAMES):
    print(name)

# for loop using range
for i in range(2):
    print(NAMES[i])

# for loop using enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
