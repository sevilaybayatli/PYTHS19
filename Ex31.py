#Question 1: Create a 4X2 integer array and Prints its attributes
#The shape of an array.
#Array dimensions.
#The Length of each element of the array in bytes.


import sys
#import numpy as np

#sarray= np.array([[64392, 31655],[32579, 0], [49248, 462], [0, 0]])

#print(sarray)

#%%%%%%%%%%%%another solution%%%%%%%%%%%%%%

import numpy

firstarray= numpy.empty([4,2],dtype=numpy.uint16)

print(firstarray)
print("array shape: ", firstarray.shape)
print("array dimension: ", firstarray.ndim)
