"""
Monte Carlo Approximation of Pi

3/26/15
Albert Liang

Uses a Monte Carlo method to approximate Pi.  User can control accuracy by determining the number of random samples.

This method uses a circle inscribed in a square.  The ratio of the area inside the circle to the area of everthing inside the square is PI/4.  Because of this, we can repeatedly sample random points within the square, determining if each point is also inside the circle.  The number of points inside the circle divided the number of points overall will give us a rough value for PI/4. 
"""
from math import *


