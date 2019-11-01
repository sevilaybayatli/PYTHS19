#Question 7: Calculate mutiplication of two random float numbers


#First random float number must be between 0.1 and 1
#Second random float number must be between 9.5 and 99.5

import sys
import random

fnum= random.uniform(0.1,1.0)
snum=random.uniform(9.0,99.5)
print("the first float number between 0.1 and 1 is ",fnum)
print("the first float number between 9.0 and 99.5 is ",snum)

print("the multiplication of two float numbers is: ", fnum*snum)
