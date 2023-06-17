class MyNumbers:
    def __init__(self, start=1):
        self.number = start

    def __iter__(self):
        return self

    def __next__(self):
        x = self.number
        self.number += 1
        return x


my_numbers_object = MyNumbers(10)
# my_iter = iter(my_numbers_object)

for item in my_numbers_object:
    if item > 20:
        break
    print(item)
