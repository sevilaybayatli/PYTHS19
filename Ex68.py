import sys
#Write a Python program to add two objects if both objects are an integer type.
def add_numbers(a,b):
    if not (isinstance(a, int)and isinstance(b, int)):
         raise TypeError("inputs must be intergers")
 
    else:
      return a+b

#a=int(input("enter a number "))
#b=int(input("enter a number "))
print(add_numbers(10,2.4))
