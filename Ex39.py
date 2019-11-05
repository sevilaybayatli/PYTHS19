#Question 9: Following is the input NumPy array delete column two and insert following new column in its place.
import numpy
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 

newColumn = numpy.array([[10,10,10]])

print(sampleArray)
print("delete column two")
rray=numpy.delete(sampleArray,1,axis=1)
print(rray)
print("insert new clumn into array")
nrray=numpy.insert(rray,1,newColumn, axis=1)
print(nrray)


