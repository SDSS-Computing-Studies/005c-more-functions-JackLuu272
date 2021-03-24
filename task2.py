#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest():
    pass
    return

assert largest([3,10,3]) == 10

list = []

n = int(input("Enter numbers of value: "))

for i in range(0,n):
    elements = float(input(""))

    list.append(elements)

def largest(list):
    return max(list)

print(max(list))
