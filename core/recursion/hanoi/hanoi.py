"""
Recursive solution to the Towers of Hanoi problem.

Parameters:
f (str): Starting rod 
s (str): Spare rod
t (str): Ending rod
n (int): Number of disks

Functionality:
Moves n disks from rod f to rod t using rod s (disk no. 1 is the topmost disk)
If n <= 0, returns.
If n == 1, prints the move from f to t.
Otherwise:
- Moves the top n-1 disks from f to s using t.
- Prints the move from f to t. 
- Moves all the n-1 disks from s to t using f.
"""


def hanoi(f, s, t, n):
    # base case(s)
    if n <= 0:
        return
    if n == 1:
        print(f"Move disk {n} from {f} to {t}")
        return
    # (else) recursive case
    # move the top n - 1 disks on f to s (with the help of t)
    hanoi(f, t, s, n - 1)
    # move the biggest disk from f to t
    print(f"Move disk {n} from {f} to {t}")
    # move the same n - 1 disks from s to t (with the help of f)
    hanoi(s, f, t, n - 1)


# take some input from the user
n = int(input("Enter the number of disks: "))
hanoi("f", "s", "t", n)
