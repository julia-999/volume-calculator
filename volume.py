"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: October 16th 2019
Module Description: Computes volume of inputted shapes
"""

# import statement
import math


# returns cube volume
def c_volume_calc(side):
    return round(side**3, 3)


# returns pyramid volume
def p_volume_calc(base, height):
    return round((1/3)*(base**2)*height, 3)


# returns ellipsoid volume
def e_volume_calc(radius1, radius2, radius3):
    return round((4/3)*math.pi*radius1*radius2*radius3, 3)
