"""
Task
Write a Python function that accepts 3 integers a,b and c from the user and print the largest among the three on the screen.

Example:

For a = 3, b = 6, c = 5, the output should be 6
For a = 2, b = 1, c = 3, the output should be 3
"""
def max3(a,b,c):
    if a > b and a > c:
        return a
    return b if b > c else c
    
a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))

