"""
Monte Carlo Approximation of Pi

3/26/15
Albert Liang

Uses a Monte Carlo method to approximate Pi.  User can control accuracy by determining the number of random samples.
The program also prints the error of its approximation, using Python's built-in PI constant as a reference.

This method uses a circle inscribed in a square.  The ratio of the area inside the circle to the area of everthing inside the square is PI/4.  Because of this, we can repeatedly sample random points within the square, determining if each point is also inside the circle.  The number of points inside the circle divided the number of points overall will give us a rough value for PI/4. 

NOTES:
# All points on or contained within the border of the circle are considered "in the circle".
# 'center' is a list of size 2. Format is [x,y].  We assume that x and y are integers.
# We assume that 'side' and 'radius' are integers greater than 0.
# Learn to use exceptions to handle the above cases, instead of relying on if-statements upon input?
"""
from math import *
from random import *

# Classes ======================================================================================================
class Square(object):
    def __init__(self,side,center):
	self.side = side
	self.c_x = center[0]
	self.c_y = center[1]
	self.max_x = self.c_x + 0.5*side
	self.min_x = self.c_x - 0.5*side
	self.max_y = self.c_y + 0.5*side
	self.min_y = self.c_y - 0.5*side
    def getRandomPoint(self):
	point = [0,0]
	point[0] = randint(self.min_x,self.max_x)
	point[1] = randint(self.min_y,self.max_y)
	return point

class Circle(object):
    def __init__(self,radius,center):
	self.radius = radius
	self.c_x = center[0]
	self.c_y = center[1]
    def pointIsInCircle(self,point):
	d = getDistance([self.c_x,self.c_y],point)
	return d <= self.radius
   
 
# Global Functions =============================================================================================
def getDistance(p1,p2):
    x_diff = p2[0]-p1[0]
    y_diff = p2[1]-p1[1]
    a = pow(x_diff,2)
    b = pow(y_diff,2)
    d = pow( (a+b),0.5 )
    return d

# Check if String Represents an Integer
# (From Stackoverflow)
def StringRepInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Main =========================================================================================================
def main():
    print '\n\nMonte Carlo Approximation of Pi:'
    print '=================================================='
    
    while(True):    
	numIter = raw_input( '\nNumber of samples to draw ( \'q\' to quit): ' )
	if( numIter.lower() == 'q' ):
	    break
	elif( not( StringRepInt(numIter) )  or int(numIter) <= 0 ):
	    print 'Please enter an integer greater than 0.'
	    continue 
	numIter = int(numIter)

	# Intialize Square and Circle	
	center = [0,0]
	radius = 100
	square = Square(2*radius,center)
	circle = Circle(radius,center)

	# Initialize Counts
	count_cir = 0.00
	count_total = 0.00

	for i in range(numIter):
	    point = square.getRandomPoint() 
	    count_total += 1
	    if( circle.pointIsInCircle(point) ):
		count_cir += 1
	approx = (count_cir/count_total) * 4
	error = approx - pi
	print 'Approximation: %s' % ( str(approx) )
	print 'Error: %s' % ( str(error) )
    print 'Exiting...\n\n'


# Run ==========================================================================================================
main()

