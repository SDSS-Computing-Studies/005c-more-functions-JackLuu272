#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""
import math
def hypotenuse(a,b,boole):
    if boole == "False":
        return math.sqrt(a**2+b**2)
    elif boole == "True" and a > b:
        return math.sqrt(a**2-b**2)
    elif boole == "True" and a < b:
        return math.sqrt(b**2-a**2)