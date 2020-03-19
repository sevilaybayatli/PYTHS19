#Question 10: Create a two 2-D array and Plot it using matplotlib
import numpy
import matplotlib.pyplot as plt
arr=numpy.arange(10,40,5)
sshp=arr.reshape([2,3])
print(sshp)
plt.plot(sshp)
plt.show()
