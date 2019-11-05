# Question 6: Split the array into four equal-sized sub-arrays
#Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

import numpy

sampleArray= numpy.arange(10,34,1)
sampleArray=sampleArray.reshape([8,3])
print(sampleArray)
print("output slice array")
print(sampleArray[0:2, 0:3]) 
print(sampleArray[2:4, 0:3])
print(sampleArray[4:6, 0:3])
print(sampleArray[6:8, 0:3])




