#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if len(filter(lambda x: x <= 0, [a, b, c])):
        raise TriangleError, "Triangles may not have a side with length less than or equal to 0."
    elif (a + b <= c) or (b + c <= a) or (a + c <= b):
        raise TriangleError, "The sum of any two sides of a triangle must be greater than the third side."

    if a == b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
