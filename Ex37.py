#Question 8: Following is the 2-D array. Print max from axis 0 and min from axis 1
import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

print("Printing Original array")
print(sampleArray)

minofAxisone=numpy.amin(sampleArray,1)
print("printing amin of axis 1")
print(minofAxisone)
maxofAxisone=numpy.amax(sampleArray,1)
print("printing max of axis 0")
print(maxofAxisone)


