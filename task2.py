#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest(a):
    b=list(a)
    b.sort(reverse=True)
    return b[0]

assert largest([3,10,3]) == 10