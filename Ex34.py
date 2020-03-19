#Question 4: Following is the given numpy array return array of odd rows and even columns
import numpy
sampleArray= numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print(sampleArray)
print("\n Printing array of odd rows and even columns")
#narray=sampleArray([::2, 1::2])
#print(narray)

newArray = sampleArray[::2, 1::2]
print(newArray)
