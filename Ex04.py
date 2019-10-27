#Question 5: Given a list of ints, return True if first and last number of a list is same
import sys

def listnum(num):

    #for i in  range (num):
    if (num[0]== num[4]):
       return True

num=[5,4,4,2,2]

print("The first and last number of a list is same")
print("result is", listnum(num)) 
