import sys
#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def pointt (n):
    
    total=0
    while n>0:
        total+=n
        n-=1
    return total
      
n=int(input("enter a number: "))
print(pointt(n))

