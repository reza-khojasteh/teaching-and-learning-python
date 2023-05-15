"""
Checks if a string is a palindrome using recursion.

Parameters: 
word (str): The string to check.

is_palindrome(word)
The main recursive function that checks if word is a palindrome.

check_two_sides(left, right)
A recursive helper function that checks if the substring from left to right is a palindrome.

Base case: 
if left >= right: 
Returns True since an empty or single-character substring is a palindrome.

General case:  
if word[left] == word[right]:
Recursively calls check_two_sides() with left + 1 and right - 1.

General case:
if word[left] != word[right]:
Returns False since the substring is not a palindrome.

# testing cases
Prints the result of calling is_palindrome() with various test strings.
"""

# A recursive solution to check if a string is a palindrome:


def is_palindrome(word):
    def check_two_sides(left, right):
        # Base case: if the left and right indices cross, we have a palindrome,
        if left >= right:
            return True
        # General case: if the letters at the left and right indices are the same,
        elif word[left] == word[right]:
            return check_two_sides(left + 1, right - 1)
        # General case: if the letters at the left and right indices are different,
        return False

    # Call the recursive function with the left and right indices.
    return check_two_sides(0, len(word) - 1)


# testing cases
print(is_palindrome("noon"))
print(is_palindrome("table"))
print(is_palindrome("racecar"))
print(is_palindrome("tacocat"))
print(is_palindrome(""))
print(is_palindrome("a"))

# Output:
# True
# False
# True
# True
# True
# True
