"""
Recursive solution to the Towers of Hanoi problem.

Parameters:
f (str): Starting rod 
s (str): Spare rod
t (str): Ending rod
n (int): Number of disks

Functionality:
Moves n disks from rod f to rod t using rod s.
If n <= 0, returns.
If n == 1, prints the move from f to t.
Otherwise:
- Moves n-1 disks from f to s using t.
- Prints the move from f to t. 
- Moves n-1 disks from s to t using f.
"""


def hanoi(f, s, t, n):
    # base case(s)
    if n <= 0:
        return
    if n == 1:
        print(f, "->", t)
    # recursive case
    else:
        hanoi(f, t, s, n - 1)
        print(f, "->", t)
        hanoi(s, f, t, n - 1)


# take some input from the user
n = int(input("Enter the number of disks: "))
hanoi("f", "s", "t", n)
