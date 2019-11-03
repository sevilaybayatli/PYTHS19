#Question 5: Add the following two NumPy arrays and Modify a result array by calculating the square root of each element
import numpy

arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
print("\n arrayOne= ", arrayOne)
print("\n arrayTwo= ", arrayTwo)
arrayThird=arrayOne+arrayTwo
print("the sum of two arrays= ", arrayThird)

print("the sqrt of third array: ", numpy.sqrt(arrayThird))

