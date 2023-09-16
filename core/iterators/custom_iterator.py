# A class to demonstrate how to create a custom iterator
class MyNumbers:
    def __init__(self, start=1):
        self.number = start

    # This method is required for iterators
    def __iter__(self):
        return self

    # This method is required for iterators
    def __next__(self):
        x = self.number
        self.number += 1
        return x

my_numbers_object = MyNumbers(10)

for item in my_numbers_object:
    if item > 20:
        break
    print(item)

my_numbers_iterator = iter(my_numbers_object)

print(next(my_numbers_iterator))
print(next(my_numbers_iterator))